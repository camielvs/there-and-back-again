from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

# Create your models here.
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Destination(models.Model):
    country = models.CharField(max_length=100)
    date = models.DateField()
    rating = models.IntegerField(validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ])
    comment = models.TextField(max_length=250)
    picture_upload = models.ImageField(default=None, blank=True, null=True, upload_to="main_app/static/images")
    picture_url = models.CharField(default='https://www.pngitem.com/pimgs/m/775-7750535_travel-globe-png-free-download-transparent-png.png', blank=True, null=True, max_length=100)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'destination_id':self.id})


class Location(models.Model):
    date_visited = models.DateField()
    location = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ])
    comment = models.TextField(max_length=250)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_location_display()} on {self.date}"

    class Meta:
        ordering = ['-date_visited'] #sorts by date: ascending / (-) descending