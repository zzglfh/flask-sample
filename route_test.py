from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return 'home page'

@app.route('/hello')
def hello():
    return 'Hello World'


@app.route('/user/<username>')
def user(username):
    return 'your name is %s' % username

@app.route('/id/<int:post_id>')
def post(post_id):
    return 'posy_id is  %s' %  post_id


if __name__ == '__main__':
    #app.run(host='0.0.0.0')
    with app.test_request_context():
        print  url_for('home')
        print  url_for('hello')
        print url_for('user',username='zzg')
        print url_for('post',post_id=3)