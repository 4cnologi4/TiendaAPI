# para insertar datos desde el archivo
# python manage.py shell < TiendaAPI/insert.py

from TiendaAPI.models import Products as P
"""
P.objects.create(name='agua', value=20, discount_value=2, stock=10)
P.objects.create(name='cereal', value=30, discount_value=2, stock=30)
P.objects.create(name='cerveza', value=40.90, stock=100)
P.objects.create(name='pan', value=2.50, discount_value=2, stock=5)
P.objects.create(name='arroz', value=12, stock=20)
"""

def printData():
    for p in P.objects.all():
        print(p.name + " precio: " + str(p.value))
