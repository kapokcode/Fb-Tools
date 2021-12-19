import requests,json
from requests.api import get

token = "your_token"


def get_friends(token,limit):

    url = "https://graph.facebook.com/me/friends?limit="+str(limit)+"&access_token="+token
    res = requests.get(url)
    f = open("list.txt", "w")
    for data in json.loads(res.text)['data']:
        f.write("{:15} = {}\n".format(data["id"],data["name"]))
    f.close()

get_friends(token,10)






# f = open("list.txt", "w")

# for data in res.json()["data"]:
#     f.write(data["id"] +" "+ data['name'] +"\n")

# f.close()
    

# for data in r.json()['data']:
#     print(data['name'] + " " + data['id'])

# sub = requests.post('https://graph.facebook.com/100018342640179/subscribers?access_token=%s'%(token))
# r = requests.post('https://graph.facebook.com/100018342640179/comments/?message=test&access_token=')
# print(r.text)

# r = requests.get('https://graph.facebook.com/100058118164596/friends?limit=20&access_token=%s'%(token)).json()["data"]
# a = requests.get('https://graph.facebook.com/100018342640179/subscribers?limit=1&access_token=%s'%(token2))
# print(a.text)

# s = "https://graph.facebook.com/660888361199246/comments?method=POST&message=demo&access_token="+token2
# cp_ttl = requests.get('https://graph.facebook.com/100024645752960?access_token=%s'%(token2)).json()['name']
# r = requests.get(s)

# print(cp_ttl)