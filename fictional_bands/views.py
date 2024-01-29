from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .models import Question, Choice, CreateUserForm

# Create your views here
def user_register(request):
	form = CreateUserForm()

	if request.method == "POST":
		form = CreateUserForm(request.POST)
		
		if form.is_valid():
			form.save()
			return redirect("fictional_bands:index")

	return render(request, 'register_&_login/register.html', {'registration_form': form})


def user_login(request):
	return render(request, 'register_&_login/login.html')
			

def authenticate_user_login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)

	if user is None:
		return HttpResponseRedirect(reverse('fictional_bands:login'))
	else:
		login(request, user)
		return HttpResponseRedirect(reverse('fictional_bands:index'))

def index(request):
	return render(request, 'pages/fictional.html')

def fiction(request):
	return render(request, 'pages/fiction.html')

def voting(request):
	latest_question_list = Question.objects.order_by('-pub_date')[::]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'pages/voting.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'pages/detail.html', {'question': question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'pages/detail.html', {'question': question, 'error_message': "You did not select a choice."})
	else:
		selected_choice.votes += 1
		selected_choice.save()

		return HttpResponseRedirect(reverse('fictional_bands:results', args=(question_id, )))

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'pages/fiction.html', {'question': question, 'quest': question_id})
