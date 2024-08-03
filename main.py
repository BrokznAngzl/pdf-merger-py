from pypdf import PdfWriter, PdfReader

file_1 = 'file1.pdf'
file_2 = 'file2.pdf'
file_3 = 'file3.pdf'

writer = PdfWriter()

reader = PdfReader(file_1)
for page in reader.pages:
    writer.add_page(page)

reader = PdfReader(file_2)
for page_num in range(2):
    writer.add_page(reader.pages[page_num])

reader = PdfReader(file_3)
for page in reader.pages:
    writer.add_page(page)

output_pdf = open('merged_document.pdf', 'wb')
writer.write(output_pdf)
output_pdf.close()