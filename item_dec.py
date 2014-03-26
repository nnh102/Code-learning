
import re
patt = re.compile("[^\t\r\n]+")
print "start"
n =1
for x in range(18, 31):
	print "process", "blood.present_receive.log.201312%01d" % x
	filename = "blood.present_receive.log.201312%01d" % x
	f = open(filename)
	item_dec = {}
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
	for p in item_dec:
		print p, ":", item_dec[p]

