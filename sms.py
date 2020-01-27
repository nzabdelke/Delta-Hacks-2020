import requests
def sendSms(phone,message):
	resp = requests.post('https://textbelt.com/text', {
  	'phone': phone,
  	'message': message,
  	'key': '198a5e37ed6c9547ae327c2bef4078822d56b8e6IQVmLhgeVPjcdgI6JkA9H7Bnd',
  	})

#print(resp.json())
