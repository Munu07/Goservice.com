from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    # Customer
    path('signup/customer/', views.customer_signup_view, name='signup_customer'),
    path('login/customer/', views.customer_login_view, name='login_customer'),
    path('dashboard/customer/', views.customer_dashboard_view, name='customer_dashboard'),
    path('dashboard/customer/profile/', views.customer_profile_view, name='customer_profile'),
    path('dashboard/customer/services/', views.customer_services_view, name='customer_services'),
    path('dashboard/customer/services/<str:profession_name>/', views.customer_providers_by_service_view, name='customer_providers_by_service'),
    path('booking/create/', views.create_booking_view, name='create_booking'),
    path('payment/<int:booking_id>/', views.payment_view, name='payment'),
    path('payment/success/', views.payment_success_view, name='payment_success'),
    path('dashboard/customer/bookings/', views.customer_bookings_view, name='customer_bookings'),
    path('booking/cancel/', views.cancel_booking_view, name='cancel_booking'),
    path('booking/status/<int:booking_id>/', views.get_booking_status_view, name='get_booking_status'),

    # Service Provider
    path('signup/provider/', views.provider_signup_view, name='signup_provider'),
    path('login/provider/', views.provider_login_view, name='login_provider'),
    path('dashboard/provider/', views.provider_dashboard_view, name='provider_dashboard'),
    path('dashboard/provider/list/', views.list_service_view, name='list_service'),
    path('dashboard/provider/profile/', views.provider_profile_view, name='provider_profile'),
    path('dashboard/provider/bookings/', views.provider_view_bookings_view, name='provider_view_bookings'),
    path('dashboard/provider/bookings/update/<int:booking_id>/', views.update_booking_status, name='update_booking_status'),

    # ✅ NEW: Provider Earnings Page
    path('dashboard/provider/earnings/', views.provider_earnings_view, name='provider_earnings'),

    # ✅ NEW: Provider Service History Page
    path('dashboard/provider/service-history/', views.provider_service_history_view, name='provider_service_history'),

    # Admin
    path('login/admin/', views.admin_login_view, name='login_admin'),
    path('dashboard/admin/', views.admin_dashboard_view, name='admin_dashboard'),
    path('dashboard/admin/providers/', views.admin_view_service_providers, name='admin_view_providers'),
    path('dashboard/admin/providers/delete/<int:provider_id>/', views.admin_delete_provider, name='admin_delete_provider'),
    path('dashboard/admin/customers/', views.admin_view_customers, name='admin_view_customers'),
    path('dashboard/admin/customers/delete/<int:customer_id>/', views.admin_delete_customer, name='admin_delete_customer'),

    # Logout
    path('logout/', views.logout_view, name='logout'),
]
