from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def googleResults(query) :
    query = query.replace(' ', '+')

    try :
        url = f"https://google.com/search?q={query}"

        getURL = requests.get(url, headers=headers)
        if getURL.status_code == 200 :
            print(getURL.status_code)
            soup = BeautifulSoup(getURL.content, "html.parser")
            # print(soup.prettify())

    except :
        print("Couldn't establish network!")

    divG = soup.find_all('div', class_='g')
    for divg in divG :
        if divg :
            a = divg.find_all('a', href=True)
            if a[0]['href'].startswith("http") :
                h3 = divg.find_all('h3') 
                if h3 :
                    print(h3[0].getText(), "------at------", a[0]['href'])
                desc = divg.find_all('span', class_='aCOpRe')
                if desc :
                    print("Description :", desc[0].getText())
                    print("------------------------------------------------------")
            
            # print(len(links)) --------->maybe>1
            # if len(links) != 0 :
            #     atag = links[0]
            #     # print(atag)
            #     hrefval = atag['href']
            #     if hrefval is not None and atag.text is not None:
            #         print(hrefval)

            # if siteLinks :
            #     if siteLinks['href'] :
            #         if len(siteLinks['href']) > 1 :
            #             print(siteLinks['href'])
            


        

googleResults(str(input("Query : ")))
