import urllib,json

try:
        response = urllib.urlopen('http://streams.magazinmixt.ro/streams.json')
        source = response.read().decode('utf-8')
except:
        response = ""
if source:
    a = json.loads(source)  # dict with data
    ll=[]
    for i in a['groups']:
    	for j in i['channels']:
    		if j['protocol'] not in ll:
    			ll.append(j['protocol'])
	    		print j['protocol']