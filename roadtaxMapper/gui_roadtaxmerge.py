import FreeSimpleGUI as sg

from roadtaxMapper.road_tax_file_merge import file_index

label_1= "Select start folder"
folder_input = sg.Input(default_text='Browse to select a folder')
start_btn = sg.Button("Scan & Save")
files_btn = sg.FolderBrowse("Add target folder", key="startfolder")
type_btn = sg.Checkbox("Select Obligations files", default=False, key="type_obligations")
type2_btn = sg.Checkbox("Select ALL", default=False, key="type2")

status_label = sg.Text("")


window = sg.Window("File library",
                   layout=[[folder_input,files_btn], [type_btn], [type2_btn],
                           [start_btn, status_label],
                           ],
                   font=("Helvetica", 15))
while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    try:
        filepaths = values['startfolder']
        type_obligations = values['type_obligations']
        all_types = values['type2']
        status_label.update(value=f"Process completed {file_index(filepaths, type_obligations, all_types)} found")
    except:
        status_label.update(value=f"Enter a valid path")

window.close()


if __name__ == "__main__":
    pass