import os
import sys
import django
from pathlib import Path

# ========================================
# CẤU HÌNH MẶC ĐỊNH - THAY ĐỔI Ở ĐÂY
# ========================================
DEFAULT_USERNAME = "admin"
DEFAULT_EMAIL = "vn01122003@gmail.com"
DEFAULT_PASSWORD = "vn01122003"

def setup_django():
    """Thiết lập Django environment"""
    project_root = Path(__file__).parent
    sys.path.insert(0, str(project_root))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
    django.setup()

def create_superuser():
    """Tạo superuser với cấu hình mặc định"""
    try:
        from django.contrib.auth.models import User
        
        print("🚀 Tạo Superuser với Cấu hình Mặc định")
        print("=" * 45)
        print(f"�� Username: {DEFAULT_USERNAME}")
        print(f"📧 Email: {DEFAULT_EMAIL}")
        print(f"�� Password: {DEFAULT_PASSWORD}")
        print("=" * 45)
        
        # Kiểm tra xem user đã tồn tại chưa
        if User.objects.filter(username=DEFAULT_USERNAME).exists():
            print(f"⚠️  Username '{DEFAULT_USERNAME}' đã tồn tại!")
            
            # Cập nhật user hiện tại thành superuser
            user = User.objects.get(username=DEFAULT_USERNAME)
            user.is_staff = True
            user.is_superuser = True
            user.set_password(DEFAULT_PASSWORD)
            user.email = DEFAULT_EMAIL
            user.save()
            
            print(f"✅ User '{DEFAULT_USERNAME}' đã được cập nhật thành superuser!")
        else:
            # Tạo superuser mới
            user = User.objects.create_user(
                username=DEFAULT_USERNAME,
                email=DEFAULT_EMAIL,
                password=DEFAULT_PASSWORD
            )
            print(f"✅ Superuser '{DEFAULT_USERNAME}' đã được tạo thành công!")
        
        print(f"\n📋 Thông tin Superuser:")
        print(f"   Username: {user.username}")
        print(f"   Email: {user.email}")
        print(f"   User ID: {user.id}")
        print(f"   Is Staff: {user.is_staff}")
        print(f"   Is Superuser: {user.is_superuser}")
        
        print(f"\n�� Bây giờ bạn có thể đăng nhập vào Django Admin:")
        print(f"   URL: http://your-domain.com/admin/")
        print(f"   Username: {DEFAULT_USERNAME}")
        print(f"   Password: {DEFAULT_PASSWORD}")
        
        return True
        
    except Exception as e:
        print(f"❌ Lỗi khi tạo superuser: {e}")
        return False

def main():
    """Hàm chính"""
    print("�� Django Quick Superuser Creator")
    print("=" * 35)
    
    # Thiết lập Django
    try:
        setup_django()
        print("✅ Django environment đã được thiết lập!")
    except Exception as e:
        print(f"❌ Lỗi khi thiết lập Django: {e}")
        sys.exit(1)
    
    # Tạo superuser
    if create_superuser():
        print("\n🎉 Hoàn thành! Superuser đã sẵn sàng sử dụng.")
    else:
        print("\n❌ Không thể tạo superuser!")
        sys.exit(1)

if __name__ == "__main__":
    main()