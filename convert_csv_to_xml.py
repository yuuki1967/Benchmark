import os
import csv

CURRENT_DIR = r"c:\Users\YuukiE\Documents\Cx\workspace\Benchmark"
CX_CSV_FILE = r"cx_results\CxIAST aggregated scan_263 results 2020-02-14T08-52-55.329Z.csv"
CX_XML_FILE = r"results\Benchmark_1.2_Scorecard_for_CxIAST_Java.xml"
BASE_FILE = r"expectedresults-1.2.csv"

os.chdir(CURRENT_DIR)

cx_xml_file = open(CX_XML_FILE, "w")
base_file = open(BASE_FILE,"r")
base_csv_file = csv.reader(base_file)

cx_file = open(CX_CSV_FILE,"r")
cx_csv_file = csv.reader(cx_file)

header_string = r"""<?xml version="1.0" encoding="utf-8"?>
<CxXMLResults ProjectName="Benchmark">"""

cx_xml_file.write(header_string)

data = []
for row in cx_csv_file:
    data.append(row)

test_name = []
for item in base_csv_file:
    test_name.append(item[0])

cx_file.close()

def convert_row(row, class_name):
    return """<Result id="%s" Type="%s" Severity="%s" Time="%s" Filename="%s" CweId="%s" Class="%s">""" % (row[0], row[1], row[2], row[3], row[8], row[15], class_name)

#print ('\n'.join([convert_row(row) for row in data[1:]]))
#cx_xml_file.write ('\n'.join([convert_row(row) for row in data[1:]]))
for row in data[1:]:
    for _test_name in test_name:
        if(_test_name in row[8]):
            cx_xml_file.write('\n'+convert_row(row, _test_name))
            cx_xml_file.write('\n</Result>')
cx_xml_file.write('\n</CxXMLResults>')
cx_xml_file.close()
base_file.close()
