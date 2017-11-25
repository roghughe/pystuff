from  urllib.request import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import ssl

'''
Create a class that manages our HTTPS request. This allows us to sort out the headers, make the request and return a response
'''
from http import cookiejar

class Requestor(object):
       
    headers = {}
    cj = cookiejar.CookieJar()
    
    def __init__(self, headers={}):
        print("This is the constructor")
        self.headers = dict(headers)
        print("Using headers: ", self.headers)
       
    def getHeaders(self):
        return self.headers
        
    # Clear all the cookies
    def clearCookies(self):
        self.cj.clear()    
        
    # Add a new cookie  
    #
    # Cookie(version, name, value, port, port_specified, domain,
    # domain_specified, domain_initial_dot, path, path_specified,
    # secure, expires, discard, comment, comment_url, rest, rfc2109=False)
    #
    # c = Cookie(None, 'asdf', None, '80', True, 'www.foo.bar', 
    #         True, False, '/', True, False, '1370002304', False, 'TestCookie', None, None, False)
    # cj.set_cookie(c)
      
    def addCookie(self,newCookie):
        self.cj.set_cookie(newCookie)
        
    
    def requestPage(self,address=""):        
        
        req = Request(address,None, self.headers)
        #Create a CookieJar object to hold the cookies
        #Create an opener to open pages using the http protocol and to process cookies.
        opener = build_opener(HTTPCookieProcessor(self.cj), HTTPHandler())


        if address.startswith("https"):
            ssl._create_default_https_context = ssl._create_unverified_context

        #Query the website and return the html to the variable 'page'
        response = opener.open(req)
        return response, self.cj
        
        