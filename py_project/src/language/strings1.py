# Okay, so lets figure out how to handle strings

line1 = "PA;IT=n3r_p_1480191075;ID=1480191075;FI=68935653;EW=1;NA=Best Of Tess;OD=6/4;JY=Timothy Thornton;IG=20171122xdd215507.png;OR=0;ST=1;PN=7;|"

print("split into a list based on the ';' character")

list1 = line1.split(";")

print("The length of the list: ",len(list1))

print("The list is: \n",list1)

print("Split the components of the list")

for item in list1:
    pair = item.split("=")
    if len(pair) > 1:
        print(pair[0], " = ", pair[1])
    else: 
        print(pair[0], " = null")
    

