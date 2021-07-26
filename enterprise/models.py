from django.db import models

# Create your models here.
class enterprise_info(models.Model):
    zhanghao = models.CharField('企业账号', max_length=50, null=True)
    ent_num = models.CharField('企业编号', max_length=50, null=True)
    name = models.CharField('企业名称', max_length=50, null=True)
    ent_property = models.CharField('企业性质', max_length=50, null=True)
    time_est = models.CharField('成立时间', max_length=50, null=True)
    num_em = models.CharField('员工人数', max_length=50, null=True)
    reg_cap = models.CharField('注册资金', max_length=50, null=True)
    ent_abstract = models.CharField('简介', max_length=500, null=True)

class emp_info(models.Model):
    ent_num = models.CharField('企业编号', max_length=50, null=True)
    name = models.CharField('企业名称', max_length=50, null=True)
    pos = models.CharField('职位', max_length=50, null=True)
    hiring = models.CharField('人数', max_length=50, null=True)
    edu_bgd = models.CharField('学历', max_length=50, null=True)
    major = models.CharField('专业', max_length=50, null=True)
    salary = models.CharField('工资', max_length=500, null=True)
    en = models.CharField('英语', max_length=50, null=True)
    job_des = models.CharField('职位描述', max_length=50, null=True)
    flag = models.CharField('标志', max_length=20, default=0)
