#!/usr/bin/env python
#using the Facebook SDK for Python
import facebook
import requests
# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
access_token = 'CAACEdEose0cBAHHipNcH1rkWkQapRU1cmnF4ZB3vvrJfZBV1JUgPihZCg1ZAgiYNBK86ztDyhjYwp5FTMM4jHyN3CHvGFi1vmmHlORhU9n6JOInz09yN2NAtAIc7I68gdBX1etzZBrFeHwJZCmmp8fzDh1hvPZC0Dnzz7GW92jhWnAAigYML0hsn3RnxXRoZCWCKINWZBsK2QJAZDZD'
photosedge = 'me/photos'
graph = facebook.GraphAPI(access_token, version='2.2')
print (graph.version)
photos = graph.get_object(photosedge)
