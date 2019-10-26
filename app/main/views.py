from flask import render_template,request,redirect,url_for
from flask_login import login_required
from . import main



#views
@main.route('/')
def index():
    hello="hello world"
    return render_template('index.html', title= 'pitch site', hello=hello)

@main.route('/pitch/comments/new/<int:id>', methods = ['GET','POST'])
@login_required
def comment(id):
    pass    
