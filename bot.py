from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

# Контент для дней
COURSE_CONTENT = {
    1: "День 1: Добро пожаловать в курс! [Ссылка на материал](https://example.com/day1)",
    2: "День 2: Второй день обучения! [Ссылка на материал](https://example.com/day2)",
    3: "День 3: Вот материал третьего дня! [Ссылка](https://example.com/day3)",
    # Добавьте остальные дни...
    21: "День 21: Финальный день! [Ссылка](https://example.com/day21)"
}

# Полезные ссылки
USEFUL_LINKS = {
    "Бады": "https://example.com/bady",
    "Программы для тренеров": "https://example.com/programs",
    "Чтение и исследования": "https://example.com/reading"
}

# Функция для команды /start
async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Основная информация", callback_data="info")],
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
    info_text = "Здесь будет информация о курсе. Вы можете добавить любые данные, например, цели курса, описание и т.д."
    keyboard = [[InlineKeyboardButton("Главное меню", callback_data="back_to_main")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.callback_query.message.reply_text(info_text, reply_markup=reply_markup)

# Функция для отображения материалов курса (с кнопками для каждого дня)
async def show_course_materials(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton(f"День {i}", callback_data=f"day_{i}") for i in range(1, 8)], # Кнопки с 1 по 7 день
        [InlineKeyboardButton(f"День {i}", callback_data=f"day_{i}") for i in range(8, 15)], # Кнопки с 8 по 14 день
        [InlineKeyboardButton(f"День {i}", callback_data=f"day_{i}") for i in range(15, 22)], # Кнопки с 15 по 21 день
        [InlineKeyboardButton("Главное меню", callback_data="back_to_main")]  # Кнопка назад
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text("Выберите день:", reply_markup=reply_markup)

# Функция для отображения полезных ссылок
async def show_useful_links(update: Update, context: CallbackContext) -> None:
    links_text = "\n".join([f"{key} - [Ссылка]({url})" for key, url in USEFUL_LINKS.items()])
    keyboard = [[InlineKeyboardButton("Главное меню", callback_data="back_to_main")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text(links_text, reply_markup=reply_markup, parse_mode="Markdown")

# Функция для отображения информации о выбранном дне
async def show_day_content(update: Update, context: CallbackContext) -> None:
    day = int(update.callback_query.data.split("_")[1])  # Извлекаем номер дня
    content = COURSE_CONTENT.get(day, "Контент для этого дня пока не готов.")
    
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
