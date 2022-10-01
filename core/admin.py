from django.contrib import admin
from .models import \
    Pessoa, \
    Marca, \
    Veiculo, \
    Parametro, \
    MovRotativo, \
    Mensalista, \
    MovMensalista


class MovRotativoAdmin(admin.ModelAdmin):
    list_display = (
        'checkin',
        'checkout',
        'valor_hora',
        'pago',
        'veiculo',
        'horas_total',
        'total')

    def veiculo(self, obj):
        return obj.veiculo

class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ('mensalista', 'dt_pgto', 'total')

    def mensalista(self, obj):
        return obj.mensalista

admin.site.register(Pessoa)
admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Parametro)
admin.site.register(MovRotativo, MovRotativoAdmin)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovMensalistaAdmin)