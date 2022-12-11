import PyPDF2

pdfFileObj = open('Demonstrativo.pdf', 'rb')
pdfReader  = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
text = pageObj.extract_text()
print(text)