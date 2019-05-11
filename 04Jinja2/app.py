from flask import Flask,render_template

app = Flask(__name__)


@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html',name = user)

@app.route('/code')
def result():
    dict = {'java':80,'python':86,'javascript':60,'c#':68,'C':30}
    return render_template('list.html',result = dict)

@app.route('/')
def index():
    return render_template('index.html')



if __name__ =='__main__':
    app.run(debug=True)