from simplepdfmaker.utils import parse_uploaded_file
from simplepdfmaker.core import render_pdf, generate_invoice

data = parse_uploaded_file("uploads/sample_invoice.csv")

for idx, invoice_data in enumerate(data):
    generate_invoice(
        data_source=invoice_data,
        output_filename=f"outputs/invoice_{idx+1}.pdf",
        theme="luxury"
    )
