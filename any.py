import sys
try:
	from bs4 import BeautifulSoup
	import requests
	import pyperclip
except ImportError:
    sys.exit("""One of the packages amongst bs4, requests, and pyperclip is not installed
    			Try running below commands:
    				pip install bs4
    				pip install requests
    				pip install pyperclip""")

domain = "https://www.pirateproxy.sh"
website = domain + "/search/"

query = input("Enter Search String : ")
website_constants = "/0/99/0"

url = website + query + website_constants
print (url)

try:
	page = requests.get(url)

except:
	print ("############## Connection Problem : Couldn't Connect #################")
	sys.exit()

if (page.status_code == 200):
	soup = BeautifulSoup(page.content, 'html.parser')
	table = soup.find_all('table')

	if(len(table) == 0):
		sys.exit("No Result Found")
	else:
		print ("Result(s) Found")
		print (soup.find_all('h2')[0].get_text())

		soup = table[0]
		print ("\n\n################# RESULTS #################\n\n")
		entry = soup.find_all('tr')
		perPageEntry = len(entry)

		for i in range(1, perPageEntry):
			print ("\n\n################# " + str(i) + " #################\n\n")
			presentWorkingEntry = entry[i].find_all('a')
			uploadInfo = entry[i].find_all('font')[0].get_text()
			seeders, leechers = entry[i].find_all('td')[2].get_text(), entry[i].find_all('td')[3].get_text()
			
			# To Show the Title of the Entry
			print (presentWorkingEntry[2].get_text())

			# To Show the Upload Information
			print (uploadInfo)

			# To Show the number of Seeders and Leechers
			print ("Seeders : " + seeders)
			print ("Leechers : " + leechers)

		entryNumber = input("Which Entry Would like to Download (Enter the entry number here) : ")
		link = domain + entry[int(entryNumber)].find_all('a')[2]['href']
		magnetLink = entry[int(entryNumber)].find_all('a')[3]['href']
		print ("\n\nLink : " + link)
		print ("\n\nMagnet Link : " + magnetLink)
		pyperclip.copy(magnetLink)
		print ("\n\nThe MagnetLink has been copied to your clipboard\n\n")