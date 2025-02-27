from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('', lambda request: HttpResponse("Welcome to the Chatbot API!"), name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('chatbot.urls')),  # This line is crucial
]
