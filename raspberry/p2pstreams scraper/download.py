# -*- coding: utf-8 -*-

import urllib,json
excluded = ['Radio', 'Moldova', 'Regionale' ,'filmeonlinenoi.org','990.ro - filme','990.ro - seriale','Pentru copii','filmoo.ro']
def bazinga():
	ll=[]
	try:
	    response = urllib.urlopen('http://streams.magazinmixt.ro/streams.json')
	    source = response.read().decode('utf-8')
	except: 
	    response= ""
	if source:
	    a = json.loads(source)  #dict with data
	    for i in a['groups']:
	        if i['name'] not in excluded:
	            for j in i['channels']:
	            	try:
	            		print(j['thumbnail'])
	            	except:
	            		print("missing thumbnail ",j['name'])
	            	try:
	            		#duh(j['name'],j['thumbnail'])
	            		print(j['thumbnail'])
	            		ll.append(j['name']+"|"+j['thumbnail'].strip())
	            	except:pass

	with open('mm.txt','w')as file:
		for i in ll:
			try:
				file.write(str(i)+' \n')
			except:pass

def notInList():
	ll=[]
	try:
		response=urllib.urlopen('http://streams.magazinmixt.ro/streams.json')
		source=response.read().decode('utf-8')
	except:
		response,source="",""
	if source:
		print "ding"
		a=json.loads(source)
		for i in a['groups']:
			if i['name'] not in excluded:
				for j in i['channels']:
					if j['name'] not in icons:
						if '\xd0' not in j['name'].encode('utf-8') and j['country']=='ro' :
							ll.append(j['name'].encode('utf-8')) 

		sorted(ll)
		print(ll)

		with open('canale.txt','w') as myfile:
			for i in ll:
				myfile.write(i+"\n")


def duh(name,path,ext):
	testfile = urllib.URLopener()
	try:
		if not "1torrent.tv" in path:
			testfile.retrieve(path, "thumb/"+name+ext)
	except:
		print("fuck")

def process():
	with open('mm.txt','r')as myfile:
		for i in myfile.readlines():
			i=i.split("|")
			print("i: ",i)
			#print(i[1][i[1].rfind("."):])
			duh(i[0],i[1].strip()[:len(i[1])-2],i[1][i[1].rfind("."):len(i[1])-2])
import os
icons=['Acasa', 'Acasa Gold', 'Al Jazeera', 'Animal Planet', 'Animal Planet Hd', 'Antena 1', 'Antena Stars', 'Antena3', 'Axn', 'Axn Black', 'Axn Spin', 'Axn White', 'B1', 'Bbc News', 'Bnt World', 'C Music', 'Canal Savoir', 'Dance Tv', 'Digi 24', 'Digi Film', 'Digisport 1', 'Discovery Channel', 'Discovery Id', 'Diva Universal', 'Dolcesport 1', 'Dolcesport 2', 'Etno Tv', 'Euforia', 'Euronews', 'Filmcafe', 'France 24', 'Hbo', 'Hbo Comedy', 'History Channel', 'Inedit Tv', 'Kanal D', 'Kiss Tv', 'Mtv', 'Nat Geo Wild', 'National Geographic', 'National Tv', 'Noroc Tv', 'Paramount', 'Party Tv', 'Prima Tv', 'Pro Cinema', 'Protv', 'Pvtv', 'Realitatea Tv', 'Retro Music Tv', 'Romania Tv', 'Rusia 1', 'Russia Today', 'Sony Sci-fi', 'Tcm', 'Tlc', 'Travel Mix', 'Tvh 2.0', 'Tvr 1', 'Tvr 2', 'Tvr News', 'Utv', 'Vh1', 'Viasat Explorer', 'Viasat History', 'Viasat Nature', 'Virgin 1', 'Vox Music']

def process2():
	ll={}
	for i in os.listdir("thumb/"):
		print i[:i.rfind(".")]
		ll[i[:i.rfind(".")]]="thumb/"+i
	print "##################"
	print sorted(ll.keys())
#bazinga()
#process2()
notInList()