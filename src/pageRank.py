"""
Created by David Goldstein on 3/11/2018
A script to:
	1) scrape urls with time limit
	2) generate page rank using networkx
	3) save to JSON in data directory
"""
# python utils
import time

# progress bar
from tqdm import tqdm

# networkx
import networkx as nx
from networkx.readwrite import json_graph


# on run
if __name__ == '__main__':
	# scrape links
	print "scraping links"
	# todo
	print "done \n"

	# indexing page rank
	print "applying page rank"
	print "done \n"

	# save graph
	print "saving graph"
	print "done\n"
