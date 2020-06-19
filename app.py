from credentials import TOKEN,URL
from methods import getBookQuotes
from flask import Flask, request, render_template
from telepot.loop import OrderedWebhook
from telepot.namedtuple import InlineKeyboardMarkup,InlineKeyboardButton
from random import randint
import telepot
import csv

app = Flask(__name__)
bot = telepot.Bot(TOKEN)

def handle(msg):
    msg_type = telepot.flavor(msg)
    if msg_type == 'chat':
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            text = msg['text']
            if text[0] == '/':
                if '/start' in text:
                    bot.sendMessage(chat_id,"Welcome to _Quotes Bot_!\nGet quotes from any book!📖",parse_mode='Markdown')
                elif '/help' in text:
                    bot.sendMessage(chat_id,"Simply send the name of a book to get quotes from it")
                else:
                    bot.sendMessage(chat_id,"Sorry, I don't recogonize this command yet")
            else:
                keyboard = [[InlineKeyboardButton(text='1️⃣',callback_data=f'1<!>{text}'),InlineKeyboardButton(text='5️⃣',callback_data=f'5<!>{text}')],[InlineKeyboardButton(text='1️⃣5️⃣',callback_data=f'15<!>{text}'),InlineKeyboardButton(text='3️⃣0️⃣',callback_data=f'30<!>{text}')]]
                bot.sendMessage(chat_id,text="How many quotes?",reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboard))
        else:
            bot.sendMessage(chat_id,"Sorry, I don't support this kind of file yet.")
    elif msg_type == 'callback_query':
        chat_id = msg['from']['id']
        text = msg['data']
        number,text = text.split('<!>')
        quotes = getBookQuotes(text)
        if quotes:
            # quotes = quotes[:int(number)-1]
            quotes_chosen = []
            if int(number) >= len(quotes):
                quotes_chosen = quotes
            else:
                while len(quotes_chosen) != int(number):
                    quote_chosen = quotes[randint(0,len(quotes)-1)]
                    if quote_chosen not in quotes_chosen: quotes_chosen.append(quote_chosen)
            for quote in quotes_chosen:
                quoteline = f"""_{quote['quote']}_\n - {quote['author']}, {quote['book']}"""
                bot.sendMessage(chat_id,quoteline,parse_mode='Markdown')
        else:
            bot.sendMessage(chat_id, f"No results found for _{text}_",parse_mode='Markdown')
    else:
        bot.sendMessage(chat_id,f"Sorry, I don't support {msg_type} yet.")

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/quotes',methods=['GET','POST'])
def lyric():
    title = request.form['title']
    try:
        quotes = [quote for quote in getBookQuotes(title) if len(quote['quote']) <= 160]
        quote = quotes[randint(0,len(quotes))]
        return render_template('quote.html',title=quote['book'], quote=quote['quote'], author=quote['author'], query=title)
    except:
        return render_template('error.html', title=title)

@app.route('/webhook_path', methods=['GET', 'POST'])
def pass_update():
    webhook.feed(request.data)
    return 'OK'

if URL != bot.getWebhookInfo()['url']:
    bot.setWebhook(URL)
webhook = OrderedWebhook(bot, handle)
webhook.run_as_thread()

if __name__ == "__main__":
    app.run(threaded=True)