from django.urls import path
from .views import upload_image


app_name = 'text_to_img'

urlpatterns = [
    path('upload-image/', upload_image, name='upload_image'),
]