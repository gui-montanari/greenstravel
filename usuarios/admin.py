from django.contrib import admin
from usuarios.models import Usuario
from .models import Newsletter, Contact

admin.site.register(Usuario)

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_subscribed')
    search_fields = ('name', 'email')
    list_filter = ('date_subscribed',)
    ordering = ('-date_subscribed',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email', 'telefone', 'data')
    search_fields = ('nome', 'sobrenome', 'email', 'telefone')
    list_filter = ('data',)
    
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'