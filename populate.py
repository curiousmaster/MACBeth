#! /usr/bin/python
# =================================================
# NAME
#    populate.py
#
# USAGE
#    populate.py [file.csv]
#
# DESCRIPTION
#    Generate sqlite3 database from csv file (see README.md)
#
# =================================================

import sys
import sqlite3
import re
import os.path


def dict_factory(cursor, row):
    # --------------------------------------------------
    # NAME
    #   dict_factory()
    #
    # DESCRIPTION
    #   Output SQLite3 queries JSON formatted
    # --------------------------------------------------

    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


CSVFILE = "oui.csv"

DB = "oui.sqlite3"
CONN = sqlite3.connect(DB)
CONN.row_factory = dict_factory
C = CONN.cursor()


def main(argv):

    if len(argv) == 2:
        csvfile = argv[1]
    else:
        csvfile = CSVFILE

    if os.path.exists(csvfile):
        sql = "CREATE TABLE IF NOT EXISTS oui (key INTEGER PRIMARY KEY, oui TEXT UNIQUE, company TEXT, address TEXT);"
        C.execute(sql)

        with open(csvfile, "r") as f:
            for line in f:
                line = line.strip()
                oui, company, address = line.split(";")
                company = re.sub("[\"]", "", company)
                company = company.strip()
    
                if company == "Private":
                    address = ""
    
                else:
                    address = re.sub("[\"]", "", address)
                    address = address.strip()
    
                sql = "INSERT INTO oui (company, oui, address) VALUES (\"{company}\", \"{oui}\", \"{address}\");".format(company=company, oui=oui, address=address)
                try:
                    C.execute(sql)
                except Exception as E:
                    print str(E) + " (" + sql
    
        CONN.commit()
        CONN.close()

    else:
        print "ERROR: csv file does not exist"
        sys.exit()

if __name__ == "__main__":
    main(sys.argv)
