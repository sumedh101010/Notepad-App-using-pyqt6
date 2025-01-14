import sys # used to quit the python program
from PyQt6.QtWidgets import QInputDialog,QFileDialog,QMenu ,QMenuBar,QTextEdit,QMainWindow,QVBoxLayout,QStackedLayout,QPushButton,QApplication  # QInputDialog to take text from user
from PyQt6.QtGui import QAction,QIcon,QTextCursor,QColor
from PyQt6.QtCore import Qt
class window(QMainWindow): # window inherits property from QMainWindow
    def __init__(self) :  # creating a constructor
     super().__init__()  # we need to call the init method because that will set up our window, super is used beacuse window is sub classs  and QMainWindow is superclass 

     self.initUI()

    def initUI(self):  # self maked the line as instance variable and can be accessed from anywhere    
        self.setWindowTitle('Notepad')
        self.setGeometry(100,100,400,300) #100,100 is the starting point from where is the window drawn
        self.edit_field=QTextEdit(self) # QTextEdit is used to have several lines of words
        self.setCentralWidget(self.edit_field)# we used centralwidget so that text edit spans the entire available spacce
        self.current_file=None # this will store th file the current file is opened or not 
        # create a menubar
        menubar=QMenuBar(self)
        self.setMenuBar(menubar)
        #creating a file menu 
        fileMenu=QMenu("FIle",self) # self is used beacuse it has to belong on the main window 
        menubar.addMenu(fileMenu)  # if u have mac then u have make the native menubar as false
        # create actions (new)
        new_action=QAction("New",self)  
        fileMenu.addAction(new_action) # this is to add under the file menu
        new_action.triggered.connect(self.new_file) # triggered means click so when this "new" is clicked then a new file should be createed 
        # open action
        open_action=QAction('Open',self)
        fileMenu.addAction(open_action)
        open_action.triggered.connect(self.open_file)
        # save action
        save_action=QAction('Save',self)
        fileMenu.addAction(save_action)
        save_action.triggered.connect(self.save_file)
        # save as action
        save_as_action=QAction('Save As',self)
        fileMenu.addAction(save_as_action)
        save_as_action.triggered.connect(self.save_file_as)
        
        #creating an edit menu 
        editmenu=QMenu("Edit",self)
        menubar.addMenu(editmenu)
        #creating undo inside edit bar
        undo_action=QAction("Undo",self)
        editmenu.addAction(undo_action)
        undo_action.triggered.connect(self.edit_field.undo)  #in edit field there is  built in function for menu
    # creating a redo action
        redo_action=QAction('Redo',self)
        editmenu.addAction(redo_action)
        redo_action.triggered.connect(self.edit_field.redo)
    # creating cut inside edit field 
        cut_action=QAction('Cut',self)
        editmenu.addAction(cut_action)
        cut_action.triggered.connect(self.edit_field.cut)
        #creating paste action
        paste_action=QAction('Paste',self)
        editmenu.addAction(paste_action)
        paste_action.triggered.connect(self.edit_field.paste)
       # creating copy action
        copy_action=QAction('Copy',self)
        editmenu.addAction(copy_action)
        copy_action.triggered.connect(self.edit_field.copy)

        # find action
        find_action=QAction('Find',self)
        editmenu.addAction(find_action)
        find_action.triggered.connect(self.find_text)







    def new_file(self):
        print("creating a new file ")  
        self.edit_field.clear()
        self.current_file=None  

    def open_file(self):
        print('opening a file')   
        file_path,_=QFileDialog.getOpenFileName(self,"Open File","","All Files(*);;Python File(*py)")  #"" is used to start from the base directory 
        with open (file_path,"r") as file :
            text=file.read() # this line reads or basically extracts the content from that file 
            self.edit_field.setText(text)
    def save_file_as(self):
        print('saving a file')
        file_path,_=QFileDialog.getSaveFileName(self,"Save File","","All Files(*);;Python File(*py)") # this line only gives u the path to save the file and open the dialog box
        if file_path:      #This code checks if file_path is not empty or None. If it's valid, it opens the file in write mode ("w") and writes the text from self.edit_field to the file
            with open (file_path,"w") as file:
                file.write(self.edit_field.toPlainText())
            self.current_file=file_path
    def save_file(self):
        print("saving a file as")      
        if self.current_file:  # used one the file is already created and we are saving the text inside it
              with open (self.current_file,"w") as file:
                file.write(self.edit_field.toPlainText())
        else: # used when the file is brand new and we have to save it to our desired location
            self.save_file_as()
    def find_text(self):
        print("finding text")  
        search_text,ok=QInputDialog.getText(self,"Find Text","Search for")     # gettext method gives 2 values -the string value is stored in search_text and the boolean value is stored in ok variable 
        if ok:
            all_words=[]
            self.edit_field.moveCursor(QTextCursor.MoveOperation.Start)  # this is used to move cursor to the very start of the edit field
            highlight_color=QColor(Qt.GlobalColor.yellow)

            while(self.edit_field.find(search_text)):
                selection=QTextEdit.ExtraSelection()
                selection.format.setBackground(highlight_color)

                selection.cursor=self.edit_field.textCursor()
                all_words.append(selection)
            self.edit_field.setExtraSelections(all_words)







app=QApplication(sys.argv)   #creating an object of QApplication and in whcih we can pass some arguemnts
window=window()
window.show()  #to display the window\
sys.exit(app.exec())