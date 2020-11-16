## Back-end del módulo de indicadores para UMMEG

# linux/MacOS
export FLASK_ENV=development
python3 manage.py runserver -h 0.0.0.0 -p 5000

# Windows PowerShell revisar el archivo manage.py y escoger el ambiente a utilizar desarrollo o produccion
$env:FLASK_ENV = "development"
python manage.py runserver -h 0.0.0.0 -p 5000
<!-- python3 manage.py runserver -h 0.0.0.0 -p 5000 -->