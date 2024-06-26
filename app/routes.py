import asyncio
import threading
from flask import render_template, request, redirect, url_for, flash
from app.forms import MessageForm, ThreadSelectForm
from app.models import Message, Thread_Message
from app import db, app
import telegram

# Initialize Telegram bot
bot_token = '7205789185:AAHeNPxbKoEq8ekym7ODnERfc6CZDRJx29M'
bot = telegram.Bot(token=bot_token)

async def send_message_to_telegram(chat_id, message_text, message_thread_id):
    message = await bot.send_message(chat_id=chat_id, text=message_text, message_thread_id = message_thread_id)
    return message.message_id

def send_telegram_message_async(chat_id, message_text, message_thread_id):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(send_message_to_telegram(chat_id, message_text, message_thread_id))

from flask import request

@app.route('/', methods=['GET', 'POST'])
def index():
    message_form = MessageForm()
    thread_form = ThreadSelectForm()

    if message_form.validate_on_submit():
        message_text = message_form.message.data
        thread_id = request.form.get('thread_id')  # Получаем thread_id из формы
        try:
            chat_id = '-1002189429912'  # Замените на ваш реальный chat_id
            message_id = send_telegram_message_async(chat_id, message_text, thread_id)
            # Пример добавления сообщения в базу данных
            thread_message = Thread_Message.query.filter_by(chat_id=chat_id, thread_id=thread_id).first()
            new_message = Message(thread_id=thread_message.id, text=message_text, message_id=message_id)
            db.session.add(new_message)
            db.session.commit()
            
            flash('Сообщение успешно отправлено!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Ошибка отправки сообщения: {str(e)}', 'error')
            return redirect(url_for('index'))

    if thread_form.validate_on_submit():
        thread_id = thread_form.thread.data
        flash(f'Вы выбрали чат с ID {thread_id}', 'info')
        return redirect(url_for('index'))

    thread_form.thread.choices = [(str(thread.thread_id), thread.thread_name) for thread in Thread_Message.query.all()]

    return render_template('index.html', message_form=message_form, thread_form=thread_form)

if __name__ == '__main__':
    app.run(debug=True)


