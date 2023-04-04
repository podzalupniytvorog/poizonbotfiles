from pyrogram import Client, filters
from pyrogram.handlers import CallbackQueryHandler, MessageHandler
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton
from pyrogram_patch import patch
from pyrogram_patch.fsm.storages import MemoryStorage
from pyrogram_patch.fsm import StatesGroup, StateItem
from pyrogram_patch.fsm import State
from pyrogram_patch.fsm.filter import StateFilter

_api_id = '8'
_api_hash = '7245de8e747a0d6fbe11f7cc14fcc0bb'
_bot_token = '6205149164:AAG263ZgqOvOdU0vrcGaEDy3isK3kuvFzus'
faq_words = {
    'faq1': '❗️ Для оплаты заказа необходимо произвести перевод на карту, номер которой будет отправлен вам после согласования заказа. После того, как вы произведете оплату, мы совершаем выкуп выбранных вами товаров на Poizon и отправляем вам квитанцию об оплате.',
    'faq2': '❗️ Чтобы понять цену товара на Poizon, необходимо умножить указанную цену в юанях на 12.'
            ' К этой цене добавляется стоимость доставки товара со склада Poizon в Москве на наш склад и наша комиссия, которая составляет 1500 рублей за одну единицу товара. Чтобы доставить товар из Москвы в ваш город, необходимо воспользоваться услугами СДЭК, Боксберри или Почтой России. Стоимость доставки оплачивается вами при получении товара в ПВЗ СДЭК, Боксберри или в Почте России.',
    'faq3': '❗️ Независимо от цены товара, мы предоставляем самые привлекательные условия в России - наша комиссия за каждую единицу товара в заказе составляет всего 1500 рублей. Более того, мы являемся крупным российским агрегатором, что обеспечивает надежность и безопасность совершаемых сделок.',
    'faq4': '❗️ Мы гарантируем, что вы получите оригинальный товар, поскольку Poizon тщательно проверяет подлинность всех вещей в своей лаборатории. Для этого используется 9 уровней проверки, контроля и досмотра, что обеспечивает полную подлинность продукта. Мы гарантируем, что у вас будет доступ к оригинальным товарам, которых нет на российском рынке.',
    'faq5': '❗️ Команда Poizon Family не принимает возврат товара, но мы можем БЕСПЛАТНО оказать помощь по продаже вашей вещи. Для получения более подробной информации о возможных вариантах, пожалуйста, обратитесь к нашем администраторам.',
}


client = Client("Poizonfamily_ROBOT",
                api_id=_api_id,
                api_hash=_api_hash,
                bot_token=_bot_token)

patch_manager = patch(client)

patch_manager.set_storage(MemoryStorage())

class ForCalculator(StatesGroup):
    price = StateItem()
    start = StateItem()

class For_user():
    user_name = None

@client.on_message(filters.command(commands=['start']) & filters.private)
async def welcome(client, message):
    await message.reply(text='Приветствуем вас на сервисе доставки товаров Poizon Family! '
                        'Мы рады помочь вам получить свои покупки быстро и удобно. Желаем приятных покупок!', reply_markup=reply_keyboard)
    await message.reply('Пожалуйста, выберите необходимое действие:', reply_markup=inline_keyboard)

    For_user.user_name = message.from_user.username


@client.on_message(filters.private & StateFilter())
async def home(client: Client,  message):
    if message.text == 'Вернуться в главное меню':
        await welcome(client, message)
        return


@client.on_message(filters.private & StateFilter())
def valid_home(client: Client, message):
    if message.text == 'Вернуться в главное меню':
        return True


reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Вернуться в главное меню'
        )
    ]
], resize_keyboard=True)


example_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Где найти ссылку?',
            callback_data='example_photo'
        )
    ]
    ])

inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='💸 Калькулятор цены',
            callback_data='total'
        )
    ],
    [
        InlineKeyboardButton(
            text='🚛 Оформить заказ',
            callback_data='order'
        )
    ],
    [
        InlineKeyboardButton(
            text='⁉️FAQ',
            callback_data='faq_add_buttons'
        )
    ],
    [
        InlineKeyboardButton(
            text='📆 Сроки доставки',
            callback_data='text_time'
        )
    ],
    [
        InlineKeyboardButton(
            text='🔔 Связаться с администратором',
            callback_data='admins_add_buttons'
        )
    ],
    [
        InlineKeyboardButton(
            text='📌 Отзывы',
            callback_data='review_add_buttons',
        )
    ],
])

