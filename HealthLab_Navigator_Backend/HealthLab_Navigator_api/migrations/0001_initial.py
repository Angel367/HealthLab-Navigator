# Generated by Django 5.0.2 on 2024-04-14 22:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название города')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, verbose_name='Email пользователя')),
                ('text', models.TextField(max_length=1000, verbose_name='Текст обращения')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания обращения')),
                ('status', models.CharField(choices=[('new', 'Новый'), ('in_progress', 'В обработке'), ('done', 'Выполнен')], default='new', max_length=20, verbose_name='Статус обращения')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(blank=True, max_length=50, null=True, verbose_name='Широта')),
                ('longitude', models.CharField(blank=True, max_length=50, null=True, verbose_name='Долгота')),
                ('house', models.CharField(blank=True, max_length=10, null=True, verbose_name='Дом')),
                ('office', models.CharField(blank=True, max_length=10, null=True, verbose_name='Офис')),
                ('status', models.CharField(choices=[('new', 'Новый'), ('waiting', 'Ожидает подтверждения'), ('confirmed', 'Подтвержден'), ('rejected', 'Отклонен')], default='new', max_length=20)),
            ],
            options={
                'verbose_name': 'Локация',
                'verbose_name_plural': 'Локации',
            },
        ),
        migrations.CreateModel(
            name='MedicalInstitution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название медицинского учреждения')),
                ('website', models.URLField(verbose_name='Сайт')),
                ('description', models.TextField(verbose_name='Описание')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
            ],
            options={
                'verbose_name': 'Медицинское учреждение',
                'verbose_name_plural': 'Медицинские учреждения',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('user_type', models.CharField(choices=[('patient', 'Пациент'), ('medical_institution_agent', 'Агент медицинского учреждения'), ('moderator', 'Модератор')], default='patient', max_length=50, verbose_name='Тип пользователя')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MetroLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название линии метро')),
                ('color', models.CharField(max_length=100, verbose_name='Цвет линии метро')),
            ],
            options={
                'verbose_name': 'Линия метро',
                'verbose_name_plural': 'Линии метро',
            },
        ),
        migrations.CreateModel(
            name='MetroStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название станции метро')),
                ('line', models.CharField(max_length=100, verbose_name='Линия метро')),
            ],
            options={
                'verbose_name': 'Станция метро',
                'verbose_name_plural': 'Станции метро',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50, unique=True, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Телефон',
                'verbose_name_plural': 'Телефоны',
            },
        ),
        migrations.CreateModel(
            name='PriceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания цены')),
                ('start', models.DateTimeField(verbose_name='Дата начала действия цены')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания действия цены')),
            ],
        ),
        migrations.CreateModel(
            name='ResearchMedicalIllness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название заболевания')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания системы')),
                ('status', models.CharField(choices=[('new', 'Новый'), ('waiting', 'Ожидает подтверждения'), ('confirmed', 'Подтвержден'), ('rejected', 'Отклонен')], default='new', max_length=20)),
            ],
            options={
                'verbose_name': 'Заболевание',
                'verbose_name_plural': 'Заболевания',
            },
        ),
        migrations.CreateModel(
            name='ResearchMedicalSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название системы для исследования')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания системы')),
                ('status', models.CharField(choices=[('new', 'Новый'), ('waiting', 'Ожидает подтверждения'), ('confirmed', 'Подтвержден'), ('rejected', 'Отклонен')], default='new', max_length=20)),
            ],
            options={
                'verbose_name': 'Система исследования',
                'verbose_name_plural': 'Системы исследования',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название района')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HealthLab_Navigator_api.city', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пациент',
                'verbose_name_plural': 'Пациенты',
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HealthLab_Navigator_api.phone', unique=True, verbose_name='Номер телефона'),
        ),
        migrations.CreateModel(
            name='MedicalInstitutionBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(default=False, verbose_name='Основной филиал')),
                ('working_hours', models.CharField(max_length=200, verbose_name='Рабочие часы')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='HealthLab_Navigator_api.location', verbose_name='Локация')),
                ('medical_institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HealthLab_Navigator_api.medicalinstitution', verbose_name='Медицинское учреждение')),
                ('metro_stations', models.ManyToManyField(blank=True, to='HealthLab_Navigator_api.metrostation', verbose_name='Станции метро')),
                ('phone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='HealthLab_Navigator_api.phone', verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Филиал медицинского учреждения',
                'verbose_name_plural': 'Филиалы медицинского учреждения',
            },
        ),
        migrations.AddField(
            model_name='medicalinstitution',
            name='main_phone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='HealthLab_Navigator_api.phone', verbose_name='Основной телефон'),
        ),
        migrations.CreateModel(
            name='MedicalService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('name', models.CharField(max_length=200, verbose_name='Название медицинской услуги')),
                ('main_description', models.TextField(verbose_name='Описание')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания системы')),
                ('status', models.CharField(choices=[('new', 'Новый'), ('waiting', 'Ожидает подтверждения'), ('confirmed', 'Подтвержден'), ('rejected', 'Отклонен')], default='new', max_length=20)),
                ('research_material', models.CharField(choices=[('blood', 'Кровь'), ('urine', 'Моча'), ('feces', 'Кал'), ('smear', 'Мазок'), ('biopsy', 'Биопсия'), ('other', 'Другое')], max_length=50, verbose_name='Материал исследования')),
                ('government_code_804n', models.CharField(blank=True, max_length=12, verbose_name='Код услуги по 804н')),
                ('research_illnesses', models.ManyToManyField(blank=True, to='HealthLab_Navigator_api.researchmedicalillness', verbose_name='Заболевания')),
                ('research_systems', models.ManyToManyField(blank=True, to='HealthLab_Navigator_api.researchmedicalsystem', verbose_name='Системы исследования')),
            ],
            options={
                'verbose_name': 'Медицинская услуга',
                'verbose_name_plural': 'Медицинские услуги',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000, verbose_name='Текст отзыва')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания отзыва')),
                ('rating_in_general', models.IntegerField(verbose_name='Общая оценка')),
                ('rating_for_service', models.IntegerField(blank=True, null=True, verbose_name='Оценка за услугу')),
                ('rating_for_branch', models.IntegerField(blank=True, null=True, verbose_name='Оценка за филиал')),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='HealthLab_Navigator_api.medicalinstitutionbranch', verbose_name='Филиал')),
                ('medical_institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HealthLab_Navigator_api.medicalinstitution', verbose_name='Медицинское учреждение')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='ReviewComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000, verbose_name='Текст комментария')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания комментария')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='HealthLab_Navigator_api.review', verbose_name='Отзыв')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий к отзыву',
                'verbose_name_plural': 'Комментарии к отзывам',
            },
        ),
        migrations.CreateModel(
            name='ServiceInMedicalInstitution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('is_available_oms', models.BooleanField(default=False, verbose_name='Доступно по ОМС')),
                ('is_available_dms', models.BooleanField(default=False, verbose_name='Доступно по ДМС')),
                ('is_available_at_home', models.BooleanField(default=False, verbose_name='Доступно на дому')),
                ('is_available_fast_result', models.BooleanField(default=False, verbose_name='Доступно при скором результате')),
                ('time_to_complete', models.DurationField(verbose_name='Время выполнения')),
                ('time_to_complete_for_fast_result', models.DurationField(verbose_name='Время выполнения при скором результате')),
                ('internal_code', models.CharField(blank=True, max_length=30, null=True, verbose_name='Внутренний код услуги')),
                ('medical_institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HealthLab_Navigator_api.medicalinstitution', verbose_name='Медицинское учреждение')),
                ('price', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='price', to='HealthLab_Navigator_api.pricehistory', verbose_name='Цена')),
                ('price_for_at_home', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='price_for_at_home', to='HealthLab_Navigator_api.pricehistory', verbose_name='Цена за выезд')),
                ('price_for_fast_result', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='price_for_fast_result', to='HealthLab_Navigator_api.pricehistory', verbose_name='Цена при скором результате')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HealthLab_Navigator_api.medicalservice', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Медицинское учреждение в услуге',
                'verbose_name_plural': 'Медицинские учреждения в услугах',
            },
        ),
        migrations.AddField(
            model_name='review',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='HealthLab_Navigator_api.serviceinmedicalinstitution', verbose_name='Услуга'),
        ),
        migrations.CreateModel(
            name='SpecialOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название специального условия')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания специального условия')),
                ('date_start', models.DateTimeField(verbose_name='Дата начала действия специального условия')),
                ('date_end', models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания действия специального условия')),
                ('medical_institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HealthLab_Navigator_api.medicalinstitution', verbose_name='Медицинское учреждение')),
                ('only_some_for_branches', models.ManyToManyField(blank=True, null=True, to='HealthLab_Navigator_api.medicalinstitutionbranch', verbose_name='Филиалы')),
                ('only_some_for_services', models.ManyToManyField(blank=True, null=True, to='HealthLab_Navigator_api.serviceinmedicalinstitution', verbose_name='Услуги')),
            ],
            options={
                'verbose_name': 'Специальное условие',
                'verbose_name_plural': 'Специальные условия',
            },
        ),
        migrations.CreateModel(
            name='SpecialOfferForPatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания специального условия для пациента')),
                ('date_start', models.DateTimeField(verbose_name='Дата начала действия специального условия для пациента')),
                ('date_end', models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания действия специального условия для пациента')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HealthLab_Navigator_api.patient', verbose_name='Пациент')),
                ('special_condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HealthLab_Navigator_api.specialoffer', verbose_name='Специальное условие')),
            ],
            options={
                'verbose_name': 'Специальное условие для пациента',
                'verbose_name_plural': 'Специальные условия для пациентов',
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название улицы')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HealthLab_Navigator_api.district', verbose_name='Район')),
            ],
            options={
                'verbose_name': 'Улица',
                'verbose_name_plural': 'Улицы',
            },
        ),
        migrations.AddField(
            model_name='location',
            name='street',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='HealthLab_Navigator_api.street', verbose_name='Улица'),
        ),
        migrations.CreateModel(
            name='Visiting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания визита')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.AddField(
            model_name='serviceinmedicalinstitution',
            name='visiting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='HealthLab_Navigator_api.visiting', verbose_name='Визиты'),
        ),
        migrations.AddField(
            model_name='medicalinstitutionbranch',
            name='visiting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='HealthLab_Navigator_api.visiting', verbose_name='Визиты'),
        ),
        migrations.AddField(
            model_name='medicalinstitution',
            name='visiting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='HealthLab_Navigator_api.visiting', verbose_name='Визиты'),
        ),
        migrations.CreateModel(
            name='MedicalInstitutionAgent',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('medical_institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HealthLab_Navigator_api.medicalinstitution', verbose_name='Медицинское учреждение')),
            ],
            options={
                'verbose_name': 'Агент медицинского учреждения',
                'verbose_name_plural': 'Агенты медицинских учреждений',
            },
            bases=('HealthLab_Navigator_api.customuser',),
        ),
    ]
