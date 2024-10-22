from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                     [KeyboardButton(text='Корзина')],
                                     [KeyboardButton(text='Контакты'), 
                                      KeyboardButton(text='О нас')]],
                           resize_keyboard=True, 
                           input_field_placeholder='Выберите пункт меню...')


catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Комплектующие', callback_data='components')],
    [InlineKeyboardButton(text='Аксессуары', callback_data='accesaccessories')]])

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='отправить номер',
                                                           request_contact=True)]],
                                 resize_keyboard=True)