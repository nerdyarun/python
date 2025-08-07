# simplepdfmaker/core.py

from jinja2 import Environment, FileSystemLoader
import pdfkit
import os
from simplepdfmaker.utils import ensure_folders
from simplepdfmaker.utils import parse_uploaded_file
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATES_DIR = "simplepdfmaker/templates"

env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

def render_pdf(template_name, data, output_filename, theme="classic"):
    env = Environment(loader=FileSystemLoader(os.path.join(BASE_DIR, "templates")))
    template = env.get_template(template_name)
    html_out = template.render(**data)

    # Convert HTML to real PDF
    HTML(string=html_out).write_pdf(output_filename)

    print(f"PDF generated at: {output_filename}")

def generate_invoice(data_source, output_filename="outputs/generated_invoice.pdf", template_file="invoice_classic.html", theme="classic"):
    # Accept either dict or list
    if isinstance(data_source, dict):
        data_source = [data_source]

    if not isinstance(data_source, list):
        raise ValueError("data_source must be a list or dict parsed data!")

    date_value = None
    if data_source and isinstance(data_source[0], dict):
        date_value = data_source[0].get("date", None)

    render_pdf(
        template_file,
        {
            "items": data_source,
            "date": date_value or datetime.now().strftime("%Y-%m-%d"),
        },
        output_filename
    )

def generate_certificate(data_source, output_filename="certificate.pdf", theme="classic"):
    """Generate a single certificate PDF."""
    if isinstance(data_source, str):
        raise ValueError("data_source must be already parsed data!")

    template_file = f"certificate_{theme}.html"
    render_pdf(template_file, data_source, output_filename)

def generate_receipt(data_source, output_filename="receipt.pdf", theme="classic"):
    """Generate a single receipt PDF."""
    if isinstance(data_source, str):
        raise ValueError("data_source must be already parsed data!")

    template_file = f"receipt_{theme}.html"
    render_pdf(template_file, data_source, output_filename)

def generate_bulk_receipts(data_source, output_filename="outputs/generated_bulk_receipts.pdf", theme="classic"):
    """
    Generates a bulk PDF receipt file from a data source (csv, excel, json)
    """
    data = parse_uploaded_file(data_source)

    for i, item in enumerate(data):
        single_output_filename = output_filename.replace(".pdf", f"_{i+1}.pdf")
        render_pdf(f"receipt_{theme}.html", item, single_output_filename)
    
    print(f"Bulk receipts generated successfully: {output_filename}")
