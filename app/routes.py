import nest_asyncio
nest_asyncio.apply()
from flask import Flask, render_template, request, redirect, url_for, flash
from app.forms import MessageForm
from app.models import Message
from app import db, app
import telegram
import asyncio

async def send_message_to_telegram(chat_id, message_text):
    message = await bot.send_message(chat_id=chat_id, text=message_text)
    return message.message_id


# Initialize Telegram bot
bot_token = '7205789185:AAHeNPxbKoEq8ekym7ODnERfc6CZDRJx29M'
bot = telegram.Bot(token=bot_token)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MessageForm()
    if form.validate_on_submit():
        message_text = form.message.data
        try:
            chat_id = '-1002189429912'  # Replace with your actual chat ID
            message_id = asyncio.run(send_message_to_telegram(chat_id, message_text))
            
            # Save message to database
            new_message = Message(chat_id=chat_id, message_id=message_id, text=message_text)
            db.session.add(new_message)
            db.session.commit()
            
            flash('Message sent successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error sending message: {str(e)}', 'error')
            return redirect(url_for('index'))
    return render_template('index.html', form=form)

@app.route('/messages')
def messages():
    messages = Message.query.all()
    return render_template('messages.html', messages=messages)


# app.py



