import argparse

from ctsf.core.handler import Config
from ctsf.core.runner import Runner


def arguments():
    parser = argparse.ArgumentParser(
        prog="ctsf", description="Certificate Transparency Subdomain Finder"
    )
    parser.add_argument("--domain", help="Uniform Resource Locator", required=True)
    parser.add_argument(
        "--who",
        help="WHOIS Data",
        default="false",
        action="store_true",
    )
    args = parser.parse_args()
    return Config(args)


def main():
    config = arguments()
    Runner(config).run()
