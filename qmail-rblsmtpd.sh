#!/bin/sh
exec \
/usr/lib/qmail/rblsmtpd -r sbl.spamhaus.org \
/usr/lib/qmail/rblsmtpd -r cbl.abuseat.org \
/usr/lib/qmail/rblsmtpd -r list.dsbl.org \
/usr/lib/qmail/rblsmtpd -r dnsbl.njabl.org \
/usr/lib/qmail/rblsmtpd -r relays.ordb.org \
/usr/lib/qmail/rblsmtpd -r opm.blitzed.org \
/usr/lib/qmail/rblsmtpd -r dsn.rfc-ignorant.org \
/usr/lib/qmail/rblsmtpd -r ipwhois.rfc-ignorant.org \
/usr/lib/qmail/rblsmtpd -r postmaster.rfc-ignorant.org \
/usr/lib/qmail/rblsmtpd -r dnsbl.sorbs.net \
/usr/lib/qmail/rblsmtpd -r bl.spamcop.net \
"$@"

exit 1
