python -m venv venv
. venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
echo 'please fill your API key in .env file!'
