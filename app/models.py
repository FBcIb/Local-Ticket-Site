from app import db

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    requester = db.Column(db.String(64), index=True, unique=False)
    request = db.Column(db.String(160), index=True, unique=True)
    urgency = db.Column(db.Boolean, index=True, unique=False, default=False)

    def __repr__(self):
        if self.urgency:
            return '<{} has the following urgent issue: {}>'.format(self.requester, self.request)
        else:
            return '<{} has the following issue: {}>'.format(self.requester, self.request)