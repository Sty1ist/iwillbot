from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext
import json

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

    if update.message:
        await update.message.reply_text("Выберите раздел:", reply_markup=reply_markup)
    else:
        await update.callback_query.message.reply_text("Выберите раздел:", reply_markup=reply_markup)

# Функция для обработки нажатий
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
        await start(update, context)
    elif query.data.startswith("day_"):
        await show_day_content(update, context)
    elif query.data == "back_to_materials":
        await show_course_materials(update, context)

# Функции для показа информации
async def show_info(update: Update, context: CallbackContext) -> None:
    info_text = "Здесь будет информация о курсе. Вы можете добавить любые данные."
    keyboard = [[InlineKeyboardButton("Главное меню", callback_data="back_to_main")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text(info_text, reply_markup=reply_markup)

async def show_course_materials(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton(f"День {i}", callback_data=f"day_{i}") for i in range(1, 8)],
        [InlineKeyboardButton(f"День {i}", callback_data=f"day_{i}") for i in range(8, 15)],
        [InlineKeyboardButton(f"День {i}", callback_data=f"day_{i}") for i in range(15, 22)],
        [InlineKeyboardButton("Главное меню", callback_data="back_to_main")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text("Выберите день:", reply_markup=reply_markup)

async def show_useful_links(update: Update, context: CallbackContext) -> None:
    links_text = "\n".join([f"{key} - [Ссылка]({url})" for key, url in USEFUL_LINKS.items()])
    keyboard = [[InlineKeyboardButton("Главное меню", callback_data="back_to_main")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text(links_text, reply_markup=reply_markup, parse_mode="Markdown")

async def show_day_content(update: Update, context: CallbackContext) -> None:
    day = int(update.callback_query.data.split("_")[1])  # Извлекаем номер дня
    content = COURSE_CONTENT.get(day, "Контент для этого дня пока не готов.")
    keyboard = [
        [InlineKeyboardButton("Назад", callback_data="back_to_materials")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.edit_text(content, parse_mode="Markdown", reply_markup=reply_markup)

# Функция для регистрации вебхука
def set_webhook(bot):
    webhook_url = 'https://your-app-name.vercel.app/api/bot'  # Замените на URL вашего развернутого приложения
    bot.set_webhook(webhook_url)

# Функция для работы с вебхуком на Vercel
def handler(request):
    if request.method == "POST":
        json_data = request.json
        update = Update.de_json(json_data, bot)
        application.update_queue.put(update)
    return "ok", 200

def main():
    from telegram import Bot

    TELEGRAM_TOKEN = 'ваш_токен_бота'
    bot = Bot(TELEGRAM_TOKEN)
    set_webhook(bot)

    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    application.run_webhook(listen="0.0.0.0", port=80)

if __name__ == "__main__":
    main()
