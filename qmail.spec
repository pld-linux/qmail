Summary:     qmail Mail Transport Agent
Summary(pl): qmail - serwer pocztowy (MTA)
Name:        qmail
Version:     1.03
Release:     13
Group:       Networking/Daemons
Group(pl):   Sieciowe/Serwery
Copyright:   Check with djb@koobera.math.uic.edu
URL:         http://www.qmail.org/
Source0:     ftp://koobera.math.uic.edu/pub/software/qmail-1.03.tar.gz
Source1:     ftp://koobera.math.uic.edu/pub/software/dot-forward-0.71.tar.gz
Source2:     ftp://koobera.math.uic.edu/pub/software/fastforward-0.51.tar.gz
Source3:     ftp://koobera.math.uic.edu/pub/software/rblsmtpd-0.70.tar.gz
Source4:     ftp://koobera.math.uic.edu/pub/software/checkpassword-0.76.shar.gz
Source5:     http://www.netmeridian.com/e-huss/queue-fix.tar.gz
Source6:     http://www.io.com/~mick/soft/qmHandle-0.4.0.tar.gz
Source7:     qmail-1.03-linux.init
Source8:     qmail-linux.sh
Source9:     qmail-linux.csh
Source10:    qmail-aliases
Source11:    qmail-default
Source12:    qmail-msglog
Source13:    qmail-default-delivery
Source14:    qmail-lint-0.51.pl
Source15:    qmail-qsanity-0.51.pl
Source16:    tarpit.README
Patch0:      qmail-1.03.install.patch
Patch1:      qmail-1.03.msglog.patch
Patch2:      qmail-1.03.redhat.patch
Patch3:      qmail-1.03.fixed-ids.patch
Patch4:      qmail-1.03.rbl.conf.patch
Patch5:      qmail-1.03.mklinux.patch
Patch6:      qmail-relayclientexternal.patch
Patch7:      qmail-1.03.checkpassword.patch
Patch8:      tarpit.patch
Patch9:      qmail-1.03-maxrcpt.patch
Patch10:     qmHandle.PLD-init.patch
Patch11:     qmail-1.03-IPv6-PLD.patch
BuildRoot:   /tmp/%{name}-%{version}-root
Provides:    smtpdaemon
Provides:    qmailmta
Provides:    qmail-server
Requires:    %{_sbindir}/tcpd
Prereq:      /sbin/chkconfig
Prereq:      /bin/hostname
Prereq:      /bin/sed
Conflicts:   qmail-client
Obsoletes:   smtpdaemon

%description
qmail is a small, fast, secure replacement for the SENDMAIL package, which is
the program that actually receives, routes, and delivers electronic mail.
This qmail also support IPv6 protocol.

Following scripts and programs have been added:

================================================================================
 Name                 Features
================================================================================
checkpassword        password-checking interface
--------------------------------------------------------------------------------
qmHandle             more powerful viewing and managing qmail queue
                     (remote and local)
--------------------------------------------------------------------------------
rblsmtpd             a generic tool to block mail from RBL-listed sites; 
                     an optional way to fight SPAM
--------------------------------------------------------------------------------
qmail-fix            a small utility for checking and repairing the qmail
                     queue structure
--------------------------------------------------------------------------------
qmail-msglog         advanced e-mail monitoring
--------------------------------------------------------------------------------
qmail-qsanity        examine all the files in the qmail queue
--------------------------------------------------------------------------------
qmail-lint           examine the qmail configuration
--------------------------------------------------------------------------------
tarpit               tool to fight with SPAM
================================================================================

*** Note: Be sure and read the documentation as there are some small but very
significant differences between SENDMAIL and QMAIL and the programs that
interact with them.

%description -l pl
qmail jest ma³±, szybk± oraz bezpieczn± alternatyw± do sendmail-a, która
umo¿liwia otrzymywanie, przesy³anie oraz wysy³anie poczty elektronicznej.
Ten qmail dodatkowo wspiera protokó³ IPv6.

Zosta³y dodane do tego pakietu nastêpuj±ce skrypty i programy:

================================================================================
 Nazwa                Opis
================================================================================
checkpassword        interfejs do sprawdzania hase³
--------------------------------------------------------------------------------
qmHandle             bardziej zaawansowane przegl±danie oraz zarz±dzanie
                     kolejk± pocztow±
