from django.db import models

# Create your models here.

class HomeSection(models.Model): # secciones de la pagina home
    tittle = models.CharField(max_length=50)
    subTittle = models.CharField(max_length=50)
    content = models.CharField(max_length=4096)


class HomeFields(models.Model): # campos de home
    tittle = models.CharField(max_length=50)
    subTittle = models.CharField(max_length=200)
    faceImg = models.ImageField(upload_to="core/assets/img/")
    content = models.CharField(max_length=100, blank=True)

