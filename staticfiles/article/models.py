from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    title=models.CharField(max_length=20,verbose_name="Basliq")
    content=RichTextField(verbose_name="Kontent")
    create_date=models.DateTimeField(auto_now_add=True,verbose_name="Yaradilma tarixi")
    image=models.FileField(null=True,blank=True,verbose_name='Sekil')
    def __str__(self):
        return self.title
