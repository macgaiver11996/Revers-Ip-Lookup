import requests, socket 

website1 = input("Enter Your Target Site :")
website = website1.replace("https://",'').replace("http://",'').replace("/",'')


ip = socket.gethostbyname(website)
api = f"https://api.hackertarget.com/reverseiplookup/?q={ip}"


response = requests.get(api)

if response.status_code == 200:
  print ("ip")
else:
  print ("Request Faild")
