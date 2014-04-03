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
    state_incorporated = models.CharField('State incorporated', choices=const.STATES, blank=True, max_length=2) 
    
    # only for LLC
    llc_number = models.CharField('LLC number', blank=True, max_length=255)
    state_registered_filed = models.CharField('State registered/filed', choices=const.STATES, blank=True, max_length=2)
    
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

    # Business address    
    ba_title = models.CharField('Number, street', blank=True, max_length=255)
    ba_city = models.CharField('City', blank=True, max_length=255)
    ba_county = models.CharField('County', blank=True, max_length=255)
    ba_state = models.CharField('State', choices=const.STATES, blank=True, max_length=2) 
    ba_zip = models.CharField('Nine-digit ZIP code', blank=True, max_length=9)
    
    is_a_licensed_facility = models.BooleanField('This address is a licensed hospital/health facility.', blank=True, default=False)
    facility_option_1 = models.BooleanField('All services are provided at this one facility location OR', blank=True, default=False)
    facility_option_2 = models.BooleanField('Services are provided at more than one licensed health facility', blank=True, default=False)
    
    


    # Pay-to address
    pa_title = models.CharField('Number, street, P.O. Box number', blank=True, max_length=255)
    pa_city = models.CharField('City', blank=True, max_length=255)
    pa_county = models.CharField('County', blank=True, max_length=255)
    pa_state = models.CharField('State', choices=const.STATES, blank=True, max_length=2) 
    pa_zip = models.CharField('Nine-digit ZIP code', blank=True, max_length=9)
    
    # Mailing address
    ma_title = models.CharField('Number, street, P.O. Box number', blank=True, max_length=255)
    ma_city = models.CharField('City', blank=True, max_length=255)
    ma_county = models.CharField('County', blank=True, max_length=255)
    ma_state = models.CharField('State', choices=const.STATES, blank=True, max_length=2) 
    ma_zip = models.CharField('Nine-digit ZIP code', blank=True, max_length=9)
    
    # Previous business address
    pr_title = models.CharField('Number, street', blank=True, max_length=255)
    pr_city = models.CharField('City', blank=True, max_length=255)
    pr_county = models.CharField('County', blank=True, max_length=255)
    pr_state = models.CharField('State', choices=const.STATES, blank=True, max_length=2) 
    pr_zip = models.CharField('Nine-digit ZIP code', blank=True, max_length=9)
    


##############################################################################################
##  Licence & Taxonomy 
##############################################################################################        
class Model_F(models.Model):
    class Meta:
        abstract = True
        
    
    license_number = models.CharField('License number', blank=True, max_length=255)
    license_effective_date = models.DateField('License effective date', blank=True, null=True)
    license_expiration_date = models.DateField('License expiration date', blank=True, null=True)
    provider_type = models.CharField('Provider type', blank=True, max_length=255)
    medicare_other_NPI= models.CharField('Medicare/Other NPI', blank=True, max_length=255)

    primary_taxonomy = models.CharField('Primary Taxonomy Code', blank=True, max_length=255)
    taxonomy_b = models.CharField('Taxonomy Code', blank=True, max_length=255)
    taxonomy_c = models.CharField('Taxonomy Code', blank=True, max_length=255)
    


##############################################################################################
##  Taxpayer & Social number
##############################################################################################        
class Model_G(models.Model):
    class Meta:
        abstract = True
    
    taxplayer_number = models.CharField('Taxpayer Identification Number (TIN) issued by the IRS (attach a legible copy of the IRS form)', blank=True, max_length=255)
    social_number = models.CharField('Social security number. If sole proprietor not using a TIN, you must disclose this number', blank=True, max_length=255)
    

##############################################################################################
##  Nurse Practitioner only
##############################################################################################        
class Model_H(models.Model):
    class Meta:
        abstract = True

    duration_of_training = models.CharField('Duration of training program and school', blank=True, max_length=255)
    clinical_training = models.CharField('Clinical and didactic training or equivalent experience completed', blank=True, max_length=255)
    

##############################################################################################
##  Other licences: Clinical Laboratory  & State Laboratory & Driver 
##############################################################################################    
class Model_I(models.Model):
    class Meta:
        abstract = True

    clia_cert_info = models.CharField('Clinical Laboratory Improvement Amendment (CLIA) Certificate number', blank=True, max_length=255)
    state_license_info = models.CharField('State Laboratory License/Registration number', blank=True, max_length=255)
    driver_license_info = models.CharField('Driver’s license or state-issued identification number and state of issuance', blank=True, max_length=255)


