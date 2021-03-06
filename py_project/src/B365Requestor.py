'''
Demostrate how to do a sub-class in Python. 
The B365 Requestor extends Requestor class.
'''
import Requestor
from http.cookiejar import Cookie


class B365Requestor(Requestor.Requestor):
           
    defaultHeaders={ 
        'Accept' : 'text/html',
        'Accept-Language' : 'en-US,en;q=0.8',
        'Cache-Control' : 'no-cache',
        'Connection' :'keep-alive',
        'Host' : 'mobile.bet365.com',
        'Pragma' : 'no-cache',
        'Referer' : 'https://mobile.bet365.com/',
        'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46/563211 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
        }
   
    #defaultCookies = 'session=processform=0; pstk=B2F39E7B866A4F13A1207FC98790BD10000003; aps03=lng=1&tzi=1&ct=197&cst=0&cg=0&oty=1' 
 
    def __init__(self, pstk='B2F39E7B866A4F13A1207FC98790BD1000000'):
        print("This is the B365 constructor")
        super().__init__(self.defaultHeaders)
        
        # some 'constants' to use in the creation of the cookies
        expiry = '1370002304'
        cookie_host = '.bet365.com'
        root = '/'
        port = '80'
        
        # Cookie(version, name, value, port, port_specified, domain,
        # domain_specified, domain_initial_dot, path, path_specified,
        # secure, expires, discard, comment, comment_url, rest, rfc2109=False)
        c = Cookie(0, 'session', 'processform=0', port, True, cookie_host, 
              True, False, root, True, False, expiry, False, 'TestCookie', None, None, False)
        super().addCookie(c)
 
        c = Cookie(0, 'pstk', pstk, port, True, cookie_host, 
              True, False, root, True, False, expiry, False, 'TestCookie', None, None, False)
        super().addCookie(c)
    
        