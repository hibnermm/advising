import os
from weasyprint import HTML

#OSError: cannot load library 'gobject-2.0-0': error 0x7e.  Additionally, ctypes.util.find_library() did not manage to locate a library called 'gobject-2.0-0


def generate_pdf(url, pdf_file):
  print("Generating PDF...")
  HTML(url).write_pdf(pdf_file)
  if __name__ == '__main__':
    url = 'http://text.npr.org'
    pdf_file = 'media/pdfs/webpage.pdf'
    generate_pdf(url, pdf_file)