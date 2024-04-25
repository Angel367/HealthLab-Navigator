import os
from datetime import timedelta

import django
from faker import Faker
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HealthLab_Navigator_Backend.settings')
django.setup()

from HealthLab_Navigator_api.models import *

fake = Faker('ru_RU')


def fake_medical_institutions(num):
    for _ in range(num):
        med = MedicalInstitution.objects.create(
            name=fake.company(),
            website=fake.url(),
            description=fake.paragraph(nb_sentences=3),
        )
        for _ in range(fake.random_int(min=1, max=3)):
            phone = Phone.objects.create(number=fake.phone_number(), institution=med)


def fake_branches(num):
    for i in range(num):
        branch = MedicalInstitutionBranch.objects.create(
            medical_institution=MedicalInstitution.objects.get(id=fake.random_int(min=1,
                                                                                  max=MedicalInstitution.objects.count())),
            latitude=fake.latitude(),
            # street=Street.objects.create(name=fake.street_name()),
            house=fake.building_number(),
            office=fake.random_int(min=1, max=100),
            is_main=i == 0,
            url=fake.url(),
            longitude=fake.longitude(),
            working_hours=fake.json(),
        )
        for _ in range(fake.random_int(min=0, max=3)):
            Phone.objects.create(number=fake.phone_number(), branch=branch)



def fake_users(num):
    custom_user = get_user_model()
    for _ in range(num):
        gender = fake.random_element(elements=('male', 'female', 'unknown'))
        if gender == 'unknown':
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            middle_name = fake.middle_name
        elif gender == 'male':
            first_name = fake.first_name_male(),
            last_name = fake.last_name_male(),
            middle_name = fake.middle_name_male()
        else:
            first_name = fake.first_name_female(),
            last_name = fake.last_name_female(),
            middle_name = fake.middle_name_female()
        user_type = fake.random_element(elements=USER_TYPE_CHOICES)
        user = custom_user.objects.create_user(
            email=fake.email(),

            date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=100),
            gender=gender,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            user_type=user_type,
            phone_number=fake.phone_number(),)

        user.set_password('12345678')
        if user_type == 'patient':
            Patient.objects.create(user=user)
        elif user_type == 'medical_institution_agent':
            MedicalInstitutionAgent.objects.create(user=user, medical_institution=MedicalInstitution.objects.get(
                id=fake.random_int(min=1, max=MedicalInstitution.objects.count())))
        else:
            user.is_admin = True
        user.save()


def fake_research_systems(num):
    for _ in range(num):
        ResearchMedicalSystem.objects.create(
            name=fake.text(max_nb_chars=40),
            description=fake.paragraph(nb_sentences=3),
        )


def fake_research_materials(num):
    for _ in range(num):
        ResearchMaterial.objects.create(
            name=fake.text(max_nb_chars=40),
            description=fake.paragraph(nb_sentences=3),
        )


def fake_research_illnesses(num):
    for _ in range(num):
        ResearchMedicalIllness.objects.create(
            name=fake.text(max_nb_chars=40),
            description=fake.paragraph(nb_sentences=3),
        )


def fake_medical_services(num):
    for _ in range(num):
        MedicalService.objects.create(
            name=fake.text(max_nb_chars=40),
            main_description=fake.paragraph(nb_sentences=3),
            government_code_804n = fake.word(),
        )


def fake_service_in_medical_institution(num):
    is_available_at_home = fake.boolean()
    is_available_fast_result = fake.boolean()
    time_to_complete = fake.time_delta(end_datetime=timedelta(days=fake.random_int(min=1, max=30)))
    for _ in range(num):
        service = ServiceInMedicalInstitution.objects.create(
            medical_institution=MedicalInstitution.objects.get(id=fake.random_int(min=1,
                                                                                  max=MedicalInstitution.objects.count())),
            service=MedicalService.objects.get(id=fake.random_int(min=1,
                                                                          max=MedicalService.objects.count())),
            is_available_dms=fake.boolean(),
            is_available_oms=fake.boolean(),
            is_available_at_home=is_available_at_home,
            internal_code=fake.random_int(min=1, max=100),
            is_available_fast_result=is_available_fast_result,
            time_to_complete=time_to_complete,
            price=PriceHistory.objects.create(
                price_value=fake.random_int(min=100, max=100000),
                start=fake.past_datetime(),
                end=fake.future_datetime()
            )

        )
        if is_available_at_home:
            service.price_for_at_home = PriceHistory.objects.create(
                price_value=fake.random_int(min=100, max=100000),
                start=fake.past_datetime(),
                end=fake.future_datetime()
            )
        if is_available_fast_result:
            service.price_for_fast_result = PriceHistory.objects.create(
                price_value=fake.random_int(min=100, max=100000),
                start=fake.past_datetime(),
                end=fake.future_datetime()
            )
            service.time_to_complete_fast_result = fake.time_delta(end_datetime=timedelta(
                days=fake.random_int(min=0, max=time_to_complete.days)))
        service.save()


def fake_special_offer(num):
    for _ in range(num):
        SpecialOffer.objects.create(
            name=fake.text(max_nb_chars=40),
            description=fake.paragraph(nb_sentences=3),
            date_start=fake.past_datetime(),
            date_end=fake.future_datetime(),
            medical_institution=MedicalInstitution.objects.get(id=fake.random_int(min=1,
                                                                                  max=MedicalInstitution.objects.count())),
        )


if __name__ == '__main__':
    if not MedicalInstitution.objects.exists():
        fake_medical_institutions(10)
    if not MedicalInstitutionBranch.objects.exists():
        fake_branches(10)
    if not get_user_model().objects.exists():
        fake_users(10)
    if not ResearchMedicalSystem.objects.exists():
        fake_research_systems(10)
    if not ResearchMaterial.objects.exists():
        fake_research_materials(10)
    if not ResearchMedicalIllness.objects.exists():
        fake_research_illnesses(10)
    if not MedicalService.objects.exists():
        fake_medical_services(10)
    if not ServiceInMedicalInstitution.objects.exists():
        fake_service_in_medical_institution(10)
    if not SpecialOffer.objects.exists():
        fake_special_offer(10)
    print('Data has been added')


