import wpf
import clr;
import sys
import os;
sys.path.append(r"../../PyExplorer")
from PyExplorer import *
from System.Windows import Application, Window


class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'Views/PyExplorerUi.xaml')
        self.DataContext = Directory('C:\Drivers')    

    def Button_Click(self, sender, e):
        self.DataContext = Directory(self.path.Text);
  



if __name__ == '__main__':
    Application().Run(MyWindow())

