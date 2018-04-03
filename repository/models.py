from django.db import models


class Teacher(models.Model):
    """老师表"""
    nid = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='姓名',max_length=32)
    gender_choices = [
        (1,"男"),
        (2,"女"),
    ]
    gender = models.IntegerField(verbose_name='性别',choices=gender_choices)
    avatar = models.ImageField(verbose_name='头像', upload_to="static/media/avatars",
                               default="static/media/avatars/default.jpg")
    level_choices = [
        (1,"讲师"),
        (2,"高级讲师"),
    ]

    teacher_level = models.IntegerField(verbose_name="职级",choices=level_choices,default=1)
    note = models.TextField(verbose_name="简介",null=True,blank=True)

    def __str__(self):
        return "%s-%s" % (self.name,self.get_teacher_level_display())


class Course(models.Model):
    """课程表"""
    nid = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="课程名称",max_length=64,unique=True)

    def __str__(self):
        return self.name


class Teacher2Course(models.Model):
    """老师课程关系表"""
    nid = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(verbose_name="老师",to="Teacher",related_name="course",to_field="nid",on_delete=models.CASCADE)
    course = models.ForeignKey(verbose_name="课程",to="Course",related_name="teacher",to_field="nid",on_delete=models.CASCADE)

    class Meta:
        unique_together = [
            ("teacher","course"),
        ]

    def __str__(self):
        return "%s-%s" % (self.teacher,self.course)


class Grade(models.Model):
    """关系表"""
    nid = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='班级名称', max_length=64,unique=True)

    def __str__(self):
        return self.name

class Course2Teacher2Grade(models.Model):
    """老师班级关系表"""
    nid = models.AutoField(primary_key=True)
    teachercourse = models.ForeignKey(verbose_name="老师_课程",to="Teacher2Course",related_name="grade",to_field="nid",on_delete=models.CASCADE)
    grade = models.OneToOneField(verbose_name="班级",to="Grade",related_name="course",to_field="nid",on_delete=models.CASCADE)  # 在此unique，表示班级是一对多的
    # grade = models.ForeignKey(verbose_name="班级",to="Grade",to_field="nid",unique=True,on_delete=models.CASCADE)  # 在此unique，表示班级是一对多的

    class Meta:
        unique_together = [
            ("teachercourse","grade"),
        ]

    def __str__(self):
        return "%s-%s" % (self.teachercourse,self.grade)



class Pic(models.Model):
    """for 图片"""
    nid = models.AutoField(primary_key=True)
    link = models.URLField(verbose_name="链接",null=True,blank=True)
    path = models.TextField(verbose_name="图片位置")
    create_time = models.DateTimeField(verbose_name="创建时间",auto_now_add=True)

    def __str__(self):
        return self.path
