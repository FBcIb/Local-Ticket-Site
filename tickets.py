from app import app, db
from app.models import Ticket

app = app

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Ticket': Ticket}