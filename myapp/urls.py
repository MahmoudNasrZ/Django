from django.urls import path
from .views import home, contact,about_us_view  # Import your views 

urlpatterns = [
    #Routes in = Node 
    path("", home, name="home"),  # Root URL ("/") = My Home Function in views 
    path("aboutus/", about_us_view , name="about_us"), 
path('contact/<int:contact_id>/', contact, name='contact'), # "/contact/" ("/contact") = My contact Function in views
]
