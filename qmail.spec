Summary:	qmail Mail Transport Agent
Summary(pl):	qmail - serwer pocztowy (MTA)
Name:		qmail
Version:	1.03
Release:	26
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Copyright:	Check with djb@koobera.math.uic.edu
URL:		http://www.qmail.org/
Source0:	ftp://koobera.math.uic.edu/pub/software/%{name}-%{version}.tar.gz
Source1:	ftp://koobera.math.uic.edu/pub/software/dot-forward-0.71.tar.gz
Source2:	ftp://koobera.math.uic.edu/pub/software/fastforward-0.51.tar.gz
Source3:	ftp://koobera.math.uic.edu/pub/software/rblsmtpd-0.70.tar.gz
Source4:	ftp://ftp.pld.org.pl/people/zagrodzki/checkpass-1.0.tar.gz
Source5:	http://www.netmeridian.com/e-huss/queue-fix.tar.gz
Source6:	http://www.io.com/~mick/soft/qmHandle-0.4.0.tar.gz
Source7:	%{name}.init
Source8:	%{name}-linux.sh
Source9:	%{name}-linux.csh
Source10:	%{name}-aliases
Source11:	%{name}-default
Source12:	%{name}-msglog
Source13:	%{name}-default-delivery
Source14:	%{name}-lint-0.51.pl
Source15:	%{name}-qsanity-0.51.pl
Source16:	tarpit.README
Source17:	%{name}-qmqp.inetd
Source18:	%{name}-smtp.inetd
Source19:	%{name}-qpop.inetd
Source20:	checkpassword.pamd
Source21:	%{name}-client.html
Patch0:		%{name}-1.03.install.patch
Patch1:		%{name}-1.03.msglog.patch
Patch2:		%{name}-1.03.redhat.patch
Patch3:		%{name}-1.03.fixed-ids.patch
Patch4:		%{name}-1.03.rbl.conf.patch
Patch5:		%{name}-1.03.mklinux.patch
Patch6:		%{name}-relayclientexternal.patch
Patch8:		tarpit.patch
Patch9:		%{name}-1.03-maxrcpt.patch
Patch10:	qmHandle.PLD-init.patch
Patch11:	%{name}-IPv6-PLD.patch
Patch12:	http://www.ckdhr.com/ckd/%{name}-dns.patch
Patch13:	ftp://dione.ids.pl/people/siewca/patches/%{name}-%{version}-etc.patch
Patch14:	%{name}-rblsmtpd-IPv6-PLD.patch
Patch15:	%{name}-rblsmtpd-syslog.patch
Patch16:	%{name}-smtpauth.patch
Patch18:	%{name}-wildmat.patch
Patch19:	%{name}-rblsmtpd-rss.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Provides:	smtpdaemon
Provides:	qmailmta
Provides:	qmail-server
Provides:	pop3daemon
Requires:	%{_sbindir}/tcpd
Requires:	inetdaemon
Requires:	rc-scripts >= 0.2.0
Prereq:		rc-inetd
Prereq:		/sbin/chkconfig
Prereq:		/bin/hostname
Prereq:		/bin/sed
Prereq:		sh-utils
Conflicts:	qmail-client
Obsoletes:	smtpdaemon
Obsoletes:	sendmail
Obsoletes:	postfix
Obsoletes:	zmailer
Obsoletes:	smail
Obsoletes:	exim
BuildRequires:	pam-devel

%description
qmail is a small, fast, secure replacement for the SENDMAIL package,
which is the program that actually receives, routes, and delivers
electronic mail. This qmail also support IPv6 protocol.

Following scripts and programs have been added:



================================================================================
Name Features
================================================================================
checkpass	- password-checking interface
qmHandle	- more powerful viewing and managing qmail queue (remote and
		  local)
rblsmtpd 	- a generic tool to block mail from RBL-listed sites; an
		  optional way to fight SPAM
qmail-fix	- a small utility for checking and repairing the qmail queue
		  structure
