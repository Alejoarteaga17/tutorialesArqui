
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

def home(request):
    return HttpResponse("Bienvenido al backend del proyecto")

# The project layout places the api urls inside the todoapp app package.
# Use the full dotted path so Python can import the module reliably.
urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]
