#
# Conditional build:
%bcond_without	msglog		# without qmail-msglog (advanced e-mail monitoring)
%bcond_without	routing		# without mail routing
%bcond_without	home_etc	# don't use home_etc
#
Summary:	qmail Mail Transport Agent
Summary(pl):	qmail - serwer pocztowy (MTA)
Name:		qmail
Version:	1.03
Release:	56
License:	DJB (http://cr.yp.to/qmail/dist.html)
Group:		Networking/Daemons
Source0:	http://cr.yp.to/software/%{name}-%{version}.tar.gz
# Source0-md5:	622f65f982e380dbe86e6574f3abcb7c
Source1:	http://cr.yp.to/software/dot-forward-0.71.tar.gz
# Source1-md5:	1fefd9760e4706491fb31c7511d69bed
Source2:	http://cr.yp.to/software/fastforward-0.51.tar.gz
# Source2-md5:	6dc619180ba9726380dc1047e45a1d8d
Source3:	http://cr.yp.to/software/rblsmtpd-0.70.tar.gz
# Source3-md5:	2b9440db40aad2429ecbe8c964f69aa9
Source4:	checkpass-1.2.tar.gz
# Source4-md5:	6818629dc74737f3ca33ca97ab4ffcc4
Source5:	http://www.netmeridian.com/e-huss/queue-fix-1.4.tar.gz
# Source5-md5:	43f915c104024e6f33a5b3ff52dfb75b
Source6:	http://www.io.com/~mick/soft/qmHandle-0.5.1.tar.gz
# Source6-md5:	c50bce18aa4e3e6c98cd5da9ed41c5a9
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
# Source16-md5:	2200af710f49fb32c1808345323c6e68
Source17:	%{name}-qmqp.inetd
Source18:	%{name}-smtp.inetd
Source19:	%{name}-qpop.inetd
Source20:	checkpassword.pamd
# Source20-md5:	78c3cb713ec00207f8fa0edcf3fe4fd2
Source21:	%{name}-client.html
Source22:	%{name}-cert.pem
Source23:	%{name}-pl-man-pages.tar.bz2
# Source23-md5:	e6230e950257cf46b9b243685d682e3f
Source24:	http://iidea.pl/~paweln/tlum/qmail-doki.tar.bz2
# Source24-md5: 2d85f0f9f8408cf6caab9f9bc8f68657
Patch0:		%{name}-1.03.install.patch
Patch1:		%{name}-1.03.msglog.patch
Patch2:		%{name}-1.03.redhat.patch
Patch3:		%{name}-1.03.fixed-ids.patch
Patch4:		%{name}-1.03.rbl.conf.patch
Patch6:		%{name}-relayclientexternal.patch
Patch8:		tarpit.patch
Patch9:		%{name}-1.03-maxrcpt.patch
Patch10:	qmHandle.PLD-init.patch
Patch11:	%{name}-1.03-v6-20000417.diff.gz
Patch12:	http://www.ckdhr.com/ckd/%{name}-dns.patch
Patch14:	%{name}-rblsmtpd-IPv6-PLD.patch
Patch15:	%{name}-rblsmtpd-syslog.patch
Patch16:	%{name}-smtpauth.patch
Patch18:	%{name}-wildmat.patch
Patch19:	%{name}-rblsmtpd-rss.patch
Patch20:	%{name}-no_mail_routing.patch
Patch21:	%{name}-qmqpc-received.patch
Patch22:	%{name}-rblsmtpd-glibc2.2.patch
Patch23:	%{name}-extbouncer.patch
# http://www.esat.kuleuven.ac.be/~vermeule/qmail/tls.patch
Patch24:	%{name}-tls.patch
# http://www.qmail.org/qmailqueue-patch
Patch25:	%{name}-queue.patch
Patch26:	%{name}-errno.patch
Patch27:	%{name}-home_etc.patch
Patch28:	%{name}-1.03.errno.patch
Patch29:	%{name}-1.03.qmail_local.patch
Patch30:	%{name}-ac_rblsmtpd.patch
URL:		http://www.qmail.org/
BuildRequires:	groff
%{?with_home_etc:BuildRequires:	home-etc-devel >= 1.0.8}
BuildRequires:	pam-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	rpmbuild(macros) >= 1.159
PreReq:		rc-scripts >= 0.2.0
PreReq:		rc-inetd
PreReq:		sh-utils
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(post):	/bin/hostname
Requires(post):	/bin/id
Requires(post):	/bin/sed
Requires(post):	fileutils
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires:	%{_sbindir}/tcpd
%{?with_home_etc:Requires:	home-etc >= 1.0.8}
Requires:	inetdaemon
Requires:	pam >= 0.77.3
Conflicts:	qmail-client
Provides:	group(nofiles)
Provides:	group(qmail)
Provides:	qmail-server
Provides:	qmailmta
Provides:	smtpdaemon
Provides:	user(alias)
Provides:	user(qmaild)
Provides:	user(qmaill)
Provides:	user(qmailp)
Provides:	user(qmailq)
Provides:	user(qmailr)
Provides:	user(qmails)
Obsoletes:	courier
Obsoletes:	exim
Obsoletes:	masqmail
Obsoletes:	nullmailer
Obsoletes:	omta
Obsoletes:	postfix
Obsoletes:	sendmail
Obsoletes:	sendmail-cf
Obsoletes:	sendmail-doc
Obsoletes:	smail
Obsoletes:	smtpdaemon
Obsoletes:	ssmtp
Obsoletes:	zmailer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# not FHS compliant
%define		varqmail	/var/qmail

%description
qmail is a small, fast, secure replacement for the SENDMAIL package,
which is the program that actually receives, routes, and delivers
electronic mail. This qmail also support IPv6 protocol.

Following scripts and programs have been added:
- checkpass - password-checking interface,
- qmHandle - more powerful viewing and managing qmail queue (remote
  and local),
- rblsmtpd - a generic tool to block mail from RBL-listed sites; an
  optional way to filter SPAM,
- qmail-fix - a small utility for checking and repairing the qmail
  queue structure,
%{?with_msglog:- qmail-msglog - advanced e-mail monitoring,}
- qmail-qsanity - examine all the files in the qmail queue,
- qmail-lint - examine the qmail configuration,
- tarpit - tool to fight with SPAM,
- TLS/SSL support. If you want to use it you must have certificate in
  /etc/qmail/control/cert.pem.

================================================================================
- *** Note: Be sure and read the documentation as there are some small
  but very significant differences between SENDMAIL and QMAIL and the
  programs that interact with them.

%description -l pl
qmail jest ma��, szybk� oraz bezpieczn� alternatyw� do sendmaila,
kt�ra umo�liwia otrzymywanie, przesy�anie oraz wysy�anie poczty
elektronicznej. Ten qmail dodatkowo wspiera protok� IPv6.

Zosta�y dodane do tego pakietu nast�puj�ce skrypty i programy:
- checkpass - interfejs do sprawdzania hase�,
- qmHandle - bardziej zaawansowane przegl�danie oraz zarz�dzanie
  kolejk� pocztow�,
- rblsmtpd - podstawowe narz�dzie do blokowania list�w z miejsc
  wyszczeg�lnionych w RBL; spos�b na filtrowanie SPAM-u,
- qmail-fix - program do sprawdzania oraz naprawiania struktury
  kolejki pocztowej qmail-a,
%{?with_msglog:- qmail-msglog - zaawansowane monitorowanie list�w,}
- qmail-qsanity - sprawdza kolejk� pocztow� qmail-a,
- qmail-lint - sprawdza konfiguracj� qmail-a,
- tarpit - kolejne narz�dzie do walki ze SPAM-em,
- Obs�uga TLS/SSL. Je�li chcesz tego u�ywa� musisz mie� certyfikat w
  /etc/qmail/control/cert.pem.

================================================================================
*** Uwaga! Przeczytaj uwa�nie dokumentacj� do tego pakietu, poniewa�
istniej� ma�e, ale znacz�ce r�nice pomi�dzy qmailem oraz sendmailem
i programami, kt�re wsp�pracuj� z nimi.

%package client
Summary:	qmail Mail Transport Agent - null client
Summary(pl):	qmail - serwer pocztowy (MTA) - cienki klient
Group:		Networking/Daemons
URL:		http://www.qmail.org/
Requires(post):	/bin/hostname
Requires(post):	/bin/sed
Requires(post):	fileutils
Conflicts:	qmail
Provides:	qmailmta
Provides:	smtpdaemon
Obsoletes:	smtpdaemon
Obsoletes:	exim
Obsoletes:	masqmail
Obsoletes:	omta
Obsoletes:	postfix
Obsoletes:	sendmail
Obsoletes:	sendmail-cf
Obsoletes:	sendmail-doc
Obsoletes:	smail
Obsoletes:	zmailer

%description client
qmail is a small, fast, secure replacement for the SENDMAIL package,
which is the program that actually receives, routes, and delivers
electronic mail. This qmail also support IPv6 protocol.

%description client -l pl
qmail jest ma��, szybk� oraz bezpieczn� alternatyw� do sendmaila,
kt�ra umo�liwia otrzymywanie, przesy�anie oraz wysy�anie poczty
elektronicznej. Ten qmail dodatkowo wspiera protok� IPv6.

%package maildirmake
Summary:	maildirmake - tool for making qmails' Maildirs
Summary(pl):	maildirmake - narz�dzie do zak�adania folerow Maildir
Group:		Applications/Mail
Conflicts:	courier-imap-maildirmake

%description maildirmake
Maildirmake is a tool for making mail folders in Maildir format.

%description maildirmake -l pl
Maildirmake jest narz�dziem do zak�adania folder�w w formacie Maildir.

%package perl
Summary:	perl scripts for qmail
Summary(pl):	Skrypty perlowe dla qmaila
Group:		Applications/Mail
Requires:	%{name} = %{version}

%description perl
Perl scripts for qmail.

%description perl -l pl
Skrypty perlowe dla qmaila.

%package pop3
Summary:	POP3 server for qmail
Summary(pl):	Serwer POP3 dla qmaila
Group:		Networking/Daemons
Requires:	%{name} = %{version}
Provides:	pop3daemon
Obsoletes:	qpopper
Obsoletes:	qpopper6
Obsoletes:	imap-pop
Obsoletes:	solid-pop3d-ssl
Obsoletes:	solid-pop3d

%description pop3
POP3 server for qmail.

%description pop3 -l pl
Serwer POP3 dla qmaila.

%prep
%setup -q -a1 -a2 -a3 -a4 -a5
install -d qmHandle-0.5.1
tar zxf %{SOURCE6} -C qmHandle-0.5.1/
%patch0 -p1
%{?with_msglog:%patch1 -p1}
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch6 -p1
%patch8 -p0
%patch9 -p0
%patch10 -p0
%patch11 -p1
%patch12 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch18 -p1
%patch19 -p1
%{!?with_routing:%patch20 -p1}
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%{?with_home_etc:%patch27 -p1}
%patch28 -p1
%patch29 -p1
%patch30 -p1

%build
%{__make} CFLAGS="%{rpmcflags}"
%{__make} man
%{__make} -C dot-forward-0.71
%{__make} -C fastforward-0.51
%{__make} -C rblsmtpd-0.70
%{__make} -C queue-fix-1.4
%{__make} -C checkpass-1.2

%install
rm -rf $RPM_BUILD_ROOT

install -d boot
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_bindir},%{_mandir},%{_libdir}/qmail,%{varqmail}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,profile.d,mail,sysconfig/rc-inetd,pam.d,security} \
	$RPM_BUILD_ROOT%{_sysconfdir}/qmail/{alias,control,users}

