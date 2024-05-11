# CTSF

Certificate Transparency Subdomain Finder + WHOIS Data

```
.------..------..------..------.
|C.--. ||T.--. ||F.--. ||S.--. |
| :/\: || :/\: || :(): || :/\: |
| :\/: || (__) || ()() || :\/: |
| '--'C|| '--'T|| '--'F|| '--'S|
`------'`------'`------'`------'
```

## About 

Tool to get subdomains via Certificate Transparency logs and WHOIS Data.

Remade to be installable with PIP.

## Installation 

###  PyPi

```
pip install ctsf 
```

###  System

```
cd CTFS

pip install .
```

### Virtual Environment 📦

```
cd CTFS

python -m venv venv

source venv/bin/activate

pip install .
```

## Usage 🃏

CTSF

```
ctfs --domain "google.com"
```

CTSF + WHOIS

```
ctfs --domain "google.com" --who
```

## Credits

Sheila A. Berta: https://github.com/UnaPibaGeek/ctfr

Richard Penman: https://github.com/richardpenman/whois
