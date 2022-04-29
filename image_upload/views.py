from django.shortcuts import render
from django.http import HttpResponse
from .forms import Imageform
from .models import Image

# Create your views here.
def index(request):
    if request.method == "POST":
        form = Imageform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = Imageform()
    img = Image.objects.all()
    return render(request,"index.html",{'img':img,'form':form})