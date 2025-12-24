from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html', title='Welcome to Ikhaya House!', club_name='Ikhaya House')

@app.route('/about')
def about():
    return render_template('about.html', title='About Ikhaya')

@app.route('/members')
def Members():
    return render_template('members.html', title='Our Members')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # 获取表单数据
        name = request.form.get('name')
        email = request.form.get('email')
        
        # 这里可以添加代码来保存数据到数据库或文件
        # 例如: save_to_database(name, email)
        
        # 返回提交成功的页面
        return render_template('contact.html', 
                             title='Contact us!', 
                             submitted=True, 
                             name=name, 
                             email=email)
    
    # GET请求时显示空表单
    return render_template('contact.html', title='Contact us!')

@app.route('/CR')
def layout():   
    return render_template("CR.html", title='Our Common Room')

if __name__=='__main__':
    app.run(debug=True)