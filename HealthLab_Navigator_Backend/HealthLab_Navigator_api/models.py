from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

STATUS_FEEDBACK_CHOICES = [
    ('new', 'Новый'),
    ('in_progress', 'В обработке'),
    ('done', 'Выполнен'),

]
STATUS_CREATED_CHOICES = [
    ('new', 'Новый'),
    ('waiting', 'Ожидает подтверждения'),
    ('confirmed', 'Подтвержден'),
    ('rejected', 'Отклонен'),
]
USER_TYPE_CHOICES = [
    ('patient', 'Пациент'),
    ('medical_institution_agent', 'Агент медицинского учреждения'),
    ('moderator', 'Модератор'),
]


class Phone(models.Model):
    number = models.CharField(max_length=50, verbose_name='Номер телефона', null=False, blank=False, unique=True)
    description = models.TextField(verbose_name='Описание номера телефона', null=False, blank=True, default="")

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None):
        """
        Creates and saves a User with the given phone_number and password.
        """
        if not phone_number:
            raise ValueError("Users must have an phone number")

        user = self.model(
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            phone_number,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        # unique=True,
        null=True,
        blank=True
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения'
    )
    phone_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Номер телефона',
        null=False,
        blank=False
    )
    is_active = models.BooleanField(
        default=True
    )
    is_admin = models.BooleanField(
        default=False
    )
    is_staff = models.BooleanField(
        default=False
    )
    is_superuser = models.BooleanField(
        default=False
    )
    is_medical_agent = models.BooleanField(
        default=False
    )
    user_type = models.CharField(
        max_length=50,
        choices=USER_TYPE_CHOICES,
        verbose_name='Тип пользователя',
        null=False,
        blank=False,
        default='patient'
    )
    first_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Фамилия'
    )
    middle_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Отчество'
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.phone_number)  # Преобразуем номер телефона в строку для вывода


class Patient(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, verbose_name='Пользователь', null=True, blank=True)

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'


class Visiting(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, verbose_name='Пользователь', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания визита')


class Feedback(models.Model):
    email = models.EmailField(max_length=100, verbose_name='Email пользователя', null=False, blank=False)
    text = models.TextField(max_length=1000, verbose_name='Текст обращения', null=False, blank=False)
    create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания обращения')
    status = models.CharField(choices=STATUS_FEEDBACK_CHOICES, default='new', max_length=20,
                              verbose_name='Статус обращения')


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название города', null=False, blank=False)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class District(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название района', null=False, blank=False)
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name='Город',
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'


