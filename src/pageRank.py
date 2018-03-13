"""
Created by David Goldstein on 3/11/2018
A script to:
	1) scrape urls with time limit
	2) generate page rank using networkx
	3) save to JSON in data directory
"""

# python utils
import time
import unittest
import sys
import argparse
import os
import datetime
import uuid

# progress bar
from tqdm import tqdm

# request / parsing utils
import httplib2
from bs4 import BeautifulSoup, SoupStrainer

# networkx
import networkx as nx
from networkx.readwrite import json_graph

######################
## Global Variables ##
######################

G=nx.DiGraph()

def scrape_data(link):
	"""
	scrapes relevant data from given link
	@param {string} link
	@return {dict} {
		url : link
		count : number of external links
		title : title of the page
		description : sample text
	}
	"""
	pass
	

def httplib(link):
	http = httplib2.Http()
	status, response = http.request(link)
	for link in BeautifulSoup(response, "html.parser", parse_only=SoupStrainer('a')):
	    if link.has_attr('href'):
	        print link['href']

def add_node_with_links(G, name, description, title, edges=[]):
	"""
	util for adding node and links to graph
	@param {nx.DiGraph}
	@param {String}
	@param {String}
	@param {list} edges associated with this node
	"""
	G.add_node(name, description=description, title=title, indexDate=datetime.datetime.now(), id=uuid.uuid4())


###########
## Tests ##
###########

class AddNodeTesting(unittest.TestCase):
    def test_G_was_initialized(self):
        self.assertIsNotNone(G)

    def test_adds_correct_node(self):
    	add_node_with_links(G, "test name", "test description", "test title")
    	self.assertEqual(G.number_of_nodes(), 1)
    	self.assertEqual(G.nodes()['test name']['description'], "test description")
    	self.assertEqual(G.nodes()['test name']['title'], "test title")
    	self.assertIsNotNone(G.nodes['test name']['indexDate'])
    	self.assertIsNotNone(G.nodes['test name']['id'])

def run_script():
	# scrape links
	print "scraping links"
	for i in range(1):
		httplib('http://www.nytimes.com')
		
	print "done \n"

	# indexing page rank
	print "applying page rank"
	print "done \n"

	# save graph
	print "saving graph"
	print "done\n"
	


# on run
if __name__ == '__main__':
	# parse args
	parser = argparse.ArgumentParser(description='Applies page rank to a webcrawl')
	parser.add_argument('--test',help='Run tests', action="store_true")
	args = parser.parse_args()

	print "Running Tests"

	suite = unittest.TestLoader().loadTestsFromTestCase(AddNodeTesting)
	testsSuccessful= unittest.TextTestRunner(verbosity=2).run(suite)

	# suite = unittest.TestLoader().loadTestsFromTestCase(AddNodeTesting)
	# testsSuccessful = unittest.TextTestRunner().run(suite)

	if testsSuccessful.wasSuccessful():
		# run_script()
		print
	else:
		print "Tests did not pass"

"""
progress bar example
pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    pbar.set_description("Processing %s" % char)
"""