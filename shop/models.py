from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0, null=True)

    def __str__(self):
        return f'{self.name}, {self.price}'


class Purchase(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    date_purchase = models.DateTimeField('date purchase')

    def __str__(self):
        return self.name
