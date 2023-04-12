## this file contains the solutions to assignment 8


## (1) What is meant by stateless in REST?
## Ans: Stateless means that each API call is independent of other calls, the data or the result of any call is not stored
## in any fashion whatsoever, that is why we can say that the state of calls is not maintained, hence stateless.


## (2) 403, 503, 301 Status Codes?
## Ans: (i) 403 - It means that the user, no matter authorized or unauthorized don't have access to the resource (Forbidden)
## (ii) 503 - It indicates that there is a performance issue on the server. Most probably due to unhandling of the load (Service Unavailable)
## (iii) 301 - It indicates the requested resource is moved permanently to a new address. (Moved Permanently)


## (3) Making GET, POST, PUT and DELETE Requests using requests module to a public API

import requests
#GET request
URL = "https://api.github.com/users/%Username"
resp = requests.get(URL)
print(resp.json())

#POST request
api_url = "https://api.github.com/users/%Username"
resp = requests.post(api_url,json={"name" : "Abhiraj"})
print(resp.json())

#put request
resp = requests.patch(api_url , json={"hello": "Abhiraj"})
print(resp.json())

#Delete Request
resp = requests.delete(api_url)
print(resp.status_code)