from django.db.models import CharField, Model, ForeignKey, CASCADE, IntegerField, ImageField, SlugField


class Product(Model):
    name = CharField(max_length=155)
    slug = SlugField(max_length=155, unique=True)
    category = ForeignKey('apps.Category', on_delete=CASCADE, related_name='products')
    price = IntegerField()
    description = CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name



class ProductSpecification(Model):
    product = ForeignKey('apps.Product', on_delete=CASCADE, related_name='specs')
    name = CharField(max_length=100)
    value = CharField(max_length=255)


class ProductImage(Model):
    product = ForeignKey('apps.Product', on_delete=CASCADE, related_name='images')
    image = ImageField(upload_to='product_images/%Y/%m/%d')
