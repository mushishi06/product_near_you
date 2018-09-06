import uuid

from django.db import models


class Shops(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, blank=False)
    lat = models.FloatField(default=0.0)
    lng = models.FloatField(default=0.0)

    def __str__(self):
        """Magic func for print in the admin page."""
        return self.name

    @classmethod
    def get(cls, **kwargs):
        """Get all Items."""
        return cls.objects.filter(**kwargs)


class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shop = models.ForeignKey(Shops, related_name='shops', on_delete=models.CASCADE, blank=False)
    title = models.CharField(max_length=200, blank=False)
    popularity = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)

    # user friendly way to display the object
    def __repr__(self):
        return self.title


class Tags(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag = models.CharField(max_length=200, blank=False)

    def __repr__(self):
        # a user friendly way to view our objects in the terminal
        return self.tag


# Model for poll options
class Taggings(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shop_id = models.ForeignKey(Shops, on_delete=models.CASCADE, blank=False)
    tag_id = models.ForeignKey(Tags, on_delete=models.CASCADE, blank=False)
