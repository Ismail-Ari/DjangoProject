from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
from login.models import EmpInsert
from django.contrib import messages


 
def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })
 
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

  
@login_required
def secret_page(request):
    return render(request, 'secret_page.html')

@login_required
def SecretPage(request):
    resultsdisplay=EmpInsert.objects.all()
    return render(request, 'secret_page2.html',{'EmpInsert':resultsdisplay})

#class SecretPage(LoginRequiredMixin, TemplateView):
 #   template_name = 'secret_page2.html'

@login_required
def Insertrecord(request):
    if request.method == 'POST':
        if request.POST.get('hyva') and request.POST.get('huono') and request.POST.get('country') and request.POST.get('aihe') and request.POST.get('arvosana'):
            saverecord=EmpInsert()
            saverecord.hyva=request.POST.get('hyva')
            saverecord.huono=request.POST.get('huono')
            saverecord.country=request.POST.get('country')
            saverecord.aihe=request.POST.get('aihe')
            saverecord.arvosana=request.POST.get('arvosana')
            saverecord.save()
            messages.success(request, 'Palautteen lähettäminen onnistui, kiitos!')
        return render(request, 'secret_page.html')
    else:
        return render(request, 'index.html') 

        