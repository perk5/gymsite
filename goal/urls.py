from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [

    path('', views.index, name='index'),
    path('workouts/', views.workouts, name='workouts'),
    path('Nutrition/', views.nutrition, name='nutrition'),
    path('About/', views.about, name='about'),
    path('Contact/', views.contact, name='contact'),
    path('submited', views.submitted, name='submit')
]

