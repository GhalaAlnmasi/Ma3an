from django.urls import path
from . import views

app_name = "backOffice"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("agencies/", views.manage_agencies, name="manage_agencies"),
    path("agencies/<int:agency_id>/", views.agency_detail, name="agency_detail"),
    path("agencies/approve/<int:agency_id>/", views.approve_agency, name="approve_agency"),
    path("agencies/reject/<int:agency_id>/", views.reject_agency, name="reject_agency"),
    path("subscriptions/", views.manage_subscriptions, name="manage_subscriptions"),
    path("users/", views.users_list, name="users_list"),
    path("security/", views.system_security, name="system_security"),
    path("subscriptions/", views.manage_subscriptions, name="manage_subscriptions"),
    path("subscriptions/edit/<int:sub_id>/", views.edit_subscription, name="edit_subscription"),
    path("subscriptions/renew/<int:sub_id>/", views.renew_subscription, name="renew_subscription"),
]
