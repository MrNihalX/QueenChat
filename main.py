
from pyrogram import Client, filters
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
import os
import re
import asyncio
import time
from datetime import datetime

API_ID = os.environ.get("API_ID", "10043760") 
API_HASH = os.environ.get("API_HASH", "789721373b7bbd1ffe7081fa15397ba0") 
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://Music:Music@cluster0.f9x4i.mongodb.net/Cluster0?retryWrites=true&w=majority")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "CuteQueenBot") 
UPDATE_CHNL = os.environ.get("UPDATE_CHNL", "+DllhdM36-tgzMDRl")
OWNER_ID = os.environ.get("OWNER_ID")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
SUPPORT_GRP = os.environ.get("SUPPORT_GRP", "+DllhdM36-tgzMDRl")
BOT_NAME = os.environ.get("BOT_NAME", "π¦βα΄ Ν₯ΙͺΝ£α΄Ν«βπ²iss πΆπππππβ")
START_IMG1 = os.environ.get("START_IMG1", "https://telegra.ph/file/613a70c0257608ef1a6fc.jpg")
START_IMG2 = os.environ.get("START_IMG2")
START_IMG3 = os.environ.get("START_IMG3")
START_IMG4 = os.environ.get("START_IMG4")
START_IMG5 = os.environ.get("START_IMG5")
START_IMG6 = os.environ.get("START_IMG6")
START_IMG7 = os.environ.get("START_IMG7")
START_IMG8 = os.environ.get("START_IMG8")
START_IMG9 = os.environ.get("START_IMG9")
START_IMG10 = os.environ.get("START_IMG10")
STKR = os.environ.get("STKR", "CAACAgQAAxkBAALRimNZXTpB8mhQbnAAAWAvCV4Ya1uHFQACnxEAAqbxcR57wYUDyflSISoE")
STKR1 = os.environ.get("STKR1", "CAACAgQAAxkBAALRi2NZXUgjZCT775L5Nr0XrLbQ6XIpAAK_EQACpvFxHq2xh5JRVJNrKgQ")
STKR2 = os.environ.get("STKR2", "CAACAgQAAxkBAALRjGNZXUs6YPggISBdtg4nXaU0vjNzAALqCwACbCIRU61ZQKi3F88DKgQ")
STKR3 = os.environ.get("STKR3", "CAACAgQAAxkBAALRjWNZXUvETcfHR2Yi9ftTQLLP2uD8AAIVDAAC1SMQU-QrCHEcbz8rKgQ")
STKR4 = os.environ.get("STKR4", "CAACAgQAAxkBAALRjmNZXWw-WbZ_iAg-4UGixa7WSz3RAAK9CQACelwRUzpqVCTmeOrfKgQ")
STKR5 = os.environ.get("STKR5", "CAACAgQAAxkBAALRj2NZXXJw6Pw7TJgYQStoq4u2oYpmAAKgEQACpvFxHk7lQeNrq3NMKgQ")
STKR6 = os.environ.get("STKR6", "CAACAgQAAxkBAALRkGNZXYmAXYRR4lmCxHGPgG012Vm0AAJiFwACpvFxHuCsJc_EpuEVKgQ")
STKR7 = os.environ.get("STKR7", "CAACAgQAAxkBAALRkWNZXYyCvkfI4d1lK0AEMkG0GdUmAAJmFwACpvFxHnvJHTM8_o9XKgQ")
STKR8 = os.environ.get("STKR8", "CAACAgQAAxkBAALRkmNZXZg1zuakmgkPf2lfXPXi4bZaAALACgACQUGpUjAAAYL3e09XCyoE")
STKR9 = os.environ.get("STKR9", "CAACAgQAAxkBAALRpWNZXzUmc-SfzlpERZFVXwABEluuGQACbQsAAlBzGVO38BzgGrQ1sCoE")

bot = Client(
    "VickBot" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)


async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]


PHOTO = [
    START_IMG1,
    START_IMG2,
    START_IMG3,
    START_IMG4,
    START_IMG5,
    START_IMG6,
    START_IMG7,
    START_IMG8,
    START_IMG9,
    START_IMG10,
]

