## Notas

Probar métodos del crud:

- [Iniciar sesión para interactuar con el proyecto](#entrar-sesion-interactiva)
- [Crear un registro](#crear-registro)

<a name="entrar-sesion-interactiva"></a>

## Sesión interactiva

```bash
python manage.py shell
```

<a name="crear-registro"></a>

## Crear registro

1era forma:

```py
>>> from web.models import Product
>>> p = Product(name="super8", price=33.99, stock=10)
>>> p.save()
```

2da forma:

```python
>>> from web.models import Product
>>> Product.objects.create(name="super8", price=33.99, stock=10)
<Product: Product object (1)>
```
