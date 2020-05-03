import pyowm
import telebot
import os

owm = pyowm.OWM('d31e35e33cd025f52f6bf826b66e9c69', language = "ru")
token = os.environ.get('BOT_TOKEN')
@bot.message_handler(commands=['start'])
def cmd_start(message): 
     bot.send_message(message.chat.id,"Привет✌!Погода в каком городе тебя интерисует? И я посоветую тебе можно гулять или нет😉 ")
       
@bot.message_handler(content_types=['text'])
def send_echo(message):
 try:  
    observation = owm.weather_at_place( message.text )
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]
    hum = w.get_humidity()
    wind = w.get_wind()["speed"]
   
    
    answer =" В городе " + message.text  +  " сейчас " + w.get_detailed_status()   +"\n"
    answer +=" Температура сейчас в районе:🌡 " + str(temp) + "\n" + "Скорость ветра:💨 " + str(wind) + "м/с" +  "\nВлажность:💧 " + str(hum) + "%" +   "\n\n"


    if temp < 10:
      answer += "Сейчас очень холодно😭, послушай бабушку!"
    elif temp <20:
      answer += "Сейчас прохладно одевайся потеплее😢 . "
    else:
      answer += "Температура отличная😻 "
   
    bot.send_message(message.chat.id, answer,) 

 except pyowm.exceptions.api_response_error.NotFoundError:
      bot.send_message(message.chat.id, 'Город не найден 😔')

    
 

bot.polling( none_stop = True)

