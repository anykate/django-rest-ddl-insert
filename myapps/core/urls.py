from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path('', views.savecolor, name='save_color_data'),
    path('api/colornew/', views.savecolor_api, name='save_color_data_api'),
]
