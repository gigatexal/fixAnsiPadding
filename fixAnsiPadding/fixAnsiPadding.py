import wpf
import os

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'fixAnsiPadding.xaml')
              

    def button_Click(self, sender, e):
        self.listBox.ItemsSource = []  
        myTest = ''
        myTest = self.lbl.GetLineText(0)
        self.listBox.ItemsSource = [myTest for x in range(1,5)]
        
            
    def textBox_TextChanged(self, sender, e):
        if self.textBox.GetLineText(0).Length > 1:
            self.listBox.ItemsSource = ['Now hit run']
    
    def listBox_SelectionChanged1(self, sender, e):
        pass
    


    
    
    

if __name__ == '__main__':
    Application().Run(MyWindow())
