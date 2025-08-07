import pdfkit
from jinja2 import Environment, FileSystemLoader
import os

class PDFGenerator:
    def __init__(self, template_path):
        self.template_path = template_path
        template_dir = os.path.dirname(template_path)
        template_file = os.path.basename(template_path)
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.template = self.env.get_template(template_file)

    def generate_pdf(self, data, output_filename):
        html_out = self.template.render(data)
        pdfkit.from_string(html_out, output_filename)
