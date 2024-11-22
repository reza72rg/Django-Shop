from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal
from .tools import UploadToPathAndRename
from .setting_models import MainModel


class ProductStatusType(models.IntegerChoices):
    publish = 1, ("نمایش")
    draft = 2, ("عدم نمایش")


class ProductCategoryModel(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True, unique=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.title


# Create your models here.
class ProductModel(MainModel):
    user = models.ForeignKey("accounts.User", on_delete=models.PROTECT)
    category = models.ManyToManyField(ProductCategoryModel)
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True, unique=True)
    image = models.ImageField(upload_to = UploadToPathAndRename("product/img/"), default = 'default/product-image.png')
    description = models.TextField()
    brief_description = models.TextField(null=True, blank=True)

    stock = models.PositiveIntegerField(default=0)
    status = models.IntegerField(choices=ProductStatusType.choices, default=ProductStatusType.draft.value)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    discount_percent = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    avg_rate = models.FloatField(default=0.0)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_price(self):
        discount_amount = self.price * Decimal(self.discount_percent / 100)
        discounted_amount = self.price - discount_amount
        discounted_amount_rounded = round(discounted_amount)

        # Format the rounded discounted price with commas
        return "{:,}".format(discounted_amount_rounded)

    def get_original_price(self):
        return "{:,}".format(self.price)

    def is_discounted(self):
        return self.discount_percent != 0

    def is_published(self):
        return self.status == ProductStatusType.publish.value

    def is_published(self):
        return self.status == ProductStatusType.publish.value


    class Meta:
        ordering = ["-created_date"]

class ProductImageModel(MainModel):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="product_images")
    file = models.ImageField(upload_to=UploadToPathAndRename("product/extra-img/"))

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]