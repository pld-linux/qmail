Summary:     qmail Mail Transport Agent
Name:        qmail
Version:     1.03
Release:     1
Copyright:   Check with djb@koobera.math.uic.edu
Group:       Utilities/System
Source0:     ftp://koobera.math.uic.edu/pub/software/qmail-1.03.tar.gz
Source1:     ftp://koobera.math.uic.edu/pub/software/dot-forward-0.71.tar.gz
Source2:     ftp://koobera.math.uic.edu/pub/software/fastforward-0.51.tar.gz
Source3:     ftp://koobera.math.uic.edu/pub/software/rblsmtpd-0.70.tar.gz
Source4:     qmail-1.03-linux.init
Source5:     qmail-linux.sh
Source6:     qmail-linux.csh
Source7:     qmail-aliases
Source8:     qmail-default
Source9:     qmail-msglog
Source10:    qmail-default-delivery
Patch0:      qmail-1.03.install.patch
Patch1:      qmail-1.03.msglog.patch
Patch2:      qmail-1.03.redhat.patch
Patch3:      qmail-1.03.ids.patch
Patch4:      qmail-1.03.rbl.conf.patch
URL:         http://www.qmail.org/
Requires:    shadow-utils
Provides:    MTA smtpdaemon qmailmta qmail-server
Conflicts:   sendmail
Buildroot:   /tmp/%{name}-%{version}-root

%description
qmail is a small, fast, secure replacement for the SENDMAIL package, which is
the program that actually receives, routes, and delivers electronic mail.
The dot-forward and fastforward packages have been added to this distribution
for (not 100%) SENDMAIL compatability.
The rblsmtpd package has been added as an optional way to fight SPAM.
A sub-package, qmail-msglog, adds (configurable) message logging.  This has 
been added as a sub-package since this necessarily slows things down a little 
bit and the author feels it necessary to distinguish the added capability as 
an add-on package.
An alternative package (smaller, easier to configure) is the qmail-client
package which will ONLY work on a LAN connected to the qmail mail server via
the QMQP protocol.

%package  msglog
Summary:     qmail Mail Transport Agent with Message Logging
Group:       Utilities/System
Requires:    qmail

%description msglog
qmail-msglog adds a (customizable) script that runs on each and every message
that goes through the mail system.  One usage example is to record Message IDs
in the log file.

%changelog

#
# MACROS
#
# Find users and groups and brand files with uids and gids.
# Set permissions, owners and groups
%define brand cd /var/qmail/bin; ./brand -f install -f instcheck -f qmail-lspawn  -f qmail-queue -f qmail-rspawn -f qmail-showctl -f qmail-start -u myauto_uida alias -u myauto_uidd qmaild -u myauto_uidl qmaill -u myauto_uido root -u myauto_uidp qmailp -u myauto_uidq qmailq -u myauto_uidr qmailr -u myauto_uids qmails -g myauto_gidq qmail -g myauto_gidn nofiles; /var/qmail/bin/install -s
#
# Error message if users or groups already exist
%define user_group_error (echo "Error $? : Required user or group already exists, please check /etc/passwd, /etc/group, and /etc/shadow files."; exit 1)

%prep
# QMAIL 1.03 Package
%setup
# DOT FORWARD Package
%setup -D -T -a 1
# FAST FORWARD Package
%setup -D -T -a 2
# RBLSMTPD Package
%setup -D -T -a 3

# Fix install
%patch0 -p1
%patch2 -p1
# IDs patch
%patch3 -p1
# RBL conf patch.
%patch4 -p0


%build
make
mv qmail-queue qmail-queue.orig
patch -p1 < $RPM_SOURCE_DIR/qmail-1.03.msglog.patch
make
mv qmail-queue qmail-queue.msglog
mv qmail-queue.orig qmail-queue
./compile -g brand.c
./load brand -g
make man

