from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ecom import views
from django.contrib.auth.views import LoginView,LogoutView
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.conf.urls.static import static

print("Available views:", [attr for attr in dir(views) if not attr.startswith('_')])
print("migrate_view exists:", hasattr(views, 'migrate_view'))
print("check_tables_view exists:", hasattr(views, 'check_tables_view'))

def migrate_view(request):
    try:
        from django.core.management import execute_from_command_line
        import sys
        
        # Chạy migrations
        execute_from_command_line(['manage.py', 'migrate'])
        return JsonResponse({'status': 'success', 'message': 'Migrations completed!'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

def check_tables_view(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name;
            """)
            tables = [row[0] for row in cursor.fetchall()]
        
        return JsonResponse({
            'status': 'success',
            'tables': tables,
            'count': len(tables)
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name='home'),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='ecom/logout.html'),name='logout'),
    path('aboutus', views.aboutus_view, name='aboutus'),
    path('contactus', views.contactus_view,name='contactus'),
    path('search', views.search_view,name='search'),
    path('send-feedback', views.send_feedback_view,name='send-feedback'),
    path('view-feedback', views.view_feedback_view,name='view-feedback'),

    path('adminclick', views.adminclick_view, name='adminclick'),
    path('adminlogin', LoginView.as_view(template_name='ecom/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('view-customer', views.view_customer_view,name='view-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),
    path('update-customer/<int:pk>', views.update_customer_view,name='update-customer'),

    path('admin-products', views.admin_products_view,name='admin-products'),
    path('admin-add-product', views.admin_add_product_view,name='admin-add-product'),
    path('delete-product/<int:pk>', views.delete_product_view,name='delete-product'),
    path('update-product/<int:pk>', views.update_product_view,name='update-product'),

    path('admin-view-booking', views.admin_view_booking_view,name='admin-view-booking'),
    path('delete-order/<int:pk>', views.delete_order_view,name='delete-order'),
    path('update-order/<int:pk>', views.update_order_view,name='update-order'),

    path('customersignup', views.customer_signup_view, name='customersignup'),
    path('customerlogin', LoginView.as_view(template_name='ecom/customerlogin.html'),name='customerlogin'),
    path('customer-home', views.customer_home_view,name='customer-home'),
    path('my-order', views.my_order_view,name='my-order'),
    path('my-profile', views.my_profile_view,name='my-profile'),
    path('edit-profile', views.edit_profile_view,name='edit-profile'),
    path('download-invoice/<int:orderID>/<int:productID>', views.download_invoice_view,name='download-invoice'),

    path('add-to-cart/<int:pk>', views.add_to_cart_view,name='add-to-cart'),
    path('cart', views.cart_view,name='cart'),
    path('remove-from-cart/<int:pk>', views.remove_from_cart_view,name='remove-from-cart'),
    path('increase-quantity/<int:pk>', views.increase_quantity_view,name='increase-quantity'),
    path('decrease-quantity/<int:pk>', views.decrease_quantity_view,name='decrease-quantity'),
    path('customer-address', views.customer_address_view,name='customer-address'),
    path('payment-success', views.payment_success_view,name='payment-success'),

    # Thêm URLs cho migrations
    path('migrate/', views.migrate_view, name='migrate'),
    path('check-tables/', views.check_tables_view, name='check_tables'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    # Production media serving
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)