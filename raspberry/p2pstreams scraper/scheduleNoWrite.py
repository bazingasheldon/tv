import os, os.path, re
# from glob import addon_log, Downloader, message, addon
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
from datetime import datetime, timedelta
from pytz import timezone
import time, sys, urllib
import pickle
nr_days = 3
current_dir = os.path.dirname(os.path.realpath(__file__))

now_utc = datetime.now(timezone('UTC'))
tz_ro = timezone('Europe/Bucharest')
dt_ro = tz_ro.normalize(now_utc.astimezone(tz_ro))
month_name_to_no = {"Ianuarie": "01",
                    "Februarie": "02",
                    "Martie": "03",
                    "Aprilie": "04",
                    "Mai": "05",
                    "Iunie": "06",
                    "Iulie": "07",
                    "August": "08",
                    "Septembrie": "09",
                    "Octombrie": "10",
                    "Noiembrie": "11",
                    "Decembrie": "12"}
start_date = dt_ro
#id_channel_port = 10168
def getScheduleForChannel(id_channel_port):
     dd=None
     url = "http://port.ro/pls/w/tv.channel?i_xday=" + str(nr_days) + "&i_date=%i-%02i-%02i&i_ch=%s" % (
         start_date.year, start_date.month, start_date.day+1, id_channel_port)
     print 'url: ' + url
     # temp = urllib.urlopen(url)
     schedule_txt=mechanize_browser(url)
     # schedule_txt =temp.read().decode('iso-8859-2')#.encode('utf-8')
     # with open("mm/"+id_channel_port+".txt",'w') as _file:
     #    _file.write(schedule_txt)
     #with open("gigi.html", 'r') as _file:
     #    schedule_txt = _file.read()
     #    _file.close()
     match = re.compile(r'class="begin_time">(?P<time>.*?)</p>').search(schedule_txt)

     if match:
             now_time = match.group('time')
     else:
             now_time = ""
         # addon_log(now_time)

     next_year = None

     match_days = re.compile(
        '<td style="vertical-align:top;text-align:center">\n*\s*<p class="date_box" style="margin-bottom:0px">\n*\s*<span>\n(?P<date>.*?)\n*\s*</span><br/>(?P<content>.*?)\n*\s*</table>\n*\s*</td>',
        re.DOTALL).findall(schedule_txt)
     
     if match_days:
        i = 1
        prev_event_day = None
        prev_event_month = None
        for date, content in match_days:
            date_obj = re.match('.*? \((.*) (.*)\)', date)

            event_day = date_obj.group(1).zfill(2)
            event_month = month_name_to_no[date_obj.group(2)]
            event_year = dt_ro.year

            if (event_day == '01') and (event_month == '01') and (((i > 1) and (i < nr_days)) or (i > nr_days + 1)):
                next_year = event_year + 1
            elif i == (nr_days + 1):
                next_year = None

            if next_year != None:
                event_year = next_year

            # addon_log(event_day + " " + event_month)

            if content:
                match_events_re = re.compile(
                    'btxt\" style=\"width:40px;margin:0px;padding:0px\">(?P<event_time>.*?)<.*?btxt\">(?P<event_title>.*?)</(?P<event_details>.*?)</td></tr>',
                    re.DOTALL)
                match_events = match_events_re.findall(content)

            prev_event_hour = None
            if match_events:
                dd={}
                for event_time, event_title, event_details in match_events:
                    if event_time == '':
                        event_time = now_time

                    event_hour = event_time.split(":")[0].zfill(2)
                    event_minutes = event_time.split(":")[1]

                    if (event_hour < prev_event_hour):  # what is after midnight is moved to the next day
                        next_day = datetime(int(event_year), int(event_month), int(event_day)) + timedelta(days=1)
                        # addon_log(next_day)
                        prev_event_day = event_day
                        prev_event_month = event_month
                        event_day = next_day.strftime('%d')
                        event_month = next_day.strftime('%m')


                    # addon_log(event_day+" "+event_month+" "+str(prev_event_day)+" "+str(prev_event_month))
                    if (event_day == '01') and (event_month == '01') and (prev_event_day == '31') and (
                        prev_event_month == '12') and (event_year == dt_ro.year):
                        event_year += 1
                        prev_event_day = None
                        prev_event_month = None

                    event_timestamp = time.mktime(time.strptime(
                        event_day + "-" + event_month + "-" + str(event_year) + " " + event_hour + ":" + event_minutes,
                        "%d-%m-%Y %H:%M"))

                    # addon_log(event_time)
                    # addon_log(event_day+" "+event_month+" "+str(event_year)+" "+event_hour+":"+event_minutes + " " + event_title)
                    # addon_log(event_time + "  " + str(event_timestamp) + " " + event_title)

                    dd[event_timestamp]=event_title
                    prev_event_hour = event_hour

            prev_event_day = event_day
            prev_event_month = event_month
            i += 1
     return dd

