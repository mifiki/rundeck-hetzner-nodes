import requests
import json

# Token can be obtained from Hetzner Cloud console
# Access -> API Tokens -> Generate API token
token = 'YOUR TOKEN HERE'

url = 'https://api.hetzner.cloud/v1/servers'
headers = {'Authorization' : 'Bearer %s' % token}

r = requests.get(url, headers=headers)

data = json.loads(r.text)
servers_data = data["servers"]
servers_arr = dict()

for element in servers_data:
  name = element["name"]
  userhost = "root@" + name
  element["public_net"]["ipv4"]["hostname"] = userhost
  servers_arr.update({name : element["public_net"]["ipv4"]})

print json.dumps(servers_arr)
