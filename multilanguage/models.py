from django.db import models
from django.urls import reverse

class Details(models.Model):
    class Meta:
        verbose_name = 'Detail'
        verbose_name_plural = 'Details'
        
    name = models.CharField(max_length=255)
    slug =models.SlugField(unique=True)
    text = models.TextField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("lanapp:details", kwargs={'slug': self.slug})