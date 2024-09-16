import telebot
# Token: 6550785527:AAFCdDOZ0Opcmoh7gE5vrCpxYjXwA4pdWAw
Toke = "6550785527:AAFCdDOZ0Opcmoh7gE5vrCpxYjXwA4pdWAw"
bot = telebot.TeleBot(Toke)

@bot.message_handler(commands=["start", "begin"] )
def start(message):
    print("start")
    bot.reply_to(message, "Hello! I'm a bot.")

@bot.message_handler(commands=["hello", "hi"])
def greeting(message):
    print("hello")
    bot.reply_to(message, "Greetings, my dear friend! Nice to see you!")

@bot.message_handler(commands=["stop", "bye"])
def stop(message):
    print("farewell")
    bot.reply_to(message, "Bye, see you later!")

@bot.message_handler(content_types=['text'])
def answer(message):
    text = message.text
    if "?" in text:
        bot.reply_to(message, "You asked a question")

    else:
        bot.reply_to(message, f"You sent message: '{text}'")

bot.polling(none_stop=True, interval=0)