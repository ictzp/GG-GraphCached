
ROOT_DIR= $(shell pwd)
#TARGETS= bin/loc bin/preprocess bin/bfs bin/wcc bin/pagerank bin/spmv bin/mis bin/radii
TARGETS= bin/loc bin/preprocess bin/wcc
CXX?= g++
CXXFLAGS?= -O3 -Wall -std=c++11 -g -fopenmp -I$(ROOT_DIR) -lmemcached
HEADERS= $(shell find . -name '*.hpp')

all: $(TARGETS)

bin/loc: tools/fp.cpp
	$(CXX) $(CXXFLAGS) -o $@ $< $(SYSLIBS)

bin/preprocess: tools/preprocess.cpp $(HEADERS)
	$(CXX) $(CXXFLAGS) -o $@ $< $(SYSLIBS)

#bin/bfs: examples/bfs.cpp $(HEADERS)
#	$(CXX) $(CXXFLAGS) -o $@ $< $(SYSLIBS)
#
bin/wcc: examples/wcc.cpp $(HEADERS)
	$(CXX) $(CXXFLAGS) -o $@ $< $(SYSLIBS)
#
#bin/pagerank: examples/pagerank.cpp $(HEADERS)
#	$(CXX) $(CXXFLAGS) -o $@ $< $(SYSLIBS)
#
#bin/spmv: examples/spmv.cpp $(HEADERS)
#	$(CXX) $(CXXFLAGS) -o $@ $< $(SYSLIBS)
#
#bin/mis: examples/mis.cpp $(HEADERS)
#	$(CXX) $(CXXFLAGS) -o $@ $< $(SYSLIBS)
#
#bin/radii: examples/radii.cpp $(HEADERS)
#	$(CXX) $(CXXFLAGS) -o $@ $< $(SYSLIBS)

clean:
	rm -rf $(TARGETS)

