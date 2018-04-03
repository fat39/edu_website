from django.shortcuts import render
from django.views import View
from repository import models

# Create your views here.

class Index(View):
    def get(self,request,*args,**kwargs):
        pics = models.Pic.objects.order_by("-create_time")[:5]  # 最新的5张图
        teacher_list = models.Teacher.objects.order_by("-teacher_level")[:5]
        response = {
            "teacher_list":teacher_list,
            "pics":pics,
        }
        return render(request,"edu_pages/index.html",response)


class Search(View):
    def get(self,request,*args,**kwargs):
        course_nid = kwargs.get("course_nid")
        grade_nid = kwargs.get("grade_nid")
        teacher_level = kwargs.get("teacher_level")
        condition = {}
        for k,v in kwargs.items():
            if v != "0":
                condition[k] = v

        course_objlist = models.Course.objects.all()
        grade_objlist = models.Grade.objects.all()
        level_choices = models.Teacher.level_choices

        # l = models.Teacher.objects.filter(
        #     course__grade__grade__nid=grade_nid,
        #     course__course__nid=course_nid,
        #     teacher_level=teacher_level,
        # )
        teacher_list = models.Teacher.objects.filter(**condition)


        response = {
            "course_objlist":course_objlist,
            "grade_objlist":grade_objlist,
            "level_choices":level_choices,
            "url_kwargs":kwargs,
            "teacher_list":teacher_list,
        }


        return render(request,"edu_pages/edu_search.html",response)