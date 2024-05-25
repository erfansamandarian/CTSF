from tabulate import tabulate
from termcolor import colored
import re
import whois


def clear_url(target):
    return re.sub(".*www\.", "", target, 1).split("/")[0].strip()


def get_who(domain):
    w = whois.whois(clear_url(domain))
    data = [
        ["Domain Name", w.domain_name],
        ["Registrar", w.registrar],
        ["WHOIS Server", w.whois_server],
        ["Referral URL", w.referral_url],
        ["Updated Date", w.updated_date],
        ["Creation Date", w.creation_date],
        ["Expiration Date", w.expiration_date],
        ["Name Servers", w.name_servers],
        ["Status", w.status],
        ["Emails", w.emails],
        ["DNSSEC", w.dnssec],
        ["Name", w.name],
        ["Org", w.org],
        ["Address", w.address],
        ["City", w.city],
        ["State", w.state],
        ["Registrant Postal Code", w.registrant_postal_code],
        ["Country", w.country],
    ]
    headers = [colored("Property", "red"), colored("Value", "red")]
    print(tabulate(data, headers=headers, tablefmt="grid"))
