#import the library used to query a website
import urllib.request
import ssl

#specify the url
#address = "https://mobile.bet365.com/"
address = "https://mobile.bet365.com/V6/home/HomePage.aspx?zone=1&isocode=GB&tzi=1&lng=1&dt=n&_=1511214746648"

# These are standard bet365 headers
headers={ 
'Accept' : 'text/html',
'Accept-Language' : 'en-US,en;q=0.8',
'Cache-Control' : 'no-cache',
'Connection' :' keep-alive',
'Cookie' : 'session=processform=0; pstk=B2F39E7B866A4F13A1207FC98790BD10000003; aps03=lng=1&tzi=1&ct=197&cst=0&cg=0&oty=1',
'Host' : 'mobile.bet365.com',
'Pragma' : 'no-cache',
'Referer' : 'https://mobile.bet365.com/',
'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
}

print("Using URL: ", address)
print("Using Headers: ",headers)
print("Creating request")

req = urllib.request.Request(address,None, headers)

#gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
#context = ssl._create_unverified_context()
ssl._create_default_https_context = ssl._create_unverified_context

#Query the website and return the html to the variable 'page'
response = urllib.request.urlopen(req)
page = response.read()

print("NEXT ----------------->")

print("Got the page - about to parse")
#import the Beautiful soup functions to parse the data returned from the website from bs4 import BeautifulSoup

from bs4 import BeautifulSoup

print("BeautifulSoup imported")

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page,"html.parser")

print("Soup type is: ", type(soup))

print("Going to prettify...")

#print (soup.prettify())

coupons = soup.find_all("div", class_="hp-PromotedCouponsContainer")

for coupon in coupons:
	dt = coupon.script.get_text()
	dt1 = dt.replace(";",";\n")
	print(dt1)
	print("Next  -------->")

print("---------------------> End")