##############################################################################################
## Proof of Liability Insurance
##############################################################################################    
class Model_J(models.Model):
    class Meta:
        abstract = True


    li_company = models.CharField('Name of insurance company', blank=True, max_length=255)
    li_number = models.CharField('Insurance policy number', blank=True, max_length=255)
    li_agent = models.CharField('Insurance agent’s name', blank=True, max_length=255)
    li_agent_phone = models.CharField('Telephone number', blank=True, max_length=255)
  
    li_policy_issued = models.DateField('Date policy issued (mm/dd/yyyy)', blank=True, null=True)
    li_policy_expiration = models.DateField('Expiration date of policy (mm/dd/yyyy)', blank=True, null=True)


##############################################################################################
## Proof of Professional Liability Insurance
##############################################################################################    
class Model_K(models.Model):
    class Meta:
        abstract = True
    
    pli_company = models.CharField('Name of insurance company', blank=True, max_length=255)
    pli_number = models.CharField('Insurance policy number', blank=True, max_length=255)
    pli_agent = models.CharField('Insurance agent’s name', blank=True, max_length=255)
    pli_agent_phone = models.CharField('Telephone number', blank=True, max_length=255)
  
    pli_policy_issued = models.DateField('Date policy issued (mm/dd/yyyy)', blank=True, null=True)
    pli_policy_expiration = models.DateField('Expiration date of policy (mm/dd/yyyy)', blank=True, null=True)


##############################################################################################
## Workers’ Compensation insurance
##############################################################################################    
class Model_L(models.Model):
    class Meta:
        abstract = True

    wci_state = models.IntegerField('Does the applicant have Workers Compensation insurance as required by state law?', choices=const.WCI_STATES, null=True)
    wci_explanation = models.CharField('If applicable, attach proof of maintenance of Workers Compensation insurance. If not applicable, check N/A and provide an explanation below', 
                                      blank=True, max_length=255)
    
   
##############################################################################################
## Date of birth & Gender & Other numbers
##############################################################################################    
class Model_M(models.Model):
    class Meta:
        abstract = True
    
    date_birth = models.DateField('Date of birth', blank=True, null=True)
    gender = models.BooleanField('Gender', default=False)
    any_local_numbers = models.CharField('Any local business license numbers, permits (attach a legible copy(ies)) If N/A, provide explanation', blank=True, max_length=255)
    sellers_permit_number= models.CharField('Seller’s Permit number', blank=True, max_length=255)


##############################################################################################
## Information About Individual Signing This Application
##############################################################################################    
class Model_N(models.Model):
    class Meta:
        abstract = True
        
    # 26
    sig_print_name = models.CharField("""Print name of applicant or provider or person 
                                         signing the application on behalf of the applicant or provider""", blank=True, max_length=255)
    # 27
    sig_gender = models.BooleanField('Gender', default=False)

    # 28
    sig_driver_license = models.CharField('Driver’s license or state-issued identification number and state of issuance', blank=True, max_length=255)
    
    # 29
    sig_date_birth = models.DateField('Date of birth', blank=True, null=True)
    
    # 30
    sig_social_number = models.CharField('Social security number', blank=True, max_length=255)


    # 31 block
    sig_signature = models.CharField('Signature of provider or person on behalf of the applicant or provider', blank=True, max_length=255)
    sig_title = models.CharField('Title', blank=True, max_length=255)
    sig_city = models.CharField('Executed at city', blank=True, max_length=255)
    sig_state = models.CharField('Executed at state', choices=const.STATES, blank=True, max_length=2)
    sig_date = models.DateField('Executed at date', blank=True, null=True)
    
    # 32
    sig_notary = models.CharField("""Notary Public — Please see instructions under number 32 for who 
                          must have their application signed by a Notary Public in the form specified by
                          Section 1189 of the Civil Code.""", blank=True, max_length=255)
    

##############################################################################################
## Contact Person’s Information
##############################################################################################    
class Model_O(models.Model):
    class Meta:
        abstract = True

    # 33 block
    con_same_person = models.BooleanField("""Check here if you are the same person identified in item 26. 
                                             If you checked the box, provide only the e-mail address and telephone number below""", default=False)
    
    con_name = models.CharField('Contact Person’s Name (last first middle)', blank=True, max_length=255)
    con_gender = models.BooleanField('Gender', default=False)

    con_title = models.CharField('Title/Position', blank=True, max_length=255)
    con_email = models.EmailField('E-mail address', blank=True, max_length=255)
    con_phone = models.CharField('Telephone number', blank=True, max_length=255)

##############################################################################################
## 
##############################################################################################    

# = models.BooleanField('', default=False)
# = models.CharField('', blank=True, max_length=255)
# = models.DateField('', blank=True, null=True)
    

class Provider(Model_A, Model_B, Model_C, Model_D, Model_E, Model_F, Model_G, Model_H, 
               Model_I, Model_J, Model_K, Model_L, Model_M, Model_N, Model_O):
    """
    Info about HC Provider
    """
    user = models.OneToOneField(User)
    



@receiver(user_registered)
def create_provider(sender, **kwargs):
    Provider.objects.create(user=kwargs['user'])
    
