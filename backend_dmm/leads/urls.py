from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'leads'

urlpatterns = [
    path('leads/', views.LeadListCreateView.as_view(), name='list_create'),
    path('briefs/', views.BriefListCreateView.as_view(),
         name='brief_list_create'),
]


urlpatterns = format_suffix_patterns(urlpatterns)