EMOJIOS = [ 
      "π£",
      "π₯",
      "πͺ",
      "π§¨",
      "β‘",
      "π€‘",
      "π»",
      "π",
      "π©",
      "π",
]
      
STICKER = [
      STKR,
      STKR1,
      STKR2,
      STKR3,
      STKR4,
      STKR5,
      STKR6,
      STKR7,
      STKR8,
      STKR9,
]
START = f"""
**ΰΉ Κα΄Κ, Ιͺ α΄α΄ [{BOT_NAME}]({START_IMG1})**
**β» α΄Ι΄ α΄Ιͺ Κα΄sα΄α΄ α΄Κα΄α΄Κα΄α΄**
**ββββββββββββββ**
**β» α΄sα΄Ι’α΄ /chatbot [α΄Ι΄/α΄??]**
<b>||ΰΉ ΚΙͺα΄ Κα΄Κα΄ Κα΄α΄α΄α΄Ι΄ ?α΄Κ Κα΄Κα΄.||</b>
"""
DEV_OP = [
    [
        InlineKeyboardButton(text="π₯ α΄α΄‘Ι΄α΄Κ π₯", url=f"t.me/{OWNER_USERNAME}"),
        InlineKeyboardButton(text="β¨ κ±α΄α΄α΄α΄Κα΄ β¨", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="π§Έ α΄α΄α΄ α΄α΄ Κα΄ΚΚ π§Έ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="π Κα΄Κα΄ & α΄α΄α΄s π", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="βοΈ sα΄α΄Κα΄α΄ βοΈ", callback_data="SOURCE"),
        InlineKeyboardButton(text="βοΈ α΄Κα΄α΄α΄ βοΈ", callback_data="ABOUT"),
    ],
]
PNG_BTN = [
    [
         InlineKeyboardButton(
             text="π§Έ α΄α΄α΄ α΄α΄ Κα΄ΚΚ π§Έ",
             url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(text="β¨ sα΄α΄α΄α΄Κα΄ β¨", 
                              url=f"https://t.me/{SUPPORT_GRP}",
         ),
     ],
]
HELP_READ = f"""
<u>**α΄α΄α΄α΄α΄Ι΄α΄s ?α΄Κ {BOT_NAME}**</u>
<u>**α΄Κα΄ Ι’Ιͺα΄ α΄Ι΄ Κα΄Κα΄α΄‘!**</u>
**α΄ΚΚ α΄Κα΄ α΄α΄α΄α΄α΄Ι΄α΄s α΄α΄Ι΄ Κα΄ α΄sα΄α΄ α΄‘Ιͺα΄Κ:/**
**ββββββββββββββ**
<b>||Β©οΈ @{OWNER_USERNAME}||</b>
"""
BACK = [
     [
           InlineKeyboardButton(text="β¨ Κα΄α΄α΄ β¨", callback_data="BACK"),
     ],
]
HELP_BTN = [
     [
          InlineKeyboardButton(text="π³ α΄Κα΄α΄Κα΄α΄ π³", callback_data="CHATBOT_CMD"),
          InlineKeyboardButton(text="π α΄α΄α΄Κs π", callback_data="TOOLS_DATA"),
     ],
     [
          InlineKeyboardButton(text="β¨ Κα΄α΄α΄ β¨", callback_data="BACK"),
          InlineKeyboardButton(text="βοΈ α΄Κα΄sα΄ βοΈ", callback_data="CLOSE"),
     ],
]

CLOSE_BTN = [
      [
           InlineKeyboardButton(text="βοΈ α΄Κα΄sα΄ βοΈ", callback_data="CLOSE"),
      ],
]

CHATBOT_ON = [
        [
            InlineKeyboardButton(text="α΄Ι΄α΄ΚΚα΄", callback_data=f"addchat"),
            InlineKeyboardButton(text="α΄Ιͺsα΄ΚΚα΄", callback_data=f"rmchat"),
        ],
]

PNG_BTN = [
    [
         InlineKeyboardButton(
             text="π§Έ α΄α΄α΄ α΄α΄ Κα΄ΚΚ π§Έ",
             url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(text="β¨ α΄Κα΄sα΄ β¨", 
                              callback_data="CLOSE",
         ),
     ],
]

TOOLS_DATA_READ = f"""
<u>**α΄α΄α΄Κs ?α΄Κ {BOT_NAME} α΄Κα΄:**</u>
**β» α΄sα΄ `/repo` ?α΄Κ Ι’α΄α΄α΄ΙͺΙ΄Ι’ sα΄α΄Κα΄α΄ α΄α΄α΄α΄!**
**ββββββββββββββ**
**β» α΄sα΄ `/ping` ?α΄Κ α΄Κα΄α΄α΄ΙͺΙ΄Ι’ α΄Κα΄ α΄ΙͺΙ΄Ι’ α΄? {BOT_NAME}**
**ββββββββββββββ**
<b>||Β©οΈ @{OWNER_USERNAME}||</b>
"""

CHATBOT_READ = f"""
<u>**α΄α΄α΄α΄α΄Ι΄α΄s ?α΄Κ {BOT_NAME}**</u>
**β» α΄sα΄ `/chatbot` α΄α΄ α΄Ι΄α΄ΚΚα΄/α΄Ιͺsα΄ΚΚα΄ α΄Κα΄ α΄Κα΄α΄Κα΄α΄.**
**ΰΉ Ι΄α΄α΄α΄ β» α΄Κα΄ α΄Κα΄α΄ α΄ α΄α΄α΄α΄α΄Ι΄α΄ ?α΄Κ α΄Κα΄α΄Κα΄α΄ α΄‘α΄Κα΄ ΙͺΙ΄ Ι’Κα΄α΄α΄ α΄Ι΄ΚΚ!!**
**βββββββββββββββ**
<b>||Β©οΈ @{OWNER_USERNAME}||</b>
"""
CHATBOT_BACK = [
        [     
              InlineKeyboardButton(text="β¨ Κα΄α΄α΄ β¨", callback_data="CHATBOT_BACK"),
              InlineKeyboardButton(text="βοΈ α΄Κα΄sα΄ βοΈ", callback_data="CLOSE"),
        ],
]
HELP_START = [
     [
            InlineKeyboardButton(text="π Κα΄Κα΄ π", callback_data="HELP"),
            InlineKeyboardButton(text="π³ α΄Κα΄sα΄ π³", callback_data="CLOSE"),
     ],
]

HELP_BUTN = [
     [
           InlineKeyboardButton(text="π Κα΄Κα΄ π", url=f"https://t.me/{BOT_USERNAME}?start=help"),
           InlineKeyboardButton(text="π³ α΄Κα΄sα΄ π³", callback_data="CLOSE"),
     ],
]

ABOUT_BTN = [
      [
           InlineKeyboardButton(text="π sα΄α΄α΄α΄Κα΄ π", url=f"https://t.me/{SUPPORT_GRP}"),  
           InlineKeyboardButton(text="π Κα΄Κα΄ π", callback_data="HELP"),
      ],
      [    
           InlineKeyboardButton(text="πΎ α΄α΄‘Ι΄α΄Κ πΎ", url=f"https://t.me/{OWNER_USERNAME}"), 
           InlineKeyboardButton(text="βοΈ sα΄α΄Κα΄α΄ βοΈ", callback_data="SOURCE"),
      ],
      [ 
           InlineKeyboardButton(text="π³ α΄α΄α΄α΄α΄α΄s π³", url=f"https://t.me/{UPDATE_CHNL}"),  
           InlineKeyboardButton(text="β¨ Κα΄α΄α΄ β¨", callback_data="BACK"),
      ],
]
SOURCE_READ = f"**Κα΄Κ, α΄Κα΄ sα΄α΄Κα΄α΄ α΄α΄α΄α΄ α΄? [{BOT_NAME}](https://t.me/{BOT_USERNAME}) Ιͺs Ι’Ιͺα΄ α΄Ι΄ Κα΄Κα΄α΄‘.**\n**α΄Κα΄α΄sα΄ ?α΄Κα΄ α΄Κα΄ Κα΄α΄α΄ & Ι’Ιͺα΄ α΄ α΄Κα΄ sα΄α΄Κ β―**\n**ββββββββββββββββββ**\n**Κα΄Κα΄ Ιͺs α΄Κα΄ [sα΄α΄Κα΄α΄ α΄α΄α΄α΄](https://t.me/+DllhdM36-tgzMDRl)**\n**ββββββββββββββββββ**\n**Ιͺ? Κα΄α΄ ?α΄α΄α΄ α΄Ι΄Κ α΄Κα΄ΚΚα΄α΄ α΄Κα΄Ι΄ α΄α΄Ι΄α΄α΄α΄α΄ α΄α΄ [sα΄α΄α΄α΄Κα΄ α΄Κα΄α΄](https://t.me/{SUPPORT_GRP}).\n<b>||Β©οΈ @{OWNER_USERNAME}||</b>"

ABOUT_READ = f"""
**β» [{BOT_NAME}](https://t.me/{BOT_USERNAME}) Ιͺs α΄Ι΄ α΄Ιͺ Κα΄sα΄α΄ α΄Κα΄α΄-Κα΄α΄.**
**β» [{BOT_NAME}](https://t.me/{BOT_USERNAME}) Κα΄α΄ΚΙͺα΄s α΄α΄α΄α΄α΄α΄α΄Ιͺα΄α΄ΚΚΚ α΄α΄ α΄ α΄sα΄Κ.**
**β» Κα΄Κα΄s Κα΄α΄ ΙͺΙ΄ α΄α΄α΄Ιͺα΄ α΄α΄ΙͺΙ΄Ι’ Κα΄α΄Κ Ι’Κα΄α΄α΄s.**
**β» α΄‘ΚΙͺα΄α΄α΄Ι΄ ΙͺΙ΄ [α΄Κα΄Κα΄Ι΄](https://www.python.org) α΄‘Ιͺα΄Κ [α΄α΄Ι΄Ι’α΄-α΄Κ](https://www.mongodb.com) α΄s α΄ α΄α΄α΄α΄Κα΄sα΄**
**ββββββββββββββ**
**β» α΄ΚΙͺα΄α΄ α΄Ι΄ α΄Κα΄ Κα΄α΄α΄α΄Ι΄s Ι’Ιͺα΄ α΄Ι΄ Κα΄Κα΄α΄‘ ?α΄Κ Ι’α΄α΄α΄ΙͺΙ΄Ι’ Κα΄sΙͺα΄ Κα΄Κα΄© α΄Ι΄α΄ ΙͺΙ΄?α΄ α΄Κα΄α΄α΄ [{BOT_NAME}](https://t.me/{BOT_USERNAME})**
"""
@bot.on_message(filters.command(["start", "aistart", f"start@{BOT_USERNAME}"]))
async def restart(client, m: Message):
    if m.chat.type == "private":
        accha = await m.reply_text(
            text = random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("__α΄ΞΉΠΈg α΄ΟΠΈg κ¨οΈ ΡΡΞ±ΡΡΞΉΠΈg..__")
        await asyncio.sleep(0.2)
        await accha.edit("__α΄ΞΉΠΈg α΄ΟΠΈg κ¨ sΡΞ±ΡΡΞΉΠΈg.....__")
        await asyncio.sleep(0.2)
        await accha.edit("__α΄ΞΉΠΈg α΄ΟΠΈg κ¨οΈ sΡΞ±ΡΡΞΉΠΈg..__")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(
            sticker = random.choice(STICKER),
        )
        await asyncio.sleep(2)
        await umm.delete()
        await m.reply_photo(
            photo = random.choice(PHOTO),
            caption=f"""**ΰΉ Κα΄Κ, Ιͺ α΄α΄ [{BOT_NAME}](t.me/{BOT_USERNAME})**\n**β» α΄Ι΄ α΄Ιͺ Κα΄sα΄α΄ α΄Κα΄α΄Κα΄α΄.**\n**ββββββββββββββ**\n**β» α΄sα΄Ι’α΄ /chatbot [α΄Ι΄/α΄??]**\n<b>||ΰΉ ΚΙͺα΄ Κα΄Κα΄ Κα΄α΄α΄α΄Ι΄ ?α΄Κ Κα΄Κα΄||</b>""",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
    else:
        await m.reply_photo(
                      photo = random.choice(PHOTO),
                      caption = START,
                      reply_markup = InlineKeyboardMarkup(HELP_START),
   )

@bot.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    vickdb = MongoClient(MONGO_URL)
    vick = vickdb["VickDb"]["Vick"]
    if query.data == "HELP":
        await query.message.edit_text(
                      text = HELP_READ,
                      reply_markup = InlineKeyboardMarkup(HELP_BTN),
                      disable_web_page_preview=True,
     )
    elif query.data == "CLOSE":
            await query.message.delete()
    elif query.data == "BACK":
            await query.message.edit(
                  text = START,
                  reply_markup=InlineKeyboardMarkup(DEV_OP),
     )
    elif query.data == "SOURCE":
            await query.message.edit(
                   text = SOURCE_READ,
                   reply_markup = InlineKeyboardMarkup(BACK),
                   disable_web_page_preview = True,

     )
    elif query.data == "ABOUT":
            await query.message.edit(
                    text = ABOUT_READ,
                    reply_markup = InlineKeyboardMarkup(ABOUT_BTN),
                    disable_web_page_preview=True,
     )
    elif query.data == "ADMINS":
            await query.message.edit(
                    text = ADMIN_READ,
                    reply_markup = InlineKeyboardMarkup(MUSIC_BACK_BTN), 
     )
    elif query.data== "TOOLS_DATA":
            await query.message.edit(
                    text= TOOLS_DATA_READ,
                    reply_markup = InlineKeyboardMarkup(CHATBOT_BACK),
     )
    elif query.data == "BACK_HELP":
            await query.message.edit(
                    text = HELP_READ,
                    reply_markup = InlineKeyboardMarkup(HELP_BTN),
     )
    elif query.data == "CHATBOT_CMD":
            await query.message.edit(
                    text = CHATBOT_READ,
                    reply_markup = InlineKeyboardMarkup(CHATBOT_BACK), 
     )
    elif query.data == "CHATBOT_BACK":
            await query.message.edit(
                    text = HELP_READ,
                    reply_markup = InlineKeyboardMarkup(HELP_BTN), 
     )
    elif query.data == "addchat":
        if query.from_user.id not in (await is_admins(query.message.chat.id)):
            return query.answer(
                "You don't have permissions to do this baby.",
                show_alert=True,
            )
        else:
            is_vick = vick.find_one({"chat_id": query.message.chat.id})
            if not is_vick:           
                await query.edit_message_text(f"**α΄Κα΄α΄-Κα΄α΄ α΄ΚΚα΄α΄α΄Κ α΄Ι΄α΄ΚΚα΄α΄.**")
            if is_vick:
                vick.delete_one({"chat_id": query.message.chat.id})
                await query.edit_message_text(f"**α΄Κα΄α΄-Κα΄α΄ α΄Ι΄α΄ΚΚα΄α΄ ΚΚ** {query.from_user.mention}.")
    elif query.data == "rmchat":
        if query.from_user.id not in (await is_admins(query.message.chat.id)):
            return query.answer(
                "**Κα΄α΄ α΄α΄Ι΄'α΄ Κα΄α΄ α΄ α΄α΄Κα΄s α΄α΄ α΄α΄ α΄ΚΙͺs Κα΄ΚΚ!**",
                show_alert=True,
            )
        else:
            is_vick = vick.find_one({"chat_id": query.message.chat.id})
            if not is_vick:
                vick.insert_one({"chat_id": query.message.chat.id})
                await query.edit_message_text(f"**α΄Κα΄α΄-Κα΄α΄ α΄Ιͺsα΄ΚΚα΄α΄ ΚΚ** {query.from_user.mention}.")
            if is_vick:
                await query.edit_message_text("**α΄Κα΄α΄-Κα΄α΄ α΄ΚΚα΄α΄α΄Κ α΄Ιͺsα΄ΚΚα΄α΄.**")
                            
@bot.on_message(filters.command("repo"))
async def repo(client, message):
    await message.reply_text(
                   text= SOURCE_READ,
                   reply_markup = InlineKeyboardMarkup(CLOSE_BTN),
                   disable_web_page_preview = True,
      )
@bot.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["+", ".", "/", "-", "?", "$"]))
async def restart(client, m: Message):
    if m.chat.type == "private":
        hmm = await m.reply_photo(
                            photo = random.choice(PHOTO),
                            caption = HELP_READ,
                            reply_markup= InlineKeyboardMarkup(HELP_BTN),
        )
    else:
        await m.reply_photo(
                      photo = random.choice(PHOTO),
                      caption = "**Κα΄Κ, α΄α΄ α΄α΄ ?α΄Κ Κα΄Κα΄ α΄α΄α΄α΄α΄Ι΄α΄s!**",
                      reply_markup = InlineKeyboardMarkup(HELP_BUTN),
      )


@bot.on_message(filters.command("ping", prefixes=["+", "/", "-", "?", "$", "&"]))
async def ping(client, message: Message):
    await message.delete()
    start = datetime.now()
    wtfbhemchomd = await message.reply_sticker(
                       sticker= random.choice(STICKER),
    )
    end = datetime.now()
    ms = (end-start).microseconds / 1000
    await message.reply_photo(
        photo=random.choice(PHOTO),
        caption=f"Π½ey Π²Ξ±Π²Ρ!!\n**[{BOT_NAME}](t.me/{BOT_USERNAME})** ΞΉΡ alΞΉve π₯ Ξ±nd worΔΈΞΉng ?ΞΉne wΞΉΡΠ½ a pΞΉng o?\nβ₯ `{ms}` ms\n\n<b>||ΠΌΞ±dΡ ΟΞΉΡΠ½ β£οΈ Π²Ρ [α evπ](https://t.me/Mr_Nihal9)||</b>",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )

                  
@bot.on_message(
    filters.command(["chatbot", f"chatbot@{BOT_USERNAME}"])
    & ~filters.private)
async def chatonoff(client: Client, message: Message):
    if not message.from_user:
        return
    else:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (await is_admins(chat_id)):
            return await message.reply_text(
                "**Κα΄α΄ α΄Κα΄'Ι΄α΄ α΄Ι΄ α΄α΄α΄ΙͺΙ΄.**"
            )
        else:
            await message.reply_text(
            text="Β» <u>**α΄Κα΄α΄sα΄ α΄Ι΄ α΄α΄©α΄Ιͺα΄Ι΄ α΄α΄ α΄Ι΄α΄ΚΚα΄/α΄Ιͺsα΄ΚΚα΄ α΄Κα΄α΄Κα΄α΄.**</u>",
            reply_markup=InlineKeyboardMarkup(CHATBOT_ON),
        )


@bot.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.bot,
)
async def vickai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})
       if not is_vick:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})    
       getme = await bot.get_me()
       bot_id = getme.id                             
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_vick:                   
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})    
               

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.bot,
)
async def vickstickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})
       if not is_vick:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})
       getme = await bot.get_me()
       bot_id = getme.id
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_vick:                    
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
               


@bot.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.bot,
)
async def vickprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
       

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.bot,
)
async def vickprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")

print(f"{BOT_NAME} Ιͺs α΄ΚΙͺα΄ α΄! Ι΄α΄α΄‘ ?α΄α΄α΄ α΄??! α΄Ι΄α΄ Ι’α΄ α΄α΄ @Wα΄_Κ?ΚΙͺα΄Ι΄α΄s ΚΙͺα΄α΄Κ!!")      
bot.run()