ln -sf ../../%{_sysconfdir}/qmail/alias $RPM_BUILD_ROOT%{varqmail}
ln -sf ../../%{_sysconfdir}/qmail/control $RPM_BUILD_ROOT%{varqmail}
ln -sf ../../%{_sysconfdir}/qmail/users $RPM_BUILD_ROOT%{varqmail}
ln -sf ../../%{_libdir}/qmail $RPM_BUILD_ROOT%{varqmail}/bin
ln -sf ../../%{_mandir} $RPM_BUILD_ROOT%{varqmail}/man
ln -sf $RPM_BUILD_DIR/%{name}-%{version}/boot $RPM_BUILD_ROOT%{varqmail}/boot

./install -s $RPM_BUILD_ROOT

ln -sf qmail-qread $RPM_BUILD_ROOT%{_bindir}/mailq
ln -sf ../../%{varqmail}/bin/sendmail $RPM_BUILD_ROOT%{_sbindir}/sendmail
ln -sf ../../%{varqmail}/bin/sendmail $RPM_BUILD_ROOT%{_libdir}/sendmail

# Set up boot procedures
install %{SOURCE7} $RPM_BUILD_ROOT/etc/rc.d/init.d/qmail
install %{SOURCE8} $RPM_BUILD_ROOT/etc/profile.d/qmail.sh
install %{SOURCE9} $RPM_BUILD_ROOT/etc/profile.d/qmail.csh

