import MySQLdb
import MySQLdb.cursors
import pymysql
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from sims import models
from sims.models import userinfo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def tomessage(request):
    return render(request, 'sims/message.html')
    # return redirect('/sims/setadmin')


def tologinin(request):
    return render(request, 'sims/login.html')

# def tobbs(request):
#     # return redirect('/bbs')
#     return render(request, 'bbs/index.html')


# 登录函数：
def loginin(request):
    if request.method == 'POST':
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if user and pwd:
            c = userinfo.objects.filter(user=user, pwd=pwd).count()
            try:
                b = userinfo.objects.get(user=user)
            except Exception as a:
                messages.error(request, '请输入正确账号密码.')
                return render(request, 'sims/login.html')
            if c == 1:
                # 学生
                if b.flag == "0":
                    return render(request, 'sims/index_student.html')
                # 教务处
                elif b.flag == "1":
                    return render(request, 'sims/index.html')
                # 学工处
                elif b.flag == "2":
                    return render(request, 'sims/index.html')
                # 企业
                elif b.flag == "3":
                    # return render(request, 'enterprise/info.html')
                    return redirect('/enterprise')
            #     管理员
                else:
                    return render(request, 'sims/index.html')
            else:
                messages.error(request, '请输入正确账号密码.')
                return render(request, 'sims/login.html')
        else:
            messages.error(request, '请输入正确账号密码.')
            return render(request, 'sims/login.html')
    elif request.method == 'GET':
        return render(request, 'sims/login.html')

# 选择注册界面 将跳转至注册功能
def toregister(requset):
    return render(requset, 'sims/register.html')


# 注册
def register(request):
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    pwd_2 = request.POST.get("pwd_2")

    username = models.userinfo.objects.filter(
        Q(user__icontains=user))
    # 获取数据的总条数
    count = username.__len__()
    if count == 0:
        if user and pwd and pwd_2:
            if pwd == pwd_2:
                us = userinfo(user=user, pwd=pwd, flag=0)
                us.save()
                messages.error(request, '注册成功，请登录.')
                return render(request, 'sims/login.html')
            else:
                messages.error(request, '两次输入的密码不一致，请重新输入.')
                return render(request, 'sims/register.html')

        else:
            messages.error(request, '请输入用户名和两次一致的密码.')
            return render(request, 'sims/register.html')
    else:
        messages.error(request, '用户名已被注册，请换个名字试试.')
        return render(request, 'sims/register.html')


# 返回首页渲染
def toindex(request):
    return render(request, 'sims/index.html')


# 返回首页渲染
def toindex_stu(request):
    return render(request, 'sims/index_student.html')


# 学生信息列表处理函数
def index(request):
    # conn = MySQLdb.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
    # students = models.Student_luhao_shanjian.objects.all()[0:20]
    student_list = models.Student_luhao_shanjian.objects.all()
    paginator = Paginator(student_list, 25) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        students = paginator.page(paginator.num_pages)

    # return render(request, 'list.html', {'contacts': contacts})
    return render(request, 'sims/user_index.html', {'students': students})


def index_stu(request):
    # conn = MySQLdb.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
    student_list = models.Student_luhao_shanjian.objects.all()
    paginator = Paginator(student_list, 25)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        students = paginator.page(paginator.num_pages)
    return render(request, 'sims/user_index_student.html', {'students': students})


# 学生16信息列表处理函数
def index16(request):
    # conn = MySQLdb.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
    student_list = models.stu16.objects.all()
    paginator = Paginator(student_list, 25)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        students = paginator.page(paginator.num_pages)
    return render(request, 'sims/user_index_16.html', {'students': students})


def index16_stu(request):
    # conn = MySQLdb.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
    student_list = models.stu16.objects.all()
    paginator = Paginator(student_list, 25)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        students = paginator.page(paginator.num_pages)
    return render(request, 'sims/user_index_16_student.html', {'students': students})


# 学生16信息列表处理函数
def index17(request):
    # conn = MySQLdb.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
    student_list = models.stu17.objects.all()
    paginator = Paginator(student_list, 25)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        students = paginator.page(paginator.num_pages)
    return render(request, 'sims/user_index_17.html', {'students': students})


def index17_stu(request):
    # conn = MySQLdb.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
    student_list = models.stu17.objects.all()
    paginator = Paginator(student_list, 25)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        students = paginator.page(paginator.num_pages)
    return render(request, 'sims/user_index_17_student.html', {'students': students})


