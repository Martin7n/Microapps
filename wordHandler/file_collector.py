import os
from docx import Document
from PyPDF2 import PdfReader





import win32com.client as win32
#

## Using built in word...
# word = win32.Dispatch("Word.Application")
# doc = word.Documents.Open(r"C:\path\to\file.doc")
# text = doc.Content.Text
# doc.Close()
# word.Quit()
#
# print(text)


def collect_files(dir_path, types="all"):
    docs_and_others = [ "doc", "docx" ,"pdf"]
    filelist = os.listdir(dir_path)

    doc_list = []
    docx_list = []
    pdf_list = []
    lst = [doc_list, docx_list,pdf_list]
    for file in filelist:
        filetype = file.split(".")[-1]
        file_key_name = file[0:6]
        if filetype == "docx":
            docx_list.append(os.path.join(dir_path, file))
        elif filetype == "doc":
            doc_list.append(os.path.join(dir_path, file))
        elif filetype=="pdf":
            pdf_list.append(os.path.join(dir_path, file))

    # pdf_reader(pdf_list)
    docx_reader(docx_list)

# def builtIn_reader_doc(file):
#
#     print(file)
#
#     doc = Document()
#     word = win32.Dispatch("Word.Application")
#     doc = word.Documents.Open(file)
#     text = doc.Content.Text
#     doc.Close()
#     word.Quit()
#
#     print(text)


def docx_reader(docx_list):
    result = ""
    for file in docx_list:
        print(file)
        doc = Document(file)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text[0:2])
        result += f"==============>, {''.join(full_text)}"

    print(result)



def pdf_reader(filelist):

    result = ""

    for file in filelist:
        print(file)
        reader = PdfReader(file)
        page = reader.pages[0]
        text_origin = page.extract_text()
        total_length = len(text_origin)
        short = total_length - 50
        text = text_origin[3:300]
        result+= text

    # print(text)
    print(result)

def content_collector(content_key, content_body):
    pass

def xls_writer(contents):
    pass



if __name__ == '__main__':
    dpath = "C:\\Drob"
    print(collect_files(dpath))