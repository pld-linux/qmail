#!/bin/sh

# manual whitelist
# -glen 2004-01-12
case "$TCPREMOTEIP" in
194.126.101.94|mail.hot.ee | \
194.106.105.6|eemail1.microlink.ee| \
194.106.120.39|red.microlink.ee )
	export RBLSMTPD=""
	;;
esac

if [ -x /usr/lib/qmail/qmail-scanner-queue ]; then
	export QMAILQUEUE="/usr/lib/qmail/qmail-scanner-queue"
fi

exec \
/usr/lib/qmail/rblsmtpd.sh \
/usr/lib/qmail/qmail-smtpd
