from django.contrib import admin
from django.urls import path
from usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('ingressos-parques/', views.parques, name='parques'),
    path('ingressos-esportivos/', views.esportivos, name='esportivos'),
    path('assessoria-consular/', views.consular, name='consular'),
    path('contato/', views.contact, name='contato'),
    path('mundial-de-clubes/', views.mundialclubes, name='mundialclubes'),
    path('voos-e-hoteis/', views.voosehoteis, name='voosehoteis'),
    path('aluguel-de-veiculo/', views.aluguelcarros, name='aluguelcarros'),
    path('passeios-e-tours/', views.tours, name='tours'),
    path('cambio/', views.cambio, name='cambio'),
    path('newsletter-signup/', views.newsletter_signup, name='newsletter_signup'),    # Adicione outras rotas conforme necessário
]