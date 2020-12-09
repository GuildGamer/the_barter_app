from django.db import models
from django.conf import settings

CATEGORY_CHOICES = (
    ('MF', 'Men\'s Fashion'),
    ('WF', 'Women\'s Fashion'),
    ('CJ', 'Clothing and Jewelry'),
    ('FO', 'Food'),
    ('WD', 'Web & Mobile Development'),
    ('ED', 'Electronics and Devices'),
    ('AS', 'Art and Stationary')
)

class Item(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    estimated_value = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    image_1 = models.ImageField(blank=True, null=True)
    image_2 = models.ImageField(blank=True, null=True)
    image_3 = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

class TradeItem(models.Model):

    pass
class Inventory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username