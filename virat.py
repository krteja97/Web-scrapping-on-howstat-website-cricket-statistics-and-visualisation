import urllib.request, urllib.parse, urllib.error
import ssl
import oauth2 as oauth
import json
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = "http://www.howstat.com/cricket/Statistics/Players/PlayerProgressBat.asp?PlayerID=3600";

# # Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


page = urllib.request.urlopen(url, context = ctx);

soup = BeautifulSoup(page, 'html.parser');


innings = soup('td', attrs = {'class' : 'AsteriskSpace'});

#print(innings);

runs= 0 ;
matches = [];
for x in innings:
	#print(x.text.strip());
	if(x.text.strip() != "-"):
		runs = runs + int(x.text.strip());
		matches.append(int(x.text.strip()));
	if(x.text.strip()[-1] == '*'):
		runs = runs + int(x.text.strip()[:-1]);

print(runs);
print(matches);
plt.hist(matches);
plt.show();
# tags = soup('a');
# for tag in tags:
# 	print(tag.get('href', None));