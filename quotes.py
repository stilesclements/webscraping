from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import plotly.express as px



# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}





authors_dict={}
quote_len_list=[]
tags_dict={}
counter=0

for i in range(0,11):
    url=f'https://quotes.toscrape.com/page/{i+1}/'
    req = Request(url,headers=headers)
    webpage= urlopen(req).read()
    soup  = BeautifulSoup(webpage,'html.parser')
    for quote in soup.findAll("div", {"class":{"quote"}}):
        author=quote.find("small", {"itemprop":{"author"}})
        quote_text=quote.find('span',{"class":{"text"}})

        if author.text not in authors_dict.keys():
            authors_dict[author.text]=1
        else:
            authors_dict[author.text]+=1
        quote_len_list.append(len(quote_text.text))
        counter+=len(quote_text.text)
        try:
            for tag in quote.find("a", {"class":{"tag"}}):
                if tag.text not in tags_dict.keys():
                    tags_dict[tag.text]=1
                else:
                    tags_dict[tag.text]+=1
        except:
            pass


for k,v in authors_dict.items():
    if v==max(authors_dict.values()):
        print("Author with the most quotes:",k)
        print(f"{k}'s quote count: {v}")

average_quote_len=counter/len(quote_len_list)
print(f"Average quote length: {average_quote_len} words")
print(f"Longest quote: {max(quote_len_list)} words")
counter=0
for k,v in tags_dict.items():
    if v==max(tags_dict.values()):
        print("Most popular tag:",k)
        print(f"{k} tag was used: {v} times")
    counter+=v
print("Total tags used across all quotes:", counter)

authors_dict=(dict(reversed(sorted(authors_dict.items(), key=lambda item: item[1]))))
authors=list(authors_dict.keys())
authors=authors[:10]
quote_count=list(authors_dict.values())
quote_count=quote_count[:10]

tags_dict=(dict(reversed(sorted(tags_dict.items(), key=lambda item: item[1]))))
tags=list(tags_dict.keys())
tags=tags[:10]
tag_count=list(tags_dict.values())
tag_count=tag_count[:10]

author_fig=px.bar(x=authors,y=quote_count,labels={'x':'Authors','y':'Quote Count'},title='Top 10 Authors by Quote Count')
author_fig.show()

tag_fig=px.bar(x=tags,y=tag_count,labels={'x':'Tags','y':'Tag Count'},title='Top 10 Tags by Frequency')
tag_fig.show()