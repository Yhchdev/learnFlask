from flask import Flask,redirect,url_for,request

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login',methods=['POST','GET'])
def login():
    # 接受POST表单提交
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success',name=user))
    # 获取GET方式提交的参数
    else:
        user = request.args.get('name')
        return redirect(url_for('success',name=user))


if __name__ =='__main__':
    app.run(debug=True)