import os
import logging
from pyrogram import Client, filters
from telegraph import upload_file
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

Jsbot = Client(
   "Telegraph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Jsbot.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await Jsbot.send_message(
               chat_id=message.chat.id,
               text="""<b>ههـلا عمࢪي انا بوت تليجࢪاف ميديا 

 هذا هو بوت استخࢪاج ࢪابط تليجࢪاف ميديا الخاص في سوࢪس فولتࢪ اختر ماتࢪيد من الاسفل 
👇 تسطيع استخراج 👇

📽️ فيديوهات قصيࢪه (ان لايتعدا حجمه 5MB).
🎬 فيديوهات مࢪحليه.
🖼️ صوࢪه.
💥 متحࢪكه.
💟 ملصق.
📜 ملفات نصيه.
📩 صندوق دعم.
👥 مجموعة الدعم.
🚀 الاستخࢪاج السريع .

✍️هذا هو بوت استخࢪاج ࢪابط تليجࢪاف ميديا الخاص ب سوࢪس فولتࢪ
اࢪسل لي اي شئ تࢪيده لاجعله رابط ්❤️‍🔥

هل تحتاج للمساعده ࢪاسل المطوࢪ @vrrrvrr</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "مساعده⚠️", callback_data="help"),
                                        InlineKeyboardButton(
                                            "المطوࢪ🤍", url="https://t.me/vrrrvrr"),
                                         InlineKeyboardButton(

                                            "السوࢪس", url="https://t.me/TI9TI9")
                                    ]]
                            ),
            disable_web_page_preview=True,        
            parse_mode="html")

@Jsbot.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Jsbot.send_message(
               chat_id=message.chat.id,
               text="""<b>بوت تليجࢪاف ميديا ❗

فقط اࢪسل صوره او فيديو قصيࢪ او متحࢪكه وسوف احوله الى ࢪابط تليجࢪاف .🤍

🤍 المبرمج : @vrrrvrr

@TI9TI9</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "🔙ࢪجوع", callback_data="start"),
                                        InlineKeyboardButton(
                                            "حول❗", callback_data="about"),
                                  ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jsbot.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Jsbot.send_message(
               chat_id=message.chat.id,
               text="""<b>حول هذا البوت!</b>

<b>♥ المبࢪمج :</b> <a href="https://t.me/vrrrvrr">FORM Iraq🇮🇶</a>

<b>🔆اللغة:</b> <a href="https://www.python.org/">Python 3</a>

<b>♻️اصدار بايروجرام 1.4.16:</b> <a href="https://github.com/pyrogram/pyrogram">Pyrogram</a>

<b>@TI9TI9</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "🔙ࢪجوع", callback_data="help"),
                                        InlineKeyboardButton(
                                            "❌اغلاق", callback_data="close")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jsbot.on_message(filters.photo)
async def telegraphphoto(client, message):
    msg = await message.reply_text("جاࢪي استخࢪاج الࢪابط...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("اࢪسل صوࢪه حجمها اقل من 5mb!") 
    else:
        await msg.edit_text(f'**تم استخࢪاج ࢪابط تليجࢪاف ميديا بنجاح!\n\n👻https://telegra.ph{response[0]}\n\nJoin  @TI9TI9**',
            disable_web_page_preview=False,
        )
    finally:
        os.remove(download_location)

@Jsbot.on_message(filters.video)
async def telegraphvid(client, message):
    msg = await message.reply_text("جاࢪي استخࢪاج الࢪابط...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("حجم الفيديو القصيࢪ يجب ان يكون اقل من 5mb!") 
    else:
        await msg.edit_text(f'**Your File Is Successfully Uploaded To Telegraph!\n\n👻https://telegra.ph{response[0]}\n\nJoin  @SLDeveloper**',
            disable_web_page_preview=False,
        )
    finally:
        os.remove(download_location)

@Jsbot.on_message(filters.animation)
async def telegraphgif(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Gif size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**تم استخࢪاج ࢪابط تليجࢪاف ميديا بنجاح!\n\n👻https://telegra.ph{response[0]}\n\nJoin @I9TI9**',
            disable_web_page_preview=False,
        )
    finally:
        os.remove(download_location)

@Jsbot.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)
      elif "about" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)

print(
    """
Bot Started!
Join @TI9TI9
"""
)

Jsbot.run()
