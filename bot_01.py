import telebot
import config

bot = telebot.TeleBot(config.Token)


def send_message(message):
    bot.send_message(message.chat.id, 'Hello')


@bot.message_handler(content_types=['text'])
def control(message):
    if len(message.text) > 55 and message.from_user.id != 1028496717 and message.from_user.id != 763070224:
        bot.forward_message(-1001393620851, message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(-1001393620851, message.from_user.id)


while True:
    bot.polling(none_stop=True)

