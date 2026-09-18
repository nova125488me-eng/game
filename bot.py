from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# توکن رباتت از BotFather را اینجا قرار بده
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    
    # لینک صفحه منوی رنگی که روی سرور قرار داده‌ای
    WEB_APP_URL = "https://your-domain.com/menu.html"
    
    text = (
        f"سلام {user_name} عزیز 👋\n\n"
        f"به **ربات شهربازی امیرعلی** خوش آمدید! 🎡\n\n"
        f"لطفاً از منوی زیر بازی مورد علاقه خود را انتخاب کنید:"
    )
    
    # دکمه‌ای که مینی‌اپ رنگی را داخل چت باز می‌کند
    keyboard = [
        [InlineKeyboardButton("🎮 ورود به شهربازی (منوی بازی‌ها)", web_app=WebAppInfo(url=WEB_APP_URL))]
    ]
    
    await update.message.reply_text(
        text, 
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("ربات شهربازی امیرعلی با موفقیت روشن شد...")
    app.run_polling()