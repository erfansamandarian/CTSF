import whois
import re


def clear_url(target):
    return re.sub(".*www\.", "", target, 1).split("/")[0].strip()


def get_who(domain):
    print("WHOIS DATA")
    print("=" * 32)
    w = whois.whois(clear_url(domain))
    print("Domain Name: {}".format(w.domain_name))
    print("-" * 32)
    print("Registrar: {}".format(w.registrar))
    print("-" * 32)
    print("WHOIS Server: {}".format(w.whois_server))
    print("-" * 32)
    print("Referral URL: {}".format(w.referral_url))
    print("-" * 32)
    print("Updated Date: {}".format(w.updated_date))
    print("-" * 32)
    print("Creation Date: {}".format(w.creation_date))
    print("-" * 32)
    print("Expiration Date: {}".format(w.expiration_date))
    print("-" * 32)
    print("Name Servers: {}".format(w.name_servers))
    print("-" * 32)
    print("Status: {}".format(w.status))
    print("-" * 32)
    print("Emails: {}".format(w.emails))
    print("-" * 32)
    print("DNSSEC: {}".format(w.dnssec))
    print("-" * 32)
    print("Name: {}".format(w.name))
    print("-" * 32)
    print("Org: {}".format(w.org))
    print("-" * 32)
    print("Address: {}".format(w.address))
    print("-" * 32)
    print("City: {}".format(w.city))
    print("-" * 32)
    print("State: {}".format(w.state))
    print("-" * 32)
    print("Registrant Postal Code: {}".format(w.registrant_postal_code))
    print("-" * 32)
    print("Country: {}".format(w.country))

    print("=" * 32)
