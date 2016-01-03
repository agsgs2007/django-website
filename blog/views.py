#coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
import datetime

from models import *

class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def say(self):
        return "My name is " + self.name

def index(request):
    t = loader.get_template("index.html")
    user = {"name":"Tom","age":10,"sex":"male"}
    person = Person("", 23, "famale")
    book_list = ['python', 'C', 'java', 'PHP']
    # book_list2 = []
    # for book in book_list:
    #     book_list2.append(book.upper())

    c = Context({"title":"django","user":user,"book_list":book_list, "today":datetime.datetime.now()})
    return HttpResponse(t.render(c))

def time(request):

    # http://127.0.0.1:8000/blog/time/?id=1451&name=123
    id = request.GET.get("id")
    name = request.GET.get("name")
    t = loader.get_template("time.html")
    c = Context({"today":datetime.datetime.now(),"id":id,"name":name})
    return HttpResponse(t.render(c))

def foo(request,p1,p2):

    # http://127.0.0.1:8000/blog/foo/2561/%E5%BC%A0%E5%8B%8B/
    t = loader.get_template("time.html")
    c = Context({"today":datetime.datetime.now(),"id":p1,"name":p2})
    return HttpResponse(t.render(c))


def bar(request,id,name):

    # http://127.0.0.1:8000/blog/bar/2561/ddd/
    t = loader.get_template("time.html")
    c = Context({"today":datetime.datetime.now(),"id":id,"name":name})
    return HttpResponse(t.render(c))


def student_list(request):

    # student list querySet
    # studentlist = Student.objects.all()
    # studentlist = Student.objects.filter(age__gt =30)
    # studentlist = Student.objects.filter(id__in =[1,2])

    teacher = Teacher.objects.get(id = 1)
    studentlist = teacher.student_teacher.all()

    # find studentlist through group id 通过兴趣组查找学生列表
    # group = Group.objects.get(id = 1)
    # studentList = group.members.all()
    #
    # #find grouplist through student id 通过学生列表查找兴趣组
    # groupList = student.group_set.all()

    # create a ManyToMany 多对多的关系 通过学生id和组id创建多对多关系
    # MemberShip(group = newgroup, student = newstudent).save()

    t = loader.get_template("student_list.html")
    c = Context({"student_list":studentlist})
    return HttpResponse(t.render(c))

def student(request):

    # single student

    singlestudent = Student.objects.get(id = 1)
    singlestudent.name = "tom"
    singlestudent.age = 12
    singlestudent.intime = "2015-2-1"
    singlestudent.save()

    singlestudent.delete()
    # batch update data
    # Student.objects.filter(age__gt = 30).update(name = "xys")

    newStudent = Student(name = "bcd", age = 55, intime = "2011-10-22")
    newStudent.save()
    t = loader.get_template("student.html")
    c = Context({"student":singlestudent})
    return HttpResponse(t.render(c))