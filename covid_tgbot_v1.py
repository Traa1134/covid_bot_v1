import telebot
from covid import Covid
from telebot import types
from bs4 import BeautifulSoup
import requests

#info about covid
covid = Covid()




#token
bot = telebot.TeleBot('token')

#start message
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'choose a country', reply_markup=markup)


#flags
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
world = types.KeyboardButton('🌎')
est = types.KeyboardButton('🇪🇪')
rus = types.KeyboardButton('🇷🇺')
fin = types.KeyboardButton('🇫🇮')
lv = types.KeyboardButton('🇱🇻') #97
usa = types.KeyboardButton('🇺🇸') #177
fr = types.KeyboardButton('🇫🇷')#63
es = types.KeyboardButton('🇪🇸')#161
it = types.KeyboardButton('🇮🇹')#86
uk = types.KeyboardButton('🇬🇧')#181
de = types.KeyboardButton('🇩🇪')#67
lt = types.KeyboardButton('🇱🇹')
markup.add(world, est, rus, fin, lv, usa, fr, es, it, uk, de, lt)


def cov(id, x, message):
    covid = Covid()
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 OPR/71.0.3770.310'}
    response = requests.get(x, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_='info_blk stat_block confirmed')
    comps = []
    location = covid.get_status_by_country_id(id)
    try:
        for item in items:
            comps.append({
                'cases': item.find('sup').get_text()
            })
        for title in comps:
            a = (title['cases'])



        bot.send_message(message.chat.id, str(location['country']) + '\n' + "Confirmed: " + str(
            location['confirmed']) + '\n' + 'Active: '
                         + str(location['active']) + '\n' + 'Recovered: ' + str(
            location['recovered']) + '\n' + 'Deaths: ' + str(
            location['deaths']) + '\n' + 'New cases: ' + a)
    except AttributeError:
        bot.send_message(message.chat.id, str(location['country']) + '\n' + "Confirmed: " + str(
            location['confirmed']) + '\n' + 'Active: '
                         + str(location['active']) + '\n' + 'Recovered: ' + str(
            location['recovered']) + '\n' + 'Deaths: ' + str(
            location['deaths']) + '\n' + 'New cases: ' + 'no data yet')




#flag function
@bot.message_handler(content_types=['text'])
def messages(message):
    if message.text == '🌎':
        active = covid.get_total_active_cases()
        confirmed = covid.get_total_confirmed_cases()
        recovered = covid.get_total_recovered()
        deaths = covid.get_total_deaths()

        bot.send_message(message.chat.id, 'World:' + '\n' + "Confirmed: " + str(confirmed) + '\n' + 'Active: '
                         + str(active) + '\n' + 'Recovered: ' + str(recovered) + '\n' + 'Deaths: ' + str(
            deaths) + '\n')

    elif message.text == '🇪🇪':
        cov(58, 'https://coronavirus-monitor.info/country/estonia/', message)

    elif message.text == '🇱🇹':
        cov(103, 'https://coronavirus-monitor.info/country/lithuania/', message)

    elif message.text.lower() == 'lithuania':
        cov(103, 'https://coronavirus-monitor.info/country/lithuania/', message)

    elif message.text == '🇷🇺':
        cov(142, 'https://coronavirus-monitor.info/country/russia/', message)

    elif message.text == '🇫🇮':
        cov(62, 'https://coronavirus-monitor.info/country/finland/', message)

    elif message.text == '🇱🇻':
        cov(97, 'https://coronavirus-monitor.info/country/latvia/', message)

    elif message.text == '🇺🇸':
       cov(178, 'https://coronavirus-monitor.info/country/usa/', message)

    elif message.text == '🇫🇷':
       cov(63, 'https://coronavirus-monitor.info/country/france/', message)

    elif message.text == '🇪🇸':
        cov(162, 'https://coronavirus-monitor.info/country/spain/', message)

    elif message.text == '🇮🇹':
        cov(86, 'https://coronavirus-monitor.info/country/italy/', message)

    elif message.text == '🇬🇧':
        cov(182, 'https://coronavirus-monitor.info/country/uk/', message)

    elif message.text == '🇩🇪':
        cov(67, 'https://coronavirus-monitor.info/country/germany/', message)

    elif message.text.lower() == 'world':

        active = covid.get_total_active_cases()
        confirmed = covid.get_total_confirmed_cases()
        recovered = covid.get_total_recovered()
        deaths = covid.get_total_deaths()

        bot.send_message(message.chat.id, 'World:' + '\n' + "Confirmed: " + str(confirmed) + '\n' + 'Active: '
                             + str(active) + '\n' + 'Recovered: ' + str(recovered) + '\n' + 'Deaths: ' + str(
                deaths) + '\n')


    elif message.text.lower() == 'estonia':
        cov(58, 'https://coronavirus-monitor.info/country/estonia/', message)

    elif message.text.lower() == 'russia':
        cov(142, 'https://coronavirus-monitor.info/country/russia/', message)

    elif message.text.lower() == 'finland':
        cov(62, 'https://coronavirus-monitor.info/country/finland/', message)

    elif message.text.lower() == 'latvia':
        cov(97, 'https://coronavirus-monitor.info/country/latvia/', message)

    elif message.text.lower() == 'usa':
        cov(178, 'https://coronavirus-monitor.info/country/usa/', message)

    elif message.text.lower() == 'france':
        cov(63, 'https://coronavirus-monitor.info/country/france/', message)

    elif message.text.lower() == 'spain':
        cov(162, 'https://coronavirus-monitor.info/country/spain/', message)

    elif message.text.lower() == 'italy':
        cov(86, 'https://coronavirus-monitor.info/country/italy/', message)

    elif message.text.lower() == 'united kingdom':
        cov(182, 'https://coronavirus-monitor.info/country/uk/', message)

    elif message.text.lower() == 'germany':
        cov(67, 'https://coronavirus-monitor.info/country/germany/', message)
#start bot
if  __name__ == '__main__':
    bot.polling(none_stop=True)

