from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(
        max_length=200, 
        verbose_name='Название покемона'
        )
    img_url = models.ImageField(
        upload_to='pokemon_images',
        blank=True,
        verbose_name='Путь к картинке'
        )
    title_ru = models.CharField(
        max_length=200, 
        blank=True, 
        verbose_name='Русское название'
        )
    title_en = models.CharField(
        max_length=200, 
        blank=True, 
        verbose_name='Английское название'
        )
    title_jp = models.CharField(
        max_length=200, 
        blank=True, 
        verbose_name='Японское название'
        )
    description = models.TextField(null=True, blank=True)
    previous_evolution = models.ForeignKey('self',
                                           verbose_name='Из кого эволюционирует',
                                           null=True,
                                           blank=True,
                                           related_name='next_evolutions',
                                           on_delete=models.SET_NULL)
    next_evolution = models.ForeignKey('self',
                                       verbose_name='В кого эволюционирует',
                                       null=True,
                                       blank=True,
                                       related_name='previous_evolutions',
                                       on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField()
    disappeared_at = models.DateTimeField()
    level = models.IntegerField(null=True)
    health = models.IntegerField(null=True)
    strength = models.IntegerField(null=True)
    defence = models.IntegerField(null=True)
    stamina = models.IntegerField(null=True)