install %{SOURCE17} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/qmqp
install %{SOURCE18} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/smtp
install %{SOURCE19} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/qpop

# Set up mailing aliases
install %{SOURCE10} $RPM_BUILD_ROOT%{_sysconfdir}/aliases
ln -sf ../aliases $RPM_BUILD_ROOT%{_sysconfdir}/mail/aliases
install %{SOURCE11} $RPM_BUILD_ROOT%{_sysconfdir}/qmail/alias/.qmail-default
%{?with_msglog:install %{SOURCE12} $RPM_BUILD_ROOT%{_sysconfdir}/qmail/alias/.qmail-msglog}

for i in mailer-daemon postmaster root; do
	> $RPM_BUILD_ROOT%{_sysconfdir}/qmail/alias/.qmail-$i
done

# Set up control files.
for i in defaultdomain locals me plusdomain rcpthosts qmqpservers idhost; do
	> $RPM_BUILD_ROOT%{_sysconfdir}/qmail/control/$i
done

# Set up blank qmail/users
for i in assign include exclude mailnames subusers append; do
	> $RPM_BUILD_ROOT%{_sysconfdir}/qmail/users/$i
done
echo -n "." > $RPM_BUILD_ROOT%{_sysconfdir}/qmail/users/assign

# Set up default delivery
install %{SOURCE13} $RPM_BUILD_ROOT%{_sysconfdir}/qmail/dot-qmail

