#!/usr/bin/env python
#using the Facebook SDK for Python
import facebook
#import requests
import sys
import webbrowser
# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
#access_token = ''
access_token = sys.argv

graph = facebook.GraphAPI(access_token, version='2.2')
print (graph.version)

# Return all connected photos for me. 
# By default, reading from the photos edge includes all photos a person has been tagged in.
photosedge = graph.get_connections(id='me', connection_name='photos')

#WORKS! 
#for each object in photosedge print the img source url
for p in photosedge['data']:
	#print(p['source'])
	url = (p['source'])
	print(url)
	id = (p['id'])
	print(id)	
	webbrowser.open(url, new=0, autoraise=True)	