from simplepdfmaker.utils import parse_uploaded_file
from simplepdfmaker.core import render_pdf, generate_invoice

# Step 1: Parse the file (CSV/Excel/JSON)
data = parse_uploaded_file("uploads/sample_invoice.json")

# Step 2: Pass parsed data
generate_invoice(
    data_source=data,
    output_filename="outputs/generated_invoice.pdf",
    theme="classic"
)

