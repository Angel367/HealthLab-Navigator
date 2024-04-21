from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(MedicalInstitution)
admin.site.register(MedicalInstitutionBranch)
admin.site.register(ServiceInMedicalInstitution)
admin.site.register(MedicalInstitutionAgent)
admin.site.register(PriceHistory)
admin.site.register(ResearchMedicalSystem)
admin.site.register(ResearchMedicalIllness)
admin.site.register(Feedback)
admin.site.register(Review)
admin.site.register(ReviewComment)
admin.site.register(SpecialOffer)
admin.site.register(SpecialOfferForPatient)
admin.site.register(MedicalService)
admin.site.register(ResearchMaterial)
admin.site.register(Phone)


