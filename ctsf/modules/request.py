import re
import requests
from tabulate import tabulate
from termcolor import colored

def banner(version):
    banner = """
.------..------..------..------.
|C.--. ||T.--. ||S.--. ||F.--. |
| :/\: || :/\: || :(): || :/\: |
| :\/: || (__) || ()() || :\/: |
| '--'C|| '--'T|| '--'S|| '--'F|
`------'`------'`------'`------'
	Version: {v}
	""".format(
        v=version
    )
    print(banner)


def clear_url(target):
    return re.sub(".*www\.", "", target, 1).split("/")[0].strip()


def get_request(domain, version):
    banner(version)
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
