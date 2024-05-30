from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='images')
    publish = models.BooleanField(default=False)
    date = models.DateTimeField()

    def __str__(self):
        return self.title