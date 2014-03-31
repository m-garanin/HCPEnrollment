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
