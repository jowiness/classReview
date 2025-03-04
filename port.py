import robot
from data_init import db
def port(st,et,kechen,keci,content,zsd,banji,num,xueyuan,biaoxian):
    query = {"date": {"$gte": st, "$lte": et}}
    mood = list(db.mood.find(query))
    for i in range(len(mood)):
        if mood[i]['mood']=='0':
            mood[i]['mood'] = '开心'
        elif mood[i]['mood']=='1':
            mood[i]['mood'] = '平淡'
        elif mood[i]['mood']=='2':
            mood[i]['mood'] = '低落'
    mood = str(mood)
    week = str(list(db.week.find(query)))
    know = str(list(db.know.find(query)))
    chat = str(list(db.chat.find(query)))
    kechen = '课程内容：'+kechen
    keci = '课次：'+keci
    content = '课次内容：'+content
    zsd = '知识点：'+zsd
    banji = '班级名称：'+banji
    num = '上课人数：'+num
    xueyuan = '班级之星（本节课上课表现亮眼的同学）：'+xueyuan
    biaoxian = '优秀表现（班级之星的优秀表现）：'+biaoxian
    mood = '今日心情：'+mood
    week = '上周大事件/简单分享：'+week
    know = '知识点评估：'+know
    chat = '学生上课聊天情况'+chat
    tdata = kechen+'\n'+keci+'\n'+content+'\n'+zsd+'\n'+banji+'\n'+num+'\n'+xueyuan+'\n'+biaoxian+'\n'
    sdata = mood+'\n'+week+'\n'+know+'\n'+chat+'\n'
    question = '我是童程童美少儿编程机构的郑景峰老师,刚刚上了一节编程课,需要你为我整理课程内容，点评学员表现并给出简单建议，直接整理和点评，无需回复无关内容。点评以总分总的形式，最好举一些实例佐证点评。需包含：1、课程概述(课程名称、授课教师、授课阶段和课次)。2、课程内容小结(知识点介绍并举例、知识点应用)3、班级上课点评(点评本节课基本情况(例如趣味性、实用性、难度、活跃度)，可以根据上课聊天数、聊天内容、学生反馈数据点评)4、学员个体表现(对每一位同学做简单点评和建议)5、总结(学员总体表现及期待)上述数据前8行为本次课的班级信息，9到倒数第2行是收集的学员今日上课反馈。'
    content_value = robot.chat(tdata+sdata+question)
    with open('data/'+kechen[5:]+'/'+banji[5:]+'/'+keci[3:]+'_'+content[5:]+'.md', 'w') as file:
        file.write(content_value)