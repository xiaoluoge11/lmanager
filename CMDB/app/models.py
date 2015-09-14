#coding: utf-8
from django.db import models
from django.contrib import admin
# Create your models here.
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import *
import time
class Idc(models.Model):
    idc_name = models.CharField(max_length=40, verbose_name=u'机房名称')
    remark = models.CharField(max_length=40, verbose_name=u'备注')
    def __unicode__(self):
	return self.idc_name
    class Meta:
	verbose_name = u'机房列表'
        verbose_name_plural = u'机房列表'	
class HostList(models.Model):
    ip = models.IPAddressField(unique=True, verbose_name=u'IP地址')
    hostname = models.CharField(max_length=30, verbose_name=u'主机名')
    group = models.ManyToManyField('Group', null=True, blank=True ,verbose_name=u'组名') 
    application = models.CharField(max_length=20, verbose_name=u'应用')
    bianhao = models.CharField(max_length=30, verbose_name=u'编号') 
    idc_name = models.CharField(max_length=40,null=True,blank=True, verbose_name=u'所属机房') 
    def __unicode__(self):
        return self.ip
    class Meta:
        verbose_name = u'主机列表'
	verbose_name_plural = u'主机列表'

class ServerAsset(models.Model):
    manufacturer = models.CharField(max_length=20, verbose_name=u'厂商')
    productname = models.CharField(max_length=30, verbose_name=u'产品型号')
    service_tag = models.CharField(max_length=80, unique=True, verbose_name=u'序列号')
    cpu_model = models.CharField(max_length=50, verbose_name=u'CPU型号')
    cpu_nums = models.PositiveSmallIntegerField(verbose_name=u'CPU线程数')
    cpu_groups = models.PositiveSmallIntegerField(verbose_name=u'CPU物理核数')
    mem = models.CharField(max_length=100, verbose_name='内存大小')
    disk = models.CharField(max_length=300, verbose_name='硬盘大小')
    hostname = models.CharField(max_length=30, verbose_name=u'主机名')
    ip = models.CharField(max_length=20, verbose_name=u'IP地址')
    os = models.CharField(max_length=20, verbose_name=u'操作系统')
    def __unicode__(self):
        return u'%s - %s' %(self.ip, self.hostname )

    class Meta:
        verbose_name = u'主机资产信息'
        verbose_name_plural = u'主机资产信息管理'

class Group(models.Model):
    name = models.CharField(max_length=50,unique=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = u'主机组信息'
        verbose_name_plural = u'主机组信息管理'
class Upload(models.Model):
    headImg = models.FileField(upload_to = './upload/')
    def __unicode__(self):
        return self.headImg
    class Meta:
	verbose_name = u'文件上传'
        verbose_name_plural = u'文件上传'
class cmd_run(models.Model):
    ip = models.IPAddressField(verbose_name=u'IP地址')
    command = models.CharField(max_length=30, verbose_name=u'命令')
    track_mark = models.IntegerField() 
    def __unicode__(self):
	return self.ip
    class Meta:
	verbose_name = u'命令管理'
	verbose_name_plural = u'命令管理'
class salt_return(models.Model):
   fun = models.CharField(max_length=50)
   jid = models.CharField(max_length=255)
   result = models.TextField()
   host = models.CharField(max_length=255)
   success = models.CharField(max_length=10)
   full_ret = models.TextField()
   def __unicode__(self):
        return self.host
   class Meta:
        verbose_name = u'命令返回结果'
        verbose_name_plural = u'命令返回结果'
