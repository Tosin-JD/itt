from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import CreateView

# import my forms and models
from .forms import ImageUploadModelForm
from .models import ImageModel


# import libraries for images and image-to-text
from PIL import Image
from pytesseract import pytesseract
import tempfile

# import my personal code
from .handle_text import clean_text


# Create your views here.
class IndexView(CreateView):
    form_class = ImageUploadModelForm
    template_name = 'text_to_img/index.html'
    # success_url = reverse('index')

    def get_success_url(self):
        return reverse('text_to_img:success')


# method to upload image
def upload_image(request):
    context = dict()
    if request.method == 'POST':
        form = ImageUploadModelForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_image = Image.open(request.FILES['image'])
            """I am not collecting any user information
            so there is no need to save the form.""" 
            # form.save()

            # I am handling files that may be large
            with tempfile.TemporaryFile() as temp_file:
                for chunk in request.FILES['image'].chunks():
                    temp_file.write(chunk)
                image = Image.open(temp_file)
                image_text = pytesseract.image_to_string(image)

                # clean the text and remove unneccery characters
                image_text = clean_text(image_text)
            context.update({'image_text':image_text})
    else:
        form = ImageUploadModelForm()

    context.update({'form': form})
    return render(request, 'text_to_img/index.html', context=context)

