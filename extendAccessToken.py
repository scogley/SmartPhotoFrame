import requests

access_token = 'temp_access_token'      # Obtained from https://developers.facebook.com/tools/accesstoken/
app_id = "app_id"                       # Obtained from https://developers.facebook.com/        
client_secret = "client_secret"         # Obtained from https://developers.facebook.com/

link = "https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=" + app_id +"&client_secret=" + client_secret + "&fb_exchange_token=" + access_token
s = requests.Session()
token = s.get(link).content
token = token.split("&")[0]                 # this strips out the expire info (now set set about 5184000 seconds, or 60 days)
token = token.strip("access_token=")        # Strips out access token
print token