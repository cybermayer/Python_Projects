import stock
import news

# Constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Initialize instances of StockAPI and TeslaNews
stock = stock.StockAPI()
news = news.TeslaNews()

# Retrieve stock prices
prises = stock.get_response()

# Calculate percentage changes
yg = format(((prises[1] / prises[2]) - 1) * 100, ".4f")
yg_perc = f"{yg}%"

tg = format(((prises[0] / prises[1]) - 1) * 100, ".4f")
tg_perc = f"{tg}%"

# Initialize lists for news and URLs
news = []
message = ""
urls = []

# Check for significant stock price changes
if tg <= -5 or tg >= 5:
    if tg >= 5:
        chart = "📈"
    elif tg <= -5:
        chart = "📉"
        
        # Attempt to fetch news articles, handle IndexError
        try:
            for i in range(0, 4):
                news.append(news.get_news(i))
        except IndexError:
            pass
        finally:
            # Prepare message based on available news
            if len(news) == 0:
                message = f"{STOCK} {chart} {tg_perc} !!! No related news can be found."
            else:
                for i in range(0, (len(news))):
                    urls.append(message[i]["url"])
                message = f"""
                
                {STOCK} {chart} {tg_perc} !!!

                HEAD:{message[0]["title"]}
                
                BRIEF:{message[0]["brief"]} 

                URL: {urls[0]}

                MORE RELATED NEWS: {urls[1:(len(urls))]}
                
                """
