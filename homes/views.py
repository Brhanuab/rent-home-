from django.shortcuts import render,redirect
from django.contrib import messages
from .models import home,renter

from .forms import homecreationForm,rentercreationForm






    



def index(request):
    return render(request,'index.html')


def homelist(request):
    homes=home.objects.all()
    return render(request,'homelist.html',{'homes':homes})





def homecreat(request):
    if request.method == 'POST':
        form=homecreationForm(request.POST)
        if form.is_valid():
           postss=form.save(commit=False)
           postss.save()
           return redirect('homelist')
       
        
    else:
       form=homecreationForm()
    return render(request,'homecfreation.html',{'form':form})



def rentercreat(request):
    if request.method == 'POST':
        form=rentercreationForm(request.POST)
        if form.is_valid():
           postss=form.save(commit=False)
           postss.save()
           messages.success(request,'created successfuly !')
           return redirect('homelist')
        
        
    else:
       form=rentercreationForm()
    return render(request,'rentercreation.html',{'form':form})





# Create your views here.
