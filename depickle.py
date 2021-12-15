#!/usr/bin/env python3

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, version 3 only
# 
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
# 
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys, getopt
import json
import pickle

class Rick(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        if type(obj).__name__ == "partial":
            return str(obj)
        if type(obj).__name__ == "Pattern":
            return str(obj)
        if type(obj).__name__ == "ndarray":
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

def unpickle(infile, outfile):
    with open(infile, "rb") as r:
        with open(outfile, "w") as w:
            json.dump(pickle.load(r), w, cls=Rick)

def usage():
    print("USAGE: depickle.py -i <INPUT> -o <OUTPUT>")
    print("  Both input and output must be provided")
    print("  Input from stdin is not supported, use the <() feature")
    print("  of bash (or your shell's equivalent) if you need this")

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["help", "input=", "output="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    infile = None
    outfile = None
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-i", "--input"):
            infile = arg
        elif opt in ("-o", "--output"):
            outfile = arg
    if not infile or not outfile:
        if not infile:
            print("No -i/--input file provided")
        if not outfile:
            print("No -o/--output file provided")
        sys.exit(1)

    unpickle(infile, outfile)

if __name__ == "__main__":
    main()
