from django.db.models import CharField, CASCADE
from mptt.models import MPTTModel, TreeForeignKey

class MpttModel(MPTTModel):
    name = CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete= CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']