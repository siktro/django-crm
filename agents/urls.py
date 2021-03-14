from django.urls import path

from .views import AgentListView, AgentCreateView, AgentDetailView, AgentDeleteView, AgentUpdateView

app_name = 'agents'
# all urls here lies unser domain.com/agents/...
urlpatterns = [
    path('', AgentListView.as_view(), name='agent-list'),
    path('create/', AgentCreateView.as_view(), name='agent-create'),
    path('<int:pk>/detail/', AgentDetailView.as_view(), name='agent-detail'),
    path('<int:pk>/update/', AgentUpdateView.as_view(), name='agent-update'),
    path('<int:pk>/delete/', AgentDeleteView.as_view(), name='agent-delete'),
]
