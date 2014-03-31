#-*- coding:utf-8 -*-

from django.db import models

from django.dispatch import receiver
from django.contrib.auth.models import User
from registration.signals import user_registered as user_registered
import const



##############################################################################################
##  Enrollment action requested (check all that apply)
##############################################################################################
class Model_A(models.Model):
    class Meta:
        abstract = True
    
    npi = models.CharField('Provider number (NPI or Denti-Cal number as applicable)', 
                           max_length=20)
    
    new_provider = models.BooleanField('New provider', blank=True, default=False)
    change_of_business_address = models.BooleanField('Change of business address', blank=True, default=False)
    additional_business_address = models.BooleanField('Additional business address', blank=True, default=False)
    
    new_taxpayer_id_number= models.BooleanField('New Taxpayer ID number', blank=True, default=False)
    facility_based_provider= models.BooleanField('Facility-Based Provider', blank=True, default=False)
    
    change_of_ownership= models.BooleanField('Change of ownership', blank=True, default=False)     
    change_of_ownership_date = models.DateField('change of ownership effective date', blank=True, null=True)
    
    cumulative_change_of_50_person = models.BooleanField('*Cumulative change of 50 percent or more in person(s) with ownership or control interest (per CCR, Title 22, Section 51000.15)', blank=True, default=False)
    sale_of_assets_50_percent = models.BooleanField('*Sale of assets 50 percent or more (per CCR, Title 22, Section 51000.30)', blank=True, default=False)
    ar_special_effective_date = models.DateField('For items above marked with * indicate effective date', blank=True, null=True)
    
    
    
    continued_enrollment = models.BooleanField("""Continued Enrollment (Do not check this box unless you have been requested 
                          by the Department to apply for continued enrollment in the Medi-Cal program pursuant to CCR, Title 22, Section 51000.55.)""",blank=True,  
                         default=False)
    i_intend = models.BooleanField("""I intend to use my current provider number to bill for services delivered at
                            this location while this application request is pending. I understand that I 
                            will be on provisional provider status during this time, pursuant to CCR, Title 22, Section 51000.51.""", blank=True, default=False)




##############################################################################################
##  Medi-Cal Application Fee (check all that apply)
##############################################################################################    
class Model_B(models.Model):
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



##############################################################################################
## Type of entity (check one)
##############################################################################################   
class Model_C(models.Model):
    class Meta:
        abstract = True

    type_of_entity = models.IntegerField('Type of entity', 
                                         choices=const.TYPE_OF_ENTITY_CHOICES, 
                                         null=True)
    
    # only for Corporation
    corporate_number = models.CharField('Corporate number', blank=True, max_length=255)
    state_incorporated = models.CharField('State incorporated', blank=True, max_length=2) # TODO: from states-dictionary
    
    # only for LLC
    llc_number = models.CharField('LLC number', blank=True, max_length=255)
    state_registered_filed = models.CharField('State registered/filed', blank=True, max_length=2) # TODO: from states-dictionary
    
    # only for Nonprofit Corporation
    type_of_nonprofit  = models.CharField('Type of nonprofit', blank=True, max_length=255)
    
    # only for Other
    other_description = models.CharField('Other description', blank=True, max_length=255)



##############################################################################################
## Legal & Business names
##############################################################################################
class Model_D(models.Model):
    class Meta:
        abstract = True
        
    legal_name = models.CharField('Legal name of applicant or provider (as listed with the IRS)', blank=True, max_length=255)
    business_name = models.CharField('Business name, if different', blank=True, max_length=255)
    
    fictitious_business_name = models.BooleanField('Is this a fictitious business name?', blank=True, default=False)
    fictitious_number = models.CharField('If yes, list the Fictitious Business Name Statement/Permit number', blank=True, max_length=255) 
    fictitious_effective_date = models.DateField('Effective date', blank=True, null=True)

    business_telephone_number = models.CharField('Business telephone number', blank=True, max_length=255)
    

    
##############################################################################################
##  Business\Pay\Mail\Prev addresses
##############################################################################################        
class Model_E(models.Model):
    class Meta:
        abstract = True

    ba_title = models.CharField('Business address (number, street)', blank=True, max_length=255)
    ba_city = models.CharField('City', blank=True, max_length=255)
    ba_county = models.CharField('County', blank=True, max_length=255)
    ba_state = models.CharField('State', choices=const.STATES, blank=True, max_length=2) 
    ba_zip = models.CharField('Nine-digit ZIP code', blank=True, max_length=9)
    

    pa_title = models.CharField('Pay-to address (number, street, P.O. Box number)', blank=True, max_length=255)
    pa_city = models.CharField('City', blank=True, max_length=255)
    pa_county = models.CharField('County', blank=True, max_length=255)
    pa_state = models.CharField('State', choices=const.STATES, blank=True, max_length=2) 
    pa_zip = models.CharField('Nine-digit ZIP code', blank=True, max_length=9)
    

    ma_title = models.CharField('Mailing address (number, street, P.O. Box number)', blank=True, max_length=255)
    ma_city = models.CharField('City', blank=True, max_length=255)
    ma_county = models.CharField('County', blank=True, max_length=255)
    ma_state = models.CharField('State', choices=const.STATES, blank=True, max_length=2) 
    ma_zip = models.CharField('Nine-digit ZIP code', blank=True, max_length=9)
    
    pr_title = models.CharField('Previous business address (number, street)', blank=True, max_length=255)
    pr_city = models.CharField('City', blank=True, max_length=255)
    pr_county = models.CharField('County', blank=True, max_length=255)
    pr_state = models.CharField('State', choices=const.STATES, blank=True, max_length=2) 
    pr_zip = models.CharField('Nine-digit ZIP code', blank=True, max_length=9)
    
    


##############################################################################################
## 
##############################################################################################    

# = models.BooleanField('', default=False)
# = models.CharField('', blank=True, max_length=255)


class Provider(Model_A, Model_B, Model_C, Model_D, Model_E):
    """
    Info about HC Provider
    """
    user = models.OneToOneField(User)
    #title = models.CharField(max_length=100)
    



@receiver(user_registered)
def create_provider(sender, **kwargs):
    Provider.objects.create(user=kwargs['user'])
    
