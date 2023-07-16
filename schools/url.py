from django.urls import path
from . import views

app_name = 'schools'

urlpatterns = [
    path('map/', views.school_map, name='school_map'),
    path('schools/', views.get_schools, name='get_schools'),
    path('schools/<int:school_id>/', views.get_school, name='get_school'),
]
