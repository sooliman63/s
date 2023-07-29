from django.urls import path
from . import views
urlpatterns = [
    # path('',views.index),
    path('',views.home,name=''),
    path('about/',views.about,name='about'),
    path('student/',views.student,name='student'),
]
