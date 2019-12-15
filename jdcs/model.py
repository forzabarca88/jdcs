from jdcs.app import db


class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(128), nullable=False)
    receiver = db.Column(db.String(128), nullable=False)
    subject = db.Column(db.String(128))
    body = db.Column(db.String(2048))
    latest_action_date = db.Column(db.DateTime, nullable=False)
    sent = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return 'ID: {} \nFrom: {} \nTo: {} \nSubject: {} \nSent?: {}'.format(
            self.id,
            self.sender,
            self.receiver,
            self.subject,
            self.sent
        )