from telebot import types
import asyncio 
from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot("7733509918:AAHwVCXFEN4s2OqBbagtO9JyBw7b5QvYxjA")

CHANNELS = [
    "@Pictures_16K"
]

async def check_user(user_id):
    for ch in CHANNELS:
        try:
            status = await bot._chat_memberget(ch, user_id).status
            if status in ('left', 'kichked'):
                return False
        except:
            return False
    return True 

async def IsSubscribe(chat_id):
    markup = types.InlineKeyboardMarkup()
    for ch in CHANNELS:
        markup.add(types.InlineKeyboardButton(text=ch, url=f"https://t.me/{ch[1:]}"))
    
    markup.add(types.InlineKeyboardButton("✅Tekshirish✅", callback_data="check"))

    await bot.send_message(chat_id, "Botdan foydalanish uchun kanallarga obuna bo'lishiniz kerak!", reply_markup=markup)

async def kinolar(message):
    await bot.reply_to(message,f"""Salom!Men Animelarni qisqa treyleylarini topib beruvchi botman.""")

    markup = types.InlineKeyboardMarkup()

    button1 = types.InlineKeyboardButton("Yolg'izlikda daraja ko'tarish", callback_data="a")
    button2 = types.InlineKeyboardButton("Ko'k zindon", callback_data="b")
    button3 = types.InlineKeyboardButton("Soyada ko'tarilish", callback_data="c")
    button4 = types.InlineKeyboardButton("Jodugarlar jangi", callback_data="d")
    button5 = types.InlineKeyboardButton("Iblis qotili", callback_data="e")
    button6 = types.InlineKeyboardButton("Naruto", callback_data="f")
    button7 = types.InlineKeyboardButton("Quvib o'tish", callback_data="g")
    button8 = types.InlineKeyboardButton("Shamolni bo'ysundurish", callback_data="h")
    button9 = types.InlineKeyboardButton("Xarobalar qirolligi", callback_data="i")
    button10 = types.InlineKeyboardButton("Titanlar hujumi", callback_data="j")


    markup.add(button1,button2)
    markup.add(button3)
    markup.add(button4)
    markup.add(button5)
    markup.add(button6)
    markup.add(button7)
    markup.add(button8)
    markup.add(button9)
    markup.add(button10)

    await bot.send_message(message.chat.id, "Buttonlardan birini tanlang", reply_markup=markup)

@bot.message_handler(commands=['start'])
async def start(message):
    user_id = message.from_user.id
    if await check_user(user_id):
        await bot.send_message(message.chat.id, "Botdan foydalanishingiz mumikin!")
        await kinolar(message)
    else:
        await IsSubscribe(message.chat.id)

@bot.callback_query_handler(func=lambda call: call.data == "check")
async def check_callback(call):
    user_id = call.from_user.id
    if await check_user(user_id):
        await bot.send_message(call.message.chat.id, "Botdan foydalanishingiz mumkin.")
        await bot.answer_callback_query(call.id)
    else:
        await bot.send_message(call.message.chat.id, "Barcha kanallarga obuna bo'lmagansiz!\nOBUNA BO'LING!")
        await bot.answer_callback_query(call.id)

@bot.message_handler(func=lambda message: True)
async def send(message):
    user_id = message.from_user.id
    if not await check_user(user_id):
        await IsSubscribe(message.chat.id)
        return

    if message.text == "/1":
        a = open("s.mp4","rb")
        await bot.send_video(message.chat.id, a)
        await bot.answer_callback_query(call.id)
    elif message.text == "/2":
        b = open("Blue Lock.mp4","rb")
        await bot.send_video(message.chat.id, b)
        await bot.answer_callback_query(call.id)
    elif message.text == "/3":
        c = open("Shadow.mp4","rb")
        await bot.send_video(message.chat.id, c)
        await bot.answer_callback_query(call.id)
    elif message.text == "/4":
        d = open("Jodugarlar Jangi.mp4","rb")
        await bot.send_video(message.chat.id, d)
        await bot.answer_callback_query(call.id)
    elif message.text == "/5":
        e = open("Iblis qotili.mp4","rb")
        await bot.send_video(message.chat.id, e)
        await bot.answer_callback_query(call.id)
    elif message.text == "/6":
        f = open("Naruto.mp4","rb")
        await bot.send_video(message.chat.id, f)
        await bot.answer_callback_query(call.id)
    elif message.text == "/7":
        g = open("Quvib o'tish.mp4","rb")
        await bot.send_video(message.chat.id, g)
        await bot.answer_callback_query(call.id)
    elif message.text == "/8":
        h = open("Shamolni o'rgatish.mp4","rb")
        await bot.send_video(message.chat.id, h)
        await bot.answer_callback_query(call.id)
    elif message.text == "/9":
        i = open("Xarobalar qirolligi.mp4","rb")
        await bot.send_video(message.chat.id, i)
        await bot.answer_callback_query(call.id)
    elif message.text == "/10":
        j = open("Titanlar hujumi.mp4","rb")
        await bot.send_video(message.chat.id, j)
        await bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=lambda callback:True)
async def nimadir(call):
    user_id = call.from_user.id
    if await check_user(user_id):
        if call.data == "a":
            a = open("s.mp4","rb")
            await bot.send_video(call.message.chat.id, a)
            await bot.answer_callback_query(call.id)
        elif call.data == "b":
            b = open("Blue Lock.mp4","rb")
            await bot.send_video(call.message.chat.id, b)
            await bot.answer_callback_query(call.id)
        elif call.data == "c":
            c = open("Shadow.mp4","rb")
            await bot.send_video(call.message.chat.id, c)
            await bot.answer_callback_query(call.id)
        elif call.data == "d":
            d = open("Jodugarlar Jangi.mp4","rb")
            await bot.send_video(call.message.chat.id, d)
            await bot.answer_callback_query(call.id)   
        elif call.data == "e":
            e = open("Iblis qotili.mp4","rb")
            await bot.send_video(call.message.chat.id, e)
            await bot.answer_callback_query(call.id)      
        elif call.data == "f":
            f = open("Naruto.mp4","rb")
            await bot.send_video(call.message.chat.id, f)
            await bot.answer_callback_query(call.id)  
        elif call.data == "g":
            g = open("Quvib o'tish.mp4","rb")
            await bot.send_video(call.message.chat.id, g)
            await bot.answer_callback_query(call.id) 
        elif call.data == "h":
            h = open("Shamolni o'rgatish.mp4","rb")
            await bot.send_video(call.message.chat.id, h)
            await bot.answer_callback_query(call.id)
        elif call.data == "i":
            i = open("Xarobalar qirolligi.mp4","rb")
            await bot.send_video(call.message.chat.id, i)
            await bot.answer_callback_query(call.id)   
        elif call.data == "j":
            j = open("Titanlar hujumi.mp4","rb")
            await bot.send_video(call.message.chat.id, j)
            await bot.answer_callback_query(call.id)
    else:
        await IsSubscribe(call.message.chat.id)

print("Iwladi")
asyncio.run(bot.polling())