# from flask import Flask
# app = Flask(__name__)

# @app.route("/")

# def index():
#     return "<h1>hiii sparsh agarwal 1</h1>"

# if __name__ =='__main__':
#     app.run()

#-----------------------------------------------------------

# @app.route('/')
# def index():
#     browser_info = request.headers.get('User-Agent')
#     return f'<h2> here is your browser info</h2> <p> {browser_info}</p>' 

# @app.route('/info')
# def info():
#     return "<h2> flask is easy to learn</h2>"


# @app.route('/user/<name>')
# def user(name):
#     return f"<h1> this is a page for user:{name.upper()}</h1>"


# @app.route('/user_latin/<name>')
# def userlatin(name):

#     if name[-1] =='y':
#         username = name[:-1] + 'iful'
#     else:
#         username = name + 'y'
    
#     return f"<h1> Hi {name}!  your user latin name is {username}</h1>"

# -----------------------------------------------------------------------

# from flask import Flask
# from flask import request
# from flask import render_template

# app = Flask(__name__)


# @app.route('/')
# def index():
#     return f'<h2>Welcome to URL Shortner!!!</h2>' 

# @app.route('/test')
# def hello(name= None):
#     return render_template('index.html',name)

# def url_shortner(url):
#     d = dict()
#     map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#     import random
#     st = 'goggle'
#     map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#     surl =str()
#     temp = random.randint(97,121)
#     id =12345
#     while(id>0):
#         surl += map[id%temp]
#         #print(surl)
#         id //=temp
#     d[url]=surl
#     return surl

# @app.route('/url', methods = ["GET","POST"])
# def url():
#     if request.method =="POST":
#         name = request.form.get("name")
#         url = request.form.get("url")
#         #d = dict()
#         short_url  = url_shortner(url)
        
#         return f"hii {name} your url is <a href="{url}> {short_url}"

#     return render_template('index.html')

# if __name__ =='__main__':
#     app.run(debug =True)
#-----------------------------------------------------------------------

# from flask import Flask
# from flask import request
# from flask import render_template
# from flask import redirect, url_for

# app = Flask(__name__)
# @app.route('/')
# def hello():
#     return "<h1> Hellooo</h1>"

# @app.route('/developer')
# def dev_user():
#     return f'<h1> Hiii developer</h1>'

# @app.route('/qa/<qa>')
# def qa_user(qa):
#     return f'<h1> hiiii {qa} working as qa</h1>'

# @app.route('/user/<name>')
# def hello_user(name):
#     if name == 'developer':
#         return redirect(url_for('developer'))
#     elif name == 'qa':
#         return redirect(url_for('qa'))
# @app.route('/i', methods = ["GET","POST"])
# def disp():
#     return render_template('index.html')

# @app.route('/url', methods = ["GET","POST"])
# def url():
#     # if request.method =="POST":
#     #     name = request.form.get("name")
#     #     dept = request.form.get("dept")
#     #     return f"hii {name} your department is {dept}"

#     return render_template('index.html')
# from flask import Flask
# from flask import request
# from flask import render_template
# from flask import redirect, url_for

# app = Flask(__name__)
# @app.route('/')
# def hi():
#     return 'Hi everyone!'
# @app.route('/home')
# def hello_user():
#     return render_template('index.html')

# @app.route('/form')
# def form():
#     return render_template('form.html')
# @app.route('/thankyou')
# def thankyou():
#     first = request.args.get('first')
#     last = request.args.get('last')
#     return render_template('thankyou.html',first=first, last=last)
    

# if __name__ =='__main__':
#     app.run(debug =True)