--------------------------------------------------------------------------------
rblsmtpd             podstawowe narzêdzie do blokowania listów z miejsc
                     wyszczególnionych w RBL; sposób na walkê ze SPAM-em
--------------------------------------------------------------------------------
qmail-fix            program do sprawdzania oraz naprawiania struktury kolejki 
                     pocztowej qmail-a
--------------------------------------------------------------------------------
qmail-msglog         zaawansowane monitorowanie listów
--------------------------------------------------------------------------------
qmail-qsanity        sprawdza kolejkê pocztow± qmail-a
--------------------------------------------------------------------------------
qmail-lint           sprawdza konfiguracjê qmail-a
--------------------------------------------------------------------------------
tarpit               kolejne narzêdzie do walki ze SPAM-em
================================================================================

*** Uwaga! Przeczytaj uwa¿nie dokumentacjê do tego pakietu, poniewa¿ istniej± 
ma³e, ale znacz±ce róznice pomiêdzy qmail-em oraz sendmail-em i programami,
które wspó³pracuj± z nimi.


%prep
%setup -q
%setup -D -T -q -a 1
%setup -D -T -q -a 2
%setup -D -T -q -a 3
install -d checkpassword-0.76
(cd checkpassword-0.76; gzip -dc %{SOURCE4} | /bin/sh)
%setup -D -T -q -a 5
install -d qmHandle-0.4.0
tar zxf %{SOURCE6} -C qmHandle-0.4.0/
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0
%ifarch ppc
%patch5 -p0
%endif
%patch6 -p1
%patch7 -p1
%patch8 -p0
%patch9 -p0
%patch10 -p0
%patch11 -p1


%build
make CFLAGS="$RPM_OPT_FLAGS"
make man
make -C dot-forward-0.71
make -C fastforward-0.51
make -C rblsmtpd-0.70
make -C queue-fix-1.3
make -C checkpassword-0.76 SHADOWLIBS=-DPW_SHADOW


%install
rm -rf $RPM_BUILD_ROOT
install -d boot
install -d $RPM_BUILD_ROOT/etc/{qmail/{alias,control,users},rc.d/init.d,profile.d}
install -d $RPM_BUILD_ROOT/{usr/{bin/qmail,lib,man,sbin},var/qmail}
install -d $RPM_BUILD_ROOT/%{_mandir}
install -d $RPM_BUILD_ROOT/%{_libdir}/qmail
ln -sf ../../etc/qmail/alias $RPM_BUILD_ROOT/var/qmail/
ln -sf ../../etc/qmail/control $RPM_BUILD_ROOT/var/qmail/
ln -sf ../../etc/qmail/users $RPM_BUILD_ROOT/var/qmail/
ln -sf ../..%{_libdir}/qmail $RPM_BUILD_ROOT/var/qmail/bin
ln -sf ../..%{_mandir} $RPM_BUILD_ROOT/var/qmail/man
ln -sf $RPM_BUILD_DIR/%{name}-%{version}/boot $RPM_BUILD_ROOT/var/qmail/boot

./install -s $RPM_BUILD_ROOT

ln -s qmail-qread $RPM_BUILD_ROOT%{_bindir}/mailq
ln -sf ../../var/qmail/bin/sendmail $RPM_BUILD_ROOT%{_sbindir}/sendmail
ln -sf ../../var/qmail/bin/sendmail $RPM_BUILD_ROOT%{_libdir}/sendmail

# Set up boot procedures
install %{SOURCE7} $RPM_BUILD_ROOT/etc/rc.d/init.d/qmail
install %{SOURCE8} $RPM_BUILD_ROOT/etc/profile.d/qmail.sh
install %{SOURCE9} $RPM_BUILD_ROOT/etc/profile.d/qmail.csh

# Set up mailing aliases
install %{SOURCE10} $RPM_BUILD_ROOT/etc/aliases
install %{SOURCE11} $RPM_BUILD_ROOT/etc/qmail/alias/.qmail-default
install %{SOURCE12} $RPM_BUILD_ROOT/etc/qmail/alias/.qmail-msglog

for i in mailer-daemon postmaster root; do
	touch $RPM_BUILD_ROOT/etc/qmail/alias/.qmail-$i
done

