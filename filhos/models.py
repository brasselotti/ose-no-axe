from django.contrib.auth.models import AbstractUser
from django.db import models


class Filho(AbstractUser):
    # Removemos username/password do AbstractUser e usamos os nativos
    # O AbstractUser já traz: username, password, first_name, last_name, email, is_staff, is_active

    # Identificação complementar
    nome = models.CharField(max_length=150, verbose_name="Nome Completo")
    telefone = models.CharField(max_length=20, blank=True)

    # Endereço
    endereco = models.CharField(max_length=255, blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    cep = models.CharField(max_length=10, blank=True)

    # Informações do Médium
    data_nascimento = models.DateField(null=True, blank=True)
    data_bori = models.DateField(null=True, blank=True)

    # Checkbox para liberar os dados da feitura
    filho_iniciado = models.BooleanField(default=False, verbose_name="Filho Iniciado?")

    # Dados da iniciação
    data_iniciacao = models.DateField(null=True, blank=True, verbose_name="Data da Iniciação")
    ordem_posto = models.CharField(max_length=100, null=True, blank=True, verbose_name="Ordem/Posto")
    orixa = models.CharField(max_length=100, null=True, blank=True, verbose_name="Orixá")
    orunko = models.CharField(max_length=100, null=True, blank=True, verbose_name="Orunkó")
    nome_ere = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nome do Erê")
    madrinha_padrinho = models.CharField(max_length=150, null=True, blank=True, verbose_name="Madrinha/Padrinho")
    mae_pai_pequeno = models.CharField(max_length=150, null=True, blank=True, verbose_name="Mãe/Pai Pequeno")

    # Perfil — usamos is_staff do AbstractUser para ADM, mas criamos campo explícito também
    eh_administrador = models.BooleanField(default=False, verbose_name="É administrador?")

    class Meta:
        verbose_name = "Filho"
        verbose_name_plural = "Filhos"

    def __str__(self):
        return self.nome or self.username