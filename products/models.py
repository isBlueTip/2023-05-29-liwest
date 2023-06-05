from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    seq = models.IntegerField()

    def __str__(self):
        return self.name


class ProductGroup(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    seq = models.IntegerField()

    def __str__(self):
        return self.name


class Product(models.Model):
    group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.name