qmail-msglog	- advanced e-mail monitoring
qmail-qsanity	- examine all the files in the qmail queue
qmail-lint	- examine the qmail configuration
tarpit		- tool to fight with SPAM
================================================================================

- *** Note: Be sure and read the documentation as there are some small
  but very significant differences between SENDMAIL and QMAIL and the
  programs that interact with them.

%description -l pl
qmail jest ma³±, szybk± oraz bezpieczn± alternatyw± do sendmail-a,
która umo¿liwia otrzymywanie, przesy³anie oraz wysy³anie poczty
elektronicznej. Ten qmail dodatkowo wspiera protokó³ IPv6.

Zosta³y dodane do tego pakietu nastêpuj±ce skrypty i programy:



================================================================================
Nazwa Opis
================================================================================
checkpass	- interfejs do sprawdzania hase³
qmHandle	- bardziej zaawansowane przegl±danie oraz zarz±dzanie
		  kolejk± pocztow±
rblsmtpd	- podstawowe narzêdzie do blokowania listów z miejsc
		  wyszczególnionych w RBL; sposób na walkê ze SPAM-em
qmail-fix	- program do sprawdzania oraz naprawiania struktury kolejki
		  pocztowej qmail-a
qmail-msglog	- zaawansowane monitorowanie listów
qmail-qsanity	- sprawdza kolejkê pocztow± qmail-a
qmail-lint	- sprawdza konfiguracjê qmail-a
tarpit		- kolejne narzêdzie do walki ze SPAM-em
================================================================================

- *** Uwaga! Przeczytaj uwa¿nie dokumentacjê do tego pakietu, poniewa¿
  istniej± ma³e, ale znacz±ce róznice pomiêdzy qmail-em oraz sendmail-em
  i programami, które wspó³pracuj± z nimi.

%package client
Summary:	qmail Mail Transport Agent - null client
Summary(pl):	qmail - serwer pocztowy (MTA) - cienki klient
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Copyright:	Check with djb@koobera.math.uic.edu
URL:		http://www.qmail.org/
Provides:	smtpdaemon
Provides:	qmailmta
Prereq:		/bin/hostname
Prereq:		/bin/sed
Prereq:		sh-utils
Conflicts:	qmail
Obsoletes:	smtpdaemon
Obsoletes:	sendmail
Obsoletes:	postfix
Obsoletes:	zmailer
Obsoletes:	smail
Obsoletes:	exim

%description client
qmail is a small, fast, secure replacement for the SENDMAIL package,
which is the program that actually receives, routes, and delivers
electronic mail. This qmail also support IPv6 protocol.

%description -l pl client
qmail jest ma³±, szybk± oraz bezpieczn± alternatyw± do sendmail-a,
która umo¿liwia otrzymywanie, przesy³anie oraz wysy³anie poczty
elektronicznej. Ten qmail dodatkowo wspiera protokó³ IPv6.

%prep
%setup -q
%setup -D -T -q -a 1
%setup -D -T -q -a 2
%setup -D -T -q -a 3
%setup -D -T -q -a 4
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
%patch8 -p0
%patch9 -p0
%patch10 -p0
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p0
%patch18 -p1
%patch19 -p1

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS"
%{__make} man
%{__make} -C dot-forward-0.71
%{__make} -C fastforward-0.51
%{__make} -C rblsmtpd-0.70
%{__make} -C queue-fix-1.3
%{__make} -C checkpass-1.0

%install
rm -rf $RPM_BUILD_ROOT

install -d boot
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir},{%{_var},%{_bindir},%{_libdir}}/qmail}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{qmail/{alias,control,users},rc.d/init.d,profile.d,mail,sysconfig/rc-inetd,pam.d,security}

