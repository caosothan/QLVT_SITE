

from django.urls import path, include
from . import views



app_name = "home"


urlpatterns = [
    path('', view = views.createHomepage),
    path('home/', view = views.createHomepage, name = 'home'),
    path("register/", view = views.register, name = "register"), 
    path("login/", view = views.login , name = "login"),
    path("logout/", view = views.logout, name = "logout"),
    path("contact/", view = views.contact, name = "contact"),
    path("", include("APP_QLVT.urls"))

]


