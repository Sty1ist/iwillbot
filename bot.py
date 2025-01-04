from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext


# Контент программы курса
COURSE_PROGRAM = [
    ("Перезагрузка – первый шаг к новой жизни", [
        "• Приветствие от Mariprovans",
        "• Онлайн тренировка с Владиславой 9:00 (Киев)",
        "• Видео от Юкаса"
    ]),
    ("Пробуждение – открываем внутреннюю энергию", [
        "• Тренировка по стрейчингу с Ириной"
    ]),
    ("Шаг вперёд – движение к осознанным изменениям", [
        "• Фитнес тренировка с Владиславой",
        "• Видео на тему что такое целлюлит от Анастасии"
    ]),
    ("Импульс – ускоряемся на пути к цели", [
        "• Тренировка от Ирины (стретчинг, запись)",
        "• Сет тренировок от Юкаса"
    ]),
    ("Гармония – находим баланс между телом и разумом", [
        "• Тренировка от Влады (ноги + ягодицы, запись)",
        "• Лекция от Анастасии (массажист): “Помогает ли массаж в борьбе с целлюлитом?”"
    ]),
    ("Сила воли – формируем привычки победителя", [
        "• 10:30 (по Киеву) – онлайн тренировка с Ириной.",
        "• 19:00 (по Киеву) – эфир “Ваша точка А: где вы сейчас?” с Инной нумерологом."
    ]),
    ("Выход за пределы – преодолеваем внутренние барьеры", [
        "• Видео: массаж лица от Екатерины косметолога - массажиста"
    ]),
    ("Лёгкость бытия – ощущаем результат первых усилий", [
        "• 9:00 (по Киеву) – онлайн-тренировка с Владой (все группы мышц).",
        "• Мотивация на неделю от Юкаса",
        "• Уход за кожей лица и тела во время похудения от практикующего косметолога Екатерины"
    ]),
    ("Ощущение успеха – фиксируем первые достижения", [
        "• Тренировка от Ирины (запись).",
        "• Лекция от Анастасии (массажист): “Как использовать сухую щётку в массаже”."
    ]),
    ("Новое дыхание – переосмысливаем себя и свои цели", [
        "• Тренировка от Влады (руки + плечи).",
        "• Лекция от Екатерины массаж лица"
    ]),
    ("Энергия перемен – подпитываем мотивацию", [
        "• Тренировка в записи стретчинг с Ириной."
    ]),
    ("Фокус на себя – концентрируемся на главном", [
        "• Тренировка от Влады (пирамида, запись).",
        "• Основы самообороны от Юкаса",
        "• Лекция от Анастасии (массажист)."
    ]),
    ("Сила привычек – закладываем основу на будущее", [
        "• 10:30 (по Киеву) – онлайн-тренировка с Ириной.",
        "• Лекция от Екатерины (косметолог): “Дефициты в анализах и их влияние на организм при похудении”.",
        "• Онлайн Лекция 19:00 по Киеву, от Инны (нумеролог): “Куда вы сливаете свою энергию?”."
    ]),
    ("Ритм движения – находим свой темп", []),
    ("Подъём – ещё ближе к вершине", [
        "• 9:00 (по Киеву) – онлайн-тренировка с Владой.",
        "• Мотивация от Юкаса.",
        "• Прямой эфир 18:00 по Киеву от Марии (нутрициолог)."
    ]),
    ("Вдохновение – черпаем силы из окружения и успехов", [
        "• Тренировка от Ирины (запись)."
    ]),
    ("Горжусь собой – фиксируем внутренние и внешние победы", [
        "• Тренировка от Влады (попа + пресс, запись).",
        "• Видео: массаж лица от Екатерины."
    ]),
    ("Шаг уверенности – финальная проверка своих сил", [
        "• Тренировка от Ирины (запись)."
    ]),
    ("Светлая точка – видим результат своей работы", [
        "• Тренировка от Влады (запись).",
        "• Лекция от Анастасии (массажист)."
    ]),
    ("Новая вершина – закрепляем успех", [
        "• 10:30 (по Киеву) – онлайн-тренировка с Ириной.",
        "• Общие рекомендации от Екатерины (косметолог).",
        "• Онлайн встреча в 19:00 по Киеву с Инной нумерологом Где брать вдохновение по дате рождения ?"
    ])
]


