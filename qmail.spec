# TODO
# - ipv6 patches do not apply (i don't need)
# - relayclient-external does not apply
# - maildir++ quota patch
# - sort patches
#
# - apply patches from http://www-dt.e-technik.uni-dortmund.de/~ma/qmail-bugs.html
#  - 3.2. RFC-2821 (SMTP) violation (Mail Routing)
#   http://www-dt.e-technik.uni-dortmund.de/~ma/qmail/patch-qmail-1.03-rfc2821.diff
#
#  - http://netdevice.com/qmail/rcptck/
#   - goodrcptto http://netdevice.com/qmail/patch/
#
#  - http://www3.sympatico.ca/humungusfungus/code/validrcptto.html
#
# - http://www.google.com/search?hl=en&lr=&client=firefox-a&q=qmail+message-id+patch&btnG=Search
# - http://asg.web.cmu.edu/archive/message.php?mailbox=archive.info-cyrus&msg=23375
#
# - http://freshmeat.net/projects/qmail_install/?branch_id=43628&release_id=146487
#
# Conditional build:
%bcond_with	msglog		# with qmail-msglog (advanced e-mail monitoring -- qmail-command to *all* local mail)
%bcond_with	routing		# with no-mail-routing patch (%)
%bcond_with	home_etc	# with home_etc
%bcond_without tls		# disable tls
%bcond_with ipv6		# enable ipv6
%bcond_without dkeys	# without domainkeys support
#
%define	qhpsi_ver	0.1.7
#
Summary:	qmail Mail Transport Agent
Summary(pl):	qmail - serwer pocztowy (MTA)
Name:		qmail
Version:	1.03
Release:	57.8
License:	DJB (http://cr.yp.to/qmail/dist.html)
Group:		Networking/Daemons
Source0:	http://cr.yp.to/software/%{name}-%{version}.tar.gz
# Source0-md5:	622f65f982e380dbe86e6574f3abcb7c
Source1:	http://cr.yp.to/software/dot-forward-0.71.tar.gz
# Source1-md5:	1fefd9760e4706491fb31c7511d69bed
Source2:	http://cr.yp.to/software/fastforward-0.51.tar.gz
# Source2-md5:	6dc619180ba9726380dc1047e45a1d8d
Source4:	checkpass-1.2.tar.gz
# Source4-md5:	6818629dc74737f3ca33ca97ab4ffcc4
Source5:	http://www.netmeridian.com/e-huss/queue-fix-1.4.tar.gz
# Source5-md5:	43f915c104024e6f33a5b3ff52dfb75b
Source6:	http://glen.alkohol.ee/pld/qmail/%{name}-conf-20050614.tar.bz2
# Source6-md5:	f002a1ff88d2160ff0abcc03252430f7
Source7:	http://iidea.pl/~paweln/tlum/%{name}-doki.tar.bz2
# Source7-md5:	2d85f0f9f8408cf6caab9f9bc8f68657
Source8:	%{name}-linux.sh
Source9:	%{name}-linux.csh
Source10:	%{name}-aliases
Source11:	%{name}-default
Source12:	%{name}-msglog
Source13:	%{name}-default-delivery
Source14:	%{name}-lint-0.51.pl
Source15:	%{name}-qsanity-0.51.pl
Source16:	tarpit.README
Source17:	http://www.fehcom.de/qmail/qhpsi/qhpsi-%(echo %{qhpsi_ver} | tr -d .)_tgz.bin
# Source17-md5:	18afa1762ba0b419deb26416b6a21a65
Source18:	%{name}.logrotate
Source19:	%{name}.logrotate-pop3
Source20:	checkpassword.pamd
Source21:	%{name}-client.html
Source22:	%{name}-cert.pem
Source23:	%{name}-pl-man-pages.tar.bz2
# Source23-md5:	e6230e950257cf46b9b243685d682e3f
Patch0:		%{name}-1.03.install.patch
Patch1:		%{name}-1.03.msglog.patch
Patch2:		%{name}-1.03.redhat.patch
Patch3:		%{name}-1.03.fixed-ids.patch
Patch6:		%{name}-relayclientexternal.patch
Patch8:		tarpit.patch
Patch9:		%{name}-1.03-maxrcpt.patch
Patch11:	%{name}-1.03-v6-20000417.diff.gz
Patch20:	%{name}-no_mail_routing.patch
Patch21:	%{name}-qmqpc-received.patch
Patch23:	%{name}-extbouncer.patch

# Let the system decide how to define errno
Patch26:	%{name}-errno.patch
Patch27:	%{name}-home_etc.patch
Patch28:	%{name}-1.03.errno.patch
# #29 local-tab.patch

# discards doublebounces without queuing them
# http://qmail.zoo-gate.fi/doublebounce-trim.patch
Patch100:	%{name}-doublebounce-trim.patch

# the envelope sender is a valid DNS name :
# http://lsc.kva.hu/dl/qmail-1.03-mfcheck.3.patch
# rediff because of tarpit/tls and other patches
Patch101:	%{name}-1.03-mfcheck.glen.patch
# and a fix for triplebounce (TODO: merge as one patch)
Patch102:	%{name}-mfcheck-triplebounce.patch

# Patch for qmail-smtpd.c which enforces a '.' character to be included in the HELO command before accepting email.
# http://www.pgregg.com/projects/qmail/qmail-smtpd.c_103_fqdnhelo-diff.txt
Patch103:	%{name}-smtpd-fqdnhelo.diff

# Removing the bodge that works around a BIND version 4 problem
# http://homepages.tesco.net./~J.deBoynePollard/Softwares/qmail/any-to-cname.patch
Patch104:	%{name}-any-to-cname.patch

# Patches from http://www-dt.e-technik.uni-dortmund.de/~ma/qmail-bugs.html
# Maildir file name creation is not collision proof. Mail loss possible depending on mail user agent.
Patch106:	http://vorlon.cwru.edu/~tmb2/qmail-1.03/%{name}-1.03-maildir-uniq.patch

# Gentoo patches 200-
# Last check: qmail-1.03-r15.ebuild

# SMTP AUTH (2 way), Qregex and STARTTLS support
Patch200:	ftp://ftp.linux.ee/pub/gentoo/distfiles/distfiles/qregex-starttls-2way-auth.patch
# Fixing a memory leak in Qregex support
Patch207:	%{name}-1.03-qregex-memleak-fix.patch

# Fixes a problem when utilizing "morercpthosts"
Patch214:	smtp-auth-close3.patch

# patch so an alternate queue processor can be used
# i.e. - qmail-scanner
Patch208:	http://www.qmail.org/%{name}queue-patch
# QMAILQUEUE info to documentation
Patch209:	%{name}-qmailqueue-docs-qhpsi.patch

# Support for remote hosts that have QMTP
Patch215:	http://www.qmail.org/%{name}-1.03-qmtpc.patch

# Large TCP DNS replies confuse it sometimes
Patch12:	http://www.ckdhr.com/ckd/%{name}-dns.patch

# Fix for tabs in .qmail bug noted at
# http://www.ornl.gov/its/archives/mailing-lists/qmail/2000/10/msg00696.html
# gentoo bug #24293
Patch216:	ftp://ftp.linux.ee/pub/gentoo/distfiles/distfiles/%{name}-local-tabs.patch

# Account for Linux filesystems lack of a synchronus link()
Patch201:	http://www.jedi.claranet.fr/%{name}-link-sync.patch

# Increase limits for large mail systems
Patch217:	http://www.qmail.org/big-concurrency.patch

# Treat 0.0.0.0 as a local address
Patch202:	http://www.suspectclass.com/~sgifford/qmail/%{name}-1.03-0.0.0.0-0.2.patch

# holdremote support
Patch210:	http://www.leverton.org/%{name}-hold-1.03.pat.gz

# sendmail's -f option sets a default From: header, and so should qmail's emulation.
# http://david.acz.org/software/sendmail-flagf.patch
Patch105:	%{name}-sendmail-flagf.patch

# Apply patch to make qmail-local and qmail-pop3d compatible with the
# maildir++ quota system that is used by vpopmail and courier-imap
# This patch has flaw, wrote to author and no resposnse.
#Patch218:	http://www.shupp.org/patches/%{name}-maildir++.patch

# Apply patch for local timestamps.
# This will make the emails headers be written in localtime rather than GMT
Patch203:	ftp://ftp.pipeline.com.au/pipeint/sources/linux/WebMail/%{name}-date-localtime.patch.txt

# Apply patch to trim large bouncing messages down greatly reduces traffic
# when multiple bounces occur (As in with spam)
Patch204:	ftp://ftp.pipeline.com.au/pipeint/sources/linux/WebMail/%{name}-limit-bounce-size.patch.txt

# Apply patch to add ESMTP SIZE support to qmail-smtpd
# This helps your server to be able to reject excessively large messages
# "up front", rather than waiting the whole message to arrive and then
# bouncing it because it exceeded your databytes setting
Patch219:	%{name}-smtpd-esmtp-size-gentoo.patch


# Reject some bad relaying attempts
# gentoo bug #18064
Patch220:	%{name}-smtpd-relay-reject.gentoo.patch

# Allow qmail to re-read concurrency limits on HUP
Patch205:	http://js.hu/package/qmail/%{name}-1.03-reread-concurrency.2.patch

# netscape progress bar bug with POP3d
Patch211:	http://www.qmail.org/netscape-progress.patch

# Making the sendmail binary ignore -N options for compatibility
Patch212:	http://www-dt.e-technik.uni-dortmund.de/~ma/djb/qmail/sendmail-ignore-N.patch

# rediff of original at http://www.qmail.org/accept-5xx.patch
Patch213:	%{name}-1.03-accept-5xx.tls.patch

# Refuse messages from the null envelope sender if they have more than one envelope recipient
Patch206:	%{name}-nullenvsender-recipcount.tarpit.patch

# Qmail does not reliably detect IP aliases on Linux.
Patch221:	http://www-dt.e-technik.uni-dortmund.de/~ma/qmail/patch-%{name}-1.03-4.3BSD-ipalias.diff

# Deliberate RFC-1652 "8BITMIME" violation
Patch222:	http://www-dt.e-technik.uni-dortmund.de/~ma/qmail/patch-%{name}-1.03-rfc1652.diff

# Let qmail accept bare LF in the mail body
Patch223:	%{name}-0.95-liberal-lf-rediff.patch

# qmail-queue replacement that signs and verifies DomainKeys signatures.
Patch224:	http://www.qmail.org/qmail-1.03-dk-0.53.patch
Patch225:	qmail-dkeys-shared.patch
Patch226:	qmail-dkeys-config.patch

URL:		http://www.qmail.org/
BuildRequires:	groff
BuildRequires:	ucspi-tcp >= 0.88
%{?with_home_etc:BuildRequires: home-etc-devel >= 1.0.8}
BuildRequires:	pam-devel
BuildRequires:	libdomainkeys-devel >= 0.66
%if %{with tls}
BuildRequires:	openssl-devel >= 0.9.7d
Requires:	openssl-tools >= 0.9.7d
Requires:	crondaemon
%endif
BuildRequires:	rpmbuild(macros) >= 1.159
PreReq:		rc-scripts >= 0.2.0
PreReq:		sh-utils
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(post):	/bin/hostname
Requires(post):	/bin/id
Requires(post):	/bin/sed
Requires(post):	fileutils
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires:	pam >= 0.77.3
Requires:	ucspi-tcp >= 0.88
Requires:	daemontools >= 0.76-1.4
Requires:	mktemp
%{?with_home_etc:Requires:	home-etc >= 1.0.8}
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

%define 	tcprules 	/etc/tcprules.d
%define		supervise	%{_sysconfdir}/qmail/supervise

# not FHS compliant
%define		varqmail	/var/qmail

%description
qmail is a small, fast, secure replacement for the SENDMAIL package,
which is the program that actually receives, routes, and delivers
electronic mail. This qmail also support IPv6 protocol.

Following scripts and programs have been added:
- checkpass - password-checking interface,
- qmail-fix - a small utility for checking and repairing the qmail
  queue structure,
%{?with_msglog:- qmail-msglog - advanced e-mail monitoring,}
- qmail-qsanity - examine all the files in the qmail queue,
- qmail-lint - examine the qmail configuration,
- tarpit - tool to fight with SPAM,
- TLS/SSL support. If you want to use it you must have certificate in
  %{_sysconfdir}/qmail/control/servercert.pem.
- QHPSI v%{qhpsi_ver} - The Qmail High Performance Scanner Interface
  http://www.fehcom.de/qmail/qmail.html

======================================================================
- *** Note: Be sure and read the documentation as there are some small
  but very significant differences between SENDMAIL and QMAIL and the
  programs that interact with them.

%description -l pl
qmail jest ma³±, szybk± oraz bezpieczn± alternatyw± do sendmaila,
która umo¿liwia otrzymywanie, przesy³anie oraz wysy³anie poczty
elektronicznej. Ten qmail dodatkowo wspiera protokó³ IPv6.

Zosta³y dodane do tego pakietu nastêpuj±ce skrypty i programy:
- checkpass - interfejs do sprawdzania hase³,
- qmail-fix - program do sprawdzania oraz naprawiania struktury
  kolejki pocztowej qmail-a,
%{?with_msglog:- qmail-msglog - zaawansowane monitorowanie listów,}
- qmail-qsanity - sprawdza kolejkê pocztow± qmail-a,
- qmail-lint - sprawdza konfiguracjê qmail-a,
- tarpit - kolejne narzêdzie do walki ze SPAM-em,
- Obs³uga TLS/SSL. Je¶li chcesz tego u¿ywaæ musisz mieæ certyfikat w
  %{_sysconfdir}/qmail/control/servercert.pem.

======================================================================
- *** Uwaga! Przeczytaj uwa¿nie dokumentacjê do tego pakietu, poniewa¿
  istniej± ma³e, ale znacz±ce ró¿nice pomiêdzy qmailem oraz sendmailem i
  programami, które wspó³pracuj± z nimi.

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
qmail jest ma³±, szybk± oraz bezpieczn± alternatyw± do sendmaila,
która umo¿liwia otrzymywanie, przesy³anie oraz wysy³anie poczty
elektronicznej. Ten qmail dodatkowo wspiera protokó³ IPv6.

%package maildirmake
Summary:	maildirmake - tool for making qmails' Maildirs
Summary(pl):	maildirmake - narzêdzie do zak³adania folerow Maildir
Group:		Applications/Mail
Conflicts:	courier-imap-maildirmake

%description maildirmake
Maildirmake is a tool for making mail folders in Maildir format.

%description maildirmake -l pl
Maildirmake jest narzêdziem do zak³adania folderów w formacie Maildir.

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
%setup -q -a1 -a2 -a4 -a5 -a6
%patch0 -p1 -b .install
%{?with_msglog:%patch1 -p1}
%patch2 -p1 -b .redhat
%patch3 -p1 -b .fixed.ids
%patch200 -p2 -b .qregex-starttls-2way-auth
%patch207 -p1 -b .qregex.memleak
#%patch6 -p1 -b .relayclient-ext .have to rethink logics with tls
%patch8 -p0 -b .tarpit
%patch9 -p0 -b .maxrcpt

# ipv6 patches fail
#%patch11 -p1 -b .qmail-ipv6

%patch12 -p1 -b .dns
%{!?with_routing:%patch20 -p1}
%patch21 -p1 -b .qmqpc-received.patch
%patch23 -p1 -b .extbouncer
%patch26 -p1 -b .errno
%{?with_home_etc:%patch27 -p1 -b .home_etc}
%patch28 -p1 -b .1.03.errno

# Not PLD patches.
%patch100 -p1 -b .doublebounce-trim

%patch101 -p1 -b .mfcheck
%patch102 -p1 -b .mfcheck.2

%patch103 -p1 -b .smtpd-fqdnhelo
# does not apply
#%patch104 -p1 -b .any-to-cname
%patch105 -p1 -b .sendmail-flagf

%patch201 -p2 -b .qmail-link-sync
%patch202 -p1 -b .qmail-0.0.0.0
%patch203 -p1 -b .qmail-date-localtime
%patch204 -p1 -b .qmail-limit-bounce-size
%patch205 -p1 -b .qmail-1.03-reread-concurrency
%patch206 -p1 -b .qmail-nullenvsender-recipcount

# qmail queue
%patch208 -p1 -b .qmailqueue
%patch209 -p1 -b .qmailqueue-docs

# holdremote
# pre-process to remove the header added upstream
zcat %{PATCH210} | sed '123,150d' | patch -p0

%patch211 -p0 -b .netscape-progress
%patch212 -p0 -b .sendmail-ignore-N
%patch213 -p1 -b .accept-5xx.tls
%patch214 -p1 -b .smtp-auth-close3
%patch215 -p1 -b .qmtpc
%patch216 -p1 -b .local-tabs
# skip. my systems have hidden limit of 1024 FD_SET size
#%patch217 -p1 -b .big-concurrency
#%patch218 -p1 -b .maildir++
#%patch219 -p1 -b .esmtp-size
%patch220 -p1 -b .smtpd-relay-reject
%patch106 -p1 -b .maildir-uniq
%patch221 -p1 -b .ipalias
#%patch222 -p1 -b .8bitmime
%patch223 -p0 -b .liberal-lf
%if %{with dkeys}
%patch224 -p1 -b .dk
%patch225 -p1 -b .dk-shared
%patch226 -p1 -b .dk-conf
%endif

mkdir -p qhpsi
tar zxvf %{SOURCE17} -C qhpsi
for a in qhpsi/*.patch; do
	patch -p2 < $a
done

# setup compiler. we use CFLAGS redefine rather using conditional patching.
echo -n "%{__cc} %{rpmcflags}" > conf-cc
echo -n "%{__cc} -s" > conf-ld

%if %{with tls}
echo "Enabling SSL/TLS functionality"
echo -n ' -DTLS' >> conf-cc
%endif

%if %{with ipv6}
echo "Enabling IPv6 support"
echo -n ' -DINET6' >> conf-cc
%endif

%if %{with home_etc}
echo "Enabling HOME_ETC"
echo -n ' -DUSE_HOME_ETC' >> conf-cc
echo -n ' -lhome_etc' >> conf-ld
%endif

# remove backup files after patching
rm -f *~

%build
%{__make} CFLAGS="%{rpmcflags}"
%{__make} man
%{__make} -C dot-forward-0.71
%{__make} -C fastforward-0.51
%{__make} -C queue-fix-1.4
%{__make} -C checkpass-1.2

%install
rm -rf $RPM_BUILD_ROOT

install -d boot
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_bindir},%{_mandir},%{_prefix}/lib,%{_libdir}/qmail,%{varqmail}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,profile.d,mail,pam.d,security,logrotate.d} \
	$RPM_BUILD_ROOT%{_sysconfdir}/qmail/{alias,control,users} \

ln -sf ../..%{_sysconfdir}/qmail/alias $RPM_BUILD_ROOT%{varqmail}
ln -sf ../..%{_sysconfdir}/qmail/control $RPM_BUILD_ROOT%{varqmail}
ln -sf ../..%{_sysconfdir}/qmail/users $RPM_BUILD_ROOT%{varqmail}
ln -sf ../..%{_libdir}/qmail $RPM_BUILD_ROOT%{varqmail}/bin
ln -sf ../..%{_mandir} $RPM_BUILD_ROOT%{varqmail}/man
ln -sf $RPM_BUILD_DIR/%{name}-%{version}/boot $RPM_BUILD_ROOT%{varqmail}/boot

./install -s $RPM_BUILD_ROOT

ln -sf qmail-qread $RPM_BUILD_ROOT%{_bindir}/mailq
ln -sf ../..%{varqmail}/bin/sendmail $RPM_BUILD_ROOT%{_sbindir}/sendmail
ln -sf ../..%{varqmail}/bin/sendmail $RPM_BUILD_ROOT%{_prefix}/lib/sendmail

# Set up boot procedures
install %{SOURCE8} $RPM_BUILD_ROOT/etc/profile.d/qmail.sh
install %{SOURCE9} $RPM_BUILD_ROOT/etc/profile.d/qmail.csh

install %{SOURCE18} $RPM_BUILD_ROOT/etc/logrotate.d/qmail
install %{SOURCE19} $RPM_BUILD_ROOT/etc/logrotate.d/qmail-pop3

# tcpserver (supervise)
PV=`basename %{SOURCE6}`
cd ${PV%.tar.bz2}

install -d $RPM_BUILD_ROOT/var/log/{,archiv/}qmail

install conf-{common,{pop3,qm{q,t}p,{rbl,}smtp}d,send} $RPM_BUILD_ROOT%{_sysconfdir}/qmail/control

install config-sanity-check qmail-config-system $RPM_BUILD_ROOT%{_libdir}/qmail
install rc $RPM_BUILD_ROOT%{varqmail}

install qmail-control $RPM_BUILD_ROOT/etc/rc.d/init.d/qmail

%if %{with tls}
install servercert.cnf $RPM_BUILD_ROOT%{_sysconfdir}/qmail/control

# SSL Certificate creation script
install mkservercert $RPM_BUILD_ROOT%{_libdir}/qmail

# RSA key generation cronjob
install -d $RPM_BUILD_ROOT/etc/cron.hourly
install qmail-genrsacert.sh $RPM_BUILD_ROOT/etc/cron.hourly

# for some files
install -d $RPM_BUILD_ROOT/var/qmail/control/tlshosts
> $RPM_BUILD_ROOT%{_sysconfdir}/qmail/control/clientcert.pem
%endif

install -d $RPM_BUILD_ROOT%{supervise}
for d in '' log; do
	for i in send smtpd qmtpd qmqpd pop3d; do
		install -d $RPM_BUILD_ROOT/var/log/{,archiv/}qmail/$i/$d

		install -d $RPM_BUILD_ROOT%{supervise}/$i/$d
		install -d $RPM_BUILD_ROOT%{supervise}/$i/$d/supervise

		> $RPM_BUILD_ROOT%{supervise}/$i/$d/supervise/lock
		> $RPM_BUILD_ROOT%{supervise}/$i/$d/supervise/status
		mkfifo $RPM_BUILD_ROOT%{supervise}/$i/$d/supervise/control
		mkfifo $RPM_BUILD_ROOT%{supervise}/$i/$d/supervise/ok

		install run-qmail$i$d $RPM_BUILD_ROOT%{supervise}/$i/$d/run
	done
done
# rblsmtpd log is separate. smtpd/log logs there
install -d $RPM_BUILD_ROOT/var/log/{,archiv/}qmail/rblsmtpd

install -d $RPM_BUILD_ROOT%{tcprules}
install Makefile.qmail{,-pop3} $RPM_BUILD_ROOT%{tcprules}
for i in smtp qmtp qmqp pop3; do
	install tcp.${i}.sample $RPM_BUILD_ROOT%{tcprules}/tcp.qmail-${i}
	tcprules $RPM_BUILD_ROOT%{tcprules}/tcp.qmail-$i.cdb \
		$RPM_BUILD_ROOT%{tcprules}/.tcp.qmail-$i.tmp < \
		$RPM_BUILD_ROOT%{tcprules}/tcp.qmail-$i
done
cd ..

# Set up mailing aliases
install %{SOURCE10} $RPM_BUILD_ROOT/etc/aliases
ln -sf ../aliases $RPM_BUILD_ROOT/etc/mail/aliases
install %{SOURCE11} $RPM_BUILD_ROOT%{_sysconfdir}/qmail/alias/.qmail-default
%{?with_msglog:install %{SOURCE12} $RPM_BUILD_ROOT%{_sysconfdir}/qmail/alias/.qmail-msglog}

for i in mailer-daemon postmaster; do
	echo "root" > $RPM_BUILD_ROOT%{_sysconfdir}/qmail/alias/.qmail-$i
done
> $RPM_BUILD_ROOT%{_sysconfdir}/qmail/alias/.qmail-root

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
install %{SOURCE13} $RPM_BUILD_ROOT%{_sysconfdir}/qmail/control/defaultdelivery

install %{SOURCE14} $RPM_BUILD_ROOT%{varqmail}/bin/qmail-lint
install %{SOURCE15} $RPM_BUILD_ROOT%{varqmail}/bin/qmail-qsanity

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

%if %{with dkeys}
install qmail-dk $RPM_BUILD_ROOT%{varqmail}/bin
install qmail-dk.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -d $RPM_BUILD_ROOT%{_sysconfdir}/qmail/control/domainkeys
%endif

# default folder in /etc/skel
install -d $RPM_BUILD_ROOT/etc/skel/Mail
./maildirmake $RPM_BUILD_ROOT/etc/skel/Mail/Maildir

install -d checkpass queue-fix
install checkpass-1.2/{CHECKPASSWORD,README} checkpass
install queue-fix-1.4/{CHANGES,README} queue-fix

cp %{SOURCE16} .

# What else?
mv -f $RPM_BUILD_ROOT%{varqmail}/bin/maildir2mbox	$RPM_BUILD_ROOT%{_bindir}
mv -f $RPM_BUILD_ROOT%{varqmail}/bin/maildirmake	$RPM_BUILD_ROOT%{_bindir}
mv -f $RPM_BUILD_ROOT%{varqmail}/bin/maildirwatch	$RPM_BUILD_ROOT%{_bindir}
mv -f $RPM_BUILD_ROOT%{varqmail}/bin/qmail-qread	$RPM_BUILD_ROOT%{_bindir}
mv -f $RPM_BUILD_ROOT%{varqmail}/bin/qmail-qsanity	$RPM_BUILD_ROOT%{_bindir}
mv -f $RPM_BUILD_ROOT%{varqmail}/bin/qmail-qstat	$RPM_BUILD_ROOT%{_bindir}
mv -f $RPM_BUILD_ROOT%{varqmail}/bin/queue-fix		$RPM_BUILD_ROOT%{_bindir}
mv -f $RPM_BUILD_ROOT%{varqmail}/bin/newaliases		$RPM_BUILD_ROOT%{_bindir}
mv -f $RPM_BUILD_ROOT%{varqmail}/bin/qmail-showctl	$RPM_BUILD_ROOT%{_bindir}

# remove mbox(5) man page which is in man-pages now and isn't strict qmail
# man page
rm -f $RPM_BUILD_ROOT%{_mandir}/man5/mbox.5

# remove doc, it's already in %doc
rm -rf $RPM_BUILD_ROOT%{varqmail}/doc

install %{SOURCE21} .

%if %{with tls}
install %{SOURCE22} $RPM_BUILD_ROOT%{_sysconfdir}/qmail/control/servercert.pem
> $RPM_BUILD_ROOT/%{_sysconfdir}/qmail/control/rsa512.pem
%endif

bzip2 -dc %{SOURCE23} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

bzip2 -dc %{SOURCE7} | tar xf -
echo "These are pl-translations taken from: \
	http://iidea.pl/~paweln/tlum/qmail-doki.tar.bz2" > qmail-doki/00-INDEX

# put manual pages to mandir
install -d $RPM_BUILD_ROOT%{_mandir}/pl/man{1,3,5,7,8,9}
# FIXME: these files conflict from qmail-pl-man-pages.tar.bz2
# qmail-clean.8 qmail-command.8 qmail-inject.8 qmail-local.8 qmail-lspawn.8
# qmail-qmqpc.8 qmail-qmqpd.8 qmail-qmtpd.8 qmail-qread.8 qmail-qstat.8
# qmail-queue.8 qmail-remote.8 qmail-rspawn.8 qmail-send.8 maildir.5
# qmail-control.5
#
# dot-qmail.9.gz qmail-getpw.9.gz qmail-limits.9.gz qmail-newmrh.9.gz
# qmail-newu.9.gz qmail-pw2u.9.gz qmail-send.9.gz qmail-start.9.gz
# qmail-users.9.gz
for a in 1 3 5 7 8 9; do
	i=$a
	# put .9 to .5
	[ "$a" = 9 ] && i=5
	install qmail-doki/*.$a $RPM_BUILD_ROOT%{_mandir}/pl/man$i
done
rm -f qmail-doki/*.[135789]

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

	echo "Now qmail will refuse to accept SMTP messages except to $FQDN."
	echo "Make sure to change rcpthosts if you add hosts to locals or virtualdomains!"
	echo Enter user, who should receive mail for root, mailer-daemon and postmaster
	echo into /etc/qmail/alias/.qmail-\{root,mailer-daemon,postmaster\}
fi

# Set up aliases
%{_bindir}/newaliases

# queue-fix makes life easy!
%{_bindir}/queue-fix %{varqmail}/queue >/dev/null

# build .cdb if missing
for i in smtp qmtp qmqp; do
	if [ ! -e %{tcprules}/tcp.qmail-$i.cdb ]; then
		tcprules %{tcprules}/tcp.qmail-$i.cdb %{tcprules}/.tcp.qmail-$i.tmp < %{tcprules}/tcp.qmail-$i
		chown qmaild:root %{tcprules}/tcp.qmail-$i.cdb
		chmod 640 %{tcprules}/tcp.qmail-$i.cdb
	fi
done

echo "The QMTP and QMQP protocols are supported, and can be started as:"
echo "ln -s %{supervise}/qmtpd /service/qmail-qmtpd"
echo "ln -s %{supervise}/qmqpd /service/qmail-qmqpd"
echo

# reload qmail-send on upgrade, the others are invoked anyway per connection
if [ -d /service/qmail-send/supervise ]; then
	svc -t /service/qmail-send /service/qmail-send/log
fi

ln -snf %{supervise}/send /service/qmail-send
ln -snf %{supervise}/smtpd /service/qmail-smtpd

%if %{with tls}
# session cert
/etc/cron.hourly/qmail-genrsacert.sh

# server cert
echo "Creating a self-signed ssl-certificate:"
%{_libdir}/qmail/mkservercert || true
%endif

%triggerpostun -- %{name} <= 1.03-56.12
if [ -f /var/lock/subsys/qmail ]; then
	if [ -f /var/lock/subsys/qmail ]; then
		. /etc/rc.d/init.d/functions
		msg_stopping qmail
		killproc qmail-send
		rm -f /var/lock/subsys/qmail
	fi
fi
/sbin/chkconfig --del qmail

# this should kill the old instance running on inetd
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
fi

%triggerpostun -- %{name}-pop3 <= 1.03-56.12
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
fi

# move dot-qmail to new location
%triggerpostun -- %{name} <= 1.03-56.5
if [ -f /etc/qmail/dot-qmail.rpmsave ]; then
	echo "Moving /etc/qmail/dot-qmail.rpmsave to /etc/qmail/control/defaultdelivery"
	mv -f /etc/qmail/control/defaultdelivery /etc/qmail/control/defaultdelivery.rpmnew
	mv -f /etc/qmail/dot-qmail.rpmsave /etc/qmail/control/defaultdelivery
fi

# move server cert to new location
if [ -f /etc/qmail/control/cert.pem.rpmsave ]; then
	echo "Moving /etc/qmail/control/cert.pem to /etc/qmail/control/servercert.pem"
	mv -f /etc/qmail/control/servercert.pem /etc/qmail/control/servercert.pem.rpmnew
	mv -f /etc/qmail/control/cert.pem.rpmsave /etc/qmail/control/servercert.pem
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
	%groupremove nofiles
	%groupremove qmail
fi

%preun
# If package is being erased for the last time.
if [ "$1" = "0" ]; then
	# remove form supervise
	# http://cr.yp.to/daemontools/faq/create.html#remove
	for i in send smtpd qmtpd qmqpd; do
		[ -d /service/qmail-$i/supervise ] || continue
		cd /service/qmail-$i
		rm /service/qmail-$i
		svc -dx . log
	done
fi

%post pop3
# build .cdb if missing
if [ ! -e %{tcprules}/tcp.qmail-pop3.cdb ]; then
	tcprules %{tcprules}/tcp.qmail-pop3.cdb %{tcprules}/.tcp.qmail-pop3.tmp < %{tcprules}/tcp.qmail-pop3
	chown qmaild:root %{tcprules}/tcp.qmail-pop3.cdb
	chmod 640 %{tcprules}/tcp.qmail-pop3.cdb
fi

# add to supervise
ln -snf %{supervise}/pop3d /service/qmail-pop3d

%preun pop3
# If package is being erased for the last time.
if [ "$1" = "0" ]; then
	# remove form supervise
	if [ -d /service/qmail-pop3d/supervise ]; then
		cd /service/qmail-pop3d
		rm /service/qmail-pop3d
		svc -dx . log
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
fi

%files
%defattr(644,root,root,755)
%doc FAQ INSTALL* PIC* REMOVE* SENDMAIL TEST* UPGRADE
%doc BLURB* README SECURITY THANKS THOUGHTS TODO VERSION
%doc boot checkpass queue-fix
%doc tarpit.README
%doc qmail-doki
%if %{with tls}
%doc README.auth README.remote-auth README.starttls README.qregex
%endif

# QHPSI License requires all files to be distributed.
%doc qhpsi

%attr(755,root,root) %dir /etc/mail
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
%attr(600,qmails,qmail) %config(noreplace) %verify(not md5 mtime size) %ghost %{varqmail}/queue/lock/sendmutex
%attr(644,qmailr,qmail) %config(noreplace) %verify(not md5 mtime size) %ghost %{varqmail}/queue/lock/tcpto
%attr(622,qmails,qmail) %config(noreplace) %verify(not md5 mtime size) %ghost %{varqmail}/queue/lock/trigger
%attr(644,root,nofiles) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/qmail/alias/.qmail-*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/defaultdomain
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/locals
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/me
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/plusdomain
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/rcpthosts
%if %{with tls}
%ghost %{_sysconfdir}/qmail/control/rsa512.pem
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/servercert.cnf
%attr(640,qmaild,qmail) %ghost %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/servercert.pem
%ghost %{_sysconfdir}/qmail/control/clientcert.pem
%endif
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/control/defaultdelivery
%config(noreplace) %verify(not mtime) %{_sysconfdir}/qmail/control/conf-common
%config(noreplace) %verify(not mtime) %{_sysconfdir}/qmail/control/conf-qmqpd
%config(noreplace) %verify(not mtime) %{_sysconfdir}/qmail/control/conf-qmtpd
%config(noreplace) %verify(not mtime) %{_sysconfdir}/qmail/control/conf-send
%config(noreplace) %verify(not mtime) %{_sysconfdir}/qmail/control/conf-smtpd
%config(noreplace) %verify(not mtime) %{_sysconfdir}/qmail/control/conf-rblsmtpd
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/qmail/users/*
%config(noreplace) %verify(not size mtime md5) /etc/aliases
/etc/mail/aliases
%config(noreplace) %verify(not mtime) /etc/logrotate.d/qmail
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) /etc/profile.d/*
%attr(754,root,root) /etc/rc.d/init.d/*
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
%attr(755,root,root) %{_bindir}/qmail-showctl
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
%if %{with dkeys}
%attr(755,root,root) %{_libdir}/qmail/qmail-dk
%dir %attr(751,qmaild,root) %{_sysconfdir}/qmail/control/domainkeys
%endif
%attr(755,root,root) %{varqmail}/rc

%attr(755,root,root) %{_libdir}/qmail/config-sanity-check
%attr(755,root,root) %{_libdir}/qmail/qmail-config-system

%if %{with tls}
%attr(755,root,root) %{_libdir}/qmail/mkservercert
%attr(755,root,root) /etc/cron.hourly/qmail-genrsacert.sh
%dir %{_sysconfdir}/qmail/control/tlshosts
%endif

%{tcprules}/Makefile.qmail
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{tcprules}/tcp.qmail-smtp
%attr(640,qmaild,root) %config(noreplace) %verify(not size mtime md5) %ghost %{tcprules}/tcp.qmail-smtp.cdb
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{tcprules}/tcp.qmail-qmtp
%attr(640,qmaild,root) %config(noreplace) %verify(not size mtime md5) %ghost %{tcprules}/tcp.qmail-qmtp.cdb
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{tcprules}/tcp.qmail-qmqp
%attr(640,qmaild,root) %config(noreplace) %verify(not size mtime md5) %ghost %{tcprules}/tcp.qmail-qmqp.cdb

%attr(755,qmaill,root) %dir /var/log/qmail
%attr(750,root,root) %dir /var/log/archiv/qmail
%attr(755,root,root) %dir %{supervise}

%attr(1755,root,root) %dir %{supervise}/smtpd
%attr(755,root,root) %{supervise}/smtpd/run
%attr(700,root,root) %dir %{supervise}/smtpd/supervise

%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{supervise}/smtpd/supervise/*
%attr(1755,root,root) %dir %{supervise}/smtpd/log
%attr(755,root,root) %{supervise}/smtpd/log/run
%attr(700,root,root) %dir %{supervise}/smtpd/log/supervise
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{supervise}/smtpd/log/supervise/*
%attr(755,qmaill,root) %dir /var/log/qmail/smtpd
%attr(750,root,root) %dir /var/log/archiv/qmail/smtpd
%attr(755,qmaill,root) %dir /var/log/qmail/rblsmtpd
%attr(750,root,root) %dir /var/log/archiv/qmail/rblsmtpd

%attr(1755,root,root) %dir %{supervise}/send
%attr(755,root,root) %{supervise}/send/run
%attr(700,root,root) %dir %{supervise}/send/supervise
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{supervise}/send/supervise/*
%attr(1755,root,root) %dir %{supervise}/send/log
%attr(755,root,root) %{supervise}/send/log/run
%attr(700,root,root) %dir %{supervise}/send/log/supervise
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{supervise}/send/log/supervise/*
%attr(755,qmaill,root) %dir /var/log/qmail/send
%attr(750,root,root) %dir /var/log/archiv/qmail/send

%attr(1755,root,root) %dir %{supervise}/qmtpd
%attr(755,root,root) %{supervise}/qmtpd/run
%attr(700,root,root) %dir %{supervise}/qmtpd/supervise
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{supervise}/qmtpd/supervise/*
%attr(1755,root,root) %dir %{supervise}/qmtpd/log
%attr(755,root,root) %{supervise}/qmtpd/log/run
%attr(700,root,root) %dir %{supervise}/qmtpd/log/supervise
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{supervise}/qmtpd/log/supervise/*
%attr(755,qmaill,root) %dir /var/log/qmail/qmtpd
%attr(750,root,root) %dir /var/log/archiv/qmail/qmtpd

%attr(1755,root,root) %dir %{supervise}/qmqpd
%attr(755,root,root) %{supervise}/qmqpd/run
%attr(700,root,root) %dir %{supervise}/qmqpd/supervise
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{supervise}/qmqpd/supervise/*
%attr(1755,root,root) %dir %{supervise}/qmqpd/log
%attr(755,root,root) %{supervise}/qmqpd/log/run
%attr(700,root,root) %dir %{supervise}/qmqpd/log/supervise
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{supervise}/qmqpd/log/supervise/*
%attr(755,qmaill,root) %dir /var/log/qmail/qmqpd
%attr(750,root,root) %dir /var/log/archiv/qmail/qmqpd

%attr(755,root,root) %{_bindir}/mailq
%attr(755,root,root) %{_sbindir}/sendmail
%attr(755,root,root) %{_prefix}/lib/sendmail
%attr(2755,alias,qmail) %{varqmail}/alias
%attr(755,root,root) %{varqmail}/bin
%attr(755,root,root) %{varqmail}/control
%attr(755,root,root) %{varqmail}/users
%{_mandir}/man1/[!m]*
%{_mandir}/man1/maildir2mbox*
%{_mandir}/man1/maildirwatch*
%{_mandir}/man1/mailsubj*
%{_mandir}/man[357]/*
%{_mandir}/man8/[!q]*
%{_mandir}/man8/qmail-[!p]*
%{_mandir}/man8/qmail-p[!o]*
%lang(pl) %{_mandir}/pl/man1/[!m]*
%lang(pl) %{_mandir}/pl/man1/maildir2mbox*
%lang(pl) %{_mandir}/pl/man1/maildirwatch*
%lang(pl) %{_mandir}/pl/man1/mailsubj*
%lang(pl) %{_mandir}/pl/man[357]/*
%lang(pl) %{_mandir}/pl/man8/[!q]*
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

%attr(755,root,root) %dir /etc/mail
%attr(755,root,root) %dir %{_sysconfdir}/qmail
%attr(755,root,root) %dir %{_sysconfdir}/qmail/control
%attr(755,root,root) %dir %{_libdir}/qmail
%attr(755,root,root) %dir %{varqmail}
%attr(755,root,root) %{varqmail}/bin
%attr(755,root,root) %{varqmail}/control
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/qmail/control/defaultdomain
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/qmail/control/me
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/qmail/control/plusdomain
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/qmail/control/idhost
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/qmail/control/qmqpservers
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/profile.d/*
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
%attr(755,root,root) %{_bindir}/qmail-showctl
%attr(755,root,root) %{_libdir}/qmail/sendmail
%attr(755,root,root) %{_sbindir}/sendmail
%attr(755,root,root) %{_prefix}/lib/sendmail
%{_mandir}/man1/maildir2mbox*
%{_mandir}/man1/maildirwatch*
%{_mandir}/man1/mailsubj*
%{_mandir}/man5/qmail-header*
%{_mandir}/man5/qmail-log*
%{_mandir}/man8/qmail-inject*
%{_mandir}/man8/qmail-qmqpc*
%{_mandir}/man8/qmail-queue*
%{_mandir}/man8/qmail-showctl*
%lang(pl) %{_mandir}/pl/man1/maildir2mbox*
%lang(pl) %{_mandir}/pl/man1/maildirwatch*
%lang(pl) %{_mandir}/pl/man1/mailsubj*
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
%lang(pl) %{_mandir}/pl/man1/maildirmake*

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qmail-qsanity
%attr(755,root,root) %{_libdir}/qmail/qmail-lint

%files pop3
%defattr(644,root,root,755)
%{tcprules}/Makefile.qmail-pop3
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{tcprules}/tcp.qmail-pop3
%attr(640,qmaild,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{tcprules}/tcp.qmail-pop3.cdb
%config(noreplace) %verify(not mtime) %{_sysconfdir}/qmail/control/conf-pop3d
%config(noreplace) %verify(not mtime) /etc/logrotate.d/qmail-pop3

%attr(1755,root,root) %dir %{supervise}/pop3d
%attr(755,root,root) %{supervise}/pop3d/run
%attr(700,root,root) %dir %{supervise}/pop3d/supervise
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{supervise}/pop3d/supervise/*
%attr(1755,root,root) %dir %{supervise}/pop3d/log
%attr(755,root,root) %{supervise}/pop3d/log/run
%attr(700,root,root) %dir %{supervise}/pop3d/log/supervise
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{supervise}/pop3d/log/supervise/*
%attr(755,qmaill,root) %dir /var/log/qmail/pop3d
%attr(750,root,root) %dir /var/log/archiv/qmail/pop3d

%attr(755,root,root) %{_libdir}/qmail/qmail-pop3d
%attr(755,root,root) %{_libdir}/qmail/qmail-popup
%{_mandir}/man8/qmail-po*
%lang(pl) %{_mandir}/pl/man8/qmail-po*
