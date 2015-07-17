 # -*- coding: utf-8 -*-
import xbmc,urllib

all_modules = [ 'https://github.com/bazingasheldon/tv/blob/master/raspberry/addon.tar.gz?raw=true']

for parser in all_modules:
    xbmc.executebuiltin('XBMC.RunPlugin("plugin://plugin.video.p2p-streams/?mode=405&name=p2p&url=' + urllib.quote(parser) + '")')
    xbmc.sleep(1000)

xbmc.executebuiltin("Notification(%s,%s,%i,%s)" % ('P2P-Streams', "All parsers imported",1,''))