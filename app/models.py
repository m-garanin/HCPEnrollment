#-*- coding:utf-8 -*-

from django.db import models

from django.dispatch import receiver
from django.contrib.auth.models import User
from registration.signals import user_registered as user_registered
import const

class Provider(models.Model):
    """
    Info about HC Provider
    """
    user = models.OneToOneField(User)
    #title = models.CharField(max_length=100)
    npi = models.CharField('Provider number (NPI or Denti-Cal number as applicable)', 
                           max_length=20)

    
    ##############################################################################################
    ##  Enrollment action requested (check all that apply)
    ##############################################################################################    
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
    legal_name = models.CharField('Legal name of applicant or provider (as listed with the IRS)', blank=True, max_length=255)
    business_name = models.CharField('Business name, if different', blank=True, max_length=255)
    
    fictitious_business_name = models.BooleanField('Is this a fictitious business name?', default=False)
    fictitious_number= models.CharField('If yes, list the Fictitious Business Name Statement/Permit number', blank=True, max_length=255) 
    fictitious_effective_date = models.DateField('Effective date', null=True)

    business_telephone_number = models.CharField('Business telephone number', blank=True, max_length=255)
    
    





    ##############################################################################################
    ## 
    ##############################################################################################    

# = models.BooleanField('', default=False)
# = models.CharField('', blank=True, max_length=255)





@receiver(user_registered)
def create_provider(sender, **kwargs):
    Provider.objects.create(user=kwargs['user'])
    