# DOT FORWARD
(cd dot-forward-0.71; make)
# FAST FORWARD
(cd fastforward-0.51; make)
# RBLSMTPD
(cd rblsmtpd-0.70; make)

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT/etc/qmail/{alias,control,users}
mkdir -p $RPM_BUILD_ROOT/usr/bin/qmail
mkdir -p $RPM_BUILD_ROOT/usr/doc/qmail-%{version}
mkdir -p $RPM_BUILD_ROOT/usr/lib/qmail/boot
mkdir -p $RPM_BUILD_ROOT/usr/man
mkdir -p $RPM_BUILD_ROOT/var/qmail
chmod 755 $RPM_BUILD_ROOT/var/qmail
ln -sf ../../etc/qmail/alias $RPM_BUILD_ROOT/var/qmail
ln -sf ../../usr/lib/qmail/boot $RPM_BUILD_ROOT/var/qmail/boot
ln -sf ../../etc/qmail/control $RPM_BUILD_ROOT/var/qmail
ln -sf ../../etc/qmail/users $RPM_BUILD_ROOT/var/qmail
ln -sf ../../usr/doc/qmail-%{version} $RPM_BUILD_ROOT/var/qmail/doc
ln -sf ../../usr/bin/qmail $RPM_BUILD_ROOT/var/qmail/bin
ln -sf ../../usr/man $RPM_BUILD_ROOT/var/qmail/man
./install $RPM_BUILD_ROOT
cp qmail-queue.msglog $RPM_BUILD_ROOT/var/qmail/bin

# Copy documentation that qmail install didn't get.
cp BLURB* README SECURITY THANKS THOUGHTS TODO VERSION $RPM_BUILD_ROOT/var/qmail/doc

# Sendmail compatable fix for user to see mail queue
ln -s qmail/qmail-qread $RPM_BUILD_ROOT/usr/bin/mailq

# Set up post installation programs
cp ./brand ./install ./instcheck ./config ./config-fast ./dnsfq ./dnsip ./dnsptr ./hostname ./ipmeprint $RPM_BUILD_ROOT/var/qmail/bin

mkdir -p $RPM_BUILD_ROOT/etc/profile.d
cp $RPM_SOURCE_DIR/qmail-linux.sh $RPM_BUILD_ROOT/etc/profile.d/qmail.sh
cp $RPM_SOURCE_DIR/qmail-linux.csh $RPM_BUILD_ROOT/etc/profile.d/qmail.csh
chmod a+x $RPM_BUILD_ROOT/etc/profile.d/qmail*
cp $RPM_SOURCE_DIR/qmail-1.03-linux.init $RPM_BUILD_ROOT/etc/rc.d/init.d/qmail

chmod a+x $RPM_BUILD_ROOT/etc/rc.d/init.d/qmail

mkdir -p $RPM_BUILD_ROOT/usr/sbin
(cd $RPM_BUILD_ROOT/usr/sbin; ln -sf ../../var/qmail/bin/sendmail)

# Set up mailing aliases
cp $RPM_SOURCE_DIR/qmail-aliases $RPM_BUILD_ROOT/etc/aliases
(cd $RPM_BUILD_ROOT/etc/qmail/alias;
touch .qmail-root;
cp $RPM_SOURCE_DIR/qmail-msglog  .qmail-msglog
cp $RPM_SOURCE_DIR/qmail-default .qmail-default
chmod 644 .qmail*
)

# Set up control files.
(cd $RPM_BUILD_ROOT/etc/qmail/control;
touch defaultdomain locals me plusdomain qmqpservers rcpthosts;
chmod 644 defaultdomain locals me plusdomain qmqpservers rcpthosts;
)

# Set up blank qmail/users
(cd $RPM_BUILD_ROOT/etc/qmail/users;
touch assign include exclude mailnames subusers append
)

# Set up default delivery
cp $RPM_SOURCE_DIR/qmail-default-delivery $RPM_BUILD_ROOT/etc/qmail/dot-qmail

