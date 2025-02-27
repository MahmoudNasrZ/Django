from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("Hello, world! This is the home page.")
    return render(request, "home.html")  # Renders the home template


def contact(request,contact_id):
    # return HttpResponse(f"Hello, world! This is the {name} page.")
    context = {"name": contact_id}  # Passes 'name' to template
    return render(request, "contact.html", context)
