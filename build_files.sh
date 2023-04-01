# build_files.sh
pip install django-cors-headers
pip install djangorestframework-simplejwt
pip install psycopg2-binary

pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput