import xlsxwriter
from io import StringIO
# https://surgery.med.uky.edu/sites/default/files/ERAS%20%28Example%29.pdf
# https://www.medschool.umaryland.edu/media/SOM/Offices-of-the-Dean/Student-Affairs/documents/ERAS-Sample-Application.pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

output_string = StringIO()
with open('simple1.pdf', 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)

# print(output_string.getvalue())
text = output_string.getvalue()
print(text)
newtxt = text.splitlines()
print(newtxt)
while(" " in newtxt) :
    newtxt.remove(" ")
while("" in newtxt) :
    newtxt.remove("")
print(newtxt)

# print()
# print(newtxt)

app = newtxt.index('Applicant ID:  2020178395')
birth = newtxt.index('Birth Date:   06/16/1902') 
mil = newtxt.index('Military Service Obligation/Deferment? No')
md = newtxt.index('University of Maryland School')
# print(newtxt.index('of Medicine'))
# print(newtxt.index('United States of America'))
# print(newtxt.count('Work Experience'))
# print(newtxt.count('Research Experience')) #0
# print(newtxt.count('Volunteer Experience')) #0
name = newtxt.index('Robert, Dorcas (14726279)')

workbook = xlsxwriter.Workbook('presentationtest1.xlsx')
worksheet = workbook.add_worksheet()


worksheet.write('A1',f'{newtxt[name]}')
worksheet.write('B1', f'{newtxt[app]}')
worksheet.write('C1', f'{newtxt[birth]}')
worksheet.write('D1', f'{newtxt[mil]}')
worksheet.write('E1', f'{newtxt[md]}')

newlist = newtxt
output_dic = {}
for i in range(len(newlist)):
    print(newlist[i])
    newlist[i] = newlist[i].split(':')
    print(newlist[i])
    if len(newlist[i]) == 2:
        output_dic[newlist[i][0]] = newlist[i][1]
print(output_dic)
print(output_dic['Applicant ID'])
print(output_dic['Most Recent Medical School'])
print(output_dic['Birth Date'])



worksheet.write('A2', 'N/A')
worksheet.write('B2', output_dic['Applicant ID'])
worksheet.write('C2', output_dic['Birth Date'])
worksheet.write('D2', f'N/a')
worksheet.write('E2', output_dic['Most Recent Medical School'])
workbook.close()