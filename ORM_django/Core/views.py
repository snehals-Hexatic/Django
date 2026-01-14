from django.shortcuts import render
from .forms import RatingForm

def index(request):
    if request.method == 'POST':
        form = RatingForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            return render(request,'index.html',{'form':form})
    context = {}
    return render(request,'index.html',context)