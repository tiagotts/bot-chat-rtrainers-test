python -m venv .venv
pip install -r requirements.txt
pip freeze > requirements.txt

streamlit run app.py