from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is home")



def contact(request):
    name=request.POST.get('name');
    email=request.POST.get('email');
    description=request.POST.get('description');
    age=request.POST.get('age');
    
    return HttpResponse(request,'index.html')