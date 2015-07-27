# -*- coding: utf-8 -*-
__author__ = 'dilo00o'

import sys, os
#import scheduleModule as schedule
import scheduleNoWrite as schedule
import urllib
import json

excluded = ['Radio', 'Moldova', 'Regionale', 'filmeonlinenoi.org', '990.ro - filme', '990.ro - seriale', 'Pentru copii',
            'filmoo.ro']
###################################
current_dir = os.path.dirname(os.path.realpath(__file__))
basename = os.path.basename(current_dir)
core_dir = current_dir.replace(basename, '').replace('parsers', '')
sys.path.append(core_dir)
# noinspection PyUnresolvedReferences
from peertopeerutils.webutils import *
# noinspection PyUnresolvedReferences
from peertopeerutils.pluginxbmc import *
# noinspection PyUnresolvedReferences
from peertopeerutils.directoryhandle import *
# noinspection PyUnresolvedReferences
import acestream as ace
# noinspection PyUnresolvedReferences
import sopcast as sop

base_url = 'http://super-pomoyka.us.to/trash/ttv-list/ttv.m3u'
# defaultChannels=[('Acasa', '10004'), ('Acasa Gold', '10253'), ('Axn', '10033'), ('Axn Black', '10072'), ('Axn Spin', '10298'), ('Axn White', '10073'), ('Digi Film', '10227'), ('Diva Universal', '10027'), ('Filmcafe', '10051'), ('Hbo', '10003'), ('Hbo Comedy', '10121'), ('Paramount', '10349'), ('Pro Cinema', '10036'), ('Tcm', '10054'), ('Tv1000', '10060'), ('Animal Planet Hd', '10021'), ('Discovery Channel', '10020'), ('Discovery Id', '10189'), ('Discovery Science', '10044'), ('Discovery World', '10147'), ('History Channel', '10168'), ('Nat Geo Wild', '10136'), ('National Geographic', '10024'), ('Pvtv', '10292'), ('Viasat Explorer', '10039'), ('Viasat History', '10040'), ('Viasat Nature', '10207'), ('Digisport 1', '10198'), ('Digisport 2', '10199'), ('Eurosport Hd', '10028'), ('Kiss Tv', '10008'), ('Antena 1', '10017'), ('Kanal D', '10097'), ('National Tv', '10031'), ('Prima Tv', '10005'), ('Protv', '10007'), ('Tvh 2.0', '10029'), ('Tvr 1', '10001'), ('Tvr 2', '10002'), ('Antena Stars', '10119'), ('Euforia', '10063'), ('Tlc', '10224'), ('Travel Mix', '10231'), ('Antena3', '10055'), ('B1', '10022'), ('Digi 24', '10282'), ('Euronews', '10113'), ('Realitatea Tv', '10019'), ('Romania Tv', '10245')]
defaultChannels=[('Acasa', '10004'), ('Acasa Gold', '10253'), ('Axn', '10033')]


roStreams='http://streams.magazinmixt.ro/streams.json'

container = list()
content = list()
containerOtherType = list()
channelSchedule=[]
scheduleDb={}

def module_tree(name, url, iconimage, mode, parser, parserfunction):
    current_dir=os.path.dirname(os.path.realpath(__file__))
    scheduleDb={}
    defaultChannels=[('Acasa', '10004'), ('Acasa Gold', '10253'), ('Axn', '10033')]
    # defaultChannels=[('Acasa', '10004'), ('Acasa Gold', '10253'), ('Axn', '10033'), ('Axn Black', '10072'), ('Axn Spin', '10298'), ('Axn White', '10073'), ('Digi Film', '10227'), ('Diva Universal', '10027'), ('Filmcafe', '10051'), ('Hbo', '10003'), ('Hbo Comedy', '10121'), ('Paramount', '10349'), ('Pro Cinema', '10036'), ('Tcm', '10054'), ('Tv1000', '10060'), ('Animal Planet Hd', '10021'), ('Discovery Channel', '10020'), ('Discovery Id', '10189'), ('Discovery Science', '10044'), ('Discovery World', '10147'), ('History Channel', '10168'), ('Nat Geo Wild', '10136'), ('National Geographic', '10024'), ('Pvtv', '10292'), ('Viasat Explorer', '10039'), ('Viasat History', '10040'), ('Viasat Nature', '10207'), ('Digisport 1', '10198'), ('Digisport 2', '10199'), ('Eurosport Hd', '10028'), ('Kiss Tv', '10008'), ('Antena 1', '10017'), ('Kanal D', '10097'), ('National Tv', '10031'), ('Prima Tv', '10005'), ('Protv', '10007'), ('Tvh 2.0', '10029'), ('Tvr 1', '10001'), ('Tvr 2', '10002'), ('Antena Stars', '10119'), ('Euforia', '10063'), ('Tlc', '10224'), ('Travel Mix', '10231'), ('Antena3', '10055'), ('B1', '10022'), ('Digi 24', '10282'), ('Euronews', '10113'), ('Realitatea Tv', '10019'), ('Romania Tv', '10245')]
    print "current dir: "+current_dir
    try:
        print '+++++++++++++++++++++++++-----------------------------------------++++++++++++++++++++++++++++'
        scheduleDb=schedule.loadSchedule(defaultChannels)
        print '+++++++++++++++++++++++++Done load from file++++++++++++++++++++++++++++'
    except Exception,e:
        print '/////////////////////////////////////////////////////'
        print e
        print '/////////////////////////////////////////////////////'
        scheduleDb=schedule.getFullSchedule(defaultChannels)
    list_all_items()


