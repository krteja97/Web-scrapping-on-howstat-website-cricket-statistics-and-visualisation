import urllib.request, urllib.parse, urllib.error
import ssl
import oauth2 as oauth
import json
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np;


def myPlayerRuns(url):
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE

	page = urllib.request.urlopen(url, context = ctx);

	soup = BeautifulSoup(page, 'html.parser');

	table = soup.find('table', attrs = {'class' : 'TableLined'});

	rows1 = table.findAll("tr", attrs = {'bgcolor' : '#E3FBE9'});
	rows2 = table.findAll("tr", attrs = {'bgcolor' : '#FFFFFF'});

	count1 = 0;
	count2 = 0;
	runs = 0;
	matches = [];

	for row in rows1:
		cells = row.findAll("td");
		innings = cells[6].text.split()[0];
		if(innings != '-' ):
			count1 = count1 + 1;
			if(innings[-1] == '*'):
				innings = innings[:-1];
			runs = runs + int(innings);
			matches.append(int(innings));

	for row in rows2:
		cells = row.findAll("td");
		innings = cells[6].text.split()[0];
		if(innings != '-' ):
			count2 = count2 + 1;
			if(innings[-1] == '*'):
				innings = innings[:-1];
			runs = runs + int(innings);
			matches.append(int(innings));

	return matches;
