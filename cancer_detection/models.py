from django.db import models

# Create your models here.

class contactForm(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length = 100,null=True)
    mobile_no = models.IntegerField(null=True)
    message = models.TextField()

    def __str__(self):
        return self.email
