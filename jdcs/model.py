from jdcs.main import db
from datetime import datetime


class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_name = db.Column(db.String(64))
    sender = db.Column(db.String(128), nullable=False)
    receiver = db.Column(db.String(128), nullable=False)
    subject = db.Column(db.String(128))
    body = db.Column(db.String(1024))
    latest_action_date = db.Column(db.DateTime, nullable=False,
                                   default=datetime.utcnow)
    sent = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return 'ID: {} \nSender Name: {} \nFrom: {} \nTo: {} \nSubject: {} \nSent?: {}'.format(
            self.id,
            self.sender_name,
            self.sender,
            self.receiver,
            self.subject,
            self.sent
        )

    def commit(self):
        db.session.add(self)
        db.session.commit()

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    static_filepath = db.Column(db.String(64), nullable=False)
    caption = db.Column(db.String(128))

    def __repr__(self):
        return 'Filename: {} \nCaption: {}'.format(
            self.static_filepath,
            self.caption
        )
