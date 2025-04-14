## 📝 License

This project is licensed under the [MIT License](LICENSE).

# 🔍 Google Scholar CLI Scraper (Hybrid Mode)

A CLI tool to scrape research paper metadata from Google Scholar.

✅ Default: Lightweight mode using `scholarly`  
🔁 Fallback: Full Chrome browser scraping when needed

---

## 📦 Installation

bash
git clone https://github.com/sharvinsoham/google-scholar-cli.git

cd google-scholar-cli
python3 -m venv venvscholar
source venvscholar/bin/activate
python3 -m pip install setuptools or pip install setuptools
pip install -r requirements.txt
python setup.py sdist bdist_wheel
pip install .

scholarcli --help
scholarcli --query "quantum machine learning" --max-results 10 --save --download-pdf