ln -sf ../..%{_sysconfdir}/qmail/alias $RPM_BUILD_ROOT/var/qmail/
ln -sf ../..%{_sysconfdir}/qmail/control $RPM_BUILD_ROOT/var/qmail/
ln -sf ../..%{_sysconfdir}/qmail/users $RPM_BUILD_ROOT/var/qmail/
ln -sf ../..%{_libdir}/qmail $RPM_BUILD_ROOT/var/qmail/bin
ln -sf ../..%{_mandir} $RPM_BUILD_ROOT/var/qmail/man
ln -sf $RPM_BUILD_DIR/%{name}-%{version}/boot $RPM_BUILD_ROOT/var/qmail/boot

./install -s $RPM_BUILD_ROOT

ln -s qmail-qread $RPM_BUILD_ROOT%{_bindir}/mailq
ln -sf ../../var/qmail/bin/sendmail $RPM_BUILD_ROOT%{_sbindir}/sendmail
ln -sf ../../var/qmail/bin/sendmail $RPM_BUILD_ROOT%{_libdir}/sendmail

# Set up boot procedures
install %{SOURCE7} $RPM_BUILD_ROOT/etc/rc.d/init.d/qmail
install %{SOURCE8} $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/qmail.sh
install %{SOURCE9} $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/qmail.csh

install %{SOURCE17} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/qmqp
install %{SOURCE18} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/smtp
install %{SOURCE19} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/qpop

# Set up mailing aliases
install %{SOURCE10} $RPM_BUILD_ROOT%{_sysconfdir}/aliases
ln -sf ../aliases $RPM_BUILD_ROOT%{_sysconfdir}/mail/aliases
install %{SOURCE11} $RPM_BUILD_ROOT%{_sysconfdir}/qmail/alias/.qmail-default
install %{SOURCE12} $RPM_BUILD_ROOT%{_sysconfdir}/qmail/alias/.qmail-msglog

for i in mailer-daemon postmaster root; do
touch $RPM_BUILD_ROOT%{_sysconfdir}/qmail/alias/.qmail-$i
done

# Set up control files.
touch $RPM_BUILD_ROOT%{_sysconfdir}/qmail/control/{defaultdomain,locals,me,plusdomain,rcpthosts,qmqpservers,idhost}

# Set up blank qmail/users
touch $RPM_BUILD_ROOT%{_sysconfdir}/qmail/users/{assign,include,exclude,mailnames,subusers,append}
echo -n "." > $RPM_BUILD_ROOT%{_sysconfdir}/qmail/users/assign

# Set up default delivery
install %{SOURCE13} $RPM_BUILD_ROOT%{_sysconfdir}/qmail/dot-qmail

install %{SOURCE14} $RPM_BUILD_ROOT/var/qmail/bin/qmail-lint
install %{SOURCE15} $RPM_BUILD_ROOT/var/qmail/bin/qmail-qsanity

# qmHandle command
install qmHandle-0.4.0/qmHandle $RPM_BUILD_ROOT/var/qmail/bin/qmHandle

# QUEUE FIX command
install queue-fix-1.3/queue-fix $RPM_BUILD_ROOT/var/qmail/bin

# CHECKPASSWORD command
install checkpass-1.0/checkpass $RPM_BUILD_ROOT/var/qmail/bin
install %{SOURCE20} $RPM_BUILD_ROOT/etc/pam.d/checkpass
echo "qmaild" > $RPM_BUILD_ROOT/etc/security/checkpass.allow

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
install -d $RPM_BUILD_ROOT/etc/skel/C/Mail
./maildirmake $RPM_BUILD_ROOT/etc/skel/C/Mail/Maildir

(set +x; rm -f checkpass-1.0/{[a-z]*,Makefile})
(set +x; rm -f dot-forward-0.71/{[a-z]*,Makefile,FILES,SYSDEPS,TARGETS})
(set +x; rm -f fastforward-0.51/{[a-z]*,Makefile,FILES,SYSDEPS,TARGETS})
(set +x; rm -f rblsmtpd-0.70/{[a-z]*,Makefile,FILES,SYSDEPS,TARGETS})
(set +x; rm -f queue-fix-1.3/{[a-z]*,Makefile,TARGETS})
(set +x; rm -f qmHandle-0.4.0/q*)

