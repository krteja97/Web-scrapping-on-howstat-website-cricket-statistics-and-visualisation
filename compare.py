import player_ids as pd;
import table as tb;

import urllib.request, urllib.parse, urllib.error
import ssl
import oauth2 as oauth
import json
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# # Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

base_url = "http://www.howstat.com/cricket/Statistics/Players/PlayerProgressBat.asp?PlayerID=";

all_players = [];

for x in pd.player_ids:
	url = base_url + str(x);
	print(url);
	matches = tb.myPlayerRuns(url);
	all_players.append(matches);

#print(all_players);
plt.hist([all_players[0], all_players[1]], bins = 20, label=['v.kohli', 'SPD smith']);
plt.legend(loc='upper right');
plt.show();