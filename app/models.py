# app/models.py

from app import db
from datetime import datetime

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.String(255))  # ID чата в Telegram
    message_id = db.Column(db.Integer)   # ID сообщения в Telegram
    text = db.Column(db.Text)
    date_sent = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Message {self.id}>'
