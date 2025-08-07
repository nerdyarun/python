🧾 SimplePDFMaker
SimplePDFMaker is a powerful yet lightweight Python tool that lets you generate Invoices, Certificates, and Receipts in bulk from JSON, CSV, or Excel files — fully customizable templates, fonts, logos, and themes!

✨ Features:

Upload CSV, Excel (.xlsx), or JSON files

Auto-generate professional PDFs

Support for Invoices, Certificates, and Receipts

Auto-create Uploads and Outputs folders

Custom HTML templates for branding (fonts, colors, logos)

Bulk generation for hundreds of records

Merge PDFs easily

Ready for selling as your own SaaS, Gumroad product, or internal tool!

📦 Folder Structure

simplepdfmaker/
├── __init__.py
├── core.py            # Core PDF generation logic
├── utils.py           # Upload parsing, folder creation, helper functions
├── templates/         # HTML templates (invoice, certificate, receipt)
│    ├── invoice_classic.html
│    ├── certificate_classic.html
│    └── receipt_classic.html
uploads/                # Uploaded CSV/Excel/JSON files
outputs/                # Generated PDF files
examples/               # Example scripts to generate invoices, receipts, etc
    ├── generate_invoice.py
    ├── generate_certificate.py
    ├── generate_receipt.py
    ├── generate_bulk_invoice.py
README.md  

🚀 Quick Start
1. Install Requirements
pip install pandas openpyxl weasyprint jinja2

2. Prepare Your Data File
Upload a .csv, .xlsx, or .json file inside the uploads/ folder.

Example structure for invoice:
[
  {
    "item": "Website Design",
    "quantity": 1,
    "price": 500,
    "date": "2025-04-27"
  },
  {
    "item": "SEO Optimization",
    "quantity": 1,
    "price": 200,
    "date": "2025-04-27"
  }
]

3. Generate PDFs
Examples available inside /examples/ folder:
python3 examples/generate_invoice.py
python3 examples/generate_certificate.py
python3 examples/generate_receipt.py
python3 examples/generate_bulk_invoice.py

Outputs will be saved inside /outputs/ automatically.

🛠 How it Works
parse_uploaded_file(file_path) → Auto-detects whether input is CSV, Excel, or JSON.

render_pdf(template, data, output) → Renders the Jinja2 template into PDF via WeasyPrint.

generate_invoice(), generate_certificate(), generate_receipt(), generate_bulk_receipts() → Smart functions to handle individual and bulk file creation.

=============================================================
🎨 Customization
Edit HTML templates inside /simplepdfmaker/templates/

Change fonts, add your own company logos, colors, etc

Use multiple template "themes" if needed


