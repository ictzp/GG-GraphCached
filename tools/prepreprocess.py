import sys
import string
import struct

if len(sys.argv) != 2:
	print "Usage: python prepreprocess.py <filename>"
	exit(0)
filename = sys.argv[1]
infile = open(filename, "r")
outfile = open(filename+".bi", "wb")
for line in infile:
	if line.strip()[0] == '#':
		continue  #skip comments lines
	edge = line.split()

	outfile.write(struct.pack('I', int(edge[0])))
	outfile.write(struct.pack('I', int(edge[1])))
outfile.close()
infile.close()


