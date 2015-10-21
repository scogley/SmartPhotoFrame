#!/usr/bin/env python
#using the Facebook SDK for Python
import facebook
import requests
# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
access_token = 'CAACEdEose0cBAD6uV4GZACAHc9fibbQdwpxNk0fBjWsVBa0frTNbARWCKW7KxZCa0yghJ44CSeerG8nrjWnDoK5e27W6vMjUPgL1AewEIwDu6MEuY9aiYmz0nvCQJaASZA4TmtRD9LCaCURqqVaihzr08MZBXTcRqnt9spCivpUbW2uwwwcRkCWuCr2haIpkyAAedvZCmrgZDZD'

graph = facebook.GraphAPI(access_token, version='2.2')
print (graph.version)

# Return all connected photos for me 
photosedge = graph.get_connections(id='me', connection_name='photos')

#WORKS! 
#for each object in photosedge print the id
for p in photosedge['data']:
	print(p['source'])









#WORKS!
#photoId = '10152852496471951'
#photo = graph.get_object(id=photoId)

#posts = graph.get_connections(id='me', connection_name='posts')

#WORKS!
#print(photosedge['data'])
#print(photosedge['data'],['id'])
#TODO: use api explorer on me/photos
#for loop each object in data and return the source property to get the url to the photo!

#works:
# Graph API Photo Node: 
# https://developers.facebook.com/docs/graph-api/reference/photo

#print(photo['id'])
#print(photo['link'])
#print(photo['from'])	
#print(photo['created_time'])


#works:
#for photo in photos:
#	print(photo, len(photo))

#works:
#for photo in photos:
#	print(photo[0])

# this seems to work but needs more investigation. Should return all photos I am tagged in
#photosedge = 'me/photos'
#photos = graph.get_object(photosedge)

# Get all of the authenticated user's friends
#friends = graph.get_connections(id='me', connection_name='friends')
# Get all the comments from a post
#comments = graph.get_connections(id='post_id', connection_name='comments')