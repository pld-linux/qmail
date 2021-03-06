#!/usr/bin/perl
# examine the qmail configuration to see if any common errors exist.
# usage: qmail-line [-v]
#   -v -- print an explanation of the reports the first time one is printed.

# Copyright 1999, Russell Nelson <nelson@crynwr.com> for publication
# in the forthcoming O'Reilly & Associates book on qmail.  Permission
# to redistribute in unmodified or modified form granted subject to
# the condition that this notice be retained, and modifications be
# identified as such.

# See http://www.qmail.org for updates to this program.

# CONFIGURATION:

$qmail = "/var/qmail";		# conf-qmail
$auto_patrn = 002;		# conf-patrn

# CHANGES:
#Jan 25 1999 released 0.50: First public release
#Contributions from Andrea Paolini <ap@dsnet.it>:
#1. Skip comments in virtualdomains.
#2. Strip username from virtualdomains when checking if hostnames are
#   defined in rcpthosts.
#3. Correct misspelling (?). Changed "=~ split(/@/)" to "= split(/@/)";
#4. Permit to mix in control/virtualdomains generic virtual domains and
#   virtual users for the same domain.
#Jan 26 1999 release 0.51

use Getopt::Std;

getopts('v');
die "usage: qmail-lint [-v]\n" if @ARGV;

# if the -v option is set, print the verbose explanation.
sub verbose {
  return unless $opt_v;
  $name = shift;
  return if $verbose_printed{$name}++;
  seek(DATA,0,0);
  while(<DATA>) {
    next unless m/^$name/;
    while(<DATA>) {
      last unless /^  /;
      print $_;
    }
  }
}

chdir($qmail) or die;

# read control/locals
if (open(F, "<control/locals")) {
  while(<F>) {
    chomp;
    push(@locals,$_);
    next if m"^#";
      $locals{$_} = "";
  }
} else {
  print "Warning: No hosts are considered local.  You will be unable to receive mail here.\n";
  &verbose("NHL");
}

# read control/virtualdomains
if (open(F, "<control/virtualdomains")) {
  while(<F>) {
    chomp;
    push(@virtualdomains,$_);
    next if m"^#";
      if (split(/:/) < 2) {
	print "Warning: Line $. in control/virtualdomains has no colon:\n";
	print "  $_\n";
	&verbose(NOCOLON);
      }
    if (defined($virtualdomains{$_[0]})) {
      if ($virtualdomains{$_[0]} != $_[1]) {
	print "Error: Line $. in control/virtualdomains redefines $_[0] to a different value:\n";
	print "  $_\n";
	&verbose(TWOVDOMS);
      } else {
	print "Warning: Line $. in control/virtualdomains redefines $_[0]:\n";
	print "  $_\n";
	&verbose(TWODOMSDIFF);
      }
    }
    $virtualdomains{$_[0]} = $_[1];
  }
}

# double-plus ungood if they have no rcpthosts file
if (open(F, "<control/rcpthosts")) {
  while(<F>) {
    chomp;
    next if m"^#";
      $rcpthosts{$_} = "";
  }
} else {
  print "Warning: Without a control/rcpthosts file, you are open to relay abuse by spammers.\n";
  &verbose(NORCPTHOSTS);
}

# it's cool if they don't have a morercpthosts file.
if (open(F, "<control/morercpthosts")) {
  while(<F>) {
    chomp;
    next if m"^#";
      $rcpthosts{$_} = "";
  }
}

# a host in locals AND in virtualdomains.  This is beyond the pale.
if (%virtualdomains) {
  foreach (@locals) {
    if (defined($virtualdomains{$_})) {
      print "Error: a host $_ in locals also appears in virtualdomains.\n";
      &verbose(LOCALVDOM);
    }
  }
}

# A host in locals but not in rcpthosts.  How odd.
if (%rcpthosts) {
  foreach (@locals) {
    next if m"^#";
    next if defined($rcpthosts{$_});
    s/^.*?\././;
    do {
      last if defined($rcpthosts{$_});
    } while (s/^\..*?(\.|$)/$1/);
    next if defined($rcpthosts{$_});
    print "Warning: a host $_ in locals does not appear in rcpthosts.\n";
    &verbose(LOCALNORCPT);
  }
}

