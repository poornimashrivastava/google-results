# google-results
This is a project focussed on web scraping and data parsing.

It works on agents : {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

It uses the url https://google.com/search?q= for starting the search. It then concatenates our query to it by https://google.com/search?q={query}

Next, we get the required URL, and then parse our google search results page for the needed information :
                                    1. title of the search result (Article page)
                                    2. description
                                    3. link of the page
                                    
 For the description of the page, we scrape the <span> class *aCOpRe* .
  
 *Video(youtube) description is not available*
