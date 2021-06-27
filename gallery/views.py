from django.shortcuts import render
from .models import image
from .forms import img

def gallery(request):
    if request.method=="GET":
        fo=image.objects.all()
        return render(request,'gallery.html',{'fo':fo})


def upload(request):
    form=img(request.POST, request.FILES)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            img_obj=form.instance
            return render(request,'success.html',{'form':form,'img_obj':img_obj})

    else:
        form=img()
    return render(request,'upload.html',{"form":form})

