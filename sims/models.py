from django.db import models


# Create your models here.

class Student_luhao_shanjian(models.Model):
    stuID = models.CharField('学号', max_length=32, unique=True)
    gender = models.CharField('性别', max_length=32, null=True)
    major = models.CharField('专业', max_length=32, null=True)
    departments = models.CharField('院系', max_length=32, null=True)
    education_background = models.CharField('学历', max_length=32, null=True)
    ruxue_year = models.CharField('年度', max_length=32, null=True)
    Cultivating_way = models.CharField('培养方式', max_length=32, null=True)
    kaoqu_yuanxi = models.CharField('考取院系', max_length=32, null=True)
    kaoqu_zhuaye = models.CharField('考取专业', max_length=32, null=True)
    xuezhi = models.CharField('学制', max_length=32, null=True)
    danwei_location = models.CharField('单位所在地', max_length=32, null=True)
    danwei = models.CharField('单位', max_length=32, null=True)


class userinfo(models.Model):
    # userID = models.CharField(primary_key=True,max_length=20)  #表单id
    user = models.CharField('用户名', max_length=20, primary_key=True)
    pwd = models.CharField('密码', max_length=20)
    flag = models.CharField('标志', max_length=20)


class stu16(models.Model):
    stuID = models.CharField('学号', max_length=20, unique=True)
    banji = models.CharField('班级', max_length=32, null=True)
    baokao_school = models.CharField('报考院校', max_length=32, null=True)
    luqu_yuanbu = models.CharField('录取院部', max_length=32, null=True)
    luqu_zhuanye = models.CharField('录取专业', max_length=32, null=True)
    paiming = models.CharField('排名', max_length=32, null=True)


class stu17(models.Model):
    stuID = models.CharField('学号', max_length=20, unique=True)
    banji = models.CharField('班级', max_length=32, null=True)
    leixing = models.CharField('工作类型', max_length=32, null=True)
    baokao_school = models.CharField('报考院校', max_length=32, null=True)
    luqu_yuanbu = models.CharField('录取院部', max_length=32, null=True)
    luqu_zhuanye = models.CharField('录取专业', max_length=32, null=True)
    leixing = models.CharField('工作类型', max_length=32, null=True)
