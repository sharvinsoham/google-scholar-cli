from setuptools import setup, find_packages

setup(
    name="google-scholar-cli",
    version="0.1.0",
    packages=find_packages(),  # this auto-detects scholar_scraper package
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "scholarcli = scholar_scrapper.app:app"  # Typer app
        ]
    },
    install_requires=[
        "typer[all]",
        "scholarly",
        "beautifulsoup4",
        "requests",
        "selenium",
        "undetected-chromedriver",
    ],
    python_requires=">=3.7",
)