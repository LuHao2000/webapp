import MySQLdb
import MySQLdb.cursors
import pymysql
from django.db.models import Q
from django.shortcuts import render, redirect
from sims import models
from enterprise import models

# Create your views here.
def tomessage(request):
    return render(request, 'sims/message.html')

def toinfo(request):
    return render(request, 'enterprise/info.html')

def torelease(request):
    return render(request, 'enterprise/release.html')


def tocontent(request):
    return render(request, 'enterprise/content.html')

def torelated(request):
    return render(request, 'enterprise/related.html')

def toindex(request):
    return render(request, 'enterprise/index_emp.html')

def toinfo_edit(request):
     return render(request, 'enterprise/info-edit.html')


def tostanderd(request):
    return render(request, 'enterprise/standard.html')

# 编辑企业信息
def editEnter(request):
    if request.method == 'GET':
        zhanghao = request.GET.get("zhanghao")
        print(zhanghao)
        conn = MySQLdb.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select * from enterprise_enterprise_info where zhanghao=%s", [zhanghao, ])
        enterprise = cursor.fetchone()
        cursor.close()
        conn.close()
        print(enterprise)
        return render(request, 'enterprise/info-edit.html', {'enterprise': enterprise})
    else:
        ent_num = request.POST.get('ent_num')
        name = request.POST.get('name')
        ent_property = request.POST.get('ent_property')
        time_est = request.POST.get('time_est')
        num_em = request.POST.get('num_em')
        reg_cap = request.POST.get('reg_cap')
        ent_abstract = request.POST.get('ent_abstract')
        zhanghao = request.POST.get('zhanghao')
        conn = pymysql.connect(host="localhost", user="root", passwd="root", db="sms", charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 执行SQL，并返回收影响行数
        cursor.execute(
            "update enterprise_enterprise_info set ent_num=%s, name=%s, ent_property=%s, time_est=%s, num_em=%s, reg_cap=%s, ent_abstract=%s where zhanghao=%s",
            [ent_num, name, ent_property, time_est, num_em, reg_cap, ent_abstract, zhanghao, ])
        conn.commit()
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        return redirect('/enterprise/')


# 删除企业信息 超级管理员
def deleteEnter(request):
    id = request.GET.get("id")
    conn = MySQLdb.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
    models.enterprise_info.objects.filter(id=id).delete()
    return redirect('/sims/loginin/user_index')  # /直接重定向 url全部替换掉 ./：拼接url


# 查询企业信息
def findEnter(request):
    # 获取搜索框的值
    str = request.POST.get("str")
    # 模糊查询
    enterprise = models.enterprise_info.objects.filter(
        Q(id__icontains=str) | Q(ent_num__icontains=str) | Q(name__icontains=str) | Q(
            time_est__icontains=str) | Q(num_em__icontains=str) | Q(reg_cap__icontains=str) | Q(ent_abstract__icontains=str) )
    # 获取数据的总条数
    count = enterprise.__len__()
    return render(request, "sims/user_index_16.html", context={"enterprise": enterprise, "count": count})


# 企业信息列表处理函数
def indexEnter(request):
    conn = MySQLdb.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
    enterprise = models.enterprise_info.objects.all()[0:20]
    return render(request, 'sims/user_index_16.html', {'enterprise': enterprise})


# 增加招聘信息
def addEmp(request):
    if request.method == 'GET':
        return render(request, 'sims/user_add16.html')
    else:
        # id = request.POST.get('id')
        ent_num = request.POST.get('ent_num')
        name = request.POST.get('name')
        pos = request.POST.get('pos')
        hiring = request.POST.get('hiring')
        edu_bgd = request.POST.get('edu_bgd')
        major = request.POST.get('major')
        salary = request.POST.get('salary')
        en = request.POST.get('en')
        job_des = request.POST.get('job_des')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
        models.emp_info.objects.create(
            ent_num=ent_num,
            name=name,
            pos=pos,
            hiring=hiring,
            edu_bgd=edu_bgd,
            major=major,
            salary=salary,
            en=en,
            job_des=job_des,

        )
        return redirect('/enterprise/toinfo')

# 修改招聘信息
def editEmp(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        print(id)
        conn = MySQLdb.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select * from enterprise_emp_info where id=%s", [id, ])
        emp = cursor.fetchone()
        cursor.close()
        conn.close()
        print(emp)
        return render(request, 'enterprise/release_edit.html', {'emp': emp})
    else:
        id = request.POST.get('id')
        ent_num = request.POST.get('ent_num')
        pos = request.POST.get('pos')
        hiring = request.POST.get('hiring')
        edu_bgd = request.POST.get('edu_bgd')
        major = request.POST.get('major')
        salary = request.POST.get('salary')
        en = request.POST.get('en')
        job_des = request.POST.get('job_des')
        conn = pymysql.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 执行SQL，并返回收影响行数
        cursor.execute(
            "update enterprise_emp_info set ent_num=%s, pos=%s, hiring=%s, edu_bgd=%s, major=%s, salary=%s, en=%s, job_des=%s where id=%s",
            [ent_num, pos, hiring, edu_bgd, major, salary, en, job_des,id,  ])
        conn.commit()
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        return redirect('../../enterprise/indexEmp')

# 删除招聘信息
def deleteEmp(request):
    id = request.GET.get("id")
    conn = MySQLdb.connect(host="localhost", user="root", passwd="717320", db="sms", charset='utf8')
    models.emp_info.objects.filter(id=id).delete()
    return redirect('../../enterprise/indexEmp')  # /直接重定向 url全部替换掉 ./：拼接url


# 招聘信息列表处理函数
def indexEmp(request):
    employment = models.emp_info.objects.all()[0:20]
    return render(request, 'enterprise/index_emp.html', {'employment': employment})

# 查询招聘信息
def findEmp(request):
    # 获取搜索框的值
    str = request.POST.get("str")
    # 模糊查询
    employment = models.emp_info.objects.filter(
        Q(id__icontains=str) | Q(ent_num__icontains=str) | Q(pos__icontains=str) | Q(
            hiring__icontains=str) | Q(edu_bgd__icontains=str) | Q(major__icontains=str) | Q(salary__icontains=str) |
        Q(en__icontains=str) | Q(job_des__icontains=str))
    # 获取数据的总条数
    count = employment.__len__()

    return render(request, "sims/user_index_16.html", context={"employment": employment, "count": count})


def toshow(request):
    return render(request, 'enterprise/show.html')