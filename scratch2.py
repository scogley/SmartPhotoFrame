import sys
# file to open is arg passed to script
filename = sys.argv
txt = open(filename, 'wb')

r = requests.get(url, stream =True)
print(r.status_code)	
with open(filepath, 'wb') as fd:
	for chunk in r.iter_content(chunk_size):
		fd.write(chunk)