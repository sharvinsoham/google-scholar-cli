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

#go to the repository
cd google-scholar-cli

#Setup a virtual environment
python3 -m venv venvscholar

#activate that virtual environment
source venvscholar/bin/activate

#Install setuptools and requirements
python3 -m pip install setuptools or pip install setuptools

pip install -r requirements.txt

#make wheel
python setup.py sdist bdist_wheel

#Install packages
pip install .

#You're good to go now.
scholarcli --help
#Demo
scholarcli --query "quantum machine learning" --max-results 10 --save --download-pdf

