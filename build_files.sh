# build_files.sh
pip install django-cors-headers
pip install djangorestframework-simplejwt

pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput