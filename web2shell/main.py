#pip install flash flask_basicauth
from flask import Flask, render_template
from flask_basicauth import BasicAuth
import subprocess

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'admin'  # 设置用户名
app.config['BASIC_AUTH_PASSWORD'] = 'admin'  # 设置密码

basic_auth = BasicAuth(app)

@app.route('/')
@basic_auth.required  # 鉴权保护该路由
def index():
    return render_template('index.html')

@app.route('/run_abc_script')
@basic_auth.required  # 鉴权保护该路由

def run_abc_script():
    subprocess.Popen(['./killst.sh'])    
    return 'abc 脚本已执行'

@app.route('/run_efg_script')
@basic_auth.required  # 鉴权保护该路由

def run_efg_script():
    subprocess.Popen(['./startst.sh'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return 'efg 脚本已在后台执行'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)