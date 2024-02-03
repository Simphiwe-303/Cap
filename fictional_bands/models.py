from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	"""
		This class create the Question model. This model will be used by admin to create question for for users to answer.
	"""
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

class Choice(models.Model):
	"""
		This class create The Choice model. This model will also be used by the admin to create choices that a user can select from regarding the questions that will be created in the Question model.
	"""
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text

class CreateUserForm(UserCreationForm):
	"""
		This model will be used by users when registering themselves in order to view the application content.
	"""
	class Meta():
		model = User
		fields = ["username", "email", "password1", "password2"]