cp $RPM_SOURCE_DIR/tarpit.README .

# What else?
mv $RPM_BUILD_ROOT/var/qmail/bin/maildir2mbox	$RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT/var/qmail/bin/maildirmake	$RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT/var/qmail/bin/maildirwatch	$RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT/var/qmail/bin/qmHandle	$RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT/var/qmail/bin/qmail-qread	$RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT/var/qmail/bin/qmail-qsanity	$RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT/var/qmail/bin/qmail-qstat	$RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT/var/qmail/bin/queue-fix	$RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT/var/qmail/bin/newaliases	$RPM_BUILD_ROOT%{_bindir}

install %{SOURCE21} .

gzip -9nf FAQ INSTALL* PIC* REMOVE* SENDMAIL TEST* UPGRADE
gzip -9nf BLURB* README SECURITY THANKS THOUGHTS TODO VERSION
gzip -9nf boot/* checkpass-1.0/* qmHandle-0.4.0/* queue-fix-1.3/*
gzip -9nf rblsmtpd-0.70/* tarpit.README
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/*

%pre
if [ $1 = 1 ]; then
# Add few users and groups
    if [ ! -n "`getgid nofiles`" ]; then
	%{_sbindir}/groupadd -f -g 81 nofiles
    fi
    if [ ! -n "`getgid qmail`" ]; then
	%{_sbindir}/groupadd -f -g 82 qmail
    fi

    if [ ! -n "`id -u qmaild 2>/dev/null`" ]; then
	%{_sbindir}/useradd -g nofiles -d /var/qmail -u 81 -s /bin/false qmaild 2> /dev/null
    fi
    if [ ! -n "`id -u alias 2>/dev/null`" ]; then
	%{_sbindir}/useradd -g nofiles -d /var/qmail/alias -u 82 -s /bin/false alias 2> /dev/null
    fi
    if [ ! -n "`id -u qmailq 2>/dev/null`" ]; then
	%{_sbindir}/useradd -g qmail -d /var/qmail -u 83 -s /bin/false qmailq 2> /dev/null
    fi
    if [ ! -n "`id -u qmailr 2>/dev/null`" ]; then
	%{_sbindir}/useradd -g qmail -d /var/qmail -u 84 -s /bin/false qmailr 2> /dev/null
    fi
    if [ ! -n "`id -u qmails 2>/dev/null`" ]; then
	%{_sbindir}/useradd -g qmail -d /var/qmail -u 85 -s /bin/false qmails 2> /dev/null
    fi
    if [ ! -n "`id -u qmaill 2>/dev/null`" ]; then
	%{_sbindir}/useradd -g nofiles -d /var/qmail -u 86 -s /bin/false qmaill 2> /dev/null
    fi
    if [ ! -n "`id -u qmailp 2>/dev/null`" ]; then
	%{_sbindir}/useradd -g nofiles -d /var/qmail -u 87 -s /bin/false qmailp 2> /dev/null
    fi
fi

%post
if [ ! -f /etc/mail/mailname -a -d /etc/mail ]; then
	(cd /etc/mail && ln -sf ../qmail/control/me mailname && chmod a+r mailname)
fi

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
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet sever" 1>&2
fi

%preun
# If package is being erased for the last time.
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/qmail ]; then
		/etc/rc.d/init.d/qmail stop
	fi
	/sbin/chkconfig --del qmail
fi

%postun
# If package is being erased for the last time.
if [ "$1" = "0" ]; then
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

	if [ -f /var/lock/subsys/rc-inetd ]; then
		/etc/rc.d/init.d/rc-inetd reload
	fi
fi

%post client
ln -sf qmail-qmqpc %{_libdir}/qmail/qmail-queue

if [ ! -f /etc/mail/mailname -a -d /etc/mail ]; then
	(cd /etc/mail && ln -sf ../qmail/control/me mailname && chmod a+r mailname)
fi

if [ ! -s /etc/qmail/control/me ]; then
	FQDN=`/bin/hostname -f`
	echo "$FQDN" > /etc/qmail/control/me
	echo "$FQDN" > /etc/qmail/control/idhost
	echo "$FQDN" | /bin/sed 's/^\([^\.]*\)\.\([^\.]*\)\./\2\./' > /etc/qmail/control/defaultdomain
	echo "$FQDN" | /bin/sed 's/^.*\.\([^\.]*\)\.\([^\.]*\)$/\1.\2/' > /etc/qmail/control/plusdomain
	chmod 644 /etc/qmail/control/*
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {FAQ,INSTALL*,PIC*,REMOVE*,SENDMAIL,TEST*,UPGRADE}.gz
%doc {BLURB*,README,SECURITY,THANKS,THOUGHTS,TODO,VERSION}.gz
%doc checkpass-1.0/ queue-fix-1.3/ qmHandle-0.4.0/ rblsmtpd-0.70/ boot/ 
%doc tarpit.README.gz

%attr( 755, root, root) %dir %{_sysconfdir}/mail
%attr( 755, root, root) %dir %{_sysconfdir}/qmail
%attr(2754, alias,nofiles) %dir %{_sysconfdir}/qmail/alias
%attr( 755, root, qmail) %dir %{_sysconfdir}/qmail/control
%attr( 755, root, root) %dir %{_sysconfdir}/qmail/users
%attr( 755,  root, qmail) %dir %{_libdir}/qmail
%attr( 755,  root, qmail) %dir /var/qmail
%attr( 750,qmailq, qmail) %dir /var/qmail/queue
%attr( 750,qmailq, qmail) %dir /var/qmail/queue/lock
%attr( 700,qmails, qmail) /var/qmail/queue/bounce
%attr( 700,qmails, qmail) /var/qmail/queue/info
%attr( 700,qmailq, qmail) /var/qmail/queue/intd
%attr( 700,qmails, qmail) /var/qmail/queue/local
%attr( 750,qmailq, qmail) /var/qmail/queue/mess
%attr( 700,qmailq, qmail) /var/qmail/queue/pid
%attr( 700,qmails, qmail) /var/qmail/queue/remote
%attr( 750,qmailq, qmail) /var/qmail/queue/todo
%attr( 600,qmails, qmail)  %config(noreplace) %verify(not mtime md5) /var/qmail/queue/lock/sendmutex
%attr( 644,qmailr, qmail)  %config(noreplace) %verify(not mtime md5) /var/qmail/queue/lock/tcpto
%attr( 622,qmails, qmail)  %config(noreplace) %verify(not mtime md5) /var/qmail/queue/lock/trigger
%attr( 640, root,nofiles) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/alias/.qmail-*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/dot-qmail
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/defaultdomain
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/locals
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/me
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/plusdomain
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/rcpthosts
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/users/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/aliases
%{_sysconfdir}/mail/aliases
%attr( 755, root, root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/profile.d/*
%attr( 754,  root,  root) /etc/rc.d/init.d/*
%attr( 640,  root,  root) %config(noreplace) %verify(not mtime md5 size) /etc/sysconfig/rc-inetd/qmqp
%attr( 640,  root,  root) %config(noreplace) %verify(not mtime md5 size) /etc/sysconfig/rc-inetd/smtp
%attr( 640,  root,  root) %config(noreplace) %verify(not mtime md5 size) /etc/sysconfig/rc-inetd/qpop
%attr( 644,  root,  root) %config(noreplace) %verify(not mtime md5 size) /etc/pam.d/checkpass
%attr( 644,  root,  root) %config(noreplace) %verify(not mtime md5 size) /etc/security/checkpass.allow
%attr( 755,  root,  root) %{_libdir}/qmail/bouncesaying
%attr( 755,  root,  root) %{_libdir}/qmail/condredirect
%attr(4755,  root,  root) %{_libdir}/qmail/checkpass
%attr( 755,  root,  root) %{_libdir}/qmail/datemail
%attr( 755,  root,  root) %{_libdir}/qmail/elq
%attr( 755,  root,  root) %{_libdir}/qmail/except
%attr( 755,  root,  root) %{_libdir}/qmail/forward
%attr( 755,  root,  root) %{_bindir}/maildir2mbox
%attr( 755,  root,  root) %{_bindir}/maildirmake
%attr( 755,  root,  root) %{_bindir}/maildirwatch
%attr( 755,  root,  root) %{_libdir}/qmail/mailsubj
%attr( 755,  root,  root) %{_libdir}/qmail/pinq
%attr( 755,  root,  root) %{_libdir}/qmail/predate
%attr( 755,  root,  root) %{_libdir}/qmail/preline
%attr( 755,  root,  root) %{_libdir}/qmail/qail
%attr( 755,  root,  root) %{_libdir}/qmail/qbiff
%attr( 755,  root,  root) %{_bindir}/qmHandle
%attr( 755,  root,  root) %{_libdir}/qmail/qmail-clean
%attr( 755,  root,  root) %{_libdir}/qmail/qmail-getpw
%attr( 755,  root,  root) %{_libdir}/qmail/qmail-inject
%attr( 755,  root,  root) %{_libdir}/qmail/qmail-lint
%attr( 755,  root,  root) %{_libdir}/qmail/qmail-local
%attr( 755,  root,  root) %{_libdir}/qmail/qmail-lspawn
%attr( 755,  root,  root) %{_libdir}/qmail/qmail-newmrh
%attr( 755,  root,  root) %{_libdir}/qmail/qmail-newu
%attr( 755,  root,  root) %{_libdir}/qmail/qmail-pop3d
%attr( 755,  root,  root) %{_libdir}/qmail/qmail-popup
%attr( 755,  root,  root) %{_libdir}/qmail/qmail-pw2u
%attr( 755,  root,  root) %{_libdir}/qmail/qmail-qmqpc
%attr( 755,  root,  root) %{_libdir}/qmail/qmail-qmqpd
%attr( 755,  root,  root) %{_libdir}/qmail/qmail-qmtpd
%attr( 755,  root,  root) %{_bindir}/qmail-qread
%attr( 755,  root,  root) %{_bindir}/qmail-qsanity
%attr( 755,  root,  root) %{_bindir}/qmail-qstat
%attr(4755,qmailq, qmail) %{_libdir}/qmail/qmail-queue
%attr( 755,  root,  root) %{_libdir}/qmail/qmail-remote
%attr( 755,  root,  root) %{_libdir}/qmail/qmail-rspawn
%attr( 755,  root,  root) %{_libdir}/qmail/qmail-send
%attr( 755,  root,  root) %{_libdir}/qmail/qmail-showctl
%attr( 755,  root,  root) %{_libdir}/qmail/qmail-smtpd
%attr( 744,  root,  root) %{_libdir}/qmail/qmail-start
%attr( 755,  root,  root) %{_libdir}/qmail/qmail-tcpok
%attr( 755,  root,  root) %{_libdir}/qmail/qmail-tcpto
%attr( 755,  root,  root) %{_libdir}/qmail/qreceipt
%attr( 755,  root,  root) %{_libdir}/qmail/qsmhook
%attr( 755,  root,  root) %{_bindir}/queue-fix
%attr( 755,  root,  root) %{_libdir}/qmail/sendmail
%attr( 755,  root,  root) %{_libdir}/qmail/splogger
%attr( 755,  root,  root) %{_libdir}/qmail/tcp-env
%attr( 755,  root,  root) %{_libdir}/qmail/dot-forward
%attr( 755,  root,  root) %{_libdir}/qmail/fastforward
%attr( 755,  root,  root) %{_bindir}/newaliases
%attr( 755,  root,  root) %{_libdir}/qmail/newinclude
%attr( 755,  root,  root) %{_libdir}/qmail/printforward
%attr( 755,  root,  root) %{_libdir}/qmail/printmaillist
%attr( 755,  root,  root) %{_libdir}/qmail/setforward
%attr( 755,  root,  root) %{_libdir}/qmail/setmaillist
%attr( 755,  root,  root) %{_libdir}/qmail/antirbl
%attr( 755,  root,  root) %{_libdir}/qmail/rblsmtpd
%attr( 755,  root,  root) %{_bindir}/mailq
%attr( 755,  root,  root) %{_sbindir}/sendmail
%attr( 755,  root,  root) %{_libdir}/sendmail
%attr(2754, alias, qmail) /var/qmail/alias
%attr( 755,  root,  root) /var/qmail/bin
%attr( 755,  root,  root) /var/qmail/control
%attr( 755,  root,  root) /var/qmail/users
%{_mandir}/man?/*

# default folder - Maildir/
%attr( 700, root, root) %dir /etc/skel/C/Mail
%attr( 700, root, root) %dir /etc/skel/C/Mail/Maildir
%attr( 700, root, root) %dir /etc/skel/C/Mail/Maildir/cur
%attr( 700, root, root) %dir /etc/skel/C/Mail/Maildir/new
%attr( 700, root, root) %dir /etc/skel/C/Mail/Maildir/tmp

%files client
%defattr(644,root,root,755)
%doc {FAQ,INSTALL*,PIC*,REMOVE*,SENDMAIL,TEST*,UPGRADE}.gz
%doc {BLURB*,README,SECURITY,THANKS,THOUGHTS,TODO,VERSION}.gz
%doc qmail-client.html

%attr(755, root, root) %dir %{_sysconfdir}/mail
%attr(755, root, root) %dir %{_sysconfdir}/qmail
%attr(755, root, root) %dir %{_sysconfdir}/qmail/control
%attr(755, root, root) %dir %{_libdir}/qmail
%attr(755, root, root) %dir /var/qmail
%attr(755, root, root) /var/qmail/bin
%attr(755, root, root) /var/qmail/control
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/defaultdomain
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/me
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/plusdomain
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/idhost
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/qmqpservers
%attr(755, root, root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/profile.d/*
%attr(755, root, root) %{_libdir}/qmail/datemail
%attr(755, root, root) %{_libdir}/qmail/elq
%attr(755, root, root) %{_libdir}/qmail/forward
%attr(755, root, root) %{_bindir}/maildir2mbox
%attr(755, root, root) %{_bindir}/maildirmake
%attr(755, root, root) %{_bindir}/maildirwatch
%attr(755, root, root) %{_libdir}/qmail/mailsubj
%attr(755, root, root) %{_libdir}/qmail/pinq
%attr(755, root, root) %{_libdir}/qmail/predate
%attr(755, root, root) %{_libdir}/qmail/qail
%attr(755, root, root) %{_libdir}/qmail/qmail-inject
%attr(755, root, root) %{_libdir}/qmail/qmail-qmqpc
%attr(755, root, root) %ghost %{_libdir}/qmail/qmail-queue
%attr(755, root, root) %{_libdir}/qmail/qmail-showctl
%attr(755, root, root) %{_libdir}/qmail/sendmail
%attr(755, root, root) %{_sbindir}/sendmail
%attr(755, root, root) %{_libdir}/sendmail
%{_mandir}/man1/mail*
%{_mandir}/man5/qmail-header*
%{_mandir}/man5/qmail-log*
%{_mandir}/man8/qmail-inject*
%{_mandir}/man8/qmail-qmqpc*
%{_mandir}/man8/qmail-queue*
%{_mandir}/man8/qmail-showctl*

# default folder - Maildir/
%attr( 700, root, root) %dir /etc/skel/C/Mail
%attr( 700, root, root) %dir /etc/skel/C/Mail/Maildir
%attr( 700, root, root) %dir /etc/skel/C/Mail/Maildir/cur
%attr( 700, root, root) %dir /etc/skel/C/Mail/Maildir/new
%attr( 700, root, root) %dir /etc/skel/C/Mail/Maildir/tmp
