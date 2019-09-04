#!/usr/bin/bash

set -eu

export PATH="/home/roland/.gem/ruby/2.5.0/bin:$PATH"

for json in *.json
do
    html="${json%.json}.html"
    odt="${json%.json}.odt"
    ./j2h.py "${json}"
    html2odt.rb -i "${html}" -o "${odt}"
done