class MetroLine(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название линии метро', null=False, blank=False)
    color = models.CharField(max_length=100, verbose_name='Цвет линии метро', null=False, blank=False)

    class Meta:
        verbose_name = 'Линия метро'
        verbose_name_plural = 'Линии метро'


class MetroStation(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название станции метро', null=False, blank=False)
    line = models.CharField(max_length=100, verbose_name='Линия метро', null=False, blank=False)

    class Meta:
        verbose_name = 'Станция метро'
        verbose_name_plural = 'Станции метро'


class Street(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название улицы', null=False, blank=False)
    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE,
        verbose_name='Район',
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'


class Location(models.Model):
    latitude = models.CharField(max_length=50, verbose_name='Широта', null=True, blank=True)
    longitude = models.CharField(max_length=50, verbose_name='Долгота', null=True, blank=True)
    street = models.ForeignKey(Street, on_delete=models.SET_NULL, verbose_name='Улица', null=True, blank=True)
    house = models.CharField(max_length=10, verbose_name='Дом', null=True, blank=True)
    office = models.CharField(max_length=10, verbose_name='Офис', null=True, blank=True)
    status = models.CharField(choices=STATUS_CREATED_CHOICES, default='new', max_length=20)

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


# Модели для медицинских учреждений
class MedicalInstitution(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название медицинского учреждения',
        null=False,
        blank=False
    )
    #  foreign key (телефонов почти всегда больше одного)
    main_phone = models.ForeignKey(
        Phone,
        on_delete=models.SET_NULL,
        verbose_name='Основной телефон',
        null=True,
        blank=True
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
    visiting = models.ForeignKey(
        Visiting,
        on_delete=models.SET_NULL,
        verbose_name='Визиты',
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        verbose_name='Активный',
        default=True,
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = 'Медицинское учреждение'
        verbose_name_plural = 'Медицинские учреждения'


class MedicalInstitutionAgent(CustomUser):
    medical_institution = models.ForeignKey(
        MedicalInstitution,
        on_delete=models.CASCADE,
        verbose_name='Медицинское учреждение',
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = 'Агент медицинского учреждения'
        verbose_name_plural = 'Агенты медицинских учреждений'


class MedicalInstitutionBranch(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.SET_NULL, verbose_name='Телефон', null=True, blank=True)
    medical_institution = models.ForeignKey(
        MedicalInstitution,
        on_delete=models.CASCADE,
        verbose_name='Медицинское учреждение',
        null=False,
        blank=False
    )
    is_main = models.BooleanField(verbose_name='Основной филиал', default=False, null=False, blank=False)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, verbose_name='Локация', null=True, blank=True)
    metro_stations = models.ManyToManyField(MetroStation, verbose_name='Станции метро', blank=True)
    working_hours = models.JSONField(verbose_name='Рабочие часы', null=False, blank=False)
    visiting = models.ForeignKey(Visiting, on_delete=models.SET_NULL, verbose_name='Визиты', null=True, blank=True)
    is_active = models.BooleanField(verbose_name='Активный', default=True, null=False, blank=False)
    latitude = models.CharField(
        max_length=50,
        verbose_name='Широта',
        null=False,
        blank=False
    )
    longitude = models.CharField(
        max_length=50,
        verbose_name='Долгота',
        null=False,
        blank=False
    )
    url = models.URLField(
        max_length=200,
        verbose_name='Ссылка на филиал',
        null=True,
        blank=True
    )
    class Meta:
        verbose_name = 'Филиал медицинского учреждения'
        verbose_name_plural = 'Филиалы медицинского учреждения'


class ResearchMaterial(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название материала',
        null=False,
        blank=False
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True,
        default=""
    )

    class Meta:
        verbose_name = 'Материал исследования'
        verbose_name_plural = 'Материалы исследования'


class ResearchMedicalSystem(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название системы для исследования',
        null=False,
        blank=False
    )
    description = models.TextField(
        verbose_name='Описание',
        null=False,
        blank=False
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания системы')
    status = models.CharField(choices=STATUS_CREATED_CHOICES, default='new', max_length=20)

    class Meta:
        verbose_name = 'Система исследования'
        verbose_name_plural = 'Системы исследования'


class ResearchMedicalIllness(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название заболевания',
        null=False,
        blank=False
    )
    description = models.TextField(
        verbose_name='Описание',
        null=False,
        blank=False
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания системы')
    status = models.CharField(choices=STATUS_CREATED_CHOICES, default='new', max_length=20)

    class Meta:
        verbose_name = 'Заболевание'
        verbose_name_plural = 'Заболевания'


class MedicalService(models.Model):
    is_active = models.BooleanField(
        verbose_name='Активный',
        default=True,
        null=False,
        blank=False
    )
    name = models.CharField(
        max_length=200,
        verbose_name='Название медицинской услуги',
        null=False,
        blank=False
    )
    main_description = models.TextField(
        verbose_name='Описание',
        null=False,
        blank=False
    )
    # для создания этой сущности необходимо подтверждение модератора
    research_systems = models.ManyToManyField(
        ResearchMedicalSystem,
        verbose_name='Системы исследования',
        blank=True
    )
    research_illnesses = models.ManyToManyField(
        ResearchMedicalIllness,
        verbose_name='Заболевания',
        blank=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания системы'
    )
    status = models.CharField(
        choices=STATUS_CREATED_CHOICES,
        default='new',
        max_length=20
    )
    research_material = models.ManyToManyField(
        ResearchMaterial,
        verbose_name='Материалы исследования',
        blank=True,
        related_name='research_material'
    )
    # не у всех ведь есть код
    government_code_804n = models.CharField(
        max_length=12,
        verbose_name='Код услуги по 804н',
        null=False,
        blank=True
    )

    class Meta:
        verbose_name = 'Медицинская услуга'
        verbose_name_plural = 'Медицинские услуги'


class PriceHistory(models.Model):
    price_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания цены')
    start = models.DateTimeField(verbose_name='Дата начала действия цены', null=False, blank=False)
    end = models.DateTimeField(verbose_name='Дата окончания действия цены', null=True, blank=True)


class ServiceInMedicalInstitution(models.Model):
    service = models.ForeignKey(MedicalService, on_delete=models.CASCADE, verbose_name='Услуга', null=False, blank=False)
    is_active = models.BooleanField(verbose_name='Активный', default=True, null=False, blank=False)
    # special_conditions = models.ManyToManyField(SpecialCondition, verbose_name='Специальные условия', blank=True)
    medical_institution = models.ForeignKey(
        MedicalInstitution,
        on_delete=models.CASCADE,
        verbose_name='Медицинское учреждение',
        null=False,
        blank=False
    )
    visiting = models.ForeignKey(Visiting, on_delete=models.SET_NULL, verbose_name='Визиты', null=True, blank=True)
    is_available_oms = models.BooleanField(verbose_name='Доступно по ОМС', default=False, null=False, blank=False)
    is_available_dms = models.BooleanField(verbose_name='Доступно по ДМС', default=False, null=False, blank=False)
    is_available_at_home = models.BooleanField(verbose_name='Доступно на дому', default=False, null=False, blank=False)
    is_available_fast_result = models.BooleanField(verbose_name='Доступно при скором результате', default=False,
                                                   null=False, blank=False)
    price_for_at_home = models.ForeignKey(PriceHistory, on_delete=models.SET_NULL, verbose_name='Цена за выезд',
                                          null=True, blank=True, related_name='price_for_at_home')
    price = models.ForeignKey(PriceHistory, on_delete=models.SET_NULL, verbose_name='Цена', null=True, blank=True, related_name='price')
    price_for_fast_result = models.ForeignKey(PriceHistory, on_delete=models.SET_NULL,
                                              verbose_name='Цена при скором результате', null=True, blank=True,
                                                related_name='price_for_fast_result')
    time_to_complete = models.DurationField(
        verbose_name='Время выполнения',
        null=False,
        blank=False
    )
    time_to_complete_for_fast_result = models.DurationField(
        verbose_name='Время выполнения при скором результате',
        null=False,
        blank=False
    )
    internal_code = models.CharField(
        max_length=30,
        verbose_name="Внутренний код услуги",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Медицинское учреждение в услуге'
        verbose_name_plural = 'Медицинские учреждения в услугах'


class SpecialOffer(models.Model):
    medical_institution = models.ForeignKey(MedicalInstitution, on_delete=models.CASCADE,
                                            verbose_name='Медицинское учреждение', null=False, blank=False)
    only_some_for_branches = models.ManyToManyField(MedicalInstitutionBranch, verbose_name='Филиалы',
                                                    blank=True)
    only_some_for_services = models.ManyToManyField(ServiceInMedicalInstitution, verbose_name='Услуги',
                                                    blank=True)
    name = models.CharField(max_length=200, verbose_name='Название специального условия', null=False, blank=False)
    description = models.TextField(verbose_name='Описание', null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания специального условия')
    date_start = models.DateTimeField(verbose_name='Дата начала действия специального условия', null=False, blank=False)
    date_end = models.DateTimeField(verbose_name='Дата окончания действия специального условия', null=True, blank=True)

    class Meta:
        verbose_name = 'Специальное условие'
        verbose_name_plural = 'Специальные условия'


class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, verbose_name='Пользователь', null=True,
                             blank=False)
    medical_institution = models.ForeignKey(MedicalInstitution, on_delete=models.CASCADE, verbose_name='Медицинское '
                                                                                                       'учреждение',
                                            null=False, blank=False)
    branch = models.ForeignKey(MedicalInstitutionBranch, on_delete=models.SET_NULL, verbose_name='Филиал', null=True,
                               blank=True)
    service = models.ForeignKey(ServiceInMedicalInstitution, on_delete=models.SET_NULL, verbose_name='Услуга',
                                null=True,
                                blank=True)

    text = models.TextField(max_length=1000, verbose_name='Текст отзыва', null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания отзыва')
    rating_in_general = models.IntegerField(verbose_name='Общая оценка', null=False, blank=False)
    rating_for_service = models.IntegerField(verbose_name='Оценка за услугу', null=True, blank=True)
    rating_for_branch = models.IntegerField(verbose_name='Оценка за филиал', null=True, blank=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class ReviewComment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь', null=False,
                             blank=False)
    review = models.ForeignKey(Review, on_delete=models.PROTECT, verbose_name='Отзыв', null=False, blank=False)
    text = models.TextField(max_length=1000, verbose_name='Текст комментария', null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания комментария')

    class Meta:
        verbose_name = 'Комментарий к отзыву'
        verbose_name_plural = 'Комментарии к отзывам'


class SpecialOfferForPatient(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Пациент', null=False, blank=False)
    special_condition = models.ForeignKey(SpecialOffer, on_delete=models.CASCADE,
                                          verbose_name='Специальное условие', null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания специального условия для пациента')
    date_start = models.DateTimeField(verbose_name='Дата начала действия специального условия для пациента', null=False,
                                      blank=False)
    date_end = models.DateTimeField(verbose_name='Дата окончания действия специального условия для пациента', null=True,
                                    blank=True)

    class Meta:
        verbose_name = 'Специальное условие для пациента'
        verbose_name_plural = 'Специальные условия для пациентов'
