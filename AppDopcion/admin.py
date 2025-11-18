from django.contrib import admin
from .models import Animal
from .models import Contacto
# No es necesario registrar User, ya que Django lo hace automáticamente

# Registra tus modelos personalizados
admin.site.register(Animal)
admin.site.register(Contacto)
