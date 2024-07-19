from django.urls import path
from . import views
urlpatterns = [
    path('',views.page,name='notes'),
    path('show_note/',views.show_note,name='show_note'),
    path('save_chat/',views.save_chat,name='save_chat'),
]

