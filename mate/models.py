from django.db import models
from django.db.models import IntegerField
from django.contrib.postgres.fields import ArrayField
#from django.contrib.auth.models import User
from myprofile.models import MyProfile

# Create your models here.


class Mate(models.Model):
    mate1 = models.ForeignKey(MyProfile, on_delete=models.CASCADE, verbose_name='USERNAME', blank=True, null=True, related_name='mate1') # 학생1의 id (User 모델과 연결)
    mate2 = models.ForeignKey(MyProfile, on_delete=models.CASCADE, verbose_name='USERNAME', blank=True, null=True, related_name='mate2') # 학생2의 id (User 모델과 연결)
    intimacy = models.IntegerField(default=0) # Quest 3%, Photo 1%, Message 1% 증가
    
    def __str__(self):
        return "%s - %s" % (self.mate1, self.mate2)

class MatePhoto(models.Model):
    mate = models.ForeignKey(Mate, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='', blank=True, null=True)

    def __str__(self):
        return "%s" % self.mate

class MateQuest(models.Model): # 0이 완료 안 된 상태
    mate = models.ForeignKey(Mate, on_delete=models.CASCADE, null=True) # Mate 모델과 연결
    quest1 = models.IntegerField(default=0)
    quest2 = models.IntegerField(default=0)
    quest3 = models.IntegerField(default=0)
    quest4 = models.IntegerField(default=0)
    quest5 = models.IntegerField(default=0)
    quest6 = models.IntegerField(default=0)
    quest7 = models.IntegerField(default=0)
    quest8 = models.IntegerField(default=0)
    quest9 = models.IntegerField(default=0)
    quest10 = models.IntegerField(default=0)
    quest11 = models.IntegerField(default=0)
    quest12 = models.IntegerField(default=0)

    def __str__(self):
        return "%s" % self.mate

class MateMsg(models.Model):
    mate = models.ForeignKey(Mate, on_delete=models.CASCADE, null=True) # Mate 모델과 연결
    sender = models.ForeignKey(MyProfile, on_delete=models.CASCADE, verbose_name='USERNAME', blank=True, null=True)
    content = models.CharField(max_length=400)

#class Task(models.Model):
#    mate = models.ForeignKey(Mate, on_delete=models.CASCADE, null=True) # Mate 모델과 연결
#    task = ArrayField(IntegerField(), size=8)