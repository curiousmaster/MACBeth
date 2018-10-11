# MACBeth
MACBeth is a quick hack to do local MAC Address lookups without external dependencies.
## populate.py
This script generates a SQLite3 database from a CSV file.

    ./populate.py {file}

    make {csv=file.py}
    
### Infile
The csv file should have three columns

    OUI;Company;Address

See: https://regauth.standards.ieee.org/standards-ra-web/pub/view.html#registries

## macbeth.py
Query local database for Company or OUI

    -h, --help            show this help message and exit
    -c COMPANY, --company COMPANY
                          Specify company
    -o OUI, --oui OUI     Specify OUI
