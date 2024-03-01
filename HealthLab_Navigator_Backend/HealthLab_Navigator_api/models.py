from django.db import models


# Модели для медицинских учреждений
class MedicalInstitution(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название медицинского учреждения',
        null=False,
        blank=False
    )
    main_phone = models.CharField(
        max_length=50,
        verbose_name='Общий телефон',
        null=False,
        blank=False
    )
    website = models.URLField(
        max_length=200,
        verbose_name='Сайт',
        null=False,
        blank=False
    )
    description = models.TextField(
        verbose_name='Описание',
        null=False,
        blank=False
    )
    is_oms_available = models.BooleanField(
        verbose_name='Доступно по ОМС',
        default=False,
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = 'Медицинское учреждение'
        verbose_name_plural = 'Медицинские учреждения'


class MedicalInstitutionBranch(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название филиала',
        null=True,
        blank=True
    )
    address = models.CharField(
        max_length=200,
        verbose_name='Адрес филиала',
        null=False,
        blank=False
    )
    phone = models.CharField(
        max_length=50,
        verbose_name='Телефон филиала',
        null=False,
        blank=False
    )
    medical_institution = models.ForeignKey(
        MedicalInstitution,
        on_delete=models.CASCADE,
        verbose_name='Медицинское учреждение',
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = 'Филиал медицинского учреждения'
        verbose_name_plural = 'Филиалы медицинского учреждения'


# Модели для медицинских услуг
research_material_choices = (
    ('blood', 'Кровь'),
    ('urine', 'Моча'),
    ('feces', 'Фекалии'),
    ('smear', 'Мазок'),
    ('biopsy', 'Биопсия'),
    ('other', 'Другое')
)


class MedicalService(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название медицинской услуги',
        null=False,
        blank=False
    )
    description = models.TextField(
        verbose_name='Описание',
        null=False,
        blank=False
    )
    research_material = models.CharField(
        max_length=50,
        choices=research_material_choices,
        verbose_name='Материал исследования',
        null=False,
        blank=False
    )
    government_code_804n = models.CharField(
        max_length=12,
        verbose_name='Код услуги по 804н',
        null=False,
        blank=True
    )

    class Meta:
        verbose_name = 'Медицинская услуга'
        verbose_name_plural = 'Медицинские услуги'


class ServiceInMedicalInstitution(models.Model):
    medical_institution = models.ForeignKey(
        MedicalInstitution,
        on_delete=models.CASCADE,
        verbose_name='Медицинское учреждение',
        null=False,
        blank=False
    )
    medical_service = models.ForeignKey(
        MedicalService,
        on_delete=models.CASCADE,
        verbose_name='Медицинская услуга',
        null=False,
        blank=False
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена',
        null=False,
        blank=False
    )
    time_to_complete = models.DurationField(
        verbose_name='Время выполнения',
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = 'Медицинское учреждение в услуге'
        verbose_name_plural = 'Медицинские учреждения в услугах'
