import os
import subprocess
import string

def get_pid(prog_name):
	while True:
		p = subprocess.Popen("ps aux | grep " + prog_name + " | grep -v systemd | grep -v grep", stdout = subprocess.PIPE, shell = True)
		line = p.stdout.read()
		if line != '':
			print line
			return string.split(line)[1]

def run_cc(filename, k):
	#command = 'systemd-run -p MemoryLimit=' + str(k) + 'G -p LimitNOFILE=40000 --setenv=WorkingDirectory=/home/zhaopeng/graph/GridGraph -t' + ' ./bin/wcc ' + filename + ' ' + str(k)
	command = 'systemd-run -p MemoryLimit=' + str(k) + 'G -p LimitNOFILE=40000 --setenv=LD_LIBRARY_PATH=/usr/local/lib --setenv=WorkingDirectory=/home/zhaopeng/graph/GridGraph -t' + ' ./bin/wcc -m ' + str(k-1) + filename
	p = subprocess.Popen(command, stdout = subprocess.PIPE, shell = True)
	pid = get_pid("./bin/wcc")
	print pid
	print "monitor starts"
	moniter = subprocess.Popen(["/home/zhaopeng/graph/GridGraph/tools/io_monitor.sh", pid, "wcc_1G_2_32G.result"])
	t = p.stdout.read()
	moniter.kill()
	print "monitor stops"
	f = open("wcc_coldpagecache_1G_2_32G_twitter.result", "a")
	f.write(t)
	print t


def clear_pagecache():
	print 'clearing page cache...'
	subprocess.Popen("sync", shell = True)
	command = "echo 3 > /proc/sys/vm/drop_caches"
	subprocess.Popen(command, shell = True)
	print 'page cahe cleared.'

size = 1
filename = "/home/zhaopeng/graph/data/twitter-2010.gg"
#filename = "/home/zhaopeng/graph/data/soc-LiveJournal1.txt"
for sz in range(0, 32):	
	clear_pagecache()
	run_cc(filename, size)
	size = size + 1
