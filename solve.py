import webbrowser
print("Hey my name's HELPER. I help people solve their doubts :)")
while True:
	question = input("Ask me your query!\n")
	url = "https://www.google.com.tr/search?q={}".format(question) 
	try:
		chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
		webbrowser.get(chrome_path).open(url)
	except:
		webbrowser.open(url)
	question2 = input("Do you want to ask another question? Y/N \n")
	if question2.lower() in ['no','nope','nah','n']:
		print("Bye")
		break

