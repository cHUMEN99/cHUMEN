from django.db import models

class articls(models.Model):
    title=models.CharField('Назва:',max_length=50)
    anons=models.CharField('Опис:',max_length=250)
    haracter=models.TextField('Характеристики:')
    date=models.DateTimeField('Дата публцікації')
    image = models.ImageField(upload_to='images/')
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Головна сторінка "
        verbose_name_plural="Головна сторінка "

