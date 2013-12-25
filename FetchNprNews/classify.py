import sys
from PyQt4 import QtGui, QtCore
from fetch import FetchNews     
# 这里用.会出现relative import只能在package外使用的问题
# 鉴于FetchNews这个名字是unique的,即不会和标准包混淆,可以直接import
# 参见http://stackoverflow.com/questions/16981921/python-3-relative-imports

TEST_URL = 'http://www.npr.org/blogs/alltechconsidered/2013/12/20/255852933/robot-olympics-test-machines-on-human-skills'


class Example(QtGui.QWidget, FetchNews):
    
    def __init__(self):
        FetchNews.__init__(self)
        super().__init__()  # 只会调用QrGui.QWidget的__init__
        self.initUI()
        
    def search_and_classify(self):
        text = self.qle.text()
        if text.startswith('http'):    # 单篇文章
            query = '&searchTerm=' + text
            self.search(query)  # FetchNews method
        else:
            self.lbl.setText('请输入合法的地址')
        
    def initUI(self):      

        self.lbl = QtGui.QLabel(self)
        self.qle = QtGui.QLineEdit(self)
        
        self.qle.move(10, 100)
        self.lbl.move(60, 40)
        self.qle.resize(500,30)
        self.qle.setText(TEST_URL)

        self.qle.textChanged[str].connect(self.onChanged)
        
        self.btn = QtGui.QPushButton('搜索&分类', self)
        self.btn.setToolTip('This is a <b>QPushButton</b> widget')
        self.btn.clicked.connect(self.search_and_classify)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(50, 50)
        
        self.setGeometry(300, 600, 380, 170)
        self.setWindowTitle('QtGui.QLineEdit')
        self.show()
        
        
    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()        
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()