# Set up control files.
touch $RPM_BUILD_ROOT/etc/qmail/control/{defaultdomain,locals,me,plusdomain,rcpthosts}

# Set up blank qmail/users
touch $RPM_BUILD_ROOT/etc/qmail/users/{assign,include,exclude,mailnames,subusers,append}

# Set up default delivery
install %{SOURCE13} $RPM_BUILD_ROOT/etc/qmail/dot-qmail

install %{SOURCE14} $RPM_BUILD_ROOT/var/qmail/bin/qmail-lint
install %{SOURCE15} $RPM_BUILD_ROOT/var/qmail/bin/qmail-qsanity

# qmHandle command
install qmHandle-0.4.0/qmHandle $RPM_BUILD_ROOT/var/qmail/bin/qmHandle

# QUEUE FIX command
install queue-fix-1.3/queue-fix $RPM_BUILD_ROOT/var/qmail/bin

# CHECKPASSWORD command
install checkpassword-0.76/checkpassword $RPM_BUILD_ROOT/var/qmail/bin

# DOT FORWARD command and doc
install dot-forward-0.71/dot-forward $RPM_BUILD_ROOT/var/qmail/bin
install dot-forward-0.71/dot-forward.1 $RPM_BUILD_ROOT/var/qmail/man/man1

