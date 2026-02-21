from django.db.models import SlugField, ImageField, JSONField, CASCADE, CharField
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = CharField(max_length=55, unique=True)
    slug = SlugField(max_length=55, unique=True, editable=False)
    image = ImageField(upload_to='categories/', blank=True, null=True)
    parent = TreeForeignKey('self', on_delete= CASCADE, null=True, blank=True, related_name='children')
    attribute = JSONField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
