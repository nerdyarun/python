from simplepdfmaker.core import generate_receipt
from simplepdfmaker.utils import parse_uploaded_file

data = parse_uploaded_file("uploads/sample_receipt.csv")  # or xlsx / json

for idx, receipt_data in enumerate(data):
    generate_receipt(
        data_source=receipt_data,
        output_filename=f"outputs/receipt_{idx+1}.pdf",
        theme="classic",  # or fancy, luxury, etc.
    )
