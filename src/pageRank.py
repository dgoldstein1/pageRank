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

def scrape_data(url):
	"""
	scrapes relevant data from given url
	@param {string} url
	@return {dict} {
		url : link
		links : list of external links
		title : title of the page
		description : sample text
	}
	"""
	http = httplib2.Http()
	try:
		status, response = http.request(url)
	except Exception as e:
		return None
	# get links
	links = []
	for link in BeautifulSoup(response, "html.parser", parse_only=SoupStrainer('a')):
	    if link.has_attr('href'):
	        links.append(link['href'])

	# get description
	soup = BeautifulSoup(response, "html.parser")
	description = soup.find('meta', attrs={'name':'og:description'}) or soup.find('meta', attrs={'property':'description'}) or soup.find('meta', attrs={'name':'description'})
	if description:
		description = description.get('content')

	# return dictionary
	return {
		"url" : url,
		"links" : links,
		"title" : BeautifulSoup(response, "html.parser"),
		"description" : description
	}

def add_node_with_links(G, name, description, title, neighbors=[]):
	"""
	util for adding node and links to graph
	@param {nx.DiGraph}
	@param {String}
	@param {String}
	@param {list} neighbors with edges to this node
	"""
	G.add_node(name, description=description, title=title, indexDate=datetime.datetime.now(), id=uuid.uuid4())
	[G.add_edge(name, node) for node in neighbors]

###########
## Tests ##
###########

class ScrapeTesting(unittest.TestCase):
	def test_scrapes_correct_values(self):
		response = scrape_data("https://www.nytimes.com/")
		self.assertIsNotNone(response)
		self.assertEqual(response['url'],"https://www.nytimes.com/")
		self.assertEqual(len(response['links']) > 0, True)
		self.assertEqual(response['description'], "The New York Times: Find breaking news, multimedia, reviews & opinion on Washington, business, sports, movies, travel, books, jobs, education, real estate, cars & more at nytimes.com.")

	def test_gracefully_handles_error(self):
		response = scrape_data("this is a bad url")
		self.assertIsNone(response)

class AddNodeTesting(unittest.TestCase):
	# tests for adding node to graph
    def test_G_was_initialized(self):
        self.assertIsNotNone(G)

    def test_adds_correct_node(self):
    	add_node_with_links(G, "test name", "test description", "test title")
    	self.assertEqual(G.nodes()['test name']['description'], "test description")
    	self.assertEqual(G.nodes()['test name']['title'], "test title")
    	self.assertIsNotNone(G.nodes['test name']['indexDate'])
    	self.assertIsNotNone(G.nodes['test name']['id'])

    def test_adds_correct_links(self):
    	add_node_with_links(G, "test name", "test description", "test title", ["node 1","node 2"])
    	self.assertEqual(G.number_of_edges(), 2)

    def tearDown(self):
    	G = nx.DiGraph()


def run_script():
	# scrape links
	print "scraping links"
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

	print "Running Tests \n"

	testsSuccessful = True
	testsSuccessful = unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(AddNodeTesting))
	testsSuccessful = testsSuccessful and unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(ScrapeTesting))

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