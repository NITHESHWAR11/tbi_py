
echo "BUILD START"
sudo apt-get install libsqlite3-dev
pip install pysqlite
pip install -r requirements.txt
python3.9 manage.py collectstatic

echo "BUILD END" 