# FAST FORWARD commands and docs
install fastforward-0.51/fastforward $RPM_BUILD_ROOT/var/qmail/bin
install fastforward-0.51/newaliases $RPM_BUILD_ROOT/var/qmail/bin
install fastforward-0.51/newinclude $RPM_BUILD_ROOT/var/qmail/bin
install fastforward-0.51/printforward $RPM_BUILD_ROOT/var/qmail/bin
install fastforward-0.51/printmaillist $RPM_BUILD_ROOT/var/qmail/bin
install fastforward-0.51/setforward $RPM_BUILD_ROOT/var/qmail/bin
install fastforward-0.51/setmaillist $RPM_BUILD_ROOT/var/qmail/bin
install fastforward-0.51/*.1 $RPM_BUILD_ROOT/var/qmail/man/man1/

# RBLSMTPD commands and doc
install rblsmtpd-0.70/antirbl $RPM_BUILD_ROOT/var/qmail/bin
install rblsmtpd-0.70/rblsmtpd $RPM_BUILD_ROOT/var/qmail/bin
install rblsmtpd-0.70/*.8 $RPM_BUILD_ROOT/var/qmail/man/man8

# default folder in /etc/skel
install -d $RPM_BUILD_ROOT/etc/skel/Mail
./maildirmake $RPM_BUILD_ROOT/etc/skel/Mail/Maildir

(set +x; rm -f checkpassword-0.76/{[a-z]*,Makefile,FILES})
(set +x; rm -f dot-forward-0.71/{[a-z]*,Makefile,FILES,SYSDEPS,TARGETS})
(set +x; rm -f fastforward-0.51/{[a-z]*,Makefile,FILES,SYSDEPS,TARGETS})
(set +x; rm -f rblsmtpd-0.70/{[a-z]*,Makefile,FILES,SYSDEPS,TARGETS})
(set +x; rm -f queue-fix-1.3/{[a-z]*,Makefile,TARGETS})
(set +x; rm -f qmHandle-0.4.0/q*)

cp $RPM_SOURCE_DIR/tarpit.README .

# What else?
mv $RPM_BUILD_ROOT/var/qmail/bin/maildir2mbox     $RPM_BUILD_ROOT/usr/bin/
mv $RPM_BUILD_ROOT/var/qmail/bin/maildirmake      $RPM_BUILD_ROOT/usr/bin/
mv $RPM_BUILD_ROOT/var/qmail/bin/maildirwatch     $RPM_BUILD_ROOT/usr/bin/
mv $RPM_BUILD_ROOT/var/qmail/bin/qmHandle         $RPM_BUILD_ROOT/usr/bin/
mv $RPM_BUILD_ROOT/var/qmail/bin/qmail-qread      $RPM_BUILD_ROOT/usr/bin/
mv $RPM_BUILD_ROOT/var/qmail/bin/qmail-qsanity    $RPM_BUILD_ROOT/usr/bin/
mv $RPM_BUILD_ROOT/var/qmail/bin/qmail-qstat      $RPM_BUILD_ROOT/usr/bin/
mv $RPM_BUILD_ROOT/var/qmail/bin/queue-fix        $RPM_BUILD_ROOT/usr/bin/
mv $RPM_BUILD_ROOT/var/qmail/bin/newaliases       $RPM_BUILD_ROOT/usr/bin/

gzip -9nf FAQ INSTALL* PIC* REMOVE* SENDMAIL TEST* UPGRADE
gzip -9nf BLURB* README SECURITY THANKS THOUGHTS TODO VERSION
gzip -9nf boot/* checkpassword-0.76/* qmHandle-0.4.0/* queue-fix-1.3/*
gzip -9nf rblsmtpd-0.70/* tarpit.README
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/*

%pre
# If package is being installed for the first time
if [ $1 = 1 ]; then
	g=`grep -c "qmail" /etc/inetd.conf || true`
	if [ $g -gt 0 ]; then
		echo "qmail already installed in /etc/inetd.conf, no need to add."
	else
		echo "Adding qmail to /etc/inetd.conf and /etc/services."
		cp -f /etc/services /etc/services.pre-qmail
		echo "qmqp		628/tcp		qmqp		# QMAIL Queuing Protocol" >> /etc/services
		echo >> /etc/services
		cp -f /etc/inetd.conf /etc/inetd.conf.pre-qmail
		echo "#smtp	stream  tcp 	nowait  qmaild  %{_sbindir}/tcpd /var/qmail/bin/tcp-env /var/qmail/bin/qmail-smtpd" >> /etc/inetd.conf
		echo "#qmqp	stream  tcp 	nowait  qmaild  %{_sbindir}/tcpd /var/qmail/bin/tcp-env /var/qmail/bin/qmail-qmqpd" >> /etc/inetd.conf
		echo >> /etc/inetd.conf
	fi

# Add few users and groups
%{_sbindir}/groupadd -f -g 81 nofiles
%{_sbindir}/groupadd -f -g 82 qmail
%{_sbindir}/useradd -M -g nofiles -d /var/qmail/ -u 81 -s /bin/true qmaild 2> /dev/null
%{_sbindir}/useradd -M -g nofiles -d /var/qmail/alias/ -u 82 -s /bin/true alias 2> /dev/null
%{_sbindir}/useradd -M -g qmail -d /var/qmail/ -u 83 -s /bin/true qmailq 2> /dev/null
%{_sbindir}/useradd -M -g qmail -d /var/qmail/ -u 84 -s /bin/true qmailr 2> /dev/null
%{_sbindir}/useradd -M -g qmail -d /var/qmail/ -u 85 -s /bin/true qmails 2> /dev/null
%{_sbindir}/useradd -M -g nofiles -d /var/qmail/ -u 86 -s /bin/true qmaill 2> /dev/null
%{_sbindir}/useradd -M -g nofiles -d /var/qmail/ -u 87 -s /bin/true qmailp 2> /dev/null

fi


%post
if [ ! -s /etc/qmail/control/me ]; then
	FQDN=`/bin/hostname -f`
	echo "$FQDN" > /etc/qmail/control/me
	echo "$FQDN" | /bin/sed 's/^\([^\.]*\)\.\([^\.]*\)\./\2\./' > /etc/qmail/control/defaultdomain
	echo "$FQDN" | /bin/sed 's/^.*\.\([^\.]*\)\.\([^\.]*\)$/\1.\2/' > /etc/qmail/control/plusdomain
	echo "$FQDN" >> /etc/qmail/control/locals
	echo "$FQDN" >> /etc/qmail/control/rcpthosts
	chmod 644 /etc/qmail/control/*

	echo "Now qmail will refuse to accept SMTP messages except to $FQDN."
	echo "Make sure to change rcpthosts if you add hosts to locals or virtualdomains!"
	echo Enter user, who should receive mail for root, mailer-daemon and postmaster
	echo into /etc/qmail/alias/.qmail-\{root,mailer-daemon,postmaster\}
fi
# Set up aliases
%{_bindir}/newaliases
/sbin/chkconfig --add qmail


%preun
# If package is being erased for the last time.
if [ $1 = 0 ]; then
	/etc/rc.d/init.d/qmail stop
	/sbin/chkconfig --del qmail

	echo "Remember to restart INETD (killall -HUP inetd)"
fi

%postun
# If package is being erased for the last time.
if [ $1 = 0 ]; then
%{_sbindir}/userdel qmaild 2> /dev/null
%{_sbindir}/userdel alias 2> /dev/null
%{_sbindir}/userdel qmaill 2> /dev/null
%{_sbindir}/userdel qmailp 2> /dev/null
%{_sbindir}/userdel qmailq 2> /dev/null
%{_sbindir}/userdel qmailr 2> /dev/null
%{_sbindir}/userdel qmails 2> /dev/null
%{_sbindir}/userdel qmail 2> /dev/null

%{_sbindir}/groupdel nofiles 2> /dev/null
%{_sbindir}/groupdel qmail 2> /dev/null
fi

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc {FAQ,INSTALL*,PIC*,REMOVE*,SENDMAIL,TEST*,UPGRADE}.gz
%doc {BLURB*,README,SECURITY,THANKS,THOUGHTS,TODO,VERSION}.gz
%doc checkpassword-0.76/ queue-fix-1.3/ qmHandle-0.4.0/ rblsmtpd-0.70/ boot/ 
%doc tarpit.README.gz

%attr( 755,   root,  root) %dir /etc/qmail
%attr(2755,  alias, qmail) %dir /etc/qmail/alias
%attr( 755,   root, qmail) %dir /etc/qmail/control
%attr( 755,   root,  root) %dir /etc/qmail/users
%attr( 755,   root, qmail) %dir %{_libdir}/qmail
%attr( 755,   root, qmail) %dir /var/qmail
%attr( 750, qmailq, qmail) %dir /var/qmail/queue
%attr( 750, qmailq, qmail) %dir /var/qmail/queue/lock
%attr( 644,   root, qmail) %config(noreplace) %verify(not size mtime md5) /etc/qmail/alias/.qmail-*
%attr( 644,   root, qmail) %config(noreplace) %verify(not size mtime md5) /etc/qmail/dot-qmail
%attr( 644,   root, qmail) %config(noreplace) %verify(not size mtime md5) /etc/qmail/control/*
%attr( 644,   root, qmail) %config(noreplace) %verify(not size mtime md5) /etc/qmail/users/*
%attr( 755,   root,  root) %config(noreplace) %verify(not size mtime md5) /etc/profile.d/*
%attr( 754,   root,  root) %config(noreplace) %verify(not size mtime md5) /etc/rc.d/init.d/*
%attr( 644,   root,  root) %config(noreplace) %verify(not size mtime md5) /etc/aliases
%attr( 755,   root, qmail) %{_libdir}/qmail/bouncesaying
%attr( 755,   root, qmail) %{_libdir}/qmail/condredirect
%attr( 755,   root, qmail) %{_libdir}/qmail/checkpassword
%attr( 755,   root, qmail) %{_libdir}/qmail/datemail
%attr( 755,   root, qmail) %{_libdir}/qmail/elq
%attr( 755,   root, qmail) %{_libdir}/qmail/except
%attr( 755,   root, qmail) %{_libdir}/qmail/forward
%attr( 755,   root, qmail) %{_bindir}/maildir2mbox
%attr( 755,   root, qmail) %{_bindir}/maildirmake
%attr( 755,   root, qmail) %{_bindir}/maildirwatch
%attr( 755,   root, qmail) %{_libdir}/qmail/mailsubj
%attr( 755,   root, qmail) %{_libdir}/qmail/pinq
%attr( 755,   root, qmail) %{_libdir}/qmail/predate
%attr( 755,   root, qmail) %{_libdir}/qmail/preline
%attr( 755,   root, qmail) %{_libdir}/qmail/qail
%attr( 755,   root, qmail) %{_libdir}/qmail/qbiff
%attr( 754,   root, qmail) %{_bindir}/qmHandle
%attr( 711,   root, qmail) %{_libdir}/qmail/qmail-clean
%attr( 711,   root, qmail) %{_libdir}/qmail/qmail-getpw
%attr( 755,   root, qmail) %{_libdir}/qmail/qmail-inject
%attr( 755,   root,  root) %{_libdir}/qmail/qmail-lint
%attr( 711,   root, qmail) %{_libdir}/qmail/qmail-local
%attr( 700,   root, qmail) %{_libdir}/qmail/qmail-lspawn
%attr( 700,   root, qmail) %{_libdir}/qmail/qmail-newmrh
%attr( 700,   root, qmail) %{_libdir}/qmail/qmail-newu
%attr( 755,   root, qmail) %{_libdir}/qmail/qmail-pop3d
%attr( 711,   root, qmail) %{_libdir}/qmail/qmail-popup
%attr( 711,   root, qmail) %{_libdir}/qmail/qmail-pw2u
%attr( 755,   root, qmail) %{_libdir}/qmail/qmail-qmqpc
%attr( 755,   root, qmail) %{_libdir}/qmail/qmail-qmqpd
%attr( 755,   root, qmail) %{_libdir}/qmail/qmail-qmtpd
%attr( 755,   root, qmail) %{_bindir}/qmail-qread
%attr( 755,   root,  root) %{_bindir}/qmail-qsanity
%attr( 755,   root, qmail) %{_bindir}/qmail-qstat
%attr(4711, qmailq, qmail) %{_libdir}/qmail/qmail-queue
%attr( 711,   root, qmail) %{_libdir}/qmail/qmail-remote
%attr( 711,   root, qmail) %{_libdir}/qmail/qmail-rspawn
%attr( 711,   root, qmail) %{_libdir}/qmail/qmail-send
%attr( 755,   root, qmail) %{_libdir}/qmail/qmail-showctl
%attr( 755,   root, qmail) %{_libdir}/qmail/qmail-smtpd
%attr( 700,   root, qmail) %{_libdir}/qmail/qmail-start
%attr( 755,   root, qmail) %{_libdir}/qmail/qmail-tcpok
%attr( 755,   root, qmail) %{_libdir}/qmail/qmail-tcpto
%attr( 755,   root, qmail) %{_libdir}/qmail/qreceipt
%attr( 755,   root, qmail) %{_libdir}/qmail/qsmhook
%attr( 751,   root,  root) %{_bindir}/queue-fix
%attr( 755,   root, qmail) %{_libdir}/qmail/sendmail
%attr( 711,   root, qmail) %{_libdir}/qmail/splogger
%attr( 755,   root, qmail) %{_libdir}/qmail/tcp-env
%attr( 755,   root,  root) %{_libdir}/qmail/dot-forward
%attr( 755,   root,  root) %{_libdir}/qmail/fastforward
%attr( 755,   root,  root) %{_bindir}/newaliases
%attr( 755,   root,  root) %{_libdir}/qmail/newinclude
%attr( 755,   root,  root) %{_libdir}/qmail/printforward
%attr( 755,   root,  root) %{_libdir}/qmail/printmaillist
%attr( 755,   root,  root) %{_libdir}/qmail/setforward
%attr( 755,   root,  root) %{_libdir}/qmail/setmaillist
%attr( 755,   root,  root) %{_libdir}/qmail/antirbl
%attr( 755,   root,  root) %{_libdir}/qmail/rblsmtpd
%attr( 777,   root,  root) %{_bindir}/mailq
%attr( 777,   root,  root) %{_sbindir}/sendmail
%attr( 777,   root,  root) %{_libdir}/sendmail
%attr( 777,  alias, qmail) /var/qmail/alias
%attr( 777,   root, qmail) /var/qmail/bin
%attr( 777,   root, qmail) /var/qmail/control
%attr( 777,   root, qmail) /var/qmail/users
%attr( 700, qmails, qmail) /var/qmail/queue/bounce
%attr( 700, qmails, qmail) /var/qmail/queue/info
%attr( 700, qmailq, qmail) /var/qmail/queue/intd
%attr( 700, qmails, qmail) /var/qmail/queue/local
%attr( 750, qmailq, qmail) /var/qmail/queue/mess
%attr( 700, qmailq, qmail) /var/qmail/queue/pid
%attr( 700, qmails, qmail) /var/qmail/queue/remote
%attr( 750, qmailq, qmail) /var/qmail/queue/todo
%attr( 600, qmails, qmail) %config(noreplace) %verify(not mtime md5) /var/qmail/queue/lock/sendmutex
%attr( 644, qmailr, qmail) %config(noreplace) %verify(not mtime md5) /var/qmail/queue/lock/tcpto
%attr( 622, qmails, qmail) %config(noreplace) %verify(not mtime md5) /var/qmail/queue/lock/trigger
%{_mandir}/man*/*