def list_all_items():
    try:
        response = urllib.urlopen('http://streams.magazinmixt.ro/streams.json')
        source = response.read().decode('utf-8')
    except:
        response = ""
    if source:
        
        a = json.loads(source)  # dict with data
        for i in a['groups']:
            if i['name'] not in excluded:
                for j in i['channels']:
                    if j['status'] == 2 and j['country'] not in ['cz', 'ru', 'pl', 'pr','rs', 'md', 'hu', 'tr'] and '\xd0' not in j['name'].encode('utf-8'):
                        if j['protocol'] == 'sop' :
                            try:
                                container.append([str( j['name']) , j['address'], 2, j['thumbnail'], 1, False])
                            except :
                                container.append([ str( j['name']) , j['address'], 2,
                                                  "http://screenshots.en.sftcdn.net/blog/en/2008/10/sopcast-logo.png",
                                                  1, False])
                        elif j['protocol'] == 'acestream':
                            try:
                                container.append([str( j['name']), j['address'], 1, j['thumbnail'], 1, False])
                            except :
                                container.append([str( j['name']), j['address'], 1,
                                                  "http://screenshots.en.sftcdn.net/blog/en/2008/10/sopcast-logo.png",
                                                  2, False])
                        else:

                            try:
                                containerOtherType.append([str( j['name']), j['address'], j['thumbnail']])    
                            except :
                                containerOtherType.append([str( j['name']), j['address'],
                                                           'http://anthrobotic.com/wp-content/uploads/2015/01/ANTHROBOTIC-VIDEO-ICON-e1420760465461.png'])
        container.sort(key=lambda x: x[0])
        containerOtherType.sort(key=lambda x: x[0])
        delimiter3()
        xbmcplugin.addDirectoryItem(int(sys.argv[1]), url='http://82.76.249.75/digiedge2/tvpaprikahq/playlist.m3u8',
                                    listitem=xbmcgui.ListItem("Paprika test", iconImage=""))
        xbmcplugin.addDirectoryItem(int(sys.argv[1]), url='http://rtmp.infomaniak.ch/livecast/ladeux/chunklist.m3u8',
                                    listitem=xbmcgui.ListItem("La Deux test", iconImage=""))
        xbmcplugin.addDirectoryItem(int(sys.argv[1]), url='http://streaming-hub.com/tv/i/tf1_1@97468/master.m3u8',
                                    listitem=xbmcgui.ListItem("TF1 test", iconImage=""))
        xbmcplugin.addDirectoryItem(int(sys.argv[1]),
                                    url='http://stream01.yamgo.com/iPhone/HLS_TS/broadcast/strictly_belly_dancing-tablet.3gp/strictly_belly_dancing-tablet.3gp-mr647k.m3u8',
                                    listitem=xbmcgui.ListItem("Bellytest", iconImage=""))
        xbmcplugin.addDirectoryItem(int(sys.argv[1]), url='http://204.107.27.233/live/1729.high.stream/playlist.m3u8',
                                    listitem=xbmcgui.ListItem("Arte", iconImage=""))
        delimiter3()
        for i in container:
            print "*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"
            print schedule.getEventAtTime(scheduleDb['Acasa'])
            try:
                print '******************** '+scheduleDb[i[0]]
                addDir(i[0]+"  "+schedule.getEventAtTime(scheduleDb[i[0]]), i[1], i[2], i[3], i[4], i[5])
            except Exception,e:
                print "#####################11111#####################"
                print e
                print "#####################22222#####################"
                try: 
                    addDir(i[0], i[1], i[2], i[3], i[4], i[5])
                except:pass
        # delimiter2()
        # torrent_tv()
        # delimiter()
        for i in containerOtherType:
            try:
                appendDifferentStreams(i)
            except:
                continue


def delimiter():
    url = ''
    li = xbmcgui.ListItem('>>> Flash Based below <<<', iconImage="")
    xbmcplugin.addDirectoryItem(int(sys.argv[1]), url=url, listitem=li)


def delimiter2():
    url = ''
    li = xbmcgui.ListItem('>>> SuperMoyka <<<', iconImage="")
    xbmcplugin.addDirectoryItem(int(sys.argv[1]), url=url, listitem=li)


def delimiter3():
    url = ''
    li = xbmcgui.ListItem('>>> test <<<', iconImage="")
    xbmcplugin.addDirectoryItem(int(sys.argv[1]), url=url, listitem=li)


def appendDifferentStreams(item):
    url = item[1]
    schedule.getEventAtTime(scheduleDb[item[0]])
    try:
        li = xbmcgui.ListItem('>>>  ' + item[0]+"  "+schedule.getEventAtTime(scheduleDb[item[0]]), iconImage=item[2])
    except:        
        li = xbmcgui.ListItem('>>>  ' + item[0], iconImage=item[2])
    xbmcplugin.addDirectoryItem(int(sys.argv[1]), url=url, listitem=li)




def torrent_tv():
    try:
        source = mechanize_browser(base_url)
    except:
        print "Something iz really fucked up"
        source = "";
        xbmcgui.Dialog().ok(translate(40000), translate(40128))
    if source:
        match = re.compile("#EXTINF:-1,(.+?)\(Спорт\)\n(.*)").findall(source)
        for name, stream_link in match:
            clean = re.compile("\((.+?)\)").findall(name)
            for cat in clean:
                name = name.replace("(" + cat + ")", "")  # remove crappy russian characters
            addDir('[COLOR orange] '+name+' [/COLOR]', stream_link, 1, current_dir + "/thumb/acestream.jpg", 2, False)
