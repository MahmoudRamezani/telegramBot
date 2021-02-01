
"""
botTelegram.py
First edition: Jan. 31, 2021
A couple of months ago, I had to write a telegram bot for a small business
which was running in the Telegram application. By a simple search in the net, 
you can find many source about how to write a bot in telegram, but I could not find
any that can be a template and can be costumized for a simple interaction with the user. 
Then, I have desided to write a simple code to include the general template and important 
commands to do so. Here, is a simple version of it that can be costumized for your goal very easily. 
I assume that the reader does not know anything about writing a bot, but know basic python scripts!

To be able to use this template easily, please read carefully the readme file.

More information in: https://core.telegram.org/bots/api

if you have any question, please feel free to email: mahmoud.ramezani@uia.no
"""

import telebot
from telebot import types
from flask import Flask, request
import os
from datetime import datetime
import pytz

TOKEN = '1604316615:AAEmZAE2wuNg8FedyM3mzhnPpqbMH73fRvA'         #Here, you have to replace the token that you got from bot father of telegram
bot = telebot.TeleBot(TOKEN)
URL = "https://telegrambot4learning.herokuapp.com/"     # Here, the address of the server that runs this bot must be inserted

server = Flask(__name__)
ads_dict = {}


class ADS:
    def __init__(self, Name):
        self.Name = Name
        self.telegramName = None
        self.userName = None
        # self.anyProperty = None, Here, all of the properties from the telegram user account that are 
                                   # important for your business can be added. 
        self.Q1 = None             # Q1 is replaced with the first question's name that you are interested
                                   # to ask from the interactive user. The same goes for the next two questions
                                   # here. I assumed here that we have three questions throughout the bot, but
                                   # feel free to add as more as you want.
        self.Q2 = None
        self.Q3 = None

        
        
@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, "Hello World! (send your welcome note here)\n")
    bot.register_next_step_handler(msg, process_Q1_step)
    bot.enable_save_next_step_handlers()
    bot.load_next_step_handlers()


def process_Q1_step(message): #Here we go for the first step, or first question
    try:
        chat_id = message.chat.id
        Q1_local_variable  = message.text 
        ads = ADS(Q1_local_variable )
        ads_dict[chat_id] = ads
        ads.userName = message.chat.username
        if ads.userName == None:
            ads.userName = 'defaultUserName'
        ads.telegramName = message.chat.first_name #just save whatever you need from the user information
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True) #This is the option in telegram bot to ask optional 
                                                                   # question, in which user select one of the options, e.g. A or B
        markup.add('option_A', 'option_B') # preparing for the next round of question
                                           # receive the answer of the user for the next question
        msg = bot.send_message(chat_id, 'some info about the options!', reply_markup=markup)
        bot.register_next_step_handler(msg, process_Q2_step)
        bot.enable_save_next_step_handlers()
        bot.load_next_step_handlers()
    except Exception:
        bot.reply_to(message, 'if any error happens! give some info \n /start')


def process_Q2_step(message): #Going for the second step
    try:
        chat_id = message.chat.id
        ads = ads_dict[chat_id]
        Q2_local_variable  = message.text

        if (Q2_local_variable  == u'option_A') or (Q2_local_variable  == u'option_B'): # Just checking if the input is correct!
            ads.Q2_local_variable  = Q2_local_variable 
        else:
            raise Exception()                
        
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('option_C', 'option_D') # Preparing for the next round of question- next step
        msg = bot.send_message(chat_id, 'Some info about the next step to the user', reply_markup=markup)
        bot.register_next_step_handler(msg, process_Q3_step)
        bot.enable_save_next_step_handlers()
        bot.load_next_step_handlers()
    except Exception:
        bot.reply_to(message, 'Again, some errors in this step! \n /start')


def process_Q3_step(message):
    try:
        chat_id = message.chat.id
        Q3_local_variable = message.text
        ads = ads_dict[chat_id]
        if (Q3_local_variable == u'option_C') or (Q3_local_variable == u'option_D'):
            ads.Q3_local_variable = Q3_local_variable
        else:
            raise Exception() 
        msg = bot.send_message(chat_id, 'ask the last questin: for example check with the user if the previous information is correct')
        bot.register_next_step_handler(msg, process_Last_step)    
        bot.enable_save_next_step_handlers()
        bot.load_next_step_handlers()
    except Exception:
        bot.reply_to(message, 'Again, think about the possible errors here and include them and add the required lines here \n /start')

## Feel free to add more steps/questions and recieve more input/infor from the user before this last step!
        
def process_Last_step(message):

    try:
        chat_id = message.chat.id
        chat_id_admin = 000000000 # you can ask the bot to send a copy of this recording to another telegram account, like yours: then insert the telegram id of that account here

        notallowedIDs = {"Here, you can add some telegram account ID's and block them who should not be able to use your bot"}
         
        Last = message.text
        ads = ads_dict[chat_id]
        ads.Last = Last       
        tz = pytz.timezone('Europe')    #hereafter, you can add some condition for publishing the results in the channel.
                                        # For example, you can limit publishing and posting to a specific time of the day 
                                        # and block it for the rest.
        time_now = datetime.now(tz)
        dt_string = time_now.strftime("%d%H%M")
        allowedTime = int(time_now.strftime("%H%M"))
        if chat_id in notallowedIDs: 
            bot.send_message(chat_id_admin, 'more information for the admin for this case')
            bot.send_message(chat_id, 'tell the blocked id why or what happend or any more info') 
        elif allowedTime>759 and allowedTime<2300:
            # Publish the result and post wherever you want, in a group/channel/admin account
            bot.send_message(chat_id_admin, 'send a copy of answers to admin' )
            bot.send_message('@telegram_group_id', 'send a copy to the group')            
            bot.send_message(chat_id, 'send the copy to the user') 
        else: 
            #do accordingly and inform others here, for example about the time limitation of postin or so on
            bot.send_message(chat_id,'for example: give some information about what the user can do now!')
    except Exception:
        bot.reply_to(message, 'some information about the error in this step')
    
    
@server.route('/' + TOKEN, methods=['GET', 'POST'])
def getMessage():

    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    #print("webwebweb")
    bot.remove_webhook()
    bot.set_webhook(url=URL + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    print("bot starts!")   

