from flask import Flask, render_template, request
from flask_mail import Mail, Message
from random import randint
from flask import Blueprint
from ..extensions import create_app

app = create_app()

mail = Mail(app)

otp = randint(000000,999999)

auth = Blueprint('auth', __name__, url_prefix='/auth', template_folder='./templates')


@auth.route('/signup')
def index():
    return render_template("verify.html")

@auth.route('/verify',methods = ["POST"])
def verify():
    email = request.form["email"]
    msg = Message('OTP',sender = 'username@gmail.com', recipients = [email])
    msg.body = str(otp)
    mail.send(msg)
    return render_template('verify.html')

@auth.route('/validate',methods=["POST"])
def validate():
    user_otp = request.form['otp']
    if otp == int(user_otp):
        return "<h3> Email verification is successful </h3>"
    return "<h3>failure, OTP does not match</h3>"


if __name__ == '__main__':
    app.run(debug = True)