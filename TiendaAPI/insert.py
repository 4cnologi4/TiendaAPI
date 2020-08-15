# para insertar datos desde el archivo
# python manage.py shell < TiendaAPI/insert.py

from TiendaAPI.models import Products as P

"""
P.objects.create(pid='1', name='agua', value=20, discount_value=2, stock=10)
P.objects.create(pid='2', name='cereal', value=30, discount_value=2, stock=30)
P.objects.create(pid='3', name='cerveza', value=40.90, stock=100)
P.objects.create(pid='4', name='pan', value=2.50, discount_value=2, stock=5)
P.objects.create(pid='5', name='arroz', value=12, stock=20)
"""
for p in P.objects.all():
    print(p.name + " precio: " + str(p.value))
