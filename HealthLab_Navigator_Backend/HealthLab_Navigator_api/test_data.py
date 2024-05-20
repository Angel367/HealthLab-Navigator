import os
from datetime import timedelta

import django
from faker import Faker
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HealthLab_Navigator_Backend.settings')
django.setup()

from HealthLab_Navigator_api.models import *

fake = Faker('ru_RU')


def fake_metro_lines(num):
    for _ in range(num):
        MetroLine.objects.create(
            name=fake.word(),
            color=fake.color(),
            city=City.objects.get(id=fake.random_int(min=1, max=City.objects.count())),
        )


def fake_metro_stations(num):
    for _ in range(num):
        MetroStation.objects.create(
            name=fake.word(),
            district=District.objects.get(id=fake.random_int(min=1, max=District.objects.count())),
            line=MetroLine.objects.get(id=fake.random_int(min=1, max=MetroLine.objects.count())),
        )


def fake_cities(num):
    for _ in range(num):
        City.objects.create(
            name=fake.city(),
        )


def fake_districts(num):
    for _ in range(num):
        District.objects.create(
            name=fake.word(),
            city=City.objects.get(id=fake.random_int(min=1, max=City.objects.count())),
        )


def fake_streets(num):
    for _ in range(num):
        street = Street.objects.create(
            name=fake.street_name(),
        )
        street.districts.set(fake.random_elements(elements=District.objects.all(),
                                                  length=fake.random_int(min=1, max=3)))



def fake_medical_institutions(num):
    for _ in range(num):
        med = MedicalInstitution.objects.create(
            name=fake.company(),
            website=fake.url(),
            description=fake.paragraph(nb_sentences=3),
        )
        for _ in range(fake.random_int(min=1, max=3)):
            try:
                phone = Phone.objects.create(number=fake.phone_number(), institution=med)
            except Exception as e:
                print(e)
                continue



def fake_branches(num):
    for i in range(num):
        address = Address.objects.create(
            street=Street.objects.get(id=fake.random_int(min=1, max=Street.objects.count())),
            house=fake.building_number(),
            office=fake.random_int(min=1, max=100),
            latitude=fake.latitude(),
            longitude=fake.longitude())

        branch = MedicalInstitutionBranch.objects.create(
            medical_institution=MedicalInstitution.objects.get(id=fake.random_int(min=1,
                                                                                  max=MedicalInstitution.objects.count())),
            address=address,
            is_main=i == 0,
            url=fake.url(),
            working_hours={
                'пн': '09:00-18:00',
                'вт': '09:00-18:00',
                'ср': '09:00-18:00',
                'чт': '09:00-18:00',
                'пт': '09:00-18:00',
                'сб': '09:00-18:00',
                'вс': '09:00-18:00',
            }
        )

        for _ in range(fake.random_int(min=1, max=3)):
            try:
                phone = Phone.objects.create(number=fake.phone_number(), branch=branch, institution=branch.medical_institution)
            except Exception as e:
                print(e)
                continue


def fake_reviews(num):
    for _ in range(num):
        review = Review.objects.create(
            text=fake.paragraph(nb_sentences=3),
            rating_in_general=fake.random_int(min=1, max=5),
            user=get_user_model().objects.get(id=fake.random_int(min=1, max=get_user_model().objects.count())),
            medical_institution=MedicalInstitution.objects.get(
                id=fake.random_int(min=1, max=MedicalInstitution.objects.count())),
        )
        if fake.boolean():
            review.rating_for_service = fake.random_int(min=1, max=5)
            services = ServiceInMedicalInstitution.objects.filter(medical_institution=review.medical_institution)
            review.service = services[fake.random_int(min=0, max=len(services) - 1)]
        if fake.boolean():
            review.rating_for_branch = fake.random_int(min=1, max=5)
            branches = (MedicalInstitutionBranch.objects.filter(medical_institution=review.medical_institution))
            review.branch = branches[fake.random_int(min=0, max=len(branches) - 1)]
        review.save()
        for _ in range(fake.random_int(min=0, max=3)):
            ReviewComment.objects.create(
                text=fake.paragraph(nb_sentences=3),
                user=get_user_model().objects.get(id=fake.random_int(min=1, max=get_user_model().objects.count())),
                review=Review.objects.get(id=fake.random_int(min=1, max=Review.objects.count())),
            )


def fake_users(num):
    custom_user = get_user_model()
    phone_number = fake.phone_number()
    email = fake.email()
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
        while custom_user.objects.filter(phone_number=phone_number).exists():
            phone_number = fake.phone_number()
        while custom_user.objects.filter(email=fake.email()).exists():
            email = fake.email()
        user = custom_user.objects.create_user(
            email=email,
            date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=100),
            gender=gender,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            user_type=user_type,
            phone_number=phone_number )

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
            government_code_804n=fake.word(),
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
    if City.objects.all().count() < 10:
        fake_cities(10)
        print('Cities have been added')
    if District.objects.all().count() < 10:
        fake_districts(10)
        print('Districts have been added')
    if Street.objects.all().count() < 10:
        fake_streets(10)
        print('Streets have been added')
    if MetroLine.objects.all().count() < 10:
        fake_metro_lines(10)
        print('Metro lines have been added')
    if MetroStation.objects.all().count() < 10:
        fake_metro_stations(10)
        print('Metro stations have been added')
    if MedicalInstitution.objects.all().count() < 10:
        fake_medical_institutions(10)
        print('Medical institutions have been added')
    if MedicalInstitutionBranch.objects.all().count() < 10:
        fake_branches(10)
        print('Branches have been added')
    if MedicalService.objects.all().count() < 10:
        fake_medical_services(10)
        print('Medical services have been added')
    if ServiceInMedicalInstitution.objects.all().count() < 10:
        fake_service_in_medical_institution(10)
        print('Services in medical institutions have been added')
    if ResearchMedicalSystem.objects.all().count() < 10:
        fake_research_systems(10)
        print('Research systems have been added')
    if ResearchMaterial.objects.all().count() < 10:
        fake_research_materials(10)
        print('Research materials have been added')
    if ResearchMedicalIllness.objects.all().count() < 10:
        fake_research_illnesses(10)
        print('Research illnesses have been added')
    if SpecialOffer.objects.all().count() < 10:
        fake_special_offer(10)
        print('Special offers have been added')
    if get_user_model().objects.all().count() < 10:
        fake_users(10)
        print('Users have been added')
    if Review.objects.all().count() < 100:
        fake_reviews(100)
        print('Reviews have been added')
    print('Data has been added')
