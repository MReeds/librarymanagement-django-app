from django.urls import reverse
from django.db import models


class Library (models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("library ")
        verbose_name_plural = ("libraries")

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("library _detail", kwargs={"pk": self.pk})
