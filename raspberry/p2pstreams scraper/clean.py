defaultChannels=[('Acasa', '10004'), ('Acasa Gold', '10253'), ('Axn', '10033'), ('Axn Black', '10072'), ('Axn Spin', '10298'), ('Axn White', '10073'), ('Digi Film', '10227'), ('Diva Universal', '10027'), ('Filmcafe', '10051'), ('Hbo', '10003'), ('Hbo Comedy', '10121'), ('Paramount', '10349'), ('Pro Cinema', '10036'), ('Pro Cinema', '10036'), ('Tcm', '10054'), ('Tv1000', '10060'), ('Animal Planet Hd', '10021'), ('Discovery Channel', '10020'), ('Discovery Id', '10189'), ('Discovery Science', '10044'), ('Discovery Science', '10044'), ('Discovery World', '10147'), ('Discovery World', '10147'), ('History Channel', '10168'), ('History Channel', '10168'), ('Investigation Discovery Europe', '10189'), ('Nat Geo Wild', '10136'), ('Nat Geo Wild', '10136'), ('National Geographic', '10024'), ('Pvtv', '10292'), ('Viasat Explorer', '10039'), ('Viasat Explorer', '10039'), ('Viasat History', '10040'), ('Viasat History', '10040'), ('Viasat Nature', '10207'), ('Viasat Nature East', '10207'), ('Digisport 1', '10198'), ('Digisport 1', '10198'), ('Digisport 2', '10199'), ('Eurosport Hd', '10028'), ('Kiss Tv', '10008'), ('Antena 1', '10017'), ('Antena 1', '10017'), ('Kanal D', '10097'), ('National Tv', '10031'), ('National Tv', '10031'), ('Prima Tv', '10005'), ('Protv', '10007'), ('Protv', '10007'), ('Tvh 2.0', '10029'), ('Tvh 2.0', '10029'), ('Tvh 2.0', '10029'), ('Tvr 1', '10001'), ('Tvr 1', '10001'), ('Tvr 1', '10001'), ('Tvr 2', '10002'), ('Antena Stars', '10119'), ('Euforia', '10063'), ('Tlc', '10224'), ('Travel Mix', '10231'), ('Antena3', '10055'), ('Antena3', '10055'), ('B1', '10022'), ('B1', '10022'), ('B1', '10022'), ('Digi 24', '10282'), ('Digi 24', '10282'), ('Euronews', '10113'), ('Realitatea Tv', '10019'), ('Realitatea Tv', '10019'), ('Romania Tv', '10245'), ('Romania Tv', '10245'), ('Romania Tv', '10245')]
sorted(defaultChannels,key=lambda x:x[0])
ll=[]
print "\n\n\n\n"
for i in defaultChannels:
	c=False
	for j in ll:
		if i[1] == j[1]:
			c=True
	if not c:
		ll.append(i)

print len(ll)
print len(defaultChannels)

print ll