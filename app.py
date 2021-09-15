

pip install adafruit-io

from Adafruit_IO import Client
aio = Client('poojitha02','aio_fIrs00Gt0br0nLfin9UPjcMlMS05')
pip install python-telegram-bot==13.0 --quite

from telegram.ext import Updater, MessageHandler, Filters

def demo1(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Light ON')
  aio.send('Light',1)

def demo2(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Light OFF')
  aio.send('Light',0)

def demo3(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan ON')
  aio.send('Fan',1)

def demo4(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan OFF')
  aio.send('Fan',0)

   

def main(bot,update):
  a= bot.message.text.lower()
  if a =="on the light":
    demo1(bot,update)
  elif a =="off the light":
    demo2(bot,update)
  elif a =="on the fan":
    demo3(bot,update)  
  elif a =="off the fan":
    demo4(bot,update)  

bot_token = '1945595379:AAE15vLVlu9Lq6B6rYhwTabQXT34VsZ1uFY'
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
