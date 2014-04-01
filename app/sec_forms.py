from django import forms
from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, ButtonHolder, Submit, Div, HTML, MultiField
from crispy_forms.bootstrap import InlineField, InlineRadios

from models import *


class BaseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))
        self.helper.layout = self.get_layout()

    def get_layout(self):
        raise NotImplemented



class SecA(BaseForm):
    class Meta:
        model = Model_A
    
    def get_layout(self):
        lo = Layout(
                    'npi',
                    Fieldset(
                        'Enrollment action requested (check all that apply)',
                        'new_provider',
                        'change_of_business_address', 
                        'additional_business_address', 
                        'new_taxpayer_id_number',
                        'facility_based_provider',
                        MultiField('Change of ownership',
                                   InlineField('change_of_ownership'),
                                   InlineField('change_of_ownership_date')) ,
                        'cumulative_change_of_50_person',
                        'sale_of_assets_50_percent',
                        'ar_special_effective_date',
                        'continued_enrollment',
                        'i_intend'
                    ),
        )
        return lo




class SecB(BaseForm):
    class Meta:
        model = Model_B

    def get_layout(self):
        lo = Layout(Fieldset('Medi-Cal Application Fee (check all that apply)',
                             'enrollment_as_an_individual_nonphysician_practitioner',
                             'enrolled_in_the_medicare_program',
                             'enrolled_in_another_program',
                             'i_have_paid_the_application_fee',
                             'i_have_included_an_application_fee'
                         ))
        return lo



class SecC(BaseForm):
    class Meta:
        model = Model_C

    def get_layout(self):
        lo = Layout(Fieldset('Type of entity',
                             'type_of_entity',
                             'corporate_number',
                             'state_incorporated',
                             'llc_number',
                             'state_registered_filed',
                             'type_of_nonprofit',
                             'other_description'))
        return lo


class SecD(BaseForm):
    class Meta:
        model = Model_D

    def get_layout(self):
        lo = Layout('legal_name',
                    'business_name',
                    'fictitious_business_name',
                    'fictitious_number',
                    'fictitious_effective_date',
                    'business_telephone_number')
        return lo


class SecE(BaseForm):
    def get_layout(self):
        lo = Layout(
               Fieldset('Business address',
                        'ba_title', 'ba_city', 'ba_county', 'ba_state', 'ba_zip'
                    ),

               Fieldset('If you are applying as a facility-based provider, complete this section:',
                        'is_a_licensed_facility',
                        HTML('<div class="alert alert-info">If yes, check the option that applies:</div>'),
                        'facility_option_1', 'facility_option_2'
                        ),
            
               Fieldset('Pay-to address',
                        'pa_title', 'pa_city', 'pa_county', 'pa_state', 'pa_zip'
                    ),            

               Fieldset('Mailing address',
                        'ma_title', 'ma_city', 'ma_county', 'ma_state', 'ma_zip'
                    ),

        
                HTML('<div class="alert alert-info">For a change of business address, enter location moving from:</div>'),
                       
               Fieldset('Previous business address',
                        'pr_title', 'pr_city', 'pr_county', 'pr_state', 'pr_zip'
                    )


            )

        return lo

    class Meta:
        model = Model_E


class SecF(BaseForm):
    def get_layout(self):
        lo = None
        return None
        
    class Meta:
        model = Model_F


class SecG(BaseForm):
    def get_layout(self):
        lo = None
        return None
        
    class Meta:
        model = Model_G

class SecH(BaseForm):
    def get_layout(self):
        lo = Layout(Fieldset('Nurse Practitioner only',
                             'duration_of_training','clinical_training'
                         )
        )
        return lo
        
    class Meta:
        model = Model_H

class SecI(BaseForm):
    def get_layout(self):
        lo = None
        return None
        
    class Meta:
        model = Model_I

class SecJ(BaseForm):
    def get_layout(self):
        lo = Layout(Fieldset('Proof of Liability Insurance',
                             'li_company','li_number', 'li_agent',
                             'li_agent_phone', 'li_policy_issued', 
                             'li_policy_expiration'
                         ))
        return lo
        
    class Meta:
        model = Model_J



class SecK(BaseForm):
    def get_layout(self):
        lo = Layout(Fieldset('Proof of Professional Liability Insurance',
                             'pli_company','pli_number', 'pli_agent',
                             'pli_agent_phone', 'pli_policy_issued', 
                             'pli_policy_expiration'
                         ))
        return lo
        
    class Meta:
        model = Model_K


class SecL(BaseForm):
    def get_layout(self):
        lo = Layout(InlineRadios('wci_state'),
                    'wci_explanation'
                    )
        return lo
        
    class Meta:
        model = Model_L

class SecM(BaseForm):
    def get_layout(self):
        lo = None
        return None
        
    class Meta:
        model = Model_M