keyboard_review = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='✈️ Телеграмм',
            url='https://t.me/+-88ObMD-rLg2MjMy'
        )
    ],
    [
        InlineKeyboardButton(
            text='🌐 ВКонтакте',
            url='https://vk.com/topic-219469694_49081656'
        )
    ],
])

keyboard_admins = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='1️⃣ Администратор',
            url='https://t.me/sellpeace'
        )
    ],
    [
        InlineKeyboardButton(
            text='2️⃣ Администратор',
            url='https://t.me/ryzzzh'
        )
    ],
])

keyboard_faq = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='❔ Как происходит оплата? 💳',
            callback_data='faq1'
        )
    ],
    [
        InlineKeyboardButton(
            text='❔ Из чего складывается цена? 💰💱',
            callback_data='faq2'
        )
    ],
    [
        InlineKeyboardButton(
            text='❔ Сколько стоят ваши услуги? 🚛',
            callback_data='faq3'
        )
    ],
    [
        InlineKeyboardButton(
            text='❔ Что, если приедет не оригинальный товар? ⛔️',
            callback_data='faq4'
        )
    ],
    [
        InlineKeyboardButton(
            text='❔ Как вернуть деньги, если товар не подошел? ↩️',
            callback_data='faq5'
        )
    ],
])


def call_data(data):
    async def filter_data(self, __, call: CallbackQuery):
        return self.data == call.data

    return filters.create(filter_data, data=data)


async def button_home(_, message: Message):
    await message.reply('ff')

async def review_add_button(client: Client, call: CallbackQuery):
    await client.answer_callback_query(call.id)
    await call.message.reply('Отзывы 👇🏻', reply_markup=keyboard_review)


async def command_basic(client: Client, call: CallbackQuery):
    await client.answer_callback_query(call.id)
    await call.message.reply(f'ты нажал на {call.data}')

@client.on_message(filters.private & StateFilter())
async def command_total(client: Client, call: CallbackQuery, state: State):
    await client.answer_callback_query(call.id)
    await call.message.reply(f'Введите сумму в юанях 🇨🇳:')
    await state.set_state(ForCalculator.price)


async def faq_add_buttons(client: Client, call: CallbackQuery):
    await client.answer_callback_query(call.id)
    await call.message.reply('Список наиболее часто задаваемых вопросов и их решения 👇🏻', reply_markup=keyboard_faq)

@client.on_message(filters.private & StateFilter(ForCalculator.price))
async def message_for_total(client: Client, message: Message, state: State):
    while True:
        if message.text == 'Вернуться в главное меню':
            await welcome(client, message)
            break
        try:
            if type(int(message.text)) == int:
                await state.set_state(ForCalculator.price)
                value_before = int(message.text)
                if value_before <= 1500:
                    value = value_before * 12 + 1500
                    await message.reply(f'''Курс юаня - 12

Ваш расчет заказа без учета доставок: {value} руб
- Цена товара на Poizon {value_before * 12} руб.
- Доставка по Китаю 0 руб.
- Доставка до склада в России 600 руб/кг.
- Комиссия сервиса 1500 руб.
- Доставка в ПВЗ по РФ зависит от размера посылки и ее веса.
- Предоплата {value} руб.

Обратите внимание, что расчет считается действительным в течение одного часа, поскольку цены на Poizon изменяются динамически и часто обновляются. Если вы собираетесь оформить заказ через час или позже, вам придется перепроверить цену товара, чтобы получить актуальную информацию.''')
                    break
                else:
                    value = value_before * 12
                    value += value / 10
                    await message.reply(f'''Курс юаня - 12

Ваш расчет заказа без учета доставок: {value} руб
- Цена товара на Poizon {value_before * 12} руб.
- Доставка по Китаю 0 руб.
- Доставка до склада в России 600 руб/кг.
- Комиссия сервиса 10%.
- Доставка в ПВЗ по РФ зависит от размера посылки и ее веса.
- Предоплата {value} руб.

Обратите внимание, что расчет считается действительным в течение одного часа, поскольку цены на Poizon изменяются динамически и часто обновляются. Если вы собираетесь оформить заказ через час или позже, вам придется перепроверить цену товара, чтобы получить актуальную информацию.''')
                    break
        except ValueError:
            await message.reply('Введите корректное значение.')
            break




async def admins_add_buttons(client: Client, call: CallbackQuery):
    await client.answer_callback_query(call.id)
    await call.message.reply('Связь 👇🏻', reply_markup=keyboard_admins)


async def output_faq(client: Client, call: CallbackQuery):
    await client.answer_callback_query(call.id)
    await call.message.reply(f'{faq_words.get(call.data)}')

async def send_photo_example(client: Client, call: CallbackQuery):
    await client.send_photo(For_user.user_name, './photo/photo_example.jpg')

