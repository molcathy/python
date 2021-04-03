import os

def read_from_file(filename):
    if not os.path.exists(filename):
        raise Exception("Bad File")
    infile = open(filename, "r")
    line = infile.readline()
    return line