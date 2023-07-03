from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Place(models.Model):
    locations_in_lagos = (
        ("mainland", "Mainland"),
        ("island", "Island")
    )

    name = models.CharField(max_length=100, blank=False)
    slug = models.SlugField(null=True, unique=True)
    address = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=50, choices=locations_in_lagos, default='Mainland')


    def get_absolute_url(self):
        return reverse("place_detail", kwargs={"slug": self.slug})
    

    def get_google_maps_str(self, *args, **kwargs):
        # To create a string to get a location on google maps eg.. ikeja+city+mall
        name_list = self.name.strip().split()
        name_part = "+".join(name_list)
        address_list = self.address.replace(",", " ").replace(".", " ").strip().split()
        address_part = "+".join(address_list)

        final_map_str = f"{name_part}+{address_part}"
        return final_map_str


    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    

class BucketList(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    places = models.ManyToManyField(Place)

    def __str__(self):
        return self.user.email
    