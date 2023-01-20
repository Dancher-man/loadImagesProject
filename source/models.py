from django.db import models


class Persons(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'persons'
        verbose_name = 'Имя человека'
        verbose_name_plural = 'Имена людей'


class Images(models.Model):
    photo = models.ImageField(verbose_name="Фото", upload_to="photos/")
    geolocation = models.CharField(max_length=250, verbose_name='Геолокация', null=True, blank=True)
    description = models.CharField(max_length=255, verbose_name='Описание', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    persons_names = models.ManyToManyField(Persons,
                                           related_name='persons_name',
                                           through='source.PersonAndImages',
                                           through_fields=('photo_pk', 'person_pk'),
                                           blank=True)

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'images'
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class PersonAndImages(models.Model):
    photo_pk = models.ForeignKey(Images, on_delete=models.CASCADE, related_name='person_photo')
    person_pk = models.ForeignKey(Persons, on_delete=models.CASCADE, related_name='person_name')

    class Meta:
        db_table = 'persons_and_images'
