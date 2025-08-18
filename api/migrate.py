import os
import sys
import django

# Thiết lập Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from django.core.management import execute_from_command_line
from django.http import JsonResponse

def handler(request):
    try:
        # Chạy migrations
        execute_from_command_line(['manage.py', 'migrate'])
        return JsonResponse({'status': 'success', 'message': 'Migrations completed!'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)