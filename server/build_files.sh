
echo "BUID START"
python -V
pip install -r requirements.txt
python manage.py collectstatic 
echo "BUID END" 
