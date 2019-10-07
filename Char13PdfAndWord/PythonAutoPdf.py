import PyPDF2
'''
读取指定pdf文档，并打印内容
'''

pdf = PyPDF2.PdfFileReader(open('PythonAuto.pdf','rb'))
print('该文档有{}页'.format(pdf.numPages))
a = pdf.getPage(0)
pdf.documentInfo
for page in range(0,pdf.numPages):
    pa = pdf.getPage(page).extractText()
    print('第{}页：{}'.format(page,pa.encode().decode('gbk')))



