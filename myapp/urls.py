from django.urls import path
from . import views
from users.views import SignUp
#from django.contrib.auth import login

urlpatterns = [
    #/myapp/
    #path('', views.question, name='index'),
    #/myapp/choice/
    path('answer/', views.ans, name='answer'),
    path('', views.index, name='index'),
    path('question/', views.question, name='question'),
    path('detail/', views.detail, name='detail'),

    #sign_up
    path('signup/', views.SignUp.as_view(), name='signup'),

    path('examples/', views.examples, name='examples'),
    path('contact/', views.contact, name='contact'),
    path('syllabus/', views.syllabus, name='syllabus'),
    path('assignments/', views.assign, name='assign'),

    path('login/', views.login, name='login'),
    #/myapp/5/
    path('<int:question_id>/', views.detail, name='detail'),
    #/myapp/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    #/myapp/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    #path('',login,{'template_name:' 'myapp/index.html'}),
]
