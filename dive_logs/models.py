from django.db import models

# Create your models here.

class Dive_Site(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text

class Diver(models.Model):
    """Something specific learnt about the Topic."""
    dive_site = models.ForeignKey(Dive_Site, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Divers'

    def __str__(self):
        """Return a string representation of this model"""
        return f"{self.text[:50]}..."
    