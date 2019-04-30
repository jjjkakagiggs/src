from flask import render_template,request,jsonify
import json

from src import app

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mystring')
def mystring():
    return 'my string'


@app.route('/dataFormAjax')
def dataFromAjax():
    test = request.args.get('mydata')
    print(test)
    return 'dataFromAjax'


@app.route('/mydict',methods=['GET','POST'])
def mydict():
    if request.method == 'POST':
        a = request.form['mydata']
        print(a)
    d = {'name':'jjj','age':18}
    return jsonify(d)


@app.route('/name',methods=['POST'])
def getname():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    d = {'name':firstname + ' ' + lastname,'age': 18}
    print(d)
    return jsonify(d)


@app.route('/myform',methods=['POST'])
def myform():
    print('post')
    a = request.form['FirstName']
    print(a)
    d = {'name': 'xmr', 'age': 18}
    return jsonify(d)


@app.route('/mylist')
def mylist():
    l = ['xmr',18]
    print('mylist')
    return json.dumps(l)


@app.route('/mytable')
def mytable():
    table = [('id', 'name', 'age', 'score'),
        ('1', 'xiemanrui', '18', '100'),
        ('2', 'yxx', '18', '100'),
        ('3', 'yaoming', '37', '88')]

    print('mytable')
    data = json.dumps(table)
    print(data)
    return data



