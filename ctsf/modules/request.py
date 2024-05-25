import re
import requests
from tabulate import tabulate
from termcolor import colored

version = "1.0.5"  # can i change this in setup.py?


def banner():
    banner = """
.------..------..------..------.
|C.--. ||T.--. ||F.--. ||S.--. |
| :/\: || :/\: || :(): || :/\: |
| :\/: || (__) || ()() || :\/: |
| '--'C|| '--'T|| '--'F|| '--'S|
`------'`------'`------'`------'
	Version: {v}
	""".format(
        v=version
    )
    print(banner)


def clear_url(target):
    return re.sub(".*www\.", "", target, 1).split("/")[0].strip()


def get_request(domain):
    banner()
    subdomains = []
    target = clear_url(domain)

    req = requests.get("https://crt.sh/?q=%.{d}&output=json".format(d=target))

    for index, value in enumerate(req.json()):
        subdomains.extend(value["name_value"].split("\n"))

    subdomains = list(sorted(set(subdomains)))

    header = "Subdomain" if len(subdomains) == 1 else "Subdomains"
    colored_header = colored(header, "red")
    data = [{colored_header: subdomain} for subdomain in subdomains]

    print(tabulate(data, headers="keys", tablefmt="grid"))
    print()
