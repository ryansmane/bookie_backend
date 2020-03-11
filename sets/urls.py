
from .api import AgentDetail, AgentList, AgencyList, AgencyDetail
from django.urls import path, include


app_name='sets'

urlpatterns = [
    path('api/pop', AgentList.as_view(), name='register_agent'),
    path('api/pop/<int:identity>', AgentDetail.as_view(), name='agent_detail'),
    path('api/agencies/', AgencyList.as_view(), name='register_agency'),
    path('api/agencies/<int:pk>', AgencyDetail.as_view(), name='agency_detail')
    
    
]
