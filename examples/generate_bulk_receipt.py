from simplepdfmaker.utils import parse_uploaded_file
from simplepdfmaker.core import render_pdf, generate_receipt

data = parse_uploaded_file("uploads/sample_receipt.csv")

for idx, item in enumerate(data):
    generate_receipt(
        data_source=item,
        output_filename=f"outputs/receipt_{idx+1}.pdf",
        theme="classic"
    )