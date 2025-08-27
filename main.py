import aiogram
import asyncio
import logging

from config import Token
from aiogram import Dispatcher, Bot, F
from aiogram.types import message, ChatMemberUpdated
from aiogram.filters import Command, IS_MEMBER, IS_NOT_MEMBER, ChatMemberUpdatedFilter
from aiogram.handlers import message, chat_member

bot = Bot(token=Token)
dp = Dispatcher()
banned_words = [
    "ставки", "коэфы", "кэфы", "спорт", "профиль", "био", "bio", "|", "загляни"
]



@dp.message(Command("start"))
async def pisun_f6(message: message.Message):
    await message.reply("pisun f6")



dp.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
async def zahod(event: ChatMemberUpdated, bot: Bot):
    await event.answer(f"привет, {event.from_user.full_name}\n\n"
                       f"<i><b>правила этой параши:::</b></i>\n"
                       f"<b>1.</b> Если у тебя имеется какой то вопрос, или же ты обратился сюда по какой то проблеме, пожалуйста, "
                       f"сформулируй свое сообщение как можно граммотнее и как можно четче опиши проблему\n"
                       f"<b>2.</b> Так как большая часть чата состоит из ебаных фриков линуксятников, при неадекватном поведении"
                       f" в вашу сторону, обратитесь к администрации или сразу же к владельцу чата, если один из администраторов окажется фриком\n"
                       f"<b>3.</b>Пожалуйста, постарайтесь сохранять себя в руках и относиться с уважением ко всем участникам чата"
                       f" (в некоторых случаях могут быть свои тонкости, так что это правило хоть и не являтся обязательным, но и"
                       f" в случае чего администратор может сослаться на это правило)\n"
                       f"<b>4.</b> Следует учитывать и тот момент, что администратор тоже может оказаться неправым в какой либо ситуации\n"
                       f"<b>5.</b> В любой непонятной ситуации связанной с ОС всегда приминимо правило с переустановкой системы или установкой линукс-дистрибутива",


                       # f"если у тебя есть какие то вопросы, то для начала выполни следущие пункты:\n1. Убедись что вопрос не тупой\n"
                       # f"2. Погугли хоть чуть чуть информацию по своей проблеме\n3. Сформулируй нормально и четко свой вопрос"
                       parse_mode ="HTML")


@dp.chat_member(ChatMemberUpdatedFilter(IS_MEMBER >> IS_NOT_MEMBER))
async def zahod(event: ChatMemberUpdated, bot: Bot):
    await event.answer(f"{event.from_user.full_name} ушол((((((")



@dp.message()
async def pidori(message: message.Message):
    if message.chat.full_name.lower() != "linux and tux chat":
        await bot.send_message(chat_id=5017631350, text=(f"{message.from_user.full_name}\n{message.from_user.full_name}"
                                                         f"({message.from_user.id}):{message.text}\n\n{message.chat.linked_chat_id}\n"
                                                         f"{message.chat.invite_link}\n{message.chat.id}"))
    elif message.text.lower() == banned_words:
        await bot.send_message(chat_id=5017631350, text="хуйлан обнаруен (по тексту сообщения)")

    elif message.from_user.full_name.lower() == banned_words:
        await bot.send_message(chat_id=5017631350, text="хуйлан обнаружен (по нику)")

    elif message.text.lower() == "windows" :
        await message.reply('я тебя забаню🤑🤑🤑🤑🤑')


async def main ():
    await dp.start_polling(bot)

while True:
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
