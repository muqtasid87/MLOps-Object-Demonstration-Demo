@echo off  # Change this to your actual directory path
start /B python src\utils\scraper\scraper.py
start streamlit run app.py
