#-*- coding: UTF-8 -*- 
from flask import Flask, render_template, request, redirect, url_for, abort, session,jsonify
import mysql_manager
import DataManager.GetRepoInfo
import Evaluate


app = Flask(__name__)
app.config['SECRET_KEY'] = 'F34TF$($e34D';
app.debug=True
tasks = [
    {
        'id': 1,
        'title': u'OSPA',
        'description': u'This is ospaf-api test', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Garvin',
        'description': u'I am garvin', 
        'done': False
    }
]
@app.route('/')
def home():
   #mysql_manager.sql_connect()
    
   return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    #session['username'] = request.form['username']
    session['message'] = request.form['message']
    return redirect(url_for('message'))

@app.route('/message')
def message():
    
  try:    
    return render_template('resume.html', message=DataManager.GetRepoInfo.GetRepoInfo((session['message'])),message_user=session['message'],message_score=Evaluate.get_score(session['message']))
  except EnvironmentError:
   	return render_template('index.html')

@app.route('/ospaf', methods=['GET'])
def ospaf():
    return jsonify({'tasks': tasks})
from bae.core.wsgi import WSGIApplication  
application = WSGIApplication(app)  

# if __name__ == '__main__':
#     app.run()
