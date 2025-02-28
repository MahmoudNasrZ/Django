from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import ClassArea,ClassRoom
#https://forum.djangoproject.com/t/url-pattern-with-parameters/34408
# Create your views here.
def home(request):
    return render(request, "home.html")  # Renders the home template


def contact(request,contact_id):
        # Retrieve all class areas from the database
    class_areas = ClassArea.objects.all()
    class_rooms = ClassRoom.objects.all()  # Get all ClassRoom objects
    context = {
        "class_id": contact_id,
        "description":"this is a class this just a filler to check the funcationality of the if function inside Contact.html",
        "class_areas" : class_areas,
        "class_rooms":class_rooms  
               } 
    return render(request, "contact.html", context)

def about_us_view(request):
    # https://medium.com/@biswajitpanda973/how-to-insert-data-to-database-using-django-through-a-html-form-1191f573b081
    # https://stackoverflow.com/questions/76490976/django-rest-how-to-create-url-view-to-extract-get-query-parameters-in-diff
    name = request.GET.get("name", "").strip()  # Strip spaces to avoid issues trim in Node
    year = request.GET.get("year", "").strip()
    subject = request.GET.get("subject", "").strip()
    # https://www.w3schools.com/django/django_queryset_filter.php
    
    class_rooms = ClassRoom.objects.all()  # Get all ClassRoom objects https://www.w3schools.com/django/django_queryset_get.php
    
    if subject: #Searchg By Subject
        class_rooms = class_rooms.filter(subject__icontains=subject)  #search
    
    
    if name: #Searchg By Subject
        class_rooms = class_rooms.filter(name__icontains=name)  #search

        
    if year.isdigit():  # data type is number before Filter
        class_rooms = class_rooms.filter(year=int(year))
    elif year:  # If year is provided but not a number, show an error
        class_rooms = ClassRoom.objects.none()  # Return an empty queryset

    return render(request, "aboutus.html", {"class_rooms": class_rooms, "search_name": name, "search_year": year,"search_subject":subject,})

