from django.db import models

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


# Create your models here.
class ImageModel(models.Model):
    image = models.ImageField(upload_to='images', null=False, blank=False)
    uploaded = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        super(ImageModel, self).delete(*args, **kwargs)
        storage.delete(path)

    def __str__(self):
        return str(self.image.name)


@receiver(pre_delete, sender=ImageModel)
def delete_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)
