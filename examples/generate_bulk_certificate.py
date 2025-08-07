from simplepdfmaker.utils import parse_uploaded_file
from simplepdfmaker.core import render_pdf, generate_certificate

data = parse_uploaded_file("uploads/sample_certificate.csv")

for idx, person in enumerate(data):
    generate_certificate(
        data_source=person,
        output_filename=f"outputs/certificate_{idx+1}.pdf",
        theme="luxury"
    )
