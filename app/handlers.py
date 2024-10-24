from gc import callbacks
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import webbrowser

import app.keyboard as kb 
import app.database.requests as rq

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer(f'<em>Здравствуйте {message.from_user.first_name}! Добро пожаловать в магазин комплектующих для пк! Что вас интересует?</em>', parse_mode='html', reply_markup=kb.main)

@router.message(Command('site', 'website'))
async def site(message: Message):
    await rq.set_user(message.from_user.id)
    webbrowser.open('https://specpcshop.pkp.kz/')
    
@router.message(F.text == 'О нас')
async def about_us(message: Message):
    await message.answer('<em>Мы - интернет магазин специализирующийся на продаже комплектующих и аксессуаров для пк.\nУ нас вы можете купить нужный вам товар по низкой стоимости и по выгодным предложением</em>',
                         parse_mode='html', reply_markup=kb.main)
    
@router.message(F.text == 'Контакты')
async def contacts(message: Message):
    await message.answer('<em><b>Контакты:\nНомер телефона: +7705-886-49-66\nEmail: specpcshop73@gmail.com\nInstagram: specpcshop73</b></em>',
                         parse_mode='html', reply_markup=kb.main)

@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите категорию товара', reply_markup=await kb.categories())

@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите товар по категории',
                                  reply_markup=await kb.items(callback.data.split('_')[1]))

@router.callback_query(F.data.startswith('item_'))
async def category(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer('Вы выбрали товар')
    await callback.message.answer(f'Название: {item_data.name}\nОписание: {item_data.description}\nЦена: {item_data.price}тг')
