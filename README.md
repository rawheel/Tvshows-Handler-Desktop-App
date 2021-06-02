# Tvshows Listing Desktop App
A simple GUI app to manage tv shows data, Developed using pyqt5 including all basics concepts and understanding.

<img src="https://github.com/rawheel/Tvshows-Listing-Desktop-App/blob/main/screenshots/ss2.png" alt="ss1">

<img src="https://github.com/rawheel/Tvshows-Listing-Desktop-App/blob/main/screenshots/ss1.png" alt="ss1">

## Design UI

```
Two windows:

1)	Main Window
  a.	Frame 
  b.	Combo Box
  c.	Go Button
  d.	Stack Widget
        i.	2 pages
        ii.	3 frames(categories)
            1.	Frame Image
            2.	Button

2)	Table Window
  a.	Table Widget

```
## Qtdesigner to python commands
#### for .ui to .py
```
pyuic5 -x filename.ui -o filename.py
```
#### for .qrc to .py
```
pyrcc5 -x imagefilename.qrc -o imagefilename.py
```

## Addition in main.py

1) Page Number Change
```
def change_page(self):
        current_combo = self.comboBox.currentIndex()
        self.stackedWidget.setCurrentIndex(current_combo)
```
2) Open Table Window
```
def table_window(self,data):
    from table import  Ui_MainWindow
    self.window = QtWidgets.QMainWindow()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self.window,data)
    self.window.show()
```
3) Button Connections
```
self.go_btn.clicked.connect(self.change_page)

from TvshowsData import get_Netflix_action_data,get_HBO_action_data,get_Disney_action_data,get_Netflix_scifi_data,get_HBO_scifi_data,get_Disney_scifi_data,get_Netflix_sitcom_data,get_HBO_sitcom_data,get_Disney_sitcom_data

self.action_btn.clicked.connect(lambda:self.table_window(get_Netflix_action_data()))
self.action_btn_2.clicked.connect(lambda:self.table_window(get_HBO_action_data()))
self.action_btn_3.clicked.connect(lambda:self.table_window(get_Disney_action_data()))

self.sci_btn.clicked.connect(lambda:self.table_window(get_Netflix_scifi_data()))
self.sci_btn_3.clicked.connect(lambda:self.table_window(get_HBO_scifi_data()))
self.sci_btn_4.clicked.connect(lambda:self.table_window(get_Disney_scifi_data()))

self.sitcom_btn.clicked.connect(lambda:self.table_window(get_Netflix_sitcom_data()))
self.sitcom_btn_2.clicked.connect(lambda:self.table_window(get_HBO_sitcom_data()))
self.sitcom_btn_3.clicked.connect(lambda:self.table_window(get_Disney_sitcom_data()))
```

## Addition in table.py

1) Add ```data``` parameter in SetupUi function
```
def setupUi(self, MainWindow,data):
```

2) Add data to table
```
def loadTableData(self,table_data):

    #table_data  = [{'id':1,'name':'GOT','seasons':7,'episodes':70,'ratings':9.5,'network':'HBO'}]
    for row_number , row_data in enumerate(table_data):

        self.tableWidget.insertRow(row_number)
        for column_no , data in enumerate(row_data.values()):
            #print(column_no,data)     
            self.tableWidget.setItem(row_number,column_no,QtWidgets.QTableWidgetItem(str(data)))
```
3) Call loadTableData method
```
self.loadTableData(data)
```
