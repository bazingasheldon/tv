import sys, os,schedule
import urllib
import json

excluded = ['Radio', 'Moldova', 'Regionale', 'filmeonlinenoi.org', '990.ro - filme', '990.ro - seriale', 'Pentru copii',
            'filmoo.ro']
###################################
current_dir = os.path.dirname(os.path.realpath(__file__))
basename = os.path.basename(current_dir)
core_dir = current_dir.replace(basename, '').replace('parsers', '')
sys.path.append(core_dir)


base_url = 'http://super-pomoyka.us.to/trash/ttv-list/ttv.m3u'


container = list()
content = list()
containerOtherType = list()
channelSchedule=[]
schedule=schedule.loadSchedule("");

def module_tree(name, url, iconimage, mode, parser, parserfunction):
    list_all_items()


def list_all_items():
    try:
        response = urllib.urlopen('http://streams.magazinmixt.ro/streams.json')
        source = response.read().decode('utf-8')
    except:
        response = ""
    if source:
        ll=[]
        a = json.loads(source)  # dict with data
        for i in a['groups']:
            if i['name'] not in excluded:
                for j in i['channels']:
                    if  j['country'] not in ['cz', 'ru', 'pl', 'pr','rs', 'md', 'hu', 'tr'] and '\xd0' not in j['name'].encode('utf-8'):
                    #if j['status'] == 2 and j['country'] not in ['cz', 'ru', 'pl', 'pr','rs', 'md', 'hu', 'tr'] and '\xd0' not in j['name'].encode('utf-8'):
                        try:
                            ll.append((j['name'].encode('utf-8'),j['schedule']['ch_id'].encode('utf-8')))
                        except:pass
        print ll

list_all_items()