# 根据首页输入框模糊查询
def findStudent(request):
    # 获取搜索框的值
    str = request.POST.get("str")
    # 模糊查询(根据姓名或者性别或者年级查询)
    students = models.Student_luhao_shanjian.objects.filter(
        Q(stuID__icontains=str) | Q(gender__icontains=str) | Q(major__icontains=str) | Q(
            departments__icontains=str) | Q(education_background__icontains=str) | Q(ruxue_year__icontains=str) | Q(
            Cultivating_way__icontains=str) | Q(kaoqu_yuanxi__icontains=str) | Q(kaoqu_zhuaye__icontains=str) | Q(
            xuezhi__icontains=str) | Q(danwei_location__icontains=str) | Q(danwei__icontains=str))
    # 获取数据的总条数
    count = students.__len__()
    return render(request, "sims/user_index.html", context={"students": students, "count": count})


def findStudent_stu(request):
    # 获取搜索框的值
    str = request.POST.get("str")
    # 模糊查询(根据姓名或者性别或者年级查询)
    students = models.Student_luhao_shanjian.objects.filter(
        Q(stuID__icontains=str) | Q(gender__icontains=str) | Q(major__icontains=str) | Q(
            departments__icontains=str) | Q(education_background__icontains=str) | Q(ruxue_year__icontains=str) | Q(
            Cultivating_way__icontains=str) | Q(kaoqu_yuanxi__icontains=str) | Q(kaoqu_zhuaye__icontains=str) | Q(
            xuezhi__icontains=str) | Q(danwei_location__icontains=str) | Q(danwei__icontains=str))
    # 获取数据的总条数
    count = students.__len__()
    return render(request, "sims/user_index_student.html", context={"students": students, "count": count})


# 根据首页输入框模糊查询
def findStudent16(request):
    # 获取搜索框的值
    str = request.POST.get("str")
    # 模糊查询(根据姓名或者性别或者年级查询)
    students = models.stu16.objects.filter(
        Q(stuID__icontains=str) | Q(banji__icontains=str) | Q(baokao_school__icontains=str) | Q(
            luqu_yuanbu__icontains=str) | Q(luqu_zhuanye__icontains=str) | Q(paiming__icontains=str))
    # 获取数据的总条数
    count = students.__len__()
    return render(request, "sims/user_index_16.html", context={"students": students, "count": count})


def findStudent16_stu(request):
    # 获取搜索框的值
    str = request.POST.get("str")
    # 模糊查询(根据姓名或者性别或者年级查询)
    students = models.stu16.objects.filter(
        Q(stuID__icontains=str) | Q(banji__icontains=str) | Q(baokao_school__icontains=str) | Q(
            luqu_yuanbu__icontains=str) | Q(luqu_zhuanye__icontains=str) | Q(paiming__icontains=str))
    # 获取数据的总条数
    count = students.__len__()
    return render(request, "sims/user_index_16_student.html", context={"students": students, "count": count})


# 根据首页输入框模糊查询
def findStudent17(request):
    # 获取搜索框的值
    str = request.POST.get("str")
    # 模糊查询(根据姓名或者性别或者年级查询)
    students = models.stu17.objects.filter(
        Q(stuID__icontains=str) | Q(banji__icontains=str) | Q(baokao_school__icontains=str) | Q(
            luqu_yuanbu__icontains=str) | Q(luqu_zhuanye__icontains=str) | Q(leixing__icontains=str))
    # 获取数据的总条数
    count = students.__len__()
    return render(request, "sims/user_index_17.html", context={"students": students, "count": count})


def findStudent17_stu(request):
    # 获取搜索框的值
    str = request.POST.get("str")
    # 模糊查询(根据姓名或者性别或者年级查询)
    students = models.stu17.objects.filter(
        Q(stuID__icontains=str) | Q(banji__icontains=str) | Q(baokao_school__icontains=str) | Q(
            luqu_yuanbu__icontains=str) | Q(luqu_zhuanye__icontains=str) | Q(leixing__icontains=str))
    # 获取数据的总条数
    count = students.__len__()
    return render(request, "sims/user_index_17_student.html", context={"students": students, "count": count})


