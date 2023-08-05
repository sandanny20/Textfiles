from PyPDF2 import PdfMerger

merger = PdfMerger()
pdfs = ['File1.pdf', 'File2.pdf','File3.pdf']
for pdf in pdfs:
    merger.append(pdf)
merger.write('merge_new_result.pdf')
print('pdffiles merged successfully')
merger.close()