install %{SOURCE14} $RPM_BUILD_ROOT%{varqmail}/bin/qmail-lint
install %{SOURCE15} $RPM_BUILD_ROOT%{varqmail}/bin/qmail-qsanity

# qmHandle command
install qmHandle-0.5.1/qmHandle $RPM_BUILD_ROOT%{varqmail}/bin/qmHandle

# QUEUE FIX command
install queue-fix-1.4/queue-fix $RPM_BUILD_ROOT%{varqmail}/bin

# CHECKPASSWORD command
install checkpass-1.2/checkpass $RPM_BUILD_ROOT%{varqmail}/bin
install %{SOURCE20} $RPM_BUILD_ROOT/etc/pam.d/checkpass
echo "qmaild" > $RPM_BUILD_ROOT/etc/security/checkpass.allow

# DOT FORWARD command and doc
install dot-forward-0.71/dot-forward $RPM_BUILD_ROOT%{varqmail}/bin
install dot-forward-0.71/dot-forward.1 $RPM_BUILD_ROOT%{varqmail}/man/man1

# FAST FORWARD commands and docs
install fastforward-0.51/fastforward $RPM_BUILD_ROOT%{varqmail}/bin
install fastforward-0.51/newaliases $RPM_BUILD_ROOT%{varqmail}/bin
install fastforward-0.51/newinclude $RPM_BUILD_ROOT%{varqmail}/bin
install fastforward-0.51/printforward $RPM_BUILD_ROOT%{varqmail}/bin
install fastforward-0.51/printmaillist $RPM_BUILD_ROOT%{varqmail}/bin
install fastforward-0.51/setforward $RPM_BUILD_ROOT%{varqmail}/bin
install fastforward-0.51/setmaillist $RPM_BUILD_ROOT%{varqmail}/bin
install fastforward-0.51/*.1 $RPM_BUILD_ROOT%{varqmail}/man/man1/

# RBLSMTPD commands and doc
install rblsmtpd-0.70/antirbl $RPM_BUILD_ROOT%{varqmail}/bin
install rblsmtpd-0.70/rblsmtpd $RPM_BUILD_ROOT%{varqmail}/bin
install rblsmtpd-0.70/*.8 $RPM_BUILD_ROOT%{varqmail}/man/man8

# default folder in /etc/skel
install -d $RPM_BUILD_ROOT/etc/skel/Mail
./maildirmake $RPM_BUILD_ROOT/etc/skel/Mail/Maildir

(set +x; rm -f checkpass-1.2/{[a-z]*,Makefile})
(set +x; rm -f dot-forward-0.71/{[a-z]*,Makefile,FILES,SYSDEPS,TARGETS})
(set +x; rm -f fastforward-0.51/{[a-z]*,Makefile,FILES,SYSDEPS,TARGETS})
(set +x; rm -f rblsmtpd-0.70/{[a-z]*,Makefile,FILES,SYSDEPS,TARGETS})
(set +x; rm -f queue-fix-1.4/{[a-z]*,Makefile,TARGETS})
(set +x; rm -f qmHandle-0.5.1/q*)

cp $RPM_SOURCE_DIR/tarpit.README .

# What else?
mv -f $RPM_BUILD_ROOT%{varqmail}/bin/maildir2mbox	$RPM_BUILD_ROOT%{_bindir}
mv -f $RPM_BUILD_ROOT%{varqmail}/bin/maildirmake	$RPM_BUILD_ROOT%{_bindir}
mv -f $RPM_BUILD_ROOT%{varqmail}/bin/maildirwatch	$RPM_BUILD_ROOT%{_bindir}
mv -f $RPM_BUILD_ROOT%{varqmail}/bin/qmHandle		$RPM_BUILD_ROOT%{_bindir}
mv -f $RPM_BUILD_ROOT%{varqmail}/bin/qmail-qread	$RPM_BUILD_ROOT%{_bindir}
mv -f $RPM_BUILD_ROOT%{varqmail}/bin/qmail-qsanity	$RPM_BUILD_ROOT%{_bindir}
mv -f $RPM_BUILD_ROOT%{varqmail}/bin/qmail-qstat	$RPM_BUILD_ROOT%{_bindir}
mv -f $RPM_BUILD_ROOT%{varqmail}/bin/queue-fix		$RPM_BUILD_ROOT%{_bindir}
mv -f $RPM_BUILD_ROOT%{varqmail}/bin/newaliases		$RPM_BUILD_ROOT%{_bindir}

# remove mbox(5) man page which is in man-pages now and isn't strict qmail
# man page
rm -f $RPM_BUILD_ROOT%{_mandir}/man5/mbox.5

install %{SOURCE21} .

install %{SOURCE22} $RPM_BUILD_ROOT%{varqmail}/control/cert.pem
bzip2 -dc %{SOURCE23} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

bzip2 -dc %{SOURCE24} | tar xf -
echo "These are pl-translations taken from: \
   http://iidea.pl/~paweln/tlum/qmail-doki.tar.bz2" > qmail-doki/00-INDEX

sed /^diff/q %{PATCH24} >README.TLS

%clean
rm -rf $RPM_BUILD_ROOT

%pre
# Add few users and groups
if [ -n "`/usr/bin/getgid nofiles`" ]; then
	if [ "`/usr/bin/getgid nofiles`" != "81" ]; then
		echo "Error: group nofiles doesn't have gid=81. Correct this before installing qmail." 1>&2
		exit 1
	fi
else
	/usr/sbin/groupadd -g 81 nofiles 1>&2
fi
if [ -n "`/usr/bin/getgid qmail`" ]; then
	if [ "`/usr/bin/getgid qmail`" != "82" ]; then
		echo "Error: group qmail doesn't have gid=82. Correct this before installing qmail." 1>&2
		exit 1
	fi
else
	/usr/sbin/groupadd -g 82 qmail 1>&2
fi
if [ -n "`/bin/id -u qmaild 2>/dev/null`" ]; then
	if [ "`/bin/id -u qmaild`" != "81" ]; then
		echo "Error: user qmaild doesn't have uid=81. Correct this before installing qmail." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -g nofiles -d %{varqmail} -u 81 -s /bin/false \
		qmaild 1>&2
fi
if [ -n "`/bin/id -u alias 2>/dev/null`" ]; then
	if [ "`/bin/id -u alias`" != "82" ]; then
		echo "Error: user alias doesn't have uid=82. Correct this before installing qmail." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -g nofiles -d %{varqmail}/alias -u 82 \
		-s /bin/false alias 1>&2
fi
if [ -n "`/bin/id -u qmailq 2>/dev/null`" ]; then
	if [ "`/bin/id -u qmailq`" != "83" ]; then
		echo "Error: user qmailq doesn't have uid=83. Correct this before installing qmail." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -g qmail -d %{varqmail} -u 83 -s /bin/false \
		qmailq 1>&2
fi
if [ -n "`/bin/id -u qmailr 2>/dev/null`" ]; then
	if [ "`/bin/id -u qmailr`" != "84" ]; then
		echo "Error: user qmailr doesn't have uid=84. Correct this before installing qmail." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -g qmail -d %{varqmail} -u 84 -s /bin/false \
		qmailr 1>&2
fi
if [ -n "`/bin/id -u qmails 2>/dev/null`" ]; then
	if [ "`/bin/id -u qmails`" != "85" ]; then
		echo "Error: user qmails doesn't have uid=85. Correct this before installing qmail." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -g qmail -d %{varqmail} -u 85 -s /bin/false \
		qmails 1>&2
fi
if [ -n "`/bin/id -u qmaill 2>/dev/null`" ]; then
	if [ "`/bin/id -u qmaill`" != "86" ]; then
		echo "Error: user qmaill doesn't have uid=86. Correct this before installing qmail." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -g nofiles -d %{varqmail} -u 86 -s /bin/false \
		qmaill 1>&2
fi
if [ -n "`/bin/id -u qmailp 2>/dev/null`" ]; then
	if [ "`/bin/id -u qmailp`" != "87" ]; then
		echo "Error: user qmailp doesn't have uid=87. Correct this before installing qmail." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -g nofiles -d %{varqmail} -u 87 -s /bin/false \
		qmailp 1>&2
fi

%post
if [ ! -f /etc/mail/mailname -a -d /etc/mail ]; then
	(cd /etc/mail && ln -sf ../qmail/control/me mailname && chmod a+r mailname)
fi

umask 022
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
if [ -f /var/lock/subsys/qmail ]; then
	/etc/rc.d/init.d/qmail restart 1>&2
else
	echo "Type \"/etc/rc.d/init.d/qmail start to start qmail" 1>&2
fi
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet server" 1>&2
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
	%userremove qmaild
	%userremove alias
	%userremove qmaill
	%userremove qmailp
	%userremove qmailq
	%userremove qmailr
	%userremove qmails
	%userremove qmail
	%groupremove nofiles
	%groupremove qmail
	if [ -f /var/lock/subsys/rc-inetd ]; then
		/etc/rc.d/init.d/rc-inetd reload
	fi
fi

%post client
ln -sf qmail-qmqpc %{_libdir}/qmail/qmail-queue

if [ ! -f /etc/mail/mailname -a -d /etc/mail ]; then
	(cd /etc/mail && ln -sf ../qmail/control/me mailname && chmod a+r mailname)
fi

umask 022
if [ ! -s /etc/qmail/control/me ]; then
	FQDN=`/bin/hostname -f`
	echo "$FQDN" > /etc/qmail/control/me
	echo "$FQDN" > /etc/qmail/control/idhost
	echo "$FQDN" | /bin/sed 's/^\([^\.]*\)\.\([^\.]*\)\./\2\./' > /etc/qmail/control/defaultdomain
	echo "$FQDN" | /bin/sed 's/^.*\.\([^\.]*\)\.\([^\.]*\)$/\1.\2/' > /etc/qmail/control/plusdomain
	chmod 644 /etc/qmail/control/*
fi

%files
%defattr(644,root,root,755)
%doc FAQ INSTALL* PIC* REMOVE* SENDMAIL TEST* UPGRADE
%doc BLURB* README SECURITY THANKS THOUGHTS TODO VERSION
%doc boot checkpass-1.2 qmHandle-0.5.1 queue-fix-1.4
%doc rblsmtpd-0.70 tarpit.README README.TLS
%doc qmail-doki

%attr(755,root,root) %dir %{_sysconfdir}/mail
%attr(755,root,root) %dir %{_sysconfdir}/qmail
%attr(2755,alias,nofiles) %dir %{_sysconfdir}/qmail/alias
%attr(755,root,qmail) %dir %{_sysconfdir}/qmail/control
%attr(755,root,root) %dir %{_sysconfdir}/qmail/users
%attr(755,root,qmail) %dir %{_libdir}/qmail
%attr(755,root,qmail) %dir %{varqmail}
%attr(750,qmailq,qmail) %dir %{varqmail}/queue
%attr(750,qmailq,qmail) %dir %{varqmail}/queue/lock
%attr(700,qmails,qmail) %{varqmail}/queue/bounce
%attr(700,qmails,qmail) %{varqmail}/queue/info
%attr(700,qmailq,qmail) %{varqmail}/queue/intd
%attr(700,qmails,qmail) %{varqmail}/queue/local
%attr(750,qmailq,qmail) %{varqmail}/queue/mess
%attr(700,qmailq,qmail) %{varqmail}/queue/pid
%attr(700,qmails,qmail) %{varqmail}/queue/remote
%attr(750,qmailq,qmail) %{varqmail}/queue/todo
%attr(600,qmails,qmail) %config(noreplace) %verify(not mtime md5) %{varqmail}/queue/lock/sendmutex
%attr(644,qmailr,qmail) %config(noreplace) %verify(not mtime md5) %{varqmail}/queue/lock/tcpto
%attr(622,qmails,qmail) %config(noreplace) %verify(not mtime md5) %{varqmail}/queue/lock/trigger
%attr(644,root,nofiles) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/alias/.qmail-*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/dot-qmail
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/defaultdomain
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/locals
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/me
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/plusdomain
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/rcpthosts
%attr(640,qmaild,qmail) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/cert.pem
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/users/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/aliases
%{_sysconfdir}/mail/aliases
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) /etc/profile.d/*
%attr(754,root,root) /etc/rc.d/init.d/*
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/rc-inetd/qmqp
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/rc-inetd/smtp
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/checkpass
%attr(644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/security/checkpass.allow
%attr(755,root,root) %{_libdir}/qmail/bouncesaying
%attr(755,root,root) %{_libdir}/qmail/condredirect
%attr(4755,root,root) %{_libdir}/qmail/checkpass
%attr(755,root,root) %{_libdir}/qmail/datemail
%attr(755,root,root) %{_libdir}/qmail/elq
%attr(755,root,root) %{_libdir}/qmail/except
%attr(755,root,root) %{_libdir}/qmail/forward
%attr(755,root,root) %{_bindir}/maildir2mbox
%attr(755,root,root) %{_bindir}/maildirwatch
%attr(755,root,root) %{_libdir}/qmail/mailsubj
%attr(755,root,root) %{_libdir}/qmail/pinq
%attr(755,root,root) %{_libdir}/qmail/predate
%attr(755,root,root) %{_libdir}/qmail/preline
%attr(755,root,root) %{_libdir}/qmail/qail
%attr(755,root,root) %{_libdir}/qmail/qbiff
%attr(755,root,root) %{_libdir}/qmail/qmail-clean
%attr(755,root,root) %{_libdir}/qmail/qmail-getpw
%attr(755,root,root) %{_libdir}/qmail/qmail-inject
%attr(755,root,root) %{_libdir}/qmail/qmail-local
%attr(755,root,root) %{_libdir}/qmail/qmail-lspawn
%attr(755,root,root) %{_libdir}/qmail/qmail-newmrh
%attr(755,root,root) %{_libdir}/qmail/qmail-newu
%attr(755,root,root) %{_libdir}/qmail/qmail-pw2u
%attr(755,root,root) %{_libdir}/qmail/qmail-qmqpc
%attr(755,root,root) %{_libdir}/qmail/qmail-qmqpd
%attr(755,root,root) %{_libdir}/qmail/qmail-qmtpd
%attr(755,root,root) %{_bindir}/qmail-qread
%attr(755,root,root) %{_bindir}/qmail-qstat
%attr(4755,qmailq,qmail) %{_libdir}/qmail/qmail-queue
%attr(755,root,root) %{_libdir}/qmail/qmail-remote
%attr(755,root,root) %{_libdir}/qmail/qmail-rspawn
%attr(755,root,root) %{_libdir}/qmail/qmail-send
%attr(755,root,root) %{_libdir}/qmail/qmail-showctl
%attr(755,root,root) %{_libdir}/qmail/qmail-smtpd
%attr(744,root,root) %{_libdir}/qmail/qmail-start
%attr(755,root,root) %{_libdir}/qmail/qmail-tcpok
%attr(755,root,root) %{_libdir}/qmail/qmail-tcpto
%attr(755,root,root) %{_libdir}/qmail/qreceipt
%attr(755,root,root) %{_libdir}/qmail/qsmhook
%attr(755,root,root) %{_bindir}/queue-fix
%attr(755,root,root) %{_libdir}/qmail/sendmail
%attr(755,root,root) %{_libdir}/qmail/splogger
%attr(755,root,root) %{_libdir}/qmail/tcp-env
%attr(755,root,root) %{_libdir}/qmail/dot-forward
%attr(755,root,root) %{_libdir}/qmail/fastforward
%attr(755,root,root) %{_bindir}/newaliases
%attr(755,root,root) %{_libdir}/qmail/newinclude
%attr(755,root,root) %{_libdir}/qmail/printforward
%attr(755,root,root) %{_libdir}/qmail/printmaillist
%attr(755,root,root) %{_libdir}/qmail/setforward
%attr(755,root,root) %{_libdir}/qmail/setmaillist
%attr(755,root,root) %{_libdir}/qmail/antirbl
%attr(755,root,root) %{_libdir}/qmail/rblsmtpd
%attr(755,root,root) %{_bindir}/mailq
%attr(755,root,root) %{_sbindir}/sendmail
%attr(755,root,root) %{_libdir}/sendmail
%attr(2755,alias,qmail) %{varqmail}/alias
%attr(755,root,root) %{varqmail}/bin
%attr(755,root,root) %{varqmail}/control
%attr(755,root,root) %{varqmail}/users
%{_mandir}/man1/[!m]*
%{_mandir}/man1/maildir2mbox*
%{_mandir}/man1/maildirwatch*
%{_mandir}/man1/mailsubj*
%{_mandir}/man[35]/*
%{_mandir}/man8/[!q]*
%{_mandir}/man8/qmail-[!p]*
%{_mandir}/man8/qmail-p[!o]*
%lang(pl) %{_mandir}/pl/man5/*
%lang(pl) %{_mandir}/pl/man8/qmail-[!p]*
%lang(pl) %{_mandir}/pl/man8/qmail-p[!o]*

# default folder - Maildir/
%attr(700,root,root) %dir /etc/skel/Mail
%attr(700,root,root) %dir /etc/skel/Mail/Maildir
%attr(700,root,root) %dir /etc/skel/Mail/Maildir/cur
%attr(700,root,root) %dir /etc/skel/Mail/Maildir/new
%attr(700,root,root) %dir /etc/skel/Mail/Maildir/tmp

%files client
%defattr(644,root,root,755)
%doc {FAQ,INSTALL*,PIC*,REMOVE*,SENDMAIL,TEST*,UPGRADE}
%doc {BLURB*,README,SECURITY,THANKS,THOUGHTS,TODO,VERSION}
%doc qmail-client.html

%attr(755,root,root) %dir %{_sysconfdir}/mail
%attr(755,root,root) %dir %{_sysconfdir}/qmail
%attr(755,root,root) %dir %{_sysconfdir}/qmail/control
%attr(755,root,root) %dir %{_libdir}/qmail
%attr(755,root,root) %dir %{varqmail}
%attr(755,root,root) %{varqmail}/bin
%attr(755,root,root) %{varqmail}/control
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/defaultdomain
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/me
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/plusdomain
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/idhost
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/qmqpservers
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) /etc/profile.d/*
%attr(755,root,root) %{_libdir}/qmail/datemail
%attr(755,root,root) %{_libdir}/qmail/elq
%attr(755,root,root) %{_libdir}/qmail/forward
%attr(755,root,root) %{_bindir}/maildir2mbox
%attr(755,root,root) %{_bindir}/maildirwatch
%attr(755,root,root) %{_libdir}/qmail/mailsubj
%attr(755,root,root) %{_libdir}/qmail/pinq
%attr(755,root,root) %{_libdir}/qmail/predate
%attr(755,root,root) %{_libdir}/qmail/qail
%attr(755,root,root) %{_libdir}/qmail/qmail-inject
%attr(755,root,root) %{_libdir}/qmail/qmail-qmqpc
%attr(755,root,root) %ghost %{_libdir}/qmail/qmail-queue
%attr(755,root,root) %{_libdir}/qmail/qmail-showctl
%attr(755,root,root) %{_libdir}/qmail/sendmail
%attr(755,root,root) %{_sbindir}/sendmail
%attr(755,root,root) %{_libdir}/sendmail
%{_mandir}/man1/maildir2mbox*
%{_mandir}/man1/maildirwatch*
%{_mandir}/man1/mailsubj*
%{_mandir}/man5/qmail-header*
%{_mandir}/man5/qmail-log*
%{_mandir}/man8/qmail-inject*
%{_mandir}/man8/qmail-qmqpc*
%{_mandir}/man8/qmail-queue*
%{_mandir}/man8/qmail-showctl*
%lang(pl) %{_mandir}/pl/man8/qmail-inject*
%lang(pl) %{_mandir}/pl/man8/qmail-qmqpc*
%lang(pl) %{_mandir}/pl/man8/qmail-queue*

# default folder - Maildir/
%attr(700,root,root) %dir /etc/skel/Mail
%attr(700,root,root) %dir /etc/skel/Mail/Maildir
%attr(700,root,root) %dir /etc/skel/Mail/Maildir/cur
%attr(700,root,root) %dir /etc/skel/Mail/Maildir/new
%attr(700,root,root) %dir /etc/skel/Mail/Maildir/tmp

%files maildirmake
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/maildirmake
%{_mandir}/man1/maildirmake*

%files perl
%defattr(644,root,root,755)
%doc qmHandle-0.5.1/
%attr(755,root,root) %{_bindir}/qmHandle
%attr(755,root,root) %{_bindir}/qmail-qsanity
%attr(755,root,root) %{_libdir}/qmail/qmail-lint

%files pop3
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/rc-inetd/qpop
%attr(755,root,root) %{_libdir}/qmail/qmail-pop3d
%attr(755,root,root) %{_libdir}/qmail/qmail-popup
%{_mandir}/man8/qmail-po*