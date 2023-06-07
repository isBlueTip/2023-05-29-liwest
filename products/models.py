from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)
    seq = models.PositiveSmallIntegerField(unique=True, blank=False, null=False)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.seq:
            self.seq = getattr(ProductCategory.objects.order_by("seq").last(), "seq", 0)
        if ProductCategory.objects.filter(seq=self.seq).exists():
            objs = ProductCategory.objects.filter(seq__gte=self.seq).order_by("seq")
            for obj in objs:
                obj.seq += 1
                obj.save()  # TODO refactor, inefficient but works

        super().save(force_insert, force_update, using, update_fields)


class ProductGroup(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)
    seq = models.PositiveSmallIntegerField(unique=True, blank=False, null=False)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.seq:
            self.seq = getattr(ProductGroup.objects.order_by("seq").last(), "seq", 0)
        if ProductCategory.objects.filter(seq=self.seq).exists():
            objs = ProductGroup.objects.filter(seq__gte=self.seq).order_by("-seq")
            for obj in objs:
                obj.seq += 1
                obj.save()  # TODO refactor, inefficient but works

        super().save(force_insert=False, force_update=False, using=None, update_fields=None)


class Product(models.Model):
    group = models.ForeignKey(ProductGroup, on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=False, null=False)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False,
        validators=[
            MinValueValidator(limit_value=0),
        ],
    )
    hidden = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return self.name