# default folder - Maildir/
%attr( 700,   root,  root) %dir /etc/skel/Mail
%attr( 700,   root,  root) %dir /etc/skel/Mail/Maildir
%attr( 700,   root,  root) %dir /etc/skel/Mail/Maildir/cur
%attr( 700,   root,  root) %dir /etc/skel/Mail/Maildir/new
%attr( 700,   root,  root) %dir /etc/skel/Mail/Maildir/tmp


%changelog
* Wed Jun 23 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [1.0.3-13]
- "Obsoletes: smtpdaemon" instead a lot of obsoletes
- install -d instead mkdir

* Sat Jun 05 1999 Arkadiusz Mi¶kiewicz <misiek@pld.org.pl>
- qmail's users and groups are added in %pre script
  and removed in %postun
- corrected IPv6 patch (not tested yet)
- removed Requires: setup (now it's obsolete)
- modified UIDs and GID in qmail-1.03.fixed-ids.patch
  to avoid conflict with amanda (see uid_gid.db.txt for details)
- fixed qmail-1.03.checkpassword.patch for shadow passwords

* Tue May 18 1999 Jan Rêkorajski <baggins@hunter.mimuw.edu.pl>
  [1.03-10]
- removed relay-allow patch - I realized it was dumb, and added
  relayclientexternal which is better solution of the problem
  (relaying besed on MAIL FROM:)

* Sun May 02 1999 Artur Wróblewski <wrobell@posexperts.com.pl>
  [1.03-9]
- gzipped manpages and documentation
- linux init script modified for PLD
- more package descriptions
- polish translations
- switch to Maildir/ folders (default now)
- default Maildir/ folder in /etc/skel/Mail
- patched qmHandle to stop and start qmail with /etc/rc.d/init.d/qmail
- perl scripts without .pl suffix

* Sun Feb 21 1999 Jan Rêkorajski <baggins@hunter.mimuw.edu.pl>
  [1.03-8]
- cleaned up this mess
- %defattr/%attr macros
- Solaris/SunOS > /dev/null
- added my control/goodmailfrom patch
- fixed init script to use chkconfig
- assume that users and groups already exist with fixed uids (see %{PATCH8})
	and added Requires: setup >= 1.10.0-3 (PLD version)
- seperated qmail-client package
- removed qmail-msglog package - msglog is a standard feature now
- made real %pre/%post/%preun scripts
- removed useless binaries from %{_bindir}/qmail like config or install
- added checkpassword-0.76 program
- added qmail-lint-0.51.pl and qmail-qsanity-0.51.pl scripts
- added qmHandle-0.3.0.tar.gz script
- added queue-fix.tar.gz program

* Tue Sep 01 1998 David W. Summers <david@summersoft.fay.ar.us>

Release 7:
- Patch to work with MkLinux DR3.

* Wed Aug 26 1998 David W. Summers <david@summersoft.fay.ar.us>

Release 6:
- Changed rblsmtpd to optionally print logging information so by default it
won't print out to the SMTP socket when used with INETD.

* Mon Aug 24 1998 David W. Summers <david@summersoft.fay.ar.us>

Release 5:
- Changed to rblsmtpd-0.70 package.

* Fri Aug 14 1998 David W. Summers <david@summersoft.fay.ar.us>

Release 4:
- Added rblsmtpd-0.50 package.
- Fixed dot-forward and fast forward packages not to complain while compiling on
  Solaris.
- Added documentation that qmail install didn't get.

* Wed Aug 05 1998 David W. Summers <david@summersoft.fay.ar.us>

Release 3:
- Added dot-forward-0.71 package.
- Added fastforward-0.51 package.

* Fri Jun 19 1998 David W. Summers <david@summersoft.fay.ar.us>

Release 2:
- Now creates backups of /etc/inetd.conf and /etc/services files.
- Fixed problem with wiping out /etc/services caused by misplaced parenthesis.

* Mon Jun 15 1998 David W. Summers <david@summersoft.fay.ar.us>

Release 1:
- conf-patrn flip-flopped from 1.02 to 1.03, hence qmail-1.03.solaris.patch.
- Started with qmail-1.03 sources and qmail-1.02-9.spec file.
