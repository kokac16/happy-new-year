import telebot
import credits
from datetime import datetime, timezone, timedelta
import db

bot = telebot.TeleBot(credits.token)


tz = timezone(timedelta(hours=5))
new_year_time = datetime(2024, 1, 1, 0, 0, 0, 0, tz)

@bot.message_handler(commands=["start", "new_year"])
def new_year(msg: telebot.types.Message):


    if datetime.now().month != 1:
        time_now = datetime.now(tz)
        tmp = new_year_time - time_now
        hours = 23 - tmp.seconds // 3600
        minutes = int(tmp.seconds // 60) % 10
        seconds = int(tmp.total_seconds() % 60)
        music_name, music_link = db.get_random_music()

        text = f"🎄До новго года осталось {tmp.days} дня, {hours} часов, {minutes} минут, {seconds} секунд\n\n✍️Список дел: {db.get_random_todos_text()}\n\n🎶Музыка: {music_name}\n\n{music_link}"

        bot.send_message(msg.chat.id, text)
    
    else:
        bot.send_message(msg.chat.id, "С новым годом!")




if __name__ == '__main__':
    bot.polling()