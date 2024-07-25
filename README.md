# CTSF

Certificate Transparency Subdomain Finder + WHOIS Data

```
.------..------..------..------.
|C.--. ||T.--. ||S.--. ||F.--. |
| :/\: || :/\: || :(): || :/\: |
| :\/: || (__) || ()() || :\/: |
| '--'C|| '--'T|| '--'S|| '--'F|
`------'`------'`------'`------'
```

## About 

Tool to get subdomains via Certificate Transparency logs and WHOIS Data.

Remade to be installable with PIP and remove duplicates.

## Example 

```
ctsf --domain centrecom.com.au

+--------------------------------+
| Subdomains                     |
+================================+
| *.centrecom.com.au             |
+--------------------------------+
| centrecom.com.au               |
+--------------------------------+
| chavington.centrecom.com.au    |
+--------------------------------+
| computers.centrecom.com.au     |
+--------------------------------+
| edm.centrecom.com.au           |
+--------------------------------+
| eduportal.centrecom.com.au     |
+--------------------------------+
| sfngya.centrecom.com.au        |
+--------------------------------+
| www.centrecom.com.au           |
+--------------------------------+
| www.computers.centrecom.com.au |
+--------------------------------+
| www.eduportal.centrecom.com.au |
+--------------------------------+
```

## Installation 

###  PyPi

```
pip install ctsf --break-system-packages && ctsf --help
```

###  System

```
git clone https://github.com/erfansamandarian/CTSF.git && cd CTFS && pip3 install . --break-system-packages && ctsf --help
```

### Virtual Environment 📦

```
git clone https://github.com/erfansamandarian/CTSF.git && cd CTFS && python3 -m venv venv && source venv/bin/activate && pip3 install . && ctsf --help
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
