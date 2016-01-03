#coding:utf-8

from __future__ import unicode_literals

from django.db import models


class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'blog_teacher'
    def __unicode__(self):    #增加此私有函数，能显示实体的名字
        return self.name

class Student(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    intime = models.DateField(db_column='inTime')  # Field name made lowercase.
    teacher = models.ForeignKey(Teacher, related_name='student_teacher')
    def __unicode__(self):
        return self.name

# 兴趣组
class Group(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(Student, through="MemberShip")   #建立多对多关系
    class Meta:
        db_table = 'blog_group'
    def __unicode__(self):
        return self.name

# 多对多关系，是单独一张表，含有两个外键，这个class可以省略，但建议创建
class MemberShip(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    student = models.ForeignKey(Student)
    group = models.ForeignKey(Group)
    class Meta:
        db_table = 'blog_membership'
