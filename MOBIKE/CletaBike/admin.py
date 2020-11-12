from django.contrib import admin
from .models import Bicicleta
from .models import Administrativo
from .models import Usuario
from .models import RegistroPago
from .models import Arriendo
# Register your models here.

class bicicletaAdmin(admin.ModelAdmin):
    list_display   = ['modelo',
                      'patente'] 

    list_display_filter = ['modelo',
                           'patente']
                           
    search_fields       = ['modelo',
                           'patente',
                           'fechaIngreso',
                           'desbloqueo']
admin.site.register(Bicicleta, bicicletaAdmin)   

class administrativoAdmin(admin.ModelAdmin):
    list_display   = ['rutAdmin',
                      'nomAdmin',
                      'correo',
                      'telefono',
                      'direccion'] 

    list_display_filter = ['rutAdmin',
                           'nomAdmin']
                           
    search_fields       = ['rutAdmin',
                           'nomAdmin',
                           'correo']
admin.site.register(Administrativo, administrativoAdmin)   

class usuarioAdmin(admin.ModelAdmin):
    list_display   = ['dniUser',
                      'rutUser',
                      'nomUser',
                      'telefono',
                      'correo',
                      'medioPago'] 

    list_display_filter = ['rutUser',
                           'medioPago']
                           
    search_fields       = ['rutUser',
                           'nomUser',
                           'correo',
                           'correo']
admin.site.register(, administrativoAdmin)

class registroPagoAdmin(admin.ModelAdmin):
    list_display   = ['dniUser'] 

    list_display_filter = ['fechaPago',
                           'metodoPago']
                           
    search_fields       = ['fechaPago',
                           'metodoPago']
admin.site.register(RegistroPago, registroPagoAdmin)

class arriendoAdmin(admin.ModelAdmin):
    list_display   = ['rutUser',
                      'idRegistroPago',
                      'idBicleta',
                      'fechaPago',
                      'horaArriendo'] 

    list_display_filter = ['rutAdmin',
                           'nomAdmin']
                           
    search_fields       = ['idRegistroPago',
                           'idBicleta',
                           'correo',
                           'fechaPago']
admin.site.register(Arriendo, arriendoAdmin)