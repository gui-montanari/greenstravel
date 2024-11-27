from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from .models import Newsletter, Contact
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Create your views here.
def index(request):
    return render(request, 'index.html')

def parques(request):
    return render(request, 'parques.html')

def esportivos(request):
    return render(request, 'esportivos.html')

def consular(request):
    return render(request, 'consular.html')

def voosehoteis(request):
    return render(request, 'vooehotel.html')

def aluguelcarros(request):
    return render(request, 'aluguelcarros.html')

def tours(request):
    return render(request, 'tours.html')

def mundialclubes(request):
    return render(request, 'mundialclubes.html')

def contact(request):
    return render(request, 'contact.html')

def cambio(request):
    return render(request, 'cambio.html')

def newsletter_signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f"Recebido: Nome={name}, Email={email}")  # Debug
        
        try:
            Newsletter.objects.create(name=name, email=email)
            messages.success(request, 'Inscrito com sucesso!')
        except Exception as e:
            print(f"Erro: {e}")  # Debug
            messages.error(request, 'Erro ao se inscrever')
            
    return redirect('index')

def contact(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email', '').lower()  # Converte email para minúsculo
        telefone = request.POST.get('telefone')
        mensagem = request.POST.get('mensagem')
        
        try:
            validate_email(email)
            Contact.objects.create(
                nome=nome,
                sobrenome=sobrenome,
                email=email,
                telefone=telefone,
                mensagem=mensagem
            )
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('contato')
            
        except (ValidationError, Exception) as e:
            return render(request, 'erro.html', {
                'mensagem_erro': 'Houve um problema ao enviar sua mensagem. Por favor, tente novamente.'
            })
    
    return render(request, 'contato.html')

def csrf_failure(request, reason=""):
    return render(request, 'erro.html', {
        'mensagem_erro': 'Erro de segurança. Por favor, tente novamente.'
    })