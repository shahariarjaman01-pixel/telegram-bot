import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
BINANCE_ID = os.getenv("BINANCE_ID")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🛒 Buy Gemini 18M ($6)", callback_data="buy")]]
    await update.message.reply_text(
        "🔥 Welcome to AI Store Bot\n\nSelect product:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "buy":
        await query.edit_message_text(
            f"📦 Product: Gemini Pro 18 Months\n"
            f"💰 Price: $6\n\n"
            f"💳 Binance Pay ID: {BINANCE_ID}\n\n"
            f"✅ Send TXID after payment to confirm."
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
