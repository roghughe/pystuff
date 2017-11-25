

# This is the HTTPS requestor
import requestor

# These are any headers we want that override the defaults
headers = {}

# create an instance of the requestor, with the headers
req = requestor.Requestor(headers)

# Call a method
result = req.getHeaders()

req.clearCookies()

response, cj = req.requestPage("https://www.bet365.com")

print("version: " , response.version, " - status: ", response.status , " reason: " , response.reason)
#Check out the cookies
print ("the cookies are: ")
for cookie in cj:
    print (cookie)
    
print("Headers: ", response.getheaders())
print(response)

body = response.read()



print("Response is: ",response)

from bs4 import BeautifulSoup

print("BeautifulSoup imported")

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(body,"html.parser")

print("Soup type is: ", type(soup))

print("Going to prettify...")

print (soup.prettify())