async def text_info_time(client: Client, call: CallbackQuery):
    await client.answer_callback_query(call.id)
    await call.message.reply('''📦 Доставка товара занимает от 15 до 25 дней. 

Почему так? 
1. От 2 до 6 дней — доставка до нашего склада в Китае. 🇨🇳
2. От 7 до 10 дней — доставка до нашего склада в России. 🇷🇺
3. От 3 до 5 дней — Доставка СДЭК, Боксберри, Почта России. Направляем на следующий день после доставки на наш склад.'''
                       )


class Parameters(StatesGroup):
    name = StateItem()
    link = StateItem()
    picture = StateItem()
    price = StateItem()
    size = StateItem()
    city = StateItem()
    user_name = StateItem()










# filters.inline_keyboard &
@client.on_message(filters.private & StateFilter())
async def order_1(client: Client, call: CallbackQuery, state: State):
    await call.message.reply('▫️Укажите наименование товара:')
    await state.set_state(Parameters.name)




@client.on_message(filters.private & StateFilter(Parameters.name))
async def order_2(client: Client, message, state: State):
    if valid_home(client, message):
        await home(client, message)
    else:
        await state.set_data({'name': message.text})
        await message.reply('▫️Отправьте ссылку на товар:', reply_markup=example_keyboard)
        await state.set_state(Parameters.link)


@client.on_message(filters.private & StateFilter(Parameters.link))
async def order_3(client: Client, message, state: State):
    if valid_home(client, message):
        await home(client, message)
    else:
        await state.set_data({'link': message.text})
        await client.send_message(message.chat.id, '▫️Введите цену товара в юанях:')
        await state.set_state(Parameters.price)


@client.on_message(filters.private & StateFilter(Parameters.price))
async def order_4(client: Client, message, state: State):
    if valid_home(client, message):
        await home(client, message)
    else:
        await state.set_data({'price': message.text})
        await client.send_message(message.chat.id, '▫️Введите размер товара:')
        await state.set_state(Parameters.size)



@client.on_message(filters.private & StateFilter(Parameters.size))
async def order_5(client: Client, message, state: State):
    if valid_home(client, message):
        await home(client, message)
    else:
        await state.set_data({'size': message.text})
        await client.send_message(message.chat.id, '▫️Введите город доставки:')
        await state.set_state(Parameters.city)




@client.on_message(filters.private & StateFilter(Parameters.city))
async def order_6(client: Client, message, state: State):
    if valid_home(client, message):
        await home(client, message)
    else:
        await state.set_data({'city': message.text})
        await state.set_data({'user_name': message.from_user.username})
        state_data = await state.get_data()
        iname = state_data['name']
        link = state_data['link']
        # picture = state_data['picture']
        price = state_data['price']
        size = state_data['size']
        city = state_data['city']
        user_name = state_data['user_name']
        await client.send_message(message.chat.id, '''▫️Наименование товара: {}
▫️Скриншот товара: {}
▫️Цена товара в юанях: {}
▫️Размер товара: {}
▫️Город доставки: {}
✅ Ваш заказ принят в обработку. С Вами свяжется администратор. Спасибо! '''.format(iname, link, price, size, city))
        await client.send_message(int(-1001623755264), '''▫️Наименование товара: {}
▫️Скриншот товара: {}
▫️Цена товара в юанях: {}
▫️Размер товара: {}
▫️Город доставки: {}
✅ Имя заказчика: @{}'''.format(iname, link, price, size, city, user_name))

        await state.finish()













client.add_handler(CallbackQueryHandler(order_1, call_data('order')))
client.add_handler(CallbackQueryHandler(send_photo_example, call_data('example_photo')))
client.add_handler(CallbackQueryHandler(text_info_time, call_data('text_time')))
client.add_handler(CallbackQueryHandler(output_faq, call_data('faq1')))
client.add_handler(CallbackQueryHandler(output_faq, call_data('faq2')))
client.add_handler(CallbackQueryHandler(output_faq, call_data('faq3')))
client.add_handler(CallbackQueryHandler(output_faq, call_data('faq4')))
client.add_handler(CallbackQueryHandler(output_faq, call_data('faq5')))
client.add_handler(CallbackQueryHandler(faq_add_buttons, call_data('faq_add_buttons')))
client.add_handler(CallbackQueryHandler(command_total, call_data('total')))
client.add_handler(CallbackQueryHandler(admins_add_buttons, call_data("admins_add_buttons")))
client.add_handler(CallbackQueryHandler(review_add_button, call_data("review_add_buttons")))


client.run()
