# examples/generate_certificate.py

from simplepdfmaker.utils import parse_uploaded_file
from simplepdfmaker.core import render_pdf, generate_certificate

data = parse_uploaded_file("uploads/sample_certificate.json")  # or csv / xlsx

generate_certificate(
    data_source=data[0],   # only one certificate per time
    output_filename="outputs/generated_certificate.pdf",
    theme="luxury"  # or "classic", "modern"
)
