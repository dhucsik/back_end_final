from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "home"),
    path('city/', views.city, name = "city"),
    path('sport/', views.sport, name = "sport"),
    path('university/', views.university, name = "university"),
    path('tradition/<slug:tradition_slug>', views.show_tradition, name='show'),
    path('foods/', views.food, name='foods'),
    path('feedback/', views.feedback, name = 'feedback'),
    path('feedback/upload/', views.upload, name = 'upload-book'),
    path('feedback/update/<int:book_id>', views.update_book),
    path('feedback/delete/<int:book_id>', views.delete_book),
    path('login/', views.signin, name = "login"),
    path('send/', views.send_message)
    ]