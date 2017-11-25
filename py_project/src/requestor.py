from  urllib.request import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import ssl

'''
Create a class that manages our HTTPS request. This allows us to sort out the headers, make the request and return a response
'''
from http import cookiejar

class Requestor(object):
   
    defaultHeaders={ 
        'Accept' : 'text/html',
        'Accept-Language' : 'en-US,en;q=0.8',
        'Cache-Control' : 'no-cache',
        'Connection' :' keep-alive',
        'Cookie' : '',
        'Host' : 'mobile.bet365.com',
        'Pragma' : 'no-cache',
        'Referer' : 'https://mobile.bet365.com/',
        'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46/563211 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
        }
   
    defaultCookies = 'session=processform=0; pstk=B2F39E7B866A4F13A1207FC98790BD10000003; aps03=lng=1&tzi=1&ct=197&cst=0&cg=0&oty=1' 
    
    headers = {}
    cookies = ""
    
    def __init__(self, headers={}):
        print("This is the constructor")
        self.headers = dict(self.defaultHeaders)
        self.headers.update(headers)
        print("Using headers: ", self.headers)
       
    def getHeaders(self):
        return self.headers
        
    # Clear all the cookies
    def clearCookies(self):
        self.cookies = ""    
        
    # Add a new cookie in the format of a=bbb    
    def addCookie(self,newCookie=""):
        self.cookies += (newCookie + "; ")
        
    
    def requestPage(self,address="",useDefaultCookies=False):        
        # add the cookies to the headers
        if useDefaultCookies:
            self.headers['Cookie'] = self.defaultCokkies
        else:
            self.headers['Cookie'] = self.cookies
        
        req = Request(address,None, self.headers)
        #Create a CookieJar object to hold the cookies
        cj = cookiejar.CookieJar()
        #Create an opener to open pages using the http protocol and to process cookies.
        opener = build_opener(HTTPCookieProcessor(cj), HTTPHandler())


        if address.startswith("https"):
            ssl._create_default_https_context = ssl._create_unverified_context

        #Query the website and return the html to the variable 'page'
        response = opener.open(req)
        return response, cj
        
        