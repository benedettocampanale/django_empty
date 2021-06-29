from django.db import models
from django.db.models import Choices


class Test(models.Model):
    class Kind(Choices):
        KEY_1 = "Value 1"
        KEY_2 = "Value 2"

    kind = models.CharField(verbose_name="Tipo", max_length=255, choices=Kind.choices)


# per ricavare il codice del modello Insegnamento: dj inspectdb --database=uni universita_insegnamento
# - rinomina il modello
# - togli le FK

# Quando usi questo modello devi fare: Insegnamento.objects.using('uni').all()
class Insegnamento(models.Model):
    ssd = models.CharField(max_length=128)
    nome = models.CharField(max_length=255)
    tipo_insegnamento = models.SmallIntegerField(blank=True, null=True)
    periodo_attivazione = models.SmallIntegerField(blank=True, null=True)
    anno_di_corso = models.SmallIntegerField(blank=True, null=True)
    area_linguistica = models.CharField(max_length=255)
    cfu = models.IntegerField()
    ore = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'universita_insegnamento'

    def save(self, *args, **kwargs):
        raise

    def delete(self, *args, **kwargs):
        raise
