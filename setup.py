from setuptools import setup, find_packages

setup(
    name="simplepdfmaker",
    version="0.1.0",
    description="Simple PDF Report Generator from JSON/CSV",
    author="Your Name",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "weasyprint",
        "jinja2",
        "pandas"
    ],
    python_requires=">=3.7",
)
