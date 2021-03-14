from django.urls import path

from .views import AgentListView

app_name = 'agents'
# all urls here lies unser domain.com/leads/...
urlpatterns = [
    path('', AgentListView.as_view(), name='agents')
]

