from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
	text = """Приветствую тебя, дорогой пользователь!

Если бы я мог, я бы выполнил любую твою команду, но пока знаю только /start"""
	print(text)
	update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)


def main():
	mybot = Updater('573293182:AAGj11JEaB5w1bunGGpa-tKNwBca3wdTL3A', request_kwargs=PROXY )
	mybot.dispatcher.add_handler(CommandHandler('start', greet_user))
	mybot.dispatcher.add_handler(MessageHandler(Filters.text, talk_to_me))

	mybot.start_polling()
	mybot.idle()

if __name__ == '__main__':
	main()
