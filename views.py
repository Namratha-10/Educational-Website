from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'app1/home.html')

def about(request):
    return render(request,'app1/about.html')

def classes(request):
    return render(request,'app1/classes.html')

def class8th(request):
    return render(request,'app1/class8th.html')

def class9th(request):
    return render(request,'app1/class9th.html')

def class10th(request):
    return render(request,'app1/class10th.html')



def gallery(request):
    return render(request,'app1/gallery.html')

def photos(request):
    return render(request,'app1/photos.html')

def videos(request):
    return render(request,'app1/videos.html')

def parentreg(request):
    return render(request,'app1/parentreg.html')

def latestnews(request):
    return render(request,'app1/latestnews.html')

def contact(request):
    return render(request,'app1/contact.html')


