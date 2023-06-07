from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/categories/%y/%m/%d/', blank=True)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Menu(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='media/meals/%y/%m/%d/', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    preparation_time = models.CharField(max_length=10)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'), )

    @staticmethod
    def get_products_by_id(ids):
        return Menu.objects.filter (id__in=ids)

    @staticmethod
    def get_all_products():
        return Menu.objects.all()


    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Menu.objects.filter (category=category_id)
        else:
            return Menu.get_all_products();

    def __str__(self):
        return self.name

 
class Booking(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=14)
    date = models.DateField()
    time = models.TimeField()
    no_of_persons = models.IntegerField(default=1)
    
    def __str__(self):
        return self.name
    

class Feature(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    body = models.TextField(max_length=100)
    image = models.ImageField(upload_to='testimonials/%y/%m/%d/', blank=True)

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.email