def getFullSchedule(channelListId):
     ''' channelListId[x][1] =  id_channel_port
     channelListId[x][0] =  channel name eg protv
     '''
     schedule={}
     schedule['date']=0
     for i in channelListId:
          m=getScheduleForChannel(i[1])
          schedule[i[0]]=getScheduleForChannel(i[1])
     try: 
          dumpSchedule(schedule)
     except:pass
     print schedule
     return schedule

def normalize(dt_ro):
     print time.mktime(time.strptime(dt_ro.strftime('%d-%m-%Y %H:%M'),"%d-%m-%Y %H:%M"))


def nowTime():
     now_utc = datetime.now(timezone('UTC'))
     tz_ro = timezone('Europe/Bucharest')
     dt_ro = tz_ro.normalize(now_utc.astimezone(tz_ro))
     return time.mktime(time.strptime(dt_ro.strftime('%d-%m-%Y %H:%M'),"%d-%m-%Y %H:%M"))

def dumpSchedule(container):
     try:
          pickle.dump(container,open(current_dir+"/schd.pk",'wb'))
     except:
          pass

def loadSchedule(channelListId):
     try:

          dd= pickle.load(open(current_dir+"/schd.pk","rb"))
          if not type(dd) is dict:
            raise Exception ('something is really fucked') 
          print "loaded"
          return dd
     except Exception,e:
          print "LOAD ERROR**************** "+e 
          container=getFullSchedule(channelListId)
          dumpSchedule(container)
          return container
     finally:
          return getFullSchedule(channelListId)

def getEventAtTime(dd):
     _time_=nowTime()
     print "asking for schedule for "+ str(dd)
     now=''
     for i in sorted(dd.keys()):
          if _time_>=i:
               now=i
          else:break
     try:
        print "giving: "+ dd[now]
        return dd[now]
     except:
        return 'Schedule unavailable'

# defaultChannels=[('Acasa', '10004'), ('Acasa Gold', '10253'), ('Axn', '10033'), ('Axn Black', '10072'), ('Axn Spin', '10298'), ('Axn White', '10073'), ('Digi Film', '10227'), ('Diva Universal', '10027'), ('Filmcafe', '10051'), ('Hbo', '10003'), ('Hbo Comedy', '10121'), ('Paramount', '10349'), ('Pro Cinema', '10036'), ('Tcm', '10054'), ('Tv1000', '10060'), ('Animal Planet Hd', '10021'), ('Discovery Channel', '10020'), ('Discovery Id', '10189'), ('Discovery Science', '10044'), ('Discovery World', '10147'), ('History Channel', '10168'), ('Nat Geo Wild', '10136'), ('National Geographic', '10024'), ('Pvtv', '10292'), ('Viasat Explorer', '10039'), ('Viasat History', '10040'), ('Viasat Nature', '10207'), ('Digisport 1', '10198'), ('Digisport 2', '10199'), ('Eurosport Hd', '10028'), ('Kiss Tv', '10008'), ('Antena 1', '10017'), ('Kanal D', '10097'), ('National Tv', '10031'), ('Prima Tv', '10005'), ('Protv', '10007'), ('Tvh 2.0', '10029'), ('Tvr 1', '10001'), ('Tvr 2', '10002'), ('Antena Stars', '10119'), ('Euforia', '10063'), ('Tlc', '10224'), ('Travel Mix', '10231'), ('Antena3', '10055'), ('B1', '10022'), ('Digi 24', '10282'), ('Euronews', '10113'), ('Realitatea Tv', '10019'), ('Romania Tv', '10245')]

# ll=[]

# for i in defaultChannels:
#     if not i in ll:
#         ll.append(i)
# print len(defaultChannels)
# print len(ll)






# print getFullSchedule(defaultChannels)