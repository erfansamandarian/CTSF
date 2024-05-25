from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="ctsf",
    description="Certificate Transparency Subdomain Finder + WHOIS Data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Erfan Samandarian",
    author_email="mail@erfansamandarian.com",
    url="https://erfansamandarian.com/ctsf",
    license="MIT",
    version="1.0.5",
    packages=find_packages(),
    install_requires=["requests", "python-whois", "tabulate", "termcolor"],
    py_modules=["ctsf"],
    entry_points={"console_scripts": ["ctsf=ctsf:main"]},
)
