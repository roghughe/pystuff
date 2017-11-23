# A few bits of map code

# This is a statically defined map
smap = {'key1':'value1',"key2" : True, 'key3' : 345}

print("Map1: ", smap)

import data.coupon

line1 = "PA;IT=n3r_p_1480191075;ID=1480191075;FI=68935653;EW=1;NA=Best Of Tess;OD=6/4;JY=Timothy Thornton;IG=20171122xdd215507.png;OR=0;ST=1;PN=7;|"

results = data.coupon.generate(line1)

# put the result into a map

# declare an empty map
cmap = {}

for pair in results:
    cmap[pair[0]] = pair[1]
    
print("Map2: ", cmap)

print("Keys are: ", cmap.keys())

print("Values are: ", cmap.values())
