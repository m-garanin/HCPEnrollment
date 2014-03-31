from django import forms
from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, MultiField
from crispy_forms.bootstrap import InlineField

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
        lo = None
        return lo

    class Meta:
        model = Model_E

