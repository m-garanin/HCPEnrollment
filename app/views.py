from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, UpdateView, FormView
from django import forms

from crispy_forms.helper import FormHelper
import sec_forms

from models import *

SECTIONS = ( ('A', {'title': 'Sec A', 'form':sec_forms.SecA } ), 
             ('B', {'title': 'Sec B', 'form':sec_forms.SecB} ),
             ('C', {'title': 'Sec C', 'form':sec_forms.SecC} ),
             ('D', {'title': 'Sec D', 'form':sec_forms.SecD} ),
             ('E', {'title': 'Sec E', 'form':sec_forms.SecE} ),
             ('F', {'title': 'Sec F', 'form':sec_forms.SecF} ),
             ('G', {'title': 'Sec G', 'form':sec_forms.SecG} ),
             ('H', {'title': 'Sec H', 'form':sec_forms.SecH} ),
             ('I', {'title': 'Sec I', 'form':sec_forms.SecI} ),
             ('J', {'title': 'Sec J', 'form':sec_forms.SecJ} ),
             ('K', {'title': 'Sec K', 'form':sec_forms.SecK} ),
             ('L', {'title': 'Sec L', 'form':sec_forms.SecL} ),
             ('M', {'title': 'Sec M', 'form':sec_forms.SecM} ),
             ('N', {'title': 'Sec N', 'form':sec_forms.SecN} ),
             ('O', {'title': 'Sec O', 'form':sec_forms.SecO} ),

)

SECTIONS_DICT = dict(SECTIONS)


class SectionEdit(UpdateView):
    template_name = 'section_edit.html'
    
    def get_form_class(self):
        code = self.kwargs['code']
        info = SECTIONS_DICT[code]
        return info['form']
    
    def get_object(self):
        prov = self.request.user.provider
        return prov

    def get_context_data(self, **kwargs):
        context = super(SectionEdit, self).get_context_data(**kwargs)
        context['active_code'] = self.kwargs['code']
        context['sections'] = SECTIONS
        return context

    def get_success_url(self):
        # go to next section or to 'A'
        code = self.kwargs['code']
        next_code = chr(ord(code)+1)
        if next_code not in SECTIONS_DICT:
            next_code = 'A'
        return reverse('section_edit', kwargs={'code':next_code})
