from django.urls import path, include
from form.views import ListView, DetailView

app_name = 'form'

urlpatterns = [
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('', ListView.as_view(), name='index')
]