# DOT FORWARD command and doc
cp dot-forward-0.71/dot-forward $RPM_BUILD_ROOT/var/qmail/bin
cp dot-forward-0.71/*.1 $RPM_BUILD_ROOT/var/qmail/man/man1

# FAST FORWARD commands and docs
cp fastforward-0.51/fastforward $RPM_BUILD_ROOT/var/qmail/bin
cp fastforward-0.51/newaliases $RPM_BUILD_ROOT/var/qmail/bin
cp fastforward-0.51/newinclude $RPM_BUILD_ROOT/var/qmail/bin
cp fastforward-0.51/printforward $RPM_BUILD_ROOT/var/qmail/bin
cp fastforward-0.51/printmaillist $RPM_BUILD_ROOT/var/qmail/bin
cp fastforward-0.51/setforward $RPM_BUILD_ROOT/var/qmail/bin
cp fastforward-0.51/setmaillist $RPM_BUILD_ROOT/var/qmail/bin
cp fastforward-0.51/*.1 $RPM_BUILD_ROOT/var/qmail/man/man1
cp fastforward-0.51/ALIASES $RPM_BUILD_ROOT/usr/doc/qmail-%{version}

# RBLSMTPD commands and doc
cp rblsmtpd-0.70/antirbl $RPM_BUILD_ROOT/var/qmail/bin
cp rblsmtpd-0.70/rblsmtpd $RPM_BUILD_ROOT/var/qmail/bin
cp rblsmtpd-0.70/*.8 $RPM_BUILD_ROOT/var/qmail/man/man8

# Fix for packaging so we don't have wierd things happen when unpacking it.
chown -R root:root $RPM_BUILD_ROOT

# Add rc boot script
echo "#! /bin/sh" > $RPM_BUILD_ROOT/var/qmail/rc
echo "/etc/rc.d/init.d/qmail start" >> $RPM_BUILD_ROOT/var/qmail/rc
chmod a+rx $RPM_BUILD_ROOT/var/qmail/rc


%pre
# If package is being installed for the first time
if [ $1 = 1 ]; then

groupadd -g 80 nofiles || %{user_group_error};
useradd -M -c qmail -s /bin/true -g nofiles -d /var/qmail -u 80 qmaild || %{user_group_error};
useradd -M -c qmail -s /bin/true -g nofiles -d /var/qmail -u 85 qmaill || %{user_group_error};
useradd -M -c qmail -s /bin/true -g nofiles -d /var/qmail -u 86 qmailp || %{user_group_error};
useradd -M -c qmail -s /bin/true -g nofiles -d /var/qmail/alias -u 81 alias || %{user_group_error};
groupadd -g 81 qmail || %{user_group_error};
useradd -M -c qmail -s /bin/true -g qmail -d /var/qmail -u 82 qmailq || %{user_group_error};
useradd -M -c qmail -s /bin/true -g qmail -d /var/qmail -u 83 qmailr || %{user_group_error};
useradd -M -c qmail -s /bin/true -g qmail -d /var/qmail -u 84 qmails || %{user_group_error};

# Remove files put there by useradd.
rm -rf /var/qmail/.[a-zA-Z]*

chmod a+r /var/qmail
chown alias /var/qmail
# Because it is a symbolic link.
# rm -rf /var/qmail/alias

g=`grep -c "qmail" /etc/inetd.conf || true`
if [ $g -gt 0 ]; then
   true;
 else
   (cat /etc/$INET/services;
   echo "qmqp		628/tcp		qmqp		# QMAIL Queuing Protocol") > /etc/$INET/services.$$ && \
      mv /etc/$INET/services /etc/$INET/services.bak && \
      mv /etc/$INET/services.$$ /etc/$INET/services
   if [ -x /usr/sbin/tcpd ]; then
      (cat /etc/$INET/inetd.conf;
      echo "#smtp	stream  tcp 	nowait  qmaild  /usr/sbin/tcpd /var/qmail/bin/tcp-env /var/qmail/bin/qmail-smtpd";
      echo "#qmqp	stream  tcp 	nowait  qmaild  /usr/sbin/tcpd /var/qmail/bin/tcp-env /var/qmail/bin/qmail-qmqpd") > /etc/$INET/inetd.conf.$$ && \
      mv /etc/inetd.conf /etc/inetd.conf.bak && \
      mv /etc/inetd.conf.$$ /etc/inetd.conf
    else
      (cat /etc/inetd.conf;
      echo "#smtp	stream  tcp 	nowait  qmaild  /var/qmail/bin/tcp-env tcp-env /var/qmail/bin/qmail-smtpd";
      echo "#qmqp	stream  tcp 	nowait  qmaild  /var/qmail/bin/tcp-env tcp-env /var/qmail/bin/qmail-qmqpd") > /etc/$INET/inetd.conf.$$ && \
         mv /etc/inetd.conf /etc/inetd.conf.bak && \
         mv /etc/inetd.conf.$$ /etc/inetd.conf
   fi
fi

# End Package installed for first time.
fi


%post
%{brand}

# Set file permissions.
chown alias:qmail /etc/qmail/alias
# Set for user access.
chmod u+s /var/qmail/bin/qmail-qread

# Run configuration script.
./config >> /tmp/qmail.install.$$.log 2>&1

# Set up aliases
/var/qmail/bin/newaliases

/sbin/chkconfig --add qmail


%preun
if [ -f /etc/rc.d/init.d/qmail ]; then
        /etc/rc.d/init.d/qmail stop
	/sbin/chkconfig --del qmail
fi

# If package is being erased for the last time.
if [ $1 = 0 ]; then
    #echo "Removing qmail from /etc/$INET/inetd.conf"
    sed -e '/qmail/d' /etc/$INET/inetd.conf > /etc/$INET/inetd.conf.$$ && \
       mv /etc/$INET/inetd.conf /etc/$INET/inetd.conf.bak && \
       mv /etc/$INET/inetd.conf.$$ /etc/$INET/inetd.conf
    sed -e '/qmqp/d' /etc/$INET/services > /etc/$INET/services.$$ && \
       mv /etc/$INET/services /etc/$INET/services.bak && \
       mv /etc/$INET/services.$$ /etc/$INET/services
    # Need to kill -HUP inetd

    # Delete qmail users
    userdel alias    || true;
    userdel qmaild   || true;
    userdel qmailq   || true;
    userdel qmailr   || true;
    userdel qmails   || true;
    userdel qmaill   || true;
    userdel qmailp   || true;

    # Delete qmail groups
    groupdel qmail   || true;
    groupdel nofiles || true;

fi


%pre msglog
/etc/rc.d/init.d/qmail stop

%post msglog
cd /var/qmail/bin
mv qmail-queue qmail-queue.pre.msglog
cp qmail-queue.msglog qmail-queue
%{brand}

%preun msglog
if [ -f /usr/bin/qmail/qmail-queue.pre.msglog ]; then
   cd /usr/bin/qmail
   mv qmail-queue.pre.msglog qmail-queue
fi


%clean
rm -rf $RPM_BUILD_ROOT


%files
%config /etc/aliases
%config /etc/qmail/alias/.qmail-root
%config /etc/qmail/alias/.qmail-default
%config /etc/qmail/dot-qmail
%config /etc/qmail/control/defaultdomain
%config /etc/qmail/control/locals
%config /etc/qmail/control/me
%config /etc/qmail/control/plusdomain
%config /etc/qmail/control/rcpthosts
%config /etc/qmail/users
%config /etc/profile.d/*
%docdir /usr/doc/qmail-%{version}
%docdir /usr/man
/etc/rc.d/init.d/qmail
/usr/bin/mailq
/usr/bin/qmail/*
%dir /usr/bin/qmail
/usr/sbin/sendmail
/usr/doc/qmail-%{version}
/usr/man/man*/*
/usr/lib/qmail/*
/var/qmail

# qmail-msglog package file list.
%files msglog
%config /etc/qmail/alias/.qmail-msglog
/usr/bin/qmail/qmail-queue.msglog
