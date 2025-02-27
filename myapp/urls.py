from django.urls import path
from .views import home, contact  # Import your views 

urlpatterns = [
    #Routes in = Node 
    path("", home, name="home"),  # Root URL ("/") = My Home Function in views 
    # path("contact/", contact , name="contact"),  # "/contact/" ("/contact") = My contact Function in views
path('contact/<int:contact_id>/', contact, name='contact'),
]
