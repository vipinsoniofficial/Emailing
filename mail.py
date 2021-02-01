from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config.update(MAIL_USE_SSL=False,
                  MAIL_USE_TLS=True,
                  MAIL_USERNAME='username',
                  MAIL_PASSWORD='password',
                  MAIL_DEBUG=True)
mail = Mail(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    try:
        msg = Message(subject="Test Email", sender='sender_mail_id',
                      recipients=["receiver_mail_id"],
                      body="This is a test email")

        # attach img with email
        with app.open_resource("img_location") as fp:
            msg.attach("photo1.jpg", "photo1/jpg", fp.read())
        mail.send(msg)
        return 'Mail sent!'
    except Exception as e:
        return e


if __name__ == '__main__':
    app.run(debug=True)
