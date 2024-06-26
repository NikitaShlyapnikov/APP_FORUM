# app/models.py

from app import db
from datetime import datetime

class Thread_Message(db.Model):
    __tablename__ = 'thread_message'
    id = db.Column(db.Integer, primary_key=True) # id ветки в БД
    chat_id = db.Column(db.String(255), nullable=False) # номер ветки в чате - от 1 до 1000 
    thread_id = db.Column(db.String(255), nullable=False) # id суперчата
    thread_name = db.Column(db.String(255), nullable=False) 

    def __repr__(self):
        return f'<Thread {self.thread_name}>'

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thread_id = db.Column(db.Integer, db.ForeignKey('thread_message.id'), nullable=False) #номер строки в таблице
    message_id = db.Column(db.Integer)
    text = db.Column(db.Text)
    date_sent = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Message {self.id}>'
