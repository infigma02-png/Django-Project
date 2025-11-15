from django.shortcuts import render,HttpResponse,redirect
from django.template import loader
from projectapp.form import makeform
# Create your views here.
def home(request):
    return HttpResponse(loader.get_template("home.html").render())
def service(request):
    return HttpResponse(loader.get_template("services.html").render())
def aboutus(request):
    return HttpResponse(loader.get_template("aboutus.html").render())
def workgallery(request):
    return HttpResponse(loader.get_template("workgallery.html").render())
from django.contrib import messages

def contact(request):
    if request.method == "POST":
        form = makeform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Form submitted successfully!")
            return redirect("/contactus")
        else:
            messages.error(request, "Form is invalid! Please check your input.")
    else:
        form = makeform()
    return render(request, "contactus.html", {"form": form})

  
