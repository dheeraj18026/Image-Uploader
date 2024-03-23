from django.shortcuts import render, HttpResponseRedirect
from myapp.models import Image
from myapp.forms import ImageForm
# Create your views here.

def home(request):
    if request.method == 'POST':
        print("Dheeraj")             
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'myapp/home.html',{'form':form,'img':img})

def delete(request, id):
    if request.method == "POST":
        pi = Image.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