# Функция для отображения программы курса
async def show_course_program(update: Update, context: CallbackContext) -> None:
    program_text = "\n\n".join([f"*{item[0]}*\n" + "\n".join(item[1]) for item in COURSE_PROGRAM])
    keyboard = [[InlineKeyboardButton("Главное меню", callback_data="back_to_main")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text(program_text, reply_markup=reply_markup, parse_mode="Markdown")

# Контент для дней (с заголовками, текстом и видео-ссылками)
COURSE_CONTENT = {
    1: {
        "title": "День 1: “Перезагрузка” – первый шаг к новой жизни",
        "text": "Сегодня мы начнем наш путь!",
        "video_links": [
            {"title": "Приветствие от Mariprovans", "url": "https://www.youtube.com/watch?v=ORw5yMbVDy8"},
            {"title": "Онлайн тренировка с Владиславой 9:00 (Киев)", "url": "https://www.youtube.com/watch?v=BWPVQQ-YT6k&embeds_referring_euri=https%3A%2F%2Fiwillcourse.com%2F&source_ve_path=Mjg2NjY"},
            {"title": "Приветствие от Юкаса", "url": "https://www.youtube.com/watch?v=WpMg7HWWbq4&t=1s"}
        ]
    },
    2: {
        "title": "День 2: Важные аспекты похудения",
        "text": "Сегодня мы обсудим важнейшие аспекты похудения, включая питание и тренировки.",
        "video_links": [
            {"title": "Видео 1: Как похудеть правильно", "url": "https://example.com/video3"},
            {"title": "Видео 2: Ошибки в диетах", "url": "https://example.com/video4"}
        ]
    },
    3: {
        "title": "День 3: Режим питания и тренировок",
        "text": "Сегодня мы подробно поговорим о правильном режиме питания и тренировок для похудения.",
        "video_links": [
            {"title": "Видео 1: Правильное питание", "url": "https://example.com/video5"},
            {"title": "Видео 2: Эффективные тренировки", "url": "https://example.com/video6"}
        ]
    },
    # Добавьте остальные дни...
    21: {
        "title": "День 21: Финальный день!",
        "text": "Поздравляю! Мы подошли к завершению курса. В этом видео подведем итоги.",
        "video_links": [
            {"title": "Видео 1: Итоги курса", "url": "https://example.com/video20"}
        ]
    }
}

# Полезные ссылки
USEFUL_LINKS = {
    "Топ полезных завтраков 🥑 🍳": "https://iwillcourse.com/zavtrak.pdf",
    "Как сдвинуть вес с места 💪 ⚖️": "https://iwillcourse.com/kak-sdvinut.pdf",
    "Масло: как выбрать 🧈 🤔": "https://iwillcourse.com/maslo.pdf",
    "Спортивное питание на жиросжигании 🏋️‍♀️ 🔥": "https://iwillcourse.com/sport-pit.pdf",
    "Овощи 🥦 🍅": "https://iwillcourse.com/ovoschi.pdf",
    "Женский цикл 🌸 🩸": "https://iwillcourse.com/jenskiy.pdf",
    "Основы питания 🥗 🍽️": "https://iwillcourse.com/osnovi.pdf",
    "Иммунитет 💪🛡️": "https://iwillcourse.com/imunka.pdf",
    "План по питанию 📅 🥗": "https://iwillcourse.com/pitanie.pdf",
    "Эффект плато 🛑": "https://iwillcourse.com/plato.pdf",
    "Дневник от I Will 📓 ✍️": "https://iwillcourse.com/dneevnik.pdf",
    "БАДы 💊 🌱": "https://iwillcourse.com/badi.pdf"
}

# Функция для команды /start
async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Основная информация", callback_data="info")],
        [InlineKeyboardButton("Программа курса", callback_data="course_program")],
        [InlineKeyboardButton("Материалы курса", callback_data="course_materials")],
        [InlineKeyboardButton("Полезные ссылки", callback_data="useful_links")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Используем message из callback_query, если это не командный запрос
    if update.message:
        await update.message.reply_text("Выберите раздел:", reply_markup=reply_markup)
    else:
        await update.callback_query.message.reply_text("Выберите раздел:", reply_markup=reply_markup)

# Функция для отображения основной информации
async def show_info(update: Update, context: CallbackContext) -> None:
    info_text = "Рады Вас приветствовать!\n\nПриглашаю вас в мой 21-дневный курс это путешествие к новой версии себя. \nЯ сама прошла через этот путь и знаю, как бывает непросто. Но вместе мы справимся! Это будет не идеализированная история, а реальный опыт, с поддержкой, вдохновением и юмором.\n Я сбросила почти 20 кг и хочу помочь вам сделать то же самое. Этот курс подойдёт не только тем, кто мечтает похудеть, но и каждой девушке, которая хочет почувствовать перемены и привести тело в порядок.\n\n Новый год — отличная возможность для новой жизни. И, чтобы было ещё интереснее, в конце курса я выберу лучшую участницу и награжу её особым призом! "
    keyboard = [[InlineKeyboardButton("Главное меню", callback_data="back_to_main")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.callback_query.message.reply_text(info_text, reply_markup=reply_markup)

# Функция для отображения материалов курса (с кнопками для каждого дня)
async def show_course_materials(update: Update, context: CallbackContext) -> None:
    keyboard = [
        # [InlineKeyboardButton(f"День {i}", callback_data=f"day_{i}") for i in range(1, 2)], # Кнопки с 1 по 7 день
        [InlineKeyboardButton(f"День {i}", callback_data=f"day_{i}") for i in range(1, 4)],
        [InlineKeyboardButton(f"День {i}", callback_data=f"day_{i}") for i in range(4, 7)], # Кнопки с 1 по 7 день
        [InlineKeyboardButton(f"День {i}", callback_data=f"day_{i}") for i in range(7, 10)], # Кнопки с 8 по 14 день
        [InlineKeyboardButton(f"День {i}", callback_data=f"day_{i}") for i in range(10, 13)], # Кнопки с 15 по 21 день
        [InlineKeyboardButton(f"День {i}", callback_data=f"day_{i}") for i in range(13, 16)], # Кнопки с 15 по 21 день
        [InlineKeyboardButton(f"День {i}", callback_data=f"day_{i}") for i in range(16, 19)], # Кнопки с 15 по 21 день
        [InlineKeyboardButton(f"День {i}", callback_data=f"day_{i}") for i in range(19, 22)], # Кнопки с 15 по 21 день
        [InlineKeyboardButton("Главное меню", callback_data="back_to_main")]  # Кнопка назад
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text("Выберите день:", reply_markup=reply_markup)

# Функция для отображения полезных ссылок
async def show_useful_links(update: Update, context: CallbackContext) -> None:
    links_text = "\n".join([f"[{key}]({url})" for key, url in USEFUL_LINKS.items()])
    keyboard = [[InlineKeyboardButton("Главное меню", callback_data="back_to_main")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text(links_text, reply_markup=reply_markup, parse_mode="Markdown")

# Функция для отображения информации о выбранном дне
async def show_day_content(update: Update, context: CallbackContext) -> None:
    day = int(update.callback_query.data.split("_")[1])  # Извлекаем номер дня
    day_content = COURSE_CONTENT.get(day, None)

    if day_content:
        # Формируем текст с заголовком, текстом и ссылками на видео
        content = f"*{day_content['title']}*\n\n{day_content['text']}\n\n"
        for video in day_content['video_links']:
            content += f"[{video['title']}]({video['url']})\n"
    else:
        content = "Контент для этого дня пока не готов."
    
    # Сохраняем текущее состояние
    context.user_data['last_menu'] = 'course_materials'  # Запоминаем, что мы находимся в меню "Материалы курса"
    
    keyboard = [
        [InlineKeyboardButton("Назад", callback_data="back_to_materials")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.edit_text(content, parse_mode="Markdown", reply_markup=reply_markup)

# Функция для обработки нажатия кнопок
async def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "info":
        await show_info(update, context)
    elif query.data == "course_materials":
        await show_course_materials(update, context)
    elif query.data == "useful_links":
        await show_useful_links(update, context)
    elif query.data == "back_to_main":
        await start(update, context)  # Возвращаемся в главное меню
    elif query.data.startswith("day_"):
        await show_day_content(update, context)  # Переходим к контенту выбранного дня
    elif query.data == "course_program":  # Обрабатываем новую кнопку
        await show_course_program(update, context)
    elif query.data == "back_to_materials":
        # Переходим обратно в меню "Материалы курса"
        await show_course_materials(update, context)

# Главная функция
def main():
    # Вставьте ваш токен здесь
    application = Application.builder().token("7065830886:AAGNCiwEcYl5SM7gUbAaBEHzxUghTwOVbrc").build()

    # Обработчики команд и кнопок
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
