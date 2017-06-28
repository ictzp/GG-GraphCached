import string
import re
import mmap
import sys

def parse_mem_scale(filename):
	iofile = open(filename, 'r')
	pattern = re.compile(r"^\d+\nrchar:\s\d+\nwchar:\s\d+\nsyscr:\s\d+\nsyscw:\s\d+\nread_bytes:\s\d+\nwrite_bytes:\s\d+\ncancelled_write_bytes:\s\d+", re.MULTILINE)
	data = iofile.read()
	#print data
	#mo1 = pattern.match("123\nrchar: 123\nwchar: 999\nsyscr: 999\nsyscw: 233\nread_bytes: 888\nwrite_bytes: 777\ncancelled_write_bytes: 888\n")
	#print mo1
	mo = pattern.findall(data)
	cur_pid = 0
	write_bytes = 0
	read_bytes = 0
	rchar = 0
	wchar = 0
	for rec in mo:
		records = re.split("\n+", rec)
		pid = records[0]
		if cur_pid != pid:
			cur_pid = pid
			#print pid
			#print read_bytes
			if sys.argv[2] == 'rb':
				print read_bytes
			elif sys.argv[2] == 'wb':
				print write_bytes
			elif sys.argv[2] == 'rc':
				print rchar
			elif sys.argv[2] == 'wc':
				print wchar
			write_bytes = records[6].split()[1]
			read_bytes = records[5].split()[1]
			rchar = records[1].split()[1]
			wchar = records[2].split()[1]
		else:
			write_bytes = records[6].split()[1]
			read_bytes = records[5].split()[1]
			rchar = records[1].split()[1]
			wchar = records[2].split()[1]
	if sys.argv[2] == 'rb':
		print read_bytes
	elif sys.argv[2] == 'wb':
		print write_bytes
	elif sys.argv[2] == 'rc':
		print rchar
	elif sys.argv[2] == 'wc':
		print wchar


if len(sys.argv) != 3:
	print "Usage: python parse_io.py [filename] [rb/wb/rc/wc]"
parse_mem_scale(sys.argv[1])
	
	
