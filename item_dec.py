import re
patt = re.compile("[^\t\r\n]+")
n =1
z = 1
def count_item(filename):
	for x in range(18, 31):
		print "process", "blood.present_receive.log.201312%01d" % x
		item_dec = {}
		filename = "blood.present_receive.log.201312%01d" % x	
		with open(filename, 'r') as f:
			for line in f:
				#n += 1
				#if n > 100:
				#	break
				a = patt.findall(line)
				for i in xrange(4, 8):
					a[i] = a[i][1:-1].split(",")
				for m in xrange(0, len(a[4])):
					if a[5][m] == "1" and a[4][m] == "1":
						if a[6][m] not in item_dec:
							item_dec[a[6][m]] = int(a[7][m])
						else:
							item_dec[a[6][m]] += int(a[7][m])
		yield item_dec
for i in count_item(z): 
	for p in i:
		print p, ":", i[p]