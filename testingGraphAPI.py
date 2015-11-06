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
#posts = graph.get_connections(profile['id'], 'posts')
albums = graph.get_connections(profile['id'], 'albums')

for a in albums['data']:
	id = (a['id'])
	name = (a['name'])
	print(id + ' ' + name)