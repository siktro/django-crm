from django.urls import path

from .views import (lead_list, lead_detail, lead_create,
                    lead_update, lead_delete, LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView)

app_name = 'leads'
# all urls here lies unser domain.com/leads/...
urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),  # ../leads/
    # 'pk' is a special kw that django understand
    path('<int:pk>/', LeadDetailView.as_view(),
         name='lead-detail'),  # ../leads/2,
    path('<int:pk>/update/', LeadUpdateView.as_view(),
         name='lead-update'),  # ../leads/2/update
    path('<int:pk>/delete/', LeadDeleteView.as_view(),
         name='lead-delete'),  # ../lead/2/delete
    path('create/', LeadCreateView.as_view(),
         name='lead-create'),  # ../leads/create/
]
