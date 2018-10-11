#! /usr/bin/python
# =================================================
# NAME
#    macbeth.py - MAC address lookup
#
# USAGE
#    macbeth.py [-h] [-c COMPANY] [-o OUI]
#       -h, --help          Show this help message and exit
#       -c COMPANY,
#       --company COMPANY   Specify company
#       -o OUI, --oui OUI   Specify OUI
#
# AUTHOR
#    Oct 11, 2018 / Curious Master
#       initial release
# =================================================

import sqlite3
import re
import sys
import argparse
import tabulate

ARGS = ""
COMPANY = ""
OUI = ""


def parseArgs():
    global ARGS
    global OUI
    global COMPANY

    ap = argparse.ArgumentParser(description="OUI Look")
    ap.add_argument("-c", "--company", required=False, help="Specify company")
    ap.add_argument("-o", "--oui", required=False, help="Specify OUI")

    ARGS = vars(ap.parse_args())

    if ARGS['oui']:
        OUI = ARGS['oui']
        OUI = re.sub("[:,\- ]", "", OUI)
        OUI = OUI.strip()
        OUI = OUI[0:6]

    if ARGS['company']:
        COMPANY = ARGS['company']


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


DB = "oui.sqlite3"
CONN = sqlite3.connect(DB)
CONN.row_factory = dict_factory
C = CONN.cursor()


def main(argv):
    parseArgs()

    if ARGS['oui']:
        sql = "SELECT * from oui WHERE oui like '%{oui}%';".format(oui=OUI)
        C.execute(sql)
        ret = C.fetchall()
        output = []
        for r in ret:
            oui = r['oui']
            company = r['company'].encode('utf8')
            address = r['address'].encode('utf8')
            output.append([
                oui,
                company,
                address
                ])

        print(tabulate.tabulate(output, headers=["OUI", "COMPANY", "ADDRESS"], tablefmt="simple"))

    CONN.commit()
    CONN.close()


if __name__ == "__main__":
    main(sys.argv)
