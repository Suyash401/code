from wit import Wit
access_token = "your access token"
client = Wit(access_token = access_token)

intents = {
	"learn" : {
	'python' : "You can learn python for free at codinground.com",
  'javascript' : "You can learn javascript at codinground.com",
  'java': "You can learn java at codinground.com"
	},
	"about" : {
	"your name" : "My name is John",
	"who created you" : "Suyash Agarwal"
	}
}
#name = input("Who are you?")
question = input("What do you want to learn?")
resp = client.message(question)

a = resp['entities']['intent'][0]['value']
if a in intents:
  try:
  	if resp['entities']['aboutus'][0]['value'] in intents['about']:
  		about = resp['entities']['about'][0]['value']
  		print(intents['about'][about])
  	if resp['entities']['language'][0]['value'] in intents['learn']:
  		language = resp['entities']['language'][0]['value']
  		print(intents['learn'][language])

  except:
    print("Error")
