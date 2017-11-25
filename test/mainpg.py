

# This is the HTTPS Requestor
import B365Requestor

# create an instance of the Requestor, with the headers
req = B365Requestor.B365Requestor()

# Call a method
result = req.getHeaders()

req.clearCookies()

response, cj = req.requestPage("https://www.bet365.com")

print("version: " , response.version, " - status: ", response.status , " reason: " , response.reason)
#Check out the cookies
print ("The cookies are: ")
for cookie in cj:
    print("Cookie name: ", cookie.name, " value: ", cookie.value)
    
print("Headers: ", response.getheaders())
print(response)

body = response.read()




