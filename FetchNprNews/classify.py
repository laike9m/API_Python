import sys
from PyQt4 import QtGui, QtCore
from fetch import FetchNews     
import os
from os.path import join

# 这里用.会出现relative import只能在package外使用的问题
# 鉴于FetchNews这个名字是unique的,即不会和标准包混淆,可以直接import
# 参见http://stackoverflow.com/questions/16981921/python-3-relative-imports

TEST_URL = [
    'http://www.npr.org/2013/11/10/243068448/a-panorama-of-devastation-drawing-of-wwi-battle-spans-24-feet', #books
    'http://www.npr.org/2013/11/18/245969799/50-years-after-assassination-kennedy-books-offer-new-analysis', #books
]

FILE = [
    'A Panorama Of Devastation- Drawing Of WWI Battle Spans 24 Feet.txt',     

]

i=0
type = "k"

class Example(QtGui.QWidget, FetchNews):
    
    def __init__(self):
        FetchNews.__init__(self)
        super().__init__()  # 只会调用QrGui.QWidget的__init__
        self.initUI()
        
    def search_and_classify(self):
        text = self.qle.toPlainText()
        if text.startswith('http'):    # 单篇文章
            query = '&searchTerm=' + text
            file = '"' + self.search(query) + '"' # FetchNews method
            print(file)
            if type == 'r':
                a = os.popen("rocchio.exe %s" % file).readlines()
                output = ''
                for line in a[-3:]:
                    output += line
            if type == 'k':
                output = ''
                a = os.popen("knn.exe %s" % file).readlines()
                output += a[-1]
            self.lbl.setText(output)
            self.lbl.adjustSize()
        else:
            self.lbl.setText('请输入合法的地址')
    
    
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        
    def initUI(self):      

        self.lbl = QtGui.QLabel(self)
        self.qle = QtGui.QTextEdit(self)
        
        self.qle.move(50, 100)
        self.lbl.move(150, 30)
        self.qle.resize(300,60)
        #self.qle.setText(TEST_URL[i])

        self.btn = QtGui.QPushButton('搜索&分类', self)
        self.btn.setToolTip('This is a <b>QPushButton</b> widget')
        self.btn.clicked.connect(self.search_and_classify)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(50, 50)
        
        self.setGeometry(300, 600, 400, 170)
        self.setWindowTitle('NewsClassify')
        self.center()
        
        self.setWindowIcon(QtGui.QIcon('images\\icon.png'))
        self.show()
              
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()