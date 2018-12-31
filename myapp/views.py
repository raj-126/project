from django.shortcuts import render
from .models import Question
from .models import answer
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic
from users.forms import CustomUserCreationForm

#from Que import Que

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/templates/signup.html'

def question(request):
    latest_question_list = Question.objects.all()
    output = ', '.join([q.question_text for q in latest_question_list])
    latest_question_list1= Question.objects.all()
    output1 = '\n'.join([q.question_text1 for q in latest_question_list1])

    return HttpResponse(output)
    
    
    '''
    template = loader.get_template('myapp/index.html')
    
    context = {
        'latest_question_list': latest_question_list
    '''

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    '''
    return render(request, 'myapp/detail.html', {'question': question})
    '''

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def login(request): 
    # numbers = [1,2,3,4,5]
    # name = 'hello'
    # args = {'myname' : name, 'numbers': numbers}
    return render(request,'myapp/login.html')


def index(request): 
    return render(request,'myapp/index.html')

def examples(request): 
    return render(request,'myapp/examples.html')

def contact(request): 
    return render(request,'myapp/contact.html')

def syllabus(request): 
    return render(request,'myapp/syllabus.html')

def assign(request): 
    return render(request,'myapp/assign.html')


def ans(request):
    latest_choice_list = answer.objects.all()
    output2 = ', '.join([q.choice_text for q in latest_choice_list])
    return HttpResponse(output2)

# question_prompts =[
#     "what is your name?\n(a) 1\n(b)2\n\n",
#     "what is your name?\n(a) 1\n(b)2\n\n",
#     "what is your name?\n(a) 1\n(b)2\n\n",

# ]
# question = [

# ]