# 学生信息新增处理函数
def add(request):
    if request.method == 'GET':
        return render(request, 'sims/user_add.html')
    else:
        stuID = request.POST.get('stuID')
        gender = request.POST.get('gender')
        major = request.POST.get('major')
        departments = request.POST.get('departments')
        education_background = request.POST.get('education_background')
        ruxue_year = request.POST.get('ruxue_year')
        Cultivating_way = request.POST.get('major')
        kaoqu_yuanxi = request.POST.get('kaoqu_yuanxi')
        kaoqu_zhuaye = request.POST.get('kaoqu_zhuaye')
        xuezhi = request.POST.get('xuezhi')
        danwei_location = request.POST.get('danwei_location')
        danwei = request.POST.get('danwei')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
        models.Student_luhao_shanjian.objects.create(
            stuID=stuID,
            gender=gender,
            major=major,
            departments=departments,
            education_background=education_background,
            ruxue_year=ruxue_year,
            Cultivating_way=Cultivating_way,
            kaoqu_yuanxi=kaoqu_yuanxi,
            kaoqu_zhuaye=kaoqu_zhuaye,
            xuezhi=xuezhi,
            danwei_location=danwei_location,
            danwei=danwei,
        )
        return redirect('/sims/loginin/user_index')


# 学生信息新增处理函数
def add16(request):
    if request.method == 'GET':
        return render(request, 'sims/user_add16.html')
    else:
        stuID = request.POST.get('stuID')
        banji = request.POST.get('banji')
        baokao_school = request.POST.get('baokao_school')
        luqu_yuanbu = request.POST.get('luqu_yuanbu')
        luqu_zhuanye = request.POST.get('luqu_zhuanye')
        paiming = request.POST.get('paiming')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
        models.stu16.objects.create(
            stuID=stuID,
            banji=banji,
            baokao_school=baokao_school,
            luqu_yuanbu=luqu_yuanbu,
            luqu_zhuanye=luqu_zhuanye,
            paiming=paiming,
        )
        return redirect('/sims/loginin/user_index_16')


# 学生17信息新增处理函数
def add17(request):
    if request.method == 'GET':
        return render(request, 'sims/user_add17.html')
    else:
        stuID = request.POST.get('stuID')
        banji = request.POST.get('banji')
        baokao_school = request.POST.get('baokao_school')
        luqu_yuanbu = request.POST.get('luqu_yuanbu')
        luqu_zhuanye = request.POST.get('luqu_zhuanye')
        leixing = request.POST.get('leixing')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
        models.stu17.objects.create(
            stuID=stuID,
            banji=banji,
            baokao_school=baokao_school,
            luqu_yuanbu=luqu_yuanbu,
            luqu_zhuanye=luqu_zhuanye,
            leixing=leixing,
        )
        return redirect('/sims/loginin/user_index_17')


