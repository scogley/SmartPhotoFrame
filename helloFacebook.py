#!/usr/bin/env python
#using the Facebook SDK for Python
import facebook
import urllib
import sys
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
	# get the id of the photo and print it
	id = (p['id'])
	print(id)
	# a unique file name using id
	filepath = id  + '.jpg'
	# get the img source url and print it
	url = (p['source'])
	print(url)
	# using urllib
    f = open(filepath,'wb')
	f.write(urllib.urlopen('http://cdn.sstatic.net/stackoverflow/img/sprites.png?v=3c6263c3453b').read())
	f.close()


#TODO
# use the Linux framebuffer app to render the image
# sample: fbi -noverbose -m 640x480 -a -u -t 6 /home/pi/art/**/*