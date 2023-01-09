from django import forms
from .models import ImageModel


class ImageUploadModelForm(forms.ModelForm):
    """form for the image model"""
    class Meta:
        model = ImageModel
        fields = ('image',)