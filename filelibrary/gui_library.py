import FreeSimpleGUI as sg

from filelibrary.indexator import file_index

label_1= "Select start folder"
folder_input = sg.Input(default_text='Browse to select a folder')
start_btn = sg.Button("Scan & Save")
files_btn = sg.FolderBrowse("Add pdf folder", key="startfolder")
type_btn = sg.Checkbox("Select All types", default=False, key="type")

status_label = sg.Text("")


window = sg.Window("File library",
                   layout=[[folder_input,files_btn], [type_btn],
                           [start_btn, status_label],
                           ],
                   font=("Helvetica", 15))
while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    try:
        filepaths = values['startfolder']
        types = values['type']
        status_label.update(value=f"Process completed {file_index(filepaths,types )} found")
    except:
        status_label.update(value=f"Enter a valid path")

window.close()


if __name__ == "__main__":
    pass