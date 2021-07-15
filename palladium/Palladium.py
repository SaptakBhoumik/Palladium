from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import os
import cnn

start_page = r'''<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
            body{overflow: hidden; color:#4cabff;}
            a:link, a:visited {
                background-color: #4cabff;
                color: white;
                padding: 14px 25px;
                text-align: center;
                border-radius:30px;
                text-decoration: none;
                display: inline-block;
            }
            
            a:hover, a:active {
                background-color: blue;
            }</style></head>
            <body>
                <div align="center" style="font-size:30px;font-family:Arial"><b>Upload the x-ray image of your chest</b></div><br><a href="#" download><div align="center" style="font-size:20px;font-family:Arial">Click here to choose a file</div></a>
            </body>
            </html>'''



result_page=r'''<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
            body{overflow: hidden; color:#4cabff;}
            a:link, a:visited {
                background-color: #4cabff;
                color: white;
                padding: 14px 25px;
                text-align: center;
                border-radius:30px;
                text-decoration: none;
                display: inline-block;
            }
            
            a:hover, a:active {
                background-color: blue;
            }</style></head>
            <body>
                <div align="center" style="font-size:30px;font-family:Arial"><b>Upload the x-ray image of your chest</b></div><br><a href="#" download><div align="center" style="font-size:20px;font-family:Arial">Click here to choose a file</div></a><br>
           <br><div style="font-size:20px;font-family:Arial"><b>report_and_i_will_replace_it</b></div><br><div  style="font-size:20px;font-family:Arial"><b>symptoms_and_i_will_replace_it</b></div>
            </body></html>'''



class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.setWindowTitle("PALLADIUM")
        self.setFixedSize(330, 620)
        self.setStyleSheet('background-color: white;color:white')
        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view .setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.view.page().profile().downloadRequested.connect(self.on_downloadRequested)
        self.view.setHtml(start_page)
        hbox = QtWidgets.QHBoxLayout(self)
        hbox.addWidget(self.view)
        self.setWindowIcon(QtGui.QIcon(os.path.join('images', 'source.jpeg')))


#yes you are right i am using download requested to call python function
    @QtCore.pyqtSlot("QWebEngineDownloadItem*")
    def on_downloadRequested(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", "", "Image(*.*);;")
        print(filename)
        try:
            report=cnn.prediction(filename)
            if report.lower()=="normal":
                report="Congratulations your lungs are in normal condition"
                symptoms=""
            if report.lower()=="covid19":
                report="Looks like you are infected by covid 19. You should go and see a doctor"
                symptoms="Some of the symptoms of covid19 are fever, dry cough, tiredness, loss of taste or smell,difficulty breathing or shortness of breath and headache"
            if report.lower()=="pneumonia":
                report="Looks like you are infected by pneumonia. You should go and see a doctor"
                symptoms="Some of the symptoms of pneumonia are cough, which may produce greenish, yellow or even bloody mucus, fever, shortness of breath rapid, shallow breathing, sharp or stabbing chest pain that gets worse when you breathe deeply or cough, loss of appetite, low energy, and fatigue."
        except:
            report="Unable to process image"
            symptoms=""
        result=result_page.replace("report_and_i_will_replace_it",report)
        result=result.replace("symptoms_and_i_will_replace_it",symptoms)
        self.view.setHtml(result)

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())
