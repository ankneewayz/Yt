import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
import yt_dlp

# --- Configuration & Personalization ---
# Replace 'YOUR_BOT_TOKEN_HERE' with the token you got from @BotFather
TOKEN = '8279926139:AAEGKYw2k-wLnBr3nmYPBVzBNZv0JLpN53A'
USER_HANDLE = "@ankneewayz"

# 1. /start Command - Welcome Message
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        f"🚀 Welcome to the Download Bot!\n\n"
        "✨ Send me a YouTube link and I will download it for you in high quality!\n\n"
        f"⚙️ Powered By: {USER_HANDLE}"
    )
    await update.message.reply_text(welcome_text)

# 2. Core Download Function
async def download_file(url, mode):
    # Setting a custom filename with your handle
    out_tmpl = f'nexunx_%(title)s.%(ext)s'
    
    ydl_opts = {
        # Selects best video + best audio merged into mp4, or best audio for mp3
        'format': 'bestvideo+bestaudio/best' if mode == 'mp4' else 'bestaudio/best',
        'outtmpl': out_tmpl,
        'quiet': True,
        'merge_output_format': 'mp4' if mode == 'mp4' else None,
    }
    
    # If user wants MP3, we use FFmpeg to extract audio
    if mode == 'mp3':
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        
        # Adjust extensions after processing
        if mode == 'mp3':
            filename = os.path.splitext(filename)[0] + ".mp3"
        elif mode == 'mp4' and not filename.endswith('.mp4'):
            filename = os.path.splitext(filename)[0] + ".mp4"
            
        return filename

# 3. Handle Incoming YouTube Links
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    if "youtube.com" in url or "youtu.be" in url:
        # Inline buttons for format selection
        keyboard = [
            [InlineKeyboardButton("Download Video 🎬", callback_data=f"vid|{url}")],
            [InlineKeyboardButton("Download Audio MP3 🎵", callback_data=f"aud|{url}")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            f"📥 Link received successfully!\nSelect your preferred format below:",
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text(f"❌ Please send a valid YouTube link to proceed.")

# 4. Handle Button Clicks (Download Process)
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    # Split the callback data to get mode and URL
    data, url = query.data.split("|")
    
    await query.edit_message_text(text=f"⏳ Processing your request on {USER_HANDLE} servers...\nPlease wait a moment.")
    
    try:
        mode = 'mp3' if data == 'aud' else 'mp4'
        file_path = await download_file(url, mode)
        
        # Check if file exists before sending
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                caption_text = f"✅ Downloaded Successfully!\n\n🔹 Bot: {USER_HANDLE}"
                await context.bot.send_document(
                    chat_id=query.message.chat_id, 
                    document=f, 
                    caption=caption_text
                )
            
            # Delete file from server after sending to save space
            os.remove(file_path) 
        else:
            raise Exception("File not found after download.")
            
    except Exception as e:
        print(f"Error details: {e}")
        await query.message.reply_text(f"⚠️ An error occurred. Please ensure the link is public and try again.")