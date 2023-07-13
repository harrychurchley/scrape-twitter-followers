from twitter_scrape_followers import *
import time

true=True;false=False
list_of_cookies=[
{
    "domain": ".twitter.com",
    "expirationDate": x,
    "hostOnly": x,
    "httpOnly": x,
    "name": "x",
    "path": "/",
    "sameSite": "x",
    "secure": x,
    "session": x,
    "storeId": "x",
    "value": "1x",
    "id": x
}]

#please replace the above sample cookies with your cookies
twitter.login_cookie(cookies=list_of_cookies)
twitter.open("https://twitter.com/x/followers")
time.sleep(2)
response=twitter.get_followers()
data=response['body']

print(data)