# 学生信息修改处理函数
def edit(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        print(id)
        conn = MySQLdb.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select * from sims_student_luhao_shanjian where id=%s", [id, ])
        student = cursor.fetchone()
        cursor.close()
        conn.close()
        print(student)
        return render(request, 'sims/user_edit.html', {'student': student})
    else:
        id = request.POST.get("id")
        stuID = request.POST.get('stuID')
        gender = request.POST.get('gender')
        major = request.POST.get('major')
        departments = request.POST.get('departments')
        education_background = request.POST.get('education_background')
        ruxue_year = request.POST.get('ruxue_year')
        Cultivating_way = request.POST.get('major')
        kaoqu_yuanxi = request.POST.get('kaoqu_yuanxi')
        kaoqu_zhuaye = request.POST.get('kaoqu_zhuaye')
        xuezhi = request.POST.get('xuezhi')
        danwei_location = request.POST.get('danwei_location')
        danwei = request.POST.get('danwei')
        conn = pymysql.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 执行SQL，并返回收影响行数
        cursor.execute(
            "update sims_student_luhao_shanjian set stuID=%s ,gender = %s ,major= %s , departments= %s , education_background= %s ,ruxue_year= %s ,Cultivating_way= %s ,kaoqu_yuanxi= %s ,kaoqu_zhuaye= %s ,xuezhi= %s ,danwei_location= %s,danwei =%s where id=%s",
            [stuID, gender, major, departments, education_background, ruxue_year, Cultivating_way, kaoqu_yuanxi,
             kaoqu_zhuaye, xuezhi, danwei_location, danwei, id, ])
        conn.commit()
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        return redirect('/sims/loginin/user_index')


# 学生16信息修改处理函数
def edit16(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        print(id)
        conn = MySQLdb.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select * from sims_stu16 where id=%s", [id, ])
        student = cursor.fetchone()
        cursor.close()
        conn.close()
        print(student)
        return render(request, 'sims/user_edit16.html', {'student': student})
    else:
        id = request.POST.get("id")
        stuID = request.POST.get('stuID')
        banji = request.POST.get("banji")
        baokao_school = request.POST.get("baokao_school")
        luqu_yuanbu = request.POST.get("luqu_yuanbu")
        luqu_zhuanye = request.POST.get("luqu_zhuanye")
        paiming = request.POST.get("paiming")
        conn = pymysql.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 执行SQL，并返回收影响行数
        cursor.execute(
            "update sims_stu16 set stuID=%s ,banji=%s,baokao_school =%s,luqu_yuanbu=%s, luqu_zhuanye=%s, paiming=%s where id = %s",
            [stuID, banji, baokao_school, luqu_yuanbu, luqu_zhuanye, paiming, id, ])
        conn.commit()
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        return redirect('/sims/loginin/user_index_16')


# 学生17信息修改处理函数
def edit17(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        print(id)
        conn = MySQLdb.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select * from sims_stu17 where id = %s", [id, ])
        student = cursor.fetchone()
        cursor.close()
        conn.close()
        print(student)
        return render(request, 'sims/user_edit17.html', {'student': student})
    else:
        id = request.POST.get("id")
        stuID = request.POST.get('stuID')
        banji = request.POST.get("banji")
        baokao_school = request.POST.get("baokao_school")
        luqu_yuanbu = request.POST.get("luqu_yuanbu")
        luqu_zhuanye = request.POST.get("luqu_zhuanye")
        leixing = request.POST.get("leixing")

        conn = pymysql.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 执行SQL，并返回收影响行数
        cursor.execute(
            "update sims_stu17 set stuID=%s,banji =%s,baokao_school  =%s,luqu_yuanbu =%s,luqu_zhuanye =%s,leixing =%s where id=%s",
            [stuID, banji, baokao_school, luqu_yuanbu, luqu_zhuanye, leixing, id, ])
        conn.commit()
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        return redirect('/sims/loginin/user_index_17')


# 学生信息删除处理函数
def delete(request):
    id = request.GET.get("id")
    conn = MySQLdb.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
    models.Student_luhao_shanjian.objects.filter(id=id).delete()
    return redirect('/sims/loginin/user_index')  # /直接重定向 url全部替换掉 ./：拼接url


# 学生16信息删除处理函数
def delete16(request):
    id = request.GET.get("id")
    conn = MySQLdb.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
    models.stu16.objects.filter(id=id).delete()
    return redirect('/sims/loginin/user_index_16')  # /直接重定向 url全部替换掉 ./：拼接url


# 学生17信息删除处理函数
def delete17(request):
    id = request.GET.get("id")
    conn = MySQLdb.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
    models.stu17.objects.filter(id=id).delete()
    return redirect('/sims/loginin/user_index_17')  # /直接重定向 url全部替换掉 ./：拼接url


# 选择密码修改界面 将跳转至密码修改功能
def tosecurity(requset):
    return render(requset, 'sims/user_old_security.html')


# 修改密码
def security(request):
    user = request.POST.get("user")
    pwd_old = request.POST.get("pwd_old")
    c = userinfo.objects.filter(user=user, pwd=pwd_old).count()
    if c != 0:
        return render(request, 'sims/user_new_security.html')
    else:
        messages.error(request, '请输入正确的原账号密码.')
        return redirect('../')


def newpw_set(request):
    username = request.POST.get("user")
    pw1 = request.POST.get("pwd_new_1")
    pw2 = request.POST.get("pwd_new_2")
    if pw2 and pw1 and username:
        if pw1 == pw2:
            conn = pymysql.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            # 执行SQL，并返回收影响行数
            cursor.execute(
                "update sims_userinfo set pwd=%s  where user=%s",
                [pw1, username, ])
            conn.commit()
            # 关闭游标
            cursor.close()
            # 关闭连接
            conn.close()
            messages.error(request, '密码修改成功，请重新登陆.')
            return redirect('/sims/tologinin')

        else:
            messages.error(request, '请输入一样的新密码.')
            return redirect('../')
    else:
        messages.error(request, '请正确输入用户名与新密码.')
        return redirect('../')


def chart12(request):
    return render(request, 'sims/chart.html')


def setadmin(request):
    if request.method == 'GET':
        return render(request, 'sims/setadmin.html')
    else:
        username = request.POST.get("user")
        conn = pymysql.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 执行SQL，并返回收影响行数
        cursor.execute("update sims_userinfo set flag=1 where user=%s", [username, ])
        conn.commit()
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        messages.error(request, '用户设置为管理员成功.')
        return redirect('/sims/setadmin')


def setuser(request):
    if request.method == 'GET':
        return render(request, 'sims/setuser.html')
    else:
        username = request.POST.get("user")
        conn = pymysql.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 执行SQL，并返回收影响行数
        cursor.execute("update sims_userinfo set flag=0 where user=%s", [username, ])
        conn.commit()
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        messages.error(request, '用户设置为管理员成功.')
        return redirect('/sims/setuser')