# A host in virtualdomains but not in rcpthosts.  How odd.
if (%rcpthosts) {
  foreach (@virtualdomains) {
    next if m"^#";
    ($host, $redirect) = split(/:/);
    $_ = $host;
    $_ =~ s/^.+@//;	# Strip username
    next if defined($rcpthosts{$_});
    s/^.*?\././;
    do {
      last if defined($rcpthosts{$_});
    } while (s/^\..*?(\.|$)/$1/);
    next if defined($rcpthosts{$_});
    print "Warning: a host $host in virtualdomains does not appear in rcpthosts.\n";
    &verbose(LOCALNORCPT);
  }
}

# a host named in a USER@HOST:MAP virtualdomains line should be remote, not local or virtual.
foreach (keys %virtualdomains) {
  ($user, $host) = split(/@/);
  next unless $user and $host;
  if (defined($locals{$host})) {
    print "Warning: a host named in a USER\@HOST:MAP virtualdomains line should be remote, not local.\n";
    print "$_\n";
    &verbose(LOCALUSERHOSTMAP);
    &verbose(USERHOSTMAP);
  }
  if (defined($virtualdomains{$host})) {
    print "Warning: a host named in a USER\@HOST:MAP virtualdomains line should be remote, not virtual.\n";
    print "$_\n";
    &verbose(VDOMUSERHOSTMAP);
    &verbose(USERHOSTMAP);
  }
}

if (-f "users/assign") {
  print "Warning: users/assign checking not implemented.\n";
#  exit;
}

# Read all of alias's .qmail files
opendir(D, "$qmail/alias") or die;
while($_ = readdir(D)) {
  next unless /^\.qmail-(.*)/;
  $alias = $1;
  $aliases{$alias} = "$_"   while $alias =~ s/-.*?//;
}
closedir(D);

# the biggest file is /etc/passwd, so we deal with it one line at a time rather
# than reading the whole thing into memory.
while(($name, $passwd, $uid, $gid, $quota, $comment, $gcos, $dir, $shell) = getpwent) {

  ($homemode, $homeuid) = (stat($dir))[2,4];

  # print all the users who cannot receive email.  We use a heuristic that skips reporting
  # any users until we've found one who can.  This skips the system accounts.
  if ($uid == 0) {
    # ignore root.
  } elsif ($dir eq $qmail) {
    # ignore qmail users.
  } elsif ($homeuid != $uid) {
    if ($foundhomedir) {
      print "Warning: cannot receive mail (does not own home directory): $name\n";
      &verbose(NOOWNHOME);
    }
  } else {
    $foundhomedir = 1;
  }

  # Warn about home directories that don't match conf-patrn.
  if ($homemode & $auto_patrn) {
    print "Warning: cannot receive mail (home directory writable by others): $name\n";
    &verbose(BADHOMEPERMS);
  }

  # Warn about .qmail files that don't match conf-patrn.
  if (opendir(D, "$dir")) {
    while($_ = readdir(D)) {
      next unless /^\.qmail/;
      $mode = (stat($_))[2];
      if ($mode & $auto_patrn) {
	print "Warning: cannot receive mail (.qmail writable by others): ~$name/$_\n";
	&verbose(BADQMAILPERMS);
      }
    }
    closedir(D);
  }

  # Remember if this user is the target of a virtualdomains match
  foreach $domain (keys %virtualdomains) {
    $virtualdomains_userok{$domain} = 1 if $virtualdomains{$domain} =~ m/^$name($|-)/;
  }

  # Make sure that there are no addresses in ~alias which appear to match valid usernames.
  if (defined($aliases{$name})) {
    print "Warning: ~alias/$aliases{$name} matches an actual username and will be ignored.\n";
    &verbose(ALIASVSUSER);
  }

}

# report on the virtualdomains whose targets are not users
foreach $domain (keys %virtualdomains) {
  next if $virtualdomains_userok{$domain};
  print "Warning: delivery of the virtual domain $domain is implicitly controlled by alias\n";
  &verbose(IMPLICITVDOM);
}


