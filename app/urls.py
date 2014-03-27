from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, RedirectView

from views import SectionEdit


urlpatterns = patterns('',
   url(r'^users/', RedirectView.as_view(url='/section/A/edit/')),
   url(r'^section/(?P<code>\w+)/edit/$', SectionEdit.as_view(), name='section_edit' ) 
)
