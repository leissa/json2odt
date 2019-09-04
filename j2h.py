#!/bin/python

import json
import os
import sys
from json2html import *

infile_json = sys.argv[1];
infile      = os.path.splitext(infile_json)[0]
infile_html  = infile + '.html'

with open(infile_json) as f:
    data = json.load(f)

#print(data)
data = data["videos"][0]["insights"]["transcript"]
for row in data:
    del row["id"]
    del row["confidence"]
    del row["language"]
    for x in row["instances"]:
        del x["adjustedStart"]
        del x["adjustedEnd"]
        start = x["start"]
        end   = x["end"]
    t = row["text"];
    i = row["instances"]
    s = row["speakerId"]

    del row["instances"]
    del row["speakerId"]
    del row["text"]

    row["start"] = start
    row["end"]   = end
    row["id"] = s
    row["text"] = t

# output = json2html.convert(json=data, table_attributes="id=\"info-table\" class=\"table table-bordered table-hover\"")
output = json2html.convert(json=data)
output = '<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>' + output

f = open(infile_html, 'w')
f.write(output)
f.close()
