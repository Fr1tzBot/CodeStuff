from os import system

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found")
    install = raw_input("Install it now?")
    if install == "yes":
	system("pip3 install beautifulsoup4")
	system("pip3 install google")
	from googlesearch import search
    else:
	exit()
# to search 
query = raw_input(">>")

for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
    print(j) 
