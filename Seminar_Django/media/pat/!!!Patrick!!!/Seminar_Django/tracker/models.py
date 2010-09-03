from django.db import models

class Teacher(models.Model):
  teacherName = models.CharField(max_length=200)
  room = models.CharField(max_length=5)
  
  def __unicode__(self):
        return u'%s in %s' % (self.teacherName , self.room)

  
class Student(models.Model):
  firstName = models.CharField(max_length=50)
  lastName = models.CharField(max_length=50)
  seminar = models.ForeignKey(Teacher)

  def __unicode__(self):
    return u'%s' % (self.firstName)

class Pass(models.Model):
  student = models.ForeignKey(Student)
  destination = models.ForeignKey(Teacher)
  date = models.DateTimeField("Time of pass")
  partA = models.BooleanField()
  partB = models.BooleanField()

  def __unicode(self):
    return u"Don't know how to do this yet..."
