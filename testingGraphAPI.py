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

for a in albums['data']:
	id = (a['id'])
	name = (a['name'])
	print(id + ' ' + name)	

# The above returns the id of each album. 
# Using the id of iOS Photos to get the album object and return photos field
# using graph api explorer: 4731781457001?fields=photos

# works!
iosAlbum = graph.get_object(id='4731781457001?fields=photos')
for i in iosAlbum['photos']:
	data = (i[0])
	id = (data[0])