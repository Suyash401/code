import requests
while True:
	hashtag = input("Enter a topic\n")
	path = "https://www.instagram.com/web/search/topsearch/?context=hashtag&query="
	url = path+hashtag
	print(url)
	r = requests.get(url)      
	data = r.json()
	data2 = data['hashtags']
	for x in data2:
		print("Position:",x['position'],end=", Hashtag: ")
		print(x['hashtag']['name'],end=", ")
		print("Total Posts: ",x['hashtag']['search_result_subtitle'])
	tryagain = input("Do you want to try again?")
	if tryagain.lower() == "n":
		break
      
#Since hashtags don't have likes, I assumed you mean whichever has the highest number of posts.(More posts == More likes)
