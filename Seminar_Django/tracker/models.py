from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
  user = models.ForeignKey(User , unique=True)
  room = models.CharField(max_length=5)
  
  def __unicode__(self):
        return u'%s in %s' % (self.user.get_full_name() , self.room)
  
class Student(models.Model):
  firstName = models.CharField(max_length=50)
  lastName = models.CharField(max_length=50)
  seminar = models.ForeignKey(Teacher)

  def __unicode__(self):
    return u'%s' % (self.firstName)

class Pass(models.Model):
  student = models.ForeignKey(Student)
  destination = models.ForeignKey(Teacher)
  date = models.DateField("Time of pass")
  partA = models.BooleanField()
  partB = models.BooleanField()
  note = models.CharField(max_length=200)

  def __unicode(self):
    return u"Don't know how to do this yet..."
