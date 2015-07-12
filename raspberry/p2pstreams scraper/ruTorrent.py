# -*- coding: utf-8 -*-

""" 
This plugin is 3rd party and not it is not part of the p2p-streams addon

Torrent-tv.ru (All categories)

"""
import urllib
import json
import sys,os
import re
import urllib
current_dir = os.path.dirname(os.path.realpath(__file__))
basename = os.path.basename(current_dir)
core_dir =  current_dir.replace(basename,'').replace('parsers','')
sys.path.append(core_dir)
#base_url = "http://api.torrent-tv.ru/t/BgF2xM3fd1KWxgEVO21eprkQPkZi55b0LosbJU8oeZVikr1wPAmjkV%2ByixKZYNGt"
base_url="http://api.torrent-tv.ru/t/BgF2xM3fd1KWxgEVO21eprkQPkZi55b0LosbJU8oeZVikr1wPAmjkV%2ByixKZYNGt"
def module_tree(name,url,iconimage,mode,parser,parserfunction):
	if not parserfunction: torrenttv()
	elif parserfunction == 'channels': torrenttv_play(name,url)
def torrenttv():
    dict_torrent = {}
    response = urllib.urlopen(base_url)
    source = response.read().decode('utf-8')
    previous=0
    source=source.replace("#EXTINF:-1,","")
    source=source.split('\n')
    source = source[1:]
    content=list()
    for index,i in enumerate(source):
        if index==0:
            continue
        elif index %2==0:
            if "sky" in i.lower() or "cbs" in i.lower():
                content.append((str(re.sub(ur'[^\x00-\x7F\x80-\xFF\u0100-\u017F\u0180-\u024F\u1E00-\u1EFF]', u'', source[index]) ),str(source[index+1])))
    print(content)
if __name__== '__main__':
    torrenttv()
