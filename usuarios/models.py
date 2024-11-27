from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, 
    AbstractBaseUser, 
    PermissionsMixin
)
# Create your models here.

class UsuarioManager(BaseUserManager):
    
    def create_user(self, email, password=None):
        usuario = self.model(
            email=self.normalize_email(email),
        )

        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)

        usuario.save(using=self._db)
        return usuario
    
    def create_superuser(self, email, password=None):
        usuario = self.create_user(
            email,
            password=password,
        )

        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True

        usuario.set_password(password)

        usuario.save()
        return usuario

class Usuario(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        unique=True,
        verbose_name='E-mail',
        max_length=255,
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Está ativo',
    )

    is_staff = models.BooleanField(
        default=False,
        verbose_name='É da equipe de desenvolvimento',
    )

    is_superuser = models.BooleanField(
        default=False,
        verbose_name='É superuser',
    )

    USERNAME_FIELD = 'email'

    objects = UsuarioManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        db_table = 'usuario'

    def __str__(self):
        return self.email
    
from django.db import models

class Newsletter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.email}"
    
class Contact(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return f"{self.nome} {self.sobrenome} - {self.data}"