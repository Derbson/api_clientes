from django.contrib import admin
from .models import Cliente


class ListarCliente(admin.ModelAdmin):
    list_display = ("id", "nome", "email","cpf","celular","ativo")
    list_display_links = ("id","nome")
    search_fields = ("nome",)
    list_editable = ("ativo",)


admin.site.register(Cliente, ListarCliente)
