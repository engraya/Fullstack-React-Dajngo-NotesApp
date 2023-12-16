from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name="api-Overview" ), 
    path('notesList', views.notesList, name="notesList"),
    path('noteDetail/<str:pk>/', views.noteDetail, name="noteDetail"),
    path('noteCreate', views.noteCreate, name="noteCreate"),
    path('noteUpdate/<str:pk>', views.noteUpdate, name="noteUpdate"),
    path('noteDelete/<str:pk>', views.noteDelete, name="noteDelete"),
]
