from gc import callbacks
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

import app.keyboard as kb
import app.database.requests as rq

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer('Здравствуйте! Добро пожаловать магазин комплектующих для пк! Что вас интересует?', reply_markup=kb.main)
    
    @router.message(F.text == 'Каталог')
    async def catalog(message: Message):
        await message.answer('Выберите категорию товара', reply_markup=await kb.categories())
        
@router.callback_query(F.data.startswith('category_'))
async def category(callbcak: CallbackQuery):
    await callbacks.answer('Вы выбрали категорию')
    await callbcak.message.answer('Выберите товар по категории',
                                  reply_markup=await kb.items(callbacks.data.split('_')[1]))