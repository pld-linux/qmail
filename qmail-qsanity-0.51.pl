#!/usr/bin/perl
# examine all the files in the qmail queue.

# Copyright 1997-1998, Russell Nelson <nelson@crynwr.com> for publication
# in the forthcoming O'Reilly & Associates book on qmail.  Permission
# to redistribute in unmodified or modified form granted subject to
# the condition that this notice be retained, and modifications be
# identified as such.

# See http://www.qmail.org for updates to this program.

# CONFIGURATION:

$qmail = "/var/qmail";		# conf-qmail
$auto_split = 23;		# conf-split

# CHANGES:
# need to change to deal with unprocessed files properly.
#Feb 24 1998 released 0.51
#Dec 30 1997 added test for extraneous files in bounce, intd, todo.
#Dec 30 1997 oops, gids on mess match the gid of the sender.
#Dec 30 1997 released 0.50: First public release


# rd - read a directory into an array.
sub rd {
    my ($subdir) = @_;

    opendir(D, $subdir) || die "cannot read $subdir";
    @$subdir = sort(grep(!/\.\.?/, readdir(D)));
    closedir(D);
}

# rdhash - read a hashed directory into an array.
sub rdhash {
    my ($subdir) = @_;
    my $i;

    @$subdir = ();
    for ($i = "0"; $i < $auto_split; $i++) {
	opendir(D, "$subdir/$i") || die "cannot read $subdir/$i";
	@_ = grep(!/\.\.?/, readdir(D));
	@_ = grep(/\D/ || $i != $_ % $auto_split?
		  !warn "queue/$subdir/$i/$_ does not belong there\n":
		  1, @_);
	push @$subdir, @_;
	closedir(D);
    }
    @$subdir = sort(@$subdir);
}

# fmtqfn - make a hashed filename
sub fmtqfn {
    my ($fn) = @_;
    return ($fn % $auto_split)."/$fn";
}

# checkfile - check the uid and maybe gid and maybe permission of a file.
sub checkfile {
    my ($fn, $uid, $gid, $perm) = @_;
    die "unable to stat $fn\n" unless (@_ = stat($fn));
    warn "uid incorrect (is $_[4], want $uid) on $fn\n" unless $_[4] == $uid;
    warn "gid incorrect (is $_[5], want $gid) on $fn\n" if $gid && ($_[5] != $gid);
    warn "permission incorrect (is $_[2], want $perm) on $fn\n"
	if $perm && (($_[2]&0777) != $perm);
}

# main
chdir "$qmail/queue" || die "no /var/qmail/queue";

# set up uids
$uidq = (@_=getpwnam("qmailq"))[2];
$uids = (@_=getpwnam("qmails"))[2];
$gid = (@_=getgrnam("qmail"))[2];
%uid = ("info"=>$uids, "mess"=>$uidq, "remote"=>$uids, "local"=>$uids);
%perms = ("info"=>0700, "mess"=>0750, "remote"=>0700, "local"=>0700);

# duplicate some tests which ``make check'' performs.
foreach $i ("info", "mess", "remote", "local") {
    rd($i);
    warn "$i/ has too few subdirectories" unless @$i == $auto_split;
    $uid = $uid{$i};
    $perms = $perms{$i};
    foreach $n (@$i) {
	checkfile("$i/$n", $uid, $gid, $perms);
    }
}

rd("bounce");
rd("intd");
rd("todo");
rdhash("info");
rdhash("mess");
rdhash("remote");
rdhash("local");

foreach $i ("bounce", "intd", "todo") {
    if (@_ = grep /\D/, @$i) {
	warn "You have files in queue/$i that do not belong: ".join(",",@_);
    }
}

# check the ownership on all the messages.
# note that the mess/ files retain the group of the program that
# executed qmail-queue.
foreach $i ("info", "mess", "remote", "local") {
    $uid = $uid{$i};
    foreach $n (@$i) {
	checkfile("$i/".fmtqfn($n), $uid, $i eq "mess"?"":$gid);
	$all{$n} = join(',', $all{$n}, $i);
    }
}

# check all the files to see if they're coherent.
foreach $m (keys(%all)) {
    $_ = $all{$m};
    warn "message has no entry in info: $m\n" unless /info/;
    warn "message has no entry in mess: $m\n" unless /mess/;
    warn "message is neither local nor remote: $m\n" unless /local/ || /remote/;
}
