import requests,json,random

def getBookQuotes(title : str) -> list:
    site = 'https://goodquotesapi.herokuapp.com/title/{}'.format(title.replace(' ','+'))
    req = requests.get(site)
    try:
        quotesjson = json.loads(req.text)
        quotes_dict = [{'quote' : quote.get('quote'), 'author' : quote.get('author'), 'book' : quote.get('publication')} for quote in quotesjson.get('quotes')]
    except:
        quotes_dict = None
    return quotes_dict

if __name__ == "__main__":
    book = "Harry Potter"
    quotes = getBookQuotes(book)
    quote = quotes[random.randint(0,len(quotes))]
    quoteline = f"""{quote['quote']} - {quote['author']}, {quote['book']}"""
    print(quoteline)