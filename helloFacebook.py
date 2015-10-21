#!/usr/bin/env python
#using the Facebook SDK for Python
import facebook
import requests
# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
access_token = 'CAACEdEose0cBAJkQt9lCKgXQ4VLcZBpZBHigYKaFcg2lIcRr3xLVwU1qgMYpGvfEPUFwx1dMLvJnTAPbX1201f4lizna6hF9hYtxn0ZBuejgLUeeb0dVj6C4dgDulrJK1CwhBpNCFQgrBBZB5vQT6IqOcoHZB3cO2wgMfXpORqidcxWX8afjZB0Cz2OfR9522w9t9kNsER7gZDZD'

graph = facebook.GraphAPI(access_token, version='2.2')
print (graph.version)

#this works!
photoId = '10152852496471951'
photo = graph.get_object(id=photoId)

# Return all connected photos for me 
photosedge = graph.get_connections(id='me', connection_name='photos')
posts = graph.get_connections(id='me', connection_name='posts')

#WORKS!
print(photosedge['data'])

#works:
# Graph API Photo Node: 
# https://developers.facebook.com/docs/graph-api/reference/photo
print(photo['id'])
print(photo['link'])
print(photo['from'])	
print(photo['created_time'])





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