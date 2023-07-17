TO RUN THE APPLICATION:


pip install -r requirements.txt

python manage.py collectstatic

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

To access django admin panel,
admin_home/

To access the customized admin panel,
admin/

crendentials for both panels,
email:admin
password:admin@123

To create super user :
python manage.py createsuperuser --username=joe --email=joe@example.com

Example :
python manage.py createsuperuser --username=admin --email=admin@example.com
password : admin@123
