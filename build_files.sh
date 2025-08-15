#!/bin/bash

# Dừng ngay lập tức nếu có bất kỳ lệnh nào thất bại
set -e

# In ra log để biết quá trình build bắt đầu
echo "BUILD START"

# Bước 1: Cài đặt các thư viện từ requirements.txt
python3.9 -m pip install -r requirements.txt

# Bước 2: Chạy migrate để tạo bảng trong database
python3.9 manage.py migrate

# Bước 3: Thu thập các file tĩnh
python3.9 manage.py collectstatic --noinput --clear

# In ra log để biết quá trình build kết thúc
echo "BUILD END"