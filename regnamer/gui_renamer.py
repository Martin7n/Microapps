from gui_renamer_func import file_rename
import FreeSimpleGUI as sg
import os

# from ocr_test_tabula.optimal_info import pdf_to_excel_min
from rename_by_ocr import ocr_file_renamer
from vars import path_to_file

label_1= "Select start folder"
folder_input = sg.Input(default_text='C:\\ren\\')
files_btn = sg.FolderBrowse("Add pdf folder", key="startfolder")


label_3 = "Select registry file"
reg_input = sg.Input(default_text="C:\\rename\\reg.xlsx")
file_input_reg = sg.FileBrowse("Reg. file", key="reg_file")

start_btn = sg.Button("Rename")
status_label = sg.Text("")



window = sg.Window("Renamer",
                   layout=[[folder_input, files_btn],
                           # [folder_input, fldr_btn],
                           [reg_input, file_input_reg],
                           [start_btn, status_label],
                           ],
                   font=("Helvetica", 15))
while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    # print(values, values)

    filepaths = values['startfolder']
    reg_file = values['reg_file']
    print(f"StartFolder {filepaths} reg_file ==> {reg_file}")

    # x_files = file_rename(filepaths, reg_file)
    ocr_file_renamer(filepaths, reg_file)
    # status_label.update(value=f"Rename completed: {x_files} renamed")



window.close()


if __name__ == "__main__":
    pass