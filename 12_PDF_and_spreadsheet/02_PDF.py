# Some PDF in general are hard to read since it's don't have a standart unlike csv.
# some diffrent format adjustment can become bizare to reading a PDF
# open source libs : PyPDF2
import PyPDF4

#  PdfFileReader is deprecated and was removed in PyPDF2 3.0.0. Use PdfReader instead
# or using PyPDF4

# READING a PDF
# 'rb' read byte
file = open('./some_pdf/Working_Business_Proposal.pdf','rb')

pdf_reader = PyPDF4.PdfFileReader(file)

# get single pages
page_one = pdf_reader.getPage(0)
# get a text 
# page_one_text = page_one.extractText()

# close data reader
file.close()


# READING and Wtiring PDF

read_f = open('./some_pdf/Working_Business_Proposal.pdf','rb',)

# List of every page's text.
# The index will correspond to the page number.
pdf_text = []

pdf_reader = PyPDF4.PdfFileReader(read_f)

# iterate by range of length pdf pages
for page in pdf_reader.pages:
    pdf_text.append(page.extractText())

# now pdf_text are populate with all text in pages

# print("This is extracted text from this pdf (Working_Business_Proposal.pdf):")
# print(pdf_text)

pages = pdf_reader.getPage(0)

# writing one pages to ea new pdf
pdf_writer = PyPDF4.PdfFileWriter()
pdf_writer.addPage(page)

# 'wb' write byte
pdf_output = open("./some_pdf/Some_New_Doc.pdf","wb")
pdf_writer.write(pdf_output)

read_f.close()
pdf_output.close()
