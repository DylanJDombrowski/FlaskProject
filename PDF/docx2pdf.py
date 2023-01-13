import docx2pdf

def convert_docx_to_pdf(docx_file, pdf_file):
  docx2pdf.convert(docx_file, pdf_file)
  print(f"Successfully converted {docx_file} to {pdf_file}")

docx_file = "DylanResume.docx"
pdf_file = "DylanResumeConverted.pdf"
convert_docx_to_pdf(docx_file, pdf_file)
