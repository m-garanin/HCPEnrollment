#-*- coding:utf-8 -*-

from django.db import models

from django.dispatch import receiver
from django.contrib.auth.models import User
from registration.signals import user_registered as user_registered

        
        
class Group_ActionRequested(models.Model):
    """ Enrollment action requested (check all that apply)
    """ 
    class Meta:
        abstract = True

    new_provider = models.BooleanField('New provider', default=False)
    change_of_business_address = models.BooleanField('Change of business address', default=False)
    additional_business_address = models.BooleanField('Additional business address', default=False)
    
    new_taxpayer_id_number= models.BooleanField('New Taxpayer ID number', default=False)
    facility_based_provider= models.BooleanField('Facility-Based Provider', default=False)
    
    change_of_ownership= models.BooleanField('Change of ownership', default=False)     
    change_of_ownership_date = models.DateField('change of ownership effective date', null=True)
    
    cumulative_change_of_50_person = models.BooleanField('*Cumulative change of 50 percent or more in person(s) with ownership or control interest (per CCR, Title 22, Section 51000.15)', default=False)
    sale_of_assets_50_percent = models.BooleanField('*Sale of assets 50 percent or more (per CCR, Title 22, Section 51000.30)', default=False)
    ar_special_effective_date = models.DateField('For items above marked with * indicate effective date', null=True)
    
    
    
    continued_enrollment = models.BooleanField("""Continued Enrollment (Do not check this box unless you have been requested 
                          by the Department to apply for continued enrollment in the Medi-Cal program pursuant to CCR, Title 22, Section 51000.55.)""", 
                         default=False)
    i_intend = models.BooleanField("""I intend to use my current provider number to bill for services delivered at
                            this location while this application request is pending. I understand that I 
                            will be on provisional provider status during this time, pursuant to CCR, Title 22, Section 51000.51.""", default=False)
    
    
class Group_MediCalApplicationFee(models.Model):
    """ Medi-Cal Application Fee (check all that apply)
    """
    class Meta:
        abstract = True

    enrollment_as_an_individual_nonphysician_practitioner = models.BooleanField('I am requesting enrollment as an individual nonphysician practitioner.', default=False)
    enrolled_in_the_medicare_program = models.BooleanField('I am currently enrolled in the Medicare program at this business address and under this legal name. (Attach verification)', default=False)
    enrolled_in_another_program = models.BooleanField("""I am currently enrolled in another State’s Medicaid or Children’s Health Insurance Program (CHIP) at this business address and under this legal name. (Attach verification)""", 
                                                      default=False)
    i_have_paid_the_application_fee = models.BooleanField("""I have paid the application fee to a Medicare contractor or another State’s Medicaid or CHIP at 
                                                           this business address and under this legal name. (Attach proof of payment)""", default=False)
    i_have_included_an_application_fee = models.BooleanField("""I have included an application fee check and/or an application fee waiver 
                                                              request with this application. (Attach cashier’s check and/or waiver request)""", default=False)


class Group_TypeOfEntity(models.Model):
    """ Type of entity (check one)
    """
    class Meta:
        abstract = True
        
    type_of_entity = models.IntegerField('Type of entity', null=True)
    


# = models.BooleanField('', default=False)


class Provider(Group_ActionRequested, Group_MediCalApplicationFee, Group_TypeOfEntity):
    """
    Info about HC Provider
    """
    user = models.OneToOneField(User)
    #title = models.CharField(max_length=100)
    npi = models.CharField(max_length=20)



@receiver(user_registered)
def create_provider(sender, signal, user, request):
    Provider.objects.create(user=user)
    
