from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, UpdateView, FormView
from django import forms


from models import *
# Create your views here.

SECTIONS = ( ('A', {'title': 'Sec A', 'model': Group_ActionRequested } ), 
             ('B', {'title': 'Sec B', 'model': Group_MediCalApplicationFee } ),
             ('C', {'title': 'Sec C', 'model': Group_TypeOfEntity } ),
             ('D', {'title': 'Sec D', 'model': Group_TypeOfEntity } ),
             ('E', {'title': 'Sec E', 'model': Group_TypeOfEntity} ),
)

SECTIONS_DICT = dict(SECTIONS)

        

class SectionEdit(UpdateView):
    template_name = 'section_edit.html'
    
    def get_form_class(self):
        code = self.kwargs['code']
        info = SECTIONS_DICT[code]
        class DynFrm(forms.ModelForm):
            class Meta:
                model = info['model']
        return DynFrm
    
    
    def get_object(self):
        prov = self.request.user.provider
        return prov

    def get_context_data(self, **kwargs):
        context = super(SectionEdit, self).get_context_data(**kwargs)
        context['active_code'] = self.kwargs['code']
        context['sections'] = SECTIONS
        return context

    def get_success_url(self):
        #url = self.request.path
        return reverse('section_edit', kwargs={'code':'A'})
