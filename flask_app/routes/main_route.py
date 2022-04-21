from flask import Blueprint, render_template, request, redirect, url_for
from flask_app.utils.main_func import get_lotto
from flask_app import mongodb
from flask_app.models.model import Users
import datetime
from flask import Flask, render_template 
import mongodb


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
        return render_template('main.html'), 200

@app.route('/predict', methods=['POST', 'GET'])
def predict():

    data = get_lotto(1)
    return render_template('predict.html',  data=data)


@app.route('/tolist', methods=['GET','POST'])
def tolist():
    if request.method == 'POST':
        
        task_content = request.form['content']
        now = datetime.datetime.today().strftime("%Y%m%d") 

        if not task_content:
            tasks = Users.query.order_by(Users.date).all()
            return render_template('alert.html')
        else:
            new_task = Users(date=now, num=task_content)

            mongodb.session.add(new_task)
            mongodb.session.commit()
            tasks = Users.query.order_by(Users.date).all()
            return render_template('tolist.html', tasks=tasks)
    else:

        tasks = Users.query.order_by(Users.date).all()
        return render_template('tolist.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Users.query.get_or_404(id)


    mongodb.session.delete(task_to_delete)
    mongodb.session.commit()
    return redirect('/tolist')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Users.query.get_or_404(id)

    if request.method == 'POST':
        task.num = request.form['content']


        mongodb.session.commit()
        return redirect('/tolist')
    
    else:
        return render_template('update.html', task=task)