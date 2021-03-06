from django.db import models

class Question(models.Model):
  text = models.CharField(max_length=200)
  def str(self):
    return self.text

class Member(models.Model):
	name = models.CharField('Nom complet', max_length=255)
	email = models.CharField('E-Mail', max_length=255)
	age = models.IntegerField('âge', blank=True, default=0)

	def __str__(self):
		return self.name
# Create your models here.
