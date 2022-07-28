from shop.models import Item, Purchase
from django.utils import timezone

Item.objects.all()
i = Item(name='Notebook', price=100)
i.save()
i2 = Item(name='Iphone', price=200)
i2.save()
i3 = Item(name='Ram', price=300)
i3.save()
i4 = Item(name='Hub', price=50)
i4.save()
i5 = Item(name='Keyboard', price=70)
i5.save()

Item.objects.all()
i.name
i.price

Purchase.objects.all()
p = Purchase(item=i, name="Uluk", age=30, date_purchase=timezone.now())
p.save()
p1 = Purchase(item=i2, name="Veronica", age=20, date_purchase=timezone.now())
p1.save()
p2 = Purchase(item=i3, name="Bermet", age=21, date_purchase=timezone.now())
p2.save()
p3 = Purchase(item=i4, name="Edil", age=25, date_purchase=timezone.now())
p3.save()
p4 = Purchase(item=i5, name="Artur", age=17, date_purchase=timezone.now())
p4.save()
p5 = Purchase(item=i, name="Jibek", age=22, date_purchase=timezone.now())
p5.save()
p6 = Purchase(item=i2, name="Timur", age=32, date_purchase=timezone.now())
p6.save()
p7 = Purchase(item=i3, name="Vlad", age=25, date_purchase=timezone.now())
p7.save()
p8 = Purchase(item=i4, name="Aikena", age=21, date_purchase=timezone.now())
p8.save()
p9 = Purchase(item=i5, name="Victor Petrovich", age=88, date_purchase=timezone.now())
p9.save()

Purchase.objects.all()
p.name
p.item
