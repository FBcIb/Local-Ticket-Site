from flask import render_template, flash
from app import app, db
from app.forms import TicketForm
from app.models import Ticket

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
@app.route('/tickets', methods = ['GET', 'POST'])
def home():
    form = TicketForm()
    if form.validate_on_submit():
        ticket = Ticket(requester=form.requester.data, request=form.request.data, urgency=form.urgency.data)
        db.session.add(ticket)
        db.session.commit()
        flash('Your ticket has been sent')
    return render_template('tickets.html', title='Home', form=form)