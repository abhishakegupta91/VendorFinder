from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def index(request):
    context = {}
    template_name = 'services/index.html'
    return render(request, template_name=template_name, context=context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else :
        form = UserCreationForm()
        context = {
            'form' : form
        }
        template_name = 'registration/signup.html'
        return render(request, template_name=template_name, context=context)

