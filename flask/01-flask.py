from flask import Flask
from flask import Response,Request


app = Flask(__name__)

@app.route('/')
def hello_word():

    # for x,y in Request.__dict__.items():
    #     print(x,':',y)
    return 'Hello,Word'


@app.route('/user/<username>')
def show_user_profile(username):

    return '%s' % username


if __name__ == '__main__':
    app.run(debug=True)