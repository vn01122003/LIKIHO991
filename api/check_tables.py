import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from django.db import connection
from django.http import JsonResponse

def handler(request):
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