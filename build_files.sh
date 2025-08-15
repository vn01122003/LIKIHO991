#!/bin/bash

set -e

echo "BUILD START"

# Bước 1: Cài đặt các thư viện từ requirements.txt
python3.9 -m pip install -r requirements.txt

# Bước 2: Chạy migrate để tạo bảng trong database (Dòng quan trọng đã thiếu)
python3.9 manage.py migrate

# Bước 3: Thu thập các file tĩnh
python3.9 manage.py collectstatic --noinput --clear

echo "BUILD END"