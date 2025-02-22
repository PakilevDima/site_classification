from django.db import models

# Create your models here.

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.png', '.jpg', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Image(models.Model):
    MODEL_CHOICES = [
        ('rn50', 'ResNet50'),
        ('v16', 'Vgg16')
    ]
    image_file = models.FileField(upload_to='files/',
                                  validators=[validate_file_extension])

    model_classification = models.CharField(max_length=60,
                                            choices=MODEL_CHOICES,
                                             name='model',
                                             verbose_name='Модель для классификации картинки'
                                             )

