from pypdf import PdfWriter, PdfReader

file_1 = 'file1.pdf'
file_2 = 'file2.pdf'
file_3 = 'file3.pdf'
output_file = 'merged_document.pdf'


def readAllPage(file, writer):
    reader = PdfReader(file)
    for page in reader.pages:
        writer.add_page(page)


def readFocusPage(file, pages, writer):
    reader = PdfReader(file)
    for page_num in pages:
        if page_num < len(reader.pages):
            writer.add_page(reader.pages[page_num])
        else:
            print(f"Page number {page_num} is out of range for this PDF file.")


writer = PdfWriter()
readAllPage(file_1, writer)
focus_page = [0, 1, 2]
readFocusPage(file_2, focus_page, writer)
readAllPage(file_3, writer)

output_pdf = open(output_file, 'wb')
try:
    writer.write(output_pdf)
finally:
    output_pdf.close()