__END__
" # GNU Emacs is sooooooo dumb about perl syntax.
  
NHL
  If you don't list any hosts in control/locals, no mail will ever be
  considered local.  qmail-local will never be run, and no mail will be
  stored in mailboxes
NOCOLON
  qmail-send ignores lines in control/virtualdomains if they have no colon.
  If you really must have such a line, consider putting a hash mark (#) in
  front of the line to make it clear that the line is just a comment.
TWOVDOMS
  No damage is done by having multiple identical entries for the same domain.
  It can cause confusion if the entry needs to be changed, and only one of
  them is changed.
TWODOMSDIFF
  No damage is done by having multiple identical entries for the same domain.
  It can cause confusion if the entry needs to be changed, and only one of
  them is changed.
NORCPTHOSTS
  Qmail-smtpd uses control/rcpthosts to determine which hosts it will receive
  mail for.  Typically, this includes any host mentioned in locals or
  virtualdomains.  It also includes any hosts for which you are a secondary
  MX.  See http://qmail-docs.surfdirect.com.au/docs/qmail-antirelay.html
LOCALVDOM
  Qmail-send examines control/locals before it examines control/virtualdomains.
  Therefore, if a host is in locals, it will never be considered virtual.
  If you're trying to create a virtual domain, remove the host from
  control/locals.
LOCALNORCPT
  If a host is not in rcpthosts, and rcpthosts exists, then qmail-smtpd will
  not be able to receive mail from the Internet at large.  It will only
  receive mail from hosts which set RELAYCLIENTS.
LOCALUSERHOSTMAP
  There is no reason or need to use the virtualdomains USER@HOST:MAP
  capability when the host is already local.  Use a .qmail file in the user's
  home directory or in alias's home directory, as needed.
VDOMUSERHOSTMAP
  There is no reason or need to use the virtualdomains USER@HOST:MAP
  capability when the host is already virtual.  Use a .qmail file in the
  controlling user's home directory.
USERHOSTMAP
  The virtualdomains USER@HOST:MAP capability is designed to allow you to
  short-circuit mail delivery.  If you're sending email to an address on a
  host which is not this host, but which will eventually be delivered to this
  host, then you should use the USER@HOST:MAP capability.
NOOWNHOME
  qmail-getpw makes several tests to see if it can deliver mail to a
  particular address.  First, it searches through /etc/passwd to see if the
  full local part exists.  If not, it strips off dash-separated subparts and
  searches.  When it finds a match, it checks to see if that user owns their
  home directory.  If not, it keeps looking.  This prevents mail deliveries to
  system userids.  This particular user doesn't own their home directory,
  so qmail-getpw will skip over their name when attempting to deliver mail.
BADHOMEPERMS
  If other users on the system can write to a user's home directory, then the
  user has no security at all.  Anyone can run any commands as that user
  simply by creating an appropriate .qmail file and sending mail to it.  To
  prevent such a security give-away, qmail checks the mode bits stored in
  conf-patrn, and defers delivery as long as the home directory is writable.
BADQMAILPERMS
  If other users on the system can write to any of a user's .qmail files, then
  the user has no security at all.  Anyone can run any commands as that user
  simply by modifying the appropriate .qmail file and sending mail to it.  To
  prevent such a security give-away, qmail checks the mode bits stored in
  conf-patrn, and defers delivery as long as the .qmail file is writable.
ALIASVSUSER
  Users always control their own mail delivery when you are not using
  users/assign.  So, if an .qmail file in ~alias resembles a username, it will
  never be used.  If you have a user named joe, then ~alias/.qmail-joe will
  never be consulted.  Instead, ~joe/.qmail will be used.  Similarly,
  ~alias/.qmail-joe-mike will also not be used.  Instead, ~joe/.qmail-mike
  will be used.
IMPLICITVDOM
  The right-hand-side of a control/virtualdomains entry is used to decide
  which user controls delivery of the virtualdomain.  If that right-hand-side
  does not correspond to an actual user, then alias will be implicitly used.
  This carries the risk that a user matching the alias will later be created.
  It's better to explicitly say "alias-vdom", rather than let the fact that no
  user matches vdom cause alias to control the mail.
