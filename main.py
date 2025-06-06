import os, logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from PIL import Image
from io import BytesIO
import requests
from logic import analyze_image

TOKEN = os.environ["BOTTOKEN"]
URL = "https://" + os.environ.get("RENDER_SERVICE_NAME", "quotex-bot") + ".onrender.com"
logging.basicConfig(level=logging.INFO)

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await context.bot.get_file(update.message.photo[-1].file_id)
    img = Image.open(BytesIO(requests.get(file.file_path).content))
    signal, reason = analyze_image(img)

    await update.message.reply_text(f"{signal}\nReason: {reason}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))
    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        webhook_url=f"{URL}/webhook"
    )
