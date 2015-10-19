#!/usr/bin/env python
#using the Facebook SDK for Python
import facebook
import requests
# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
access_token = 'CAACEdEose0cBAMvUwZCd7qFZCWecv4yJTogbGqrlZBvDahpMPAijDBCQkSUzqrDUcxeA2KkClsvVWPTSZAytwocFVmncbpK2cUYp1g4LTilJvJWLXTYjavnVxXeZA4zzEcmX5H6jv23KQtZC40moStuEmD1WZCcULm10nJ425NiAFGuWAmZA2PtrhXFQ40MG6t5gneD9zRD3mwZDZD'

graph = facebook.GraphAPI(access_token, version='2.2')
print (graph.version)

#this works!
photoId = '10152852496471951'
photo = graph.get_object(id=photoId)

# this seems to work but needs more investigation. Should return all photos I am tagged in
#photosedge = 'me/photos'
#photos = graph.get_object(photosedge)