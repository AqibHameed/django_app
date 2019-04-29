import datetime
from django.shortcuts import render
#importing loading from django template
from django.template import loader
from webapp.form import StudentForm

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from webapp.models import Blog
from webapp.functions.functions import handle_uploaded_file
from django.views.generic import TemplateView


class BlogList(ListView):
    # model = Blog
    # context_object_name = 'blog_list'
    queryset = Blog.objects.all()
    template_name = 'blog_list.html'

class MyView(View):
    def get(self, request):
        template = loader.get_template('index.html')  # getting our template
        name = {
            'student': 'rahul'
        }
        return HttpResponse(template.render(name))

class MyFormView(View):
    form_class = StudentForm
    template_name = 'form.html'
    def get(self, request, *args, **kwargs):
        student = self.form_class
        print(student)
        return render(request, self.template_name, {'form':student})
    def post(self, request, *args, **kwargs):
        student = self.form_class(request.POST, request.FILES)
        if student.is_valid():
           handle_uploaded_file(request.FILES['file'])
           return HttpResponse("Class base view form uploaded successfuly")

class BlogName(TemplateView):
    template_name = 'blog_names.html'

    def get_context_data(self, **kwargs):
        context = super(BlogName, self).get_context_data(**kwargs)
        context['first'] = Blog.objects.first()
        context['second'] = Blog.objects.last()
        return context



def hello(request):
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")
def index(request):
    template = loader.get_template('index.html')  # getting our template
    name = {
        'student': 'rahul'
    }
    return HttpResponse(template.render(name))  # rendering the template in HttpResponse

def index_form(request):
    if request.method == 'POST':
        student = StudentForm(request.POST, request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfuly")
    else:
        print("hello ***")
        student = StudentForm
        print(student)
        return render(request, "form.html", {'form':student})
def setcookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('java-tutorial', 'javatpoint.com')
    return response

def getcookie(request):
    tutorial  = request.COOKIES['java-tutorial']
    return HttpResponse("java tutorials @: "+  tutorial);

def bootstrap_form(request):
    template = loader.get_template('bootstrap.html')
    return HttpResponse(template.render())
