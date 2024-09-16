import telebot
Toke = "7432313323:AAHJRiFyqiyrkZ0kk-Y2oh_kgXvpur3Ojlk"
bot=telebot.TeleBot(Toke)

# TRIGGERED AFTER "START_GAME", WAITING FOR USER ANSWER
is_waiting = False 

#boundaries for start and end of the search segment
left = None # start of segment

right = None # end of segment 

# function for calculating middle
def middle(left, right):
    return int((right - left) / 2 + left)


#BOT'S NUMBER
bot_number = None 
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hi! Let's play a game - you think of a number from 1 to 100, and I'll guess it. To start the game, use the command /start_game ") 

@bot.message_handler(commands=['help'])

def help(message):
    bot.send_message(message.chat.id, "Hello! Here is a list of available commands:\n/start - start work\n/start_game - start the game\n/help - list of available commands") 

@bot.message_handler(commands=['start_game'])
def start_game(message):
    bot.send_message(message.chat.id, "So, let's begin. What is the smallest number you can think of?") 
    global is_waiting
    is_waiting = True 

@bot.message_handler(content_types=['text'])
def answer(message):
    global is_waiting
    global bot_number
    global left
    global right
    if is_waiting and message.text == 'done': 
        bot_number = middle(left, right)
        bot.send_message(message.chat.id, f"I think your number is {bot_number}. \nIf I guessed right, write '=', if your number is bigger - '>', and if it is smaller, then '<' ")  
        is_waiting = False 
    elif message.text == '<' and bot_number != None:
       right = bot_number - 1
       bot_number = middle(left, right)
       bot.send_message(message.chat.id,
       f"I think your number is {bot_number}. \nIf I guessed right, write '=', if your number is bigger - '>', and if it is smaller, then '<' ") 
    
    elif message.text == '>' and bot_number != None:
        left = bot_number + 1
        bot_number = middle(left, right)
        bot.send_message(message.chat.id, f"I think your number is {bot_number}. \nIf I guessed right, write '=', if your number is bigger, write '>', and if it's smaller, write '<'") 

    elif message.text == '='and bot_number != None:
        bot.send_message(message.chat.id, "Hurray! I guessed right! \nTo start the game again, use the /start_game command")
        bot_number = None 
        left = None
        right = None 

    elif message.text.isdigit() and left == None:
        left = int(message.text)
        bot.send_message(message.chat.id, "What is the biggest number you can think of?")

    elif message.text.isdigit() and right == None:
        right = int(message.text)
        bot.send_message(message.chat.id, f"Think of a number from {left} to {right} and write 'done', I'll try to guess.") 



    else:
        bot.send_message(message.chat.id, "To start the game, use the command /start_game") 










bot.polling(none_stop=True, interval=0) 


