import os, sys
import eyed3
from PyQt5.QtWidgets import QApplication, QFileDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

def process_audio_files(file_path, input_value):
    filenames = os.listdir(file_path)
    print(filenames)
    list_file_path = os.path.join(file_path, 'list_sys.txt')
    f = open(list_file_path, 'w')
    
    for name in filenames:
        src = os.path.join(file_path, name)
        audiofile = eyed3.load(src)

        tt = name.split('_')
        ttf = '%04d' % (int(tt[0]) + int(input_value))
        mdst = str(ttf)
        ddst = str(ttf)
        for i in range(1, len(tt)):
            mdst = mdst + "_" + tt[i]

        audiofile.tag.artist = "WSU 2023.08.01"
        audiofile.tag.title = mdst
        audiofile.tag.album = "Free For All Comp LP"
        audiofile.tag.album_artist = "For DOF18"
        audiofile.tag.track_num = ttf
        audiofile.tag.save()

        print(name + "\t\t\t>>>" + '{' + tt[0] + '}' + '{' +
            tt[1] + '}' + "\t>>>" + str(ttf) + "\tdst>>>" + mdst)
        ddst = ddst + ".mp3"
        dst = os.path.join(file_path, ddst)
        os.rename(src, dst)
        abc = str(ttf) + " " + mdst
        f.write(abc)
        f.write("\n")

    f.close()

def run_gui():
    app = QApplication(sys.argv)

    # Create the main widget
    widget = QWidget()
    widget.setWindowTitle("Audio File Processing GUI")

    # Create the widgets for input and output
    label_input = QLabel("Enter the input value (e.g., 5730):")
    input_value = QLineEdit()

    label_output = QLabel("Select Folder:")
    output_folder = QLineEdit()
    output_folder.setReadOnly(True)

    button_select_folder = QPushButton("Select Folder")
    button_process_files = QPushButton("Process Files")

    # Create the layout
    layout = QVBoxLayout()
    layout.addWidget(label_input)
    layout.addWidget(input_value)
    layout.addWidget(label_output)
    layout.addWidget(output_folder)
    layout.addWidget(button_select_folder)
    layout.addWidget(button_process_files)

    # Connect the buttons to their respective functions
    def select_folder():
        folder_path = QFileDialog.getExistingDirectory(None, 'Select Folder')
        output_folder.setText(folder_path)

    def process_files():
        folder_path = output_folder.text()
        input_value_text = input_value.text()
        process_audio_files(folder_path, input_value_text)

    button_select_folder.clicked.connect(select_folder)
    button_process_files.clicked.connect(process_files)

    # Set the layout for the main widget
    widget.setLayout(layout)
    widget.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    run_gui()
