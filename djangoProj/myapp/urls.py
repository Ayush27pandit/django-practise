from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert_teacher/',views.insert_teacher,name='insert_teacher'),
    path('showpage/',views.show_page,name='showpage'),
    path('edit/<int:pk>',views.EditPage,name='editpage'),
    path('update/<int:pk>',views.updateData,name='update')
  
]