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

profile = graph.get_object('me')
# using graph api explorer: me/albums
albums = graph.get_connections(profile['id'], 'albums')

# lists the id and name of each album
for a in albums['data']:
	id = (a['id'])
	name = (a['name'])
	print(id + ' ' + name)	

# Using the id of iOS Photos to get the album object and return photos field
# using graph api explorer: 4731781457001?fields=photos
# works! prints the source img url for each image in the album
iosAlbum = graph.get_object(id='4731781457001?fields=photos')
photos = iosAlbum['photos']
data = (photos['data'])
for d in data:
	source = (d['source'])
	print(source) # this is the source url for the image!