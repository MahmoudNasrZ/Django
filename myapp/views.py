from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import ClassArea,ClassRoom

# Create your views here.
def home(request):
    # return HttpResponse("Hello, world! This is the home page.")
    return render(request, "home.html")  # Renders the home template


def contact(request,contact_id):
    # return HttpResponse(f"Hello, world! This is the {name} page.")
        # Retrieve all class areas from the database
    class_areas = ClassArea.objects.all()
    class_rooms = ClassRoom.objects.all()  # Get all ClassRoom objects
    context = {
        "class_id": contact_id,
        "description":"this is a class this just a filler to check the funcationality of the if function inside Contact.html",
        "class_areas" : class_areas,
        "class_rooms":class_rooms  
               }  # Passes 'name' to template
    return render(request, "contact.html", context)

def about_us_view(request):
    name = request.GET.get("name", "").strip()  # Strip spaces to avoid issues
    year = request.GET.get("year", "").strip()

    class_rooms = ClassRoom.objects.all()  # Get all ClassRoom objects

    if name:
        class_rooms = class_rooms.filter(name__icontains=name)  # Case-insensitive search

    if year.isdigit():  # Ensure year is a number before filtering
        class_rooms = class_rooms.filter(year=int(year))
    elif year:  # If year is provided but not a number, show an error
        class_rooms = ClassRoom.objects.none()  # Return an empty queryset

    return render(request, "aboutus.html", {"class_rooms": class_rooms, "search_name": name, "search_year": year})

