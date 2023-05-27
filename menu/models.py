from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    # slug = models.CharField(max_length=100, db_index=True, unique=True, verbose_name='Ссылка')

    @staticmethod
    def get_all_categories():
        return Category.objects.all()


    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    description = models.TextField(blank=True, verbose_name='Описание')
    # slug = models.CharField(max_length=100, db_index=True, unique=True, verbose_name='Ссылка')
    image = models.ImageField(upload_to='uploads/products/')
    

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        # index_together = (('id', 'slug'), )

    def __str__(self):
        return self.name

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter (id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()


    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter (category=category_id)
        else:
            return Product.get_all_products();

    def __str__(self):
        return self.name

 

