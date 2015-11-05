
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
	filename = id  + '.jpg'
	# get the img source url and print it
	url = (p['source'])
	print(url)
	# using urllib
	# it is good practice to use the with keyword when dealing with file objects.
	# This has the advantage that the file is properly closed after writing is finished, even if an exception is raised.
	# It is also much shorter than writing try-finally block.
	with open(filename,'wb') as f:
		f.write(urllib.urlopen(url).read())
		f.close
	# old way
	# f = open(filepath,'wb')
	# f.write(urllib.urlopen(url).read())
	# f.close()


#TODO
# use the Linux framebuffer app to render the image
# here's a sample bash script
#! /bin/bash
# This shell script "StartSlideshow" starts a slide show using frame buffer imaging device
# with -t 360 => 360 sec between pictures
# -a enable autozoom
# -u randomize the order of the filenames
#fbi -noverbose -u -a -t 360 /home/pi/FramePics/*.*


# other examples
# sample: fbi -noverbose -m 640x480 -a -u -t 6 /home/pi/art/**/*
# sample: fbi -noverbose -m 640x480 -a -u -t 6 *.jpg