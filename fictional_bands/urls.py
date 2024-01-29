from django.urls import path, include, re_path
from . import views

"""
	The app_name variable is used to separate this application urls from other application urls created in this project.

	The urlpatterns store the application's paths that the app uses to navigate.
"""

app_name = 'fictional_bands'
urlpatterns = [
	path('', views.user_register, name='register'),
	path('login/', views.user_login, name='login'),
	path('authenticate_user_login/', views.authenticate_user_login, name='authenticate_user_login'),
	path('index/', views.index, name='index'),
	path('fiction/', views.fiction, name='fiction'),
	path('voting/', views.voting, name='voting'),
	path('<int:question_id>', views.detail, name='detail'),
	path('<int:question_id>/vote/', views.vote, name='vote'),
	path('<int:question_id>/results/', views.results, name='results')
]