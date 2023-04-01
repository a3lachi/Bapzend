# build_files.sh
which python
pwd
echo '------------------------------------------------------------------------'
echo '------------------------------------------------------------------------'
echo '------------------------------------------------------------------------'
echo '------------------------------------------------------------------------'
echo '------------------------------------------------------------------------'
echo '------------------------------------------------------------------------'
pip install psycopg2-binary

pip install django-cors-headers
pip install djangorestframework-simplejwt
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput