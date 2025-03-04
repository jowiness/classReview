from flask import Flask, render_template,request,jsonify
from data_init import db
import datetime
import port

project = Flask(__name__)
project.debug = True
startTime = datetime.datetime.now()

@project.route('/mood')
def mood():
    date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    name = request.args.get('name')
    if name=='':
        return '请填写昵称！'
    mood = request.args.get('mood')
    if mood=='x':
        return '请选择心情！'
    db.mood.insert({'date':date,'name':name,'mood':mood})
    return '提交成功！'
@project.route('/week')
def week():
    date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    name = request.args.get('name')
    if name=='':
        return '请填写昵称！'
    week = request.args.get('week')
    if len(week)<2:
        return '事件字数稍微多一些吧！！O(∩_∩)O~~'
    db.week.insert({'date':date,'name':name,'week':week})
    return '提交成功！'
@project.route('/chat')
def chat():
    date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    name = request.args.get('name')
    if name=='':
        return '请填写昵称！'
    chat = request.args.get('chat')
    if chat=='':
        return '发言不能为空哦~'
    if len(chat)>50:
        return '输入字数不能多于50个'
    db.chat.insert({'date':date,'name':name,'chat':chat})
    return '提交成功！'
@project.route('/know',methods=['POST'])
def know():
    date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    name = request.form.get('name')
    if name=='':
        return '请填写昵称！'
    try:
        d1 = int(request.form.get('d1'))
        d2 = int(request.form.get('d2'))
        d3 = int(request.form.get('d3'))
        d4 = int(request.form.get('d4'))
        if d1<1 or d1>5 or d2<1 or d2>5 or d3<1 or d3>5 or d4<1 or d4>5:
            return '请输入1-5的整数'
    except ValueError:
        return '请输入1-5的整数'
    d5 = request.form.get('d5')
    lv = ['非常低','低','中等','中高','高','非常高']
    db.know.insert({'date':date,'name':name,'趣味性':lv[d1],'实用性':lv[d2],'课程难度':lv[d3-1],'掌握情况':lv[d4],'期待项目':d5})
    return '提交成功！'

@project.route('/showmsg')
def showmsg():
    global startTime
    nowTime = datetime.datetime.now()
    if nowTime-startTime >= datetime.timedelta(hours=2):
        startTime = nowTime - datetime.timedelta(hours=2)
    #startTime = nowTime - datetime.timedelta(hours=2)
    st = startTime.strftime('%Y-%m-%d %H:%M:%S')
    et = nowTime.strftime('%Y-%m-%d %H:%M:%S')
    query = {"date": {"$gte": st, "$lte": et}}
    result = list(db.chat.find(query))
    s = ''
    for i in result:
        s += '<p>'+str(i['name'])+':'+str(i['chat'])+'</p>'
    return s
    
@project.route('/', methods=['GET'])
def index():
    return render_template('index.html')
@project.route('/report', methods=['GET'])
def gen():
    return render_template('report.html')
@project.route('/report',methods=['POST'])
def report():
    global startTime
    nowTime = datetime.datetime.now()
    if nowTime-startTime >= datetime.timedelta(hours=2):
        startTime = nowTime - datetime.timedelta(hours=2)
    #startTime = nowTime - datetime.timedelta(hours=2)
    st = startTime.strftime('%Y-%m-%d %H:%M:%S')
    et = nowTime.strftime('%Y-%m-%d %H:%M:%S')
    kechen = request.form.get('kechen')
    keci = request.form.get('keci')
    content = request.form.get('content')
    zsd = request.form.get('zsd')
    banji = request.form.get('banji')
    num = request.form.get('num')
    xueyuan = request.form.get('xueyuan')
    biaoxian = request.form.get('biaoxian')
    port.port(st,et,kechen,keci,content,zsd,banji,num,xueyuan,biaoxian)
    return '生成成功！！'

project.run(host='0.0.0.0', port=8000)