# -*- coding: utf-8 -*-
__author__ = 'dilo00o'

import sys, os
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


def module_tree(name, url, iconimage, mode, parser, parserfunction):
    list_all_items()


container = list()
content = list()
containerOtherType = list()


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
                    if j['status'] == 2:
                        if j['protocol'] == 'sop' and j['country'] not in ['cz', 'ru', 'pl', 'rs', 'md', 'hu', 'tr']:
                            try:
                                container.append(['[COLOR red]' + j['name'] + ' [/COLOR]', j['address'], 2, j['thumbnail'], 1, False])
                            except KeyError:
                                container.append(['[COLOR red]' + j['name'] + ' [/COLOR]', j['address'], 2,
                                                  "http://screenshots.en.sftcdn.net/blog/en/2008/10/sopcast-logo.png",
                                                  1, False])
                        elif j['protocol'] == 'acestream':
                            try:
                                container.append(
                                    ['[COLOR orange]' + j['name'] + ' [/COLOR]', j['address'], 1, j['thumbnail'], 1,
                                     False])
                            except KeyError:
                                container.append(['[COLOR orange]' + j['name'] + ' [/COLOR]', j['address'], 1,
                                                  "http://screenshots.en.sftcdn.net/blog/en/2008/10/sopcast-logo.png",
                                                  1, False])
                        else:

                            try:
                                if j['protocol'] == 'http':
                                    containerOtherType.append(['[COLOR blueviolet]'+j['name']+'[/COLOR]', j['address'], j['thumbnail']])    
                                else:
                                    containerOtherType.append(['[COLOR blueviolet]'+j['name']+'[/COLOR]', j['address'], j['thumbnail']])
                            except KeyError:
                                    if j['protocol'] == 'http':
                                        containerOtherType.append(['[COLOR blueviolet]'+j['name']+'[/COLOR]', j['address'],
                                                           'http://anthrobotic.com/wp-content/uploads/2015/01/ANTHROBOTIC-VIDEO-ICON-e1420760465461.png'])
                                    else:
                                        containerOtherType.append(['[COLOR blueviolet]'+j['name']+'[/COLOR]', j['address'],
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
            try:
                addDir(i[0], i[1], i[2], i[3], i[4], i[5])
            except:
                continue
        delimiter2()
        torrent_tv()
        delimiter()
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
    li = xbmcgui.ListItem('>>>  ' + item[0], iconImage=item[2])
    xbmcplugin.addDirectoryItem(int(sys.argv[1]), url=url, listitem=li)


def torrenttv2():
    lst = {'Sky Sports 5 ': 'acestream://e72bb7060e8e4780e65ed45e81bf09bf352f496b',
           'BT Sport 1 ': 'acestream://21cdf320596fdd8a42dbd1ec2c6bfa7af2cea654',
           'BBC Two ': 'acestream://7c4d5ec7f9dcfb7c8d6bcc8bd942fae1971d20e4',
           'beIN Sports 11HD English ': 'acestream://1e821480f7d6c641d888e8a9f56078293ece83fa',
           'Sky Sports 3 HD ': 'acestream://b9ad84e9103cbaa6b81f3c1c791c40d1d1cb88e7',
           'BBC World News': 'acestream://9c498628fca36184d19d9802f66a3b4a4c1e7cd6',
           'Sky Sports 1 ': 'acestream://e6aaeb0c93c291a4cfe2c04d05c6b1e906f54955',
           'beIN Sports 12HD English ': 'acestream://31dd6c07342831e3d304e6ea811f3e91e8344fc7',
           'Sky Sports F1 ': 'acestream://2dff503259045e4d119e6e972a3db8521c47198a',
           'BT Sport 2': 'acestream://3c698092322e91fb20e9d716ff11bd7f70dc079d',
           'Sky Sports 2 ': 'acestream://97518ab8451a5c9e8da2b92245ac0ea6622a519c',
           'BBC One ': 'acestream://304528e8bd201ae6eec3bb321ab3247f3f09366f',
           'Sky Sports 3 ': 'acestream://7f480a00ac478b65fb75cfdde76ef38ee151b887'}
    for i in sorted(lst.keys()):
        addDir(i, lst[i], 1, 'http://minionslovebananas.com/images/check-in-minion.jpg', 1, False)


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
            addDir('[COLOR orange]'+name+'[/COLOR]', stream_link, 1, current_dir + "thumb/acestream.jpg", 1, False)
