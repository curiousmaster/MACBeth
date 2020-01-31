# MACBeth
MACBeth is a quick hack to do local MAC Address lookups without external dependencies.
## populate.py
This script generates a SQLite3 database from a CSV file.

    ./populate.py {file}

    make {csv=file.py}
    
### Infile
The csv file should have three (four) columns

    [HEADER,]OUI,Company,Address

See: https://regauth.standards.ieee.org/standards-ra-web/pub/view.html#registries
     http://standards-oui.ieee.org/oui/oui.csv


## macbeth.py
Query local database for Company or OUI

    -h, --help            show this help message and exit
    -c COMPANY, --company COMPANY
                          Specify company
    -o OUI, --oui OUI     Specify OU
