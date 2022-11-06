## 201611466 정원용
## 나만의 음악플레이어

import sys
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QAction, qApp, QDesktopWidget, QFileDialog, QGraphicsOpacityEffect
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, pyqtSlot, Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaContent, QMediaPlayer
from PyQt5.QtMultimedia import *

## GUI 파트
class Ui_Dialog(object):
    def __init__(self):
        self.player = Player(self)
        self.playlist = []
        self.selectedList = [0]
        self.playOption = QMediaPlaylist.Sequential
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(682, 379)        
        ## 프로그램 아이콘 지정
        Dialog.setWindowIcon(QIcon('아이콘.png'))
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 441, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.tableWidget = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 421, 161))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        ## 테이블위젯 스타일시트(재생목록표시부분)
        self.tableWidget.setStyleSheet("QWidget {\n"
                                        "    background-color: transparent;\n"
                                        "}\n"
                                        "\n"
                                        "QHeaderView::section {\n"
                                        "    background-color: transparent;\n"
                                        "    color: #FFFFFF;\n"
                                        "    border-style: solid;\n"
                                        "    border-width: 0px;\n"
                                        "    border-color: #FFFFFF;\n"
                                        "    border-radius: 9px;\n"
                                        "}\n"
                                        "\n"
                                        "QTableWidget {\n"
                                        "    background-color: transparent;\n"
                                        "    color: #FFFFFF;\n"
                                        "    border-style: solid;\n"
                                        "    border-width: 2px;\n"
                                        "    border-color: #FFFFFF;\n"
                                        "    border-radius: 9px;\n"
                                        "}")
        ## 테이블 수정불가(아이템 수정 거부) 트리거
        self.tableWidget.setEditTriggers(self.tableWidget.NoEditTriggers)
        ## QtableWidget 제목부분 사이즈 조절
        self.tableWidget.setColumnWidth(0,420)
        ## 테이블위젯 클릭시 처리
        self.tableWidget.itemSelectionChanged.connect(self.tableChanged)
        self.tableWidget.itemDoubleClicked.connect(self.tableDbClicked)
        #brush = QtGui.QBrush(QtGui.QColor(55, 182, 144))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        #item = QtWidgets.QTableWidgetItem()
        #item.setBackground(QtGui.QColor(255, 255, 255))
        #self.tableWidget.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(460, 10, 161, 191))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.gridLayoutWidget_2)
        self.groupBox_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.playsong = QtWidgets.QPushButton(self.groupBox_2)
        self.playsong.setGeometry(QtCore.QRect(10, 30, 141, 23))
        ## 재생버튼 스타일 지정
        self.playsong.setStyleSheet("color: #FFFFFF;"
                                    "border-style: solid;"
                                    "border-width: 2px;"
                                    "border-color: #FFFFFF;"
                                    "border-radius: 9px")
        self.playsong.clicked.connect(self.playbutton)
        self.playsong.setObjectName("playsong")
        self.pausesong = QtWidgets.QPushButton(self.groupBox_2)
        self.pausesong.setGeometry(QtCore.QRect(10, 60, 141, 23))
        self.pausesong.setStyleSheet("color: #FFFFFF;"
                                    "border-style: solid;"
                                    "border-width: 2px;"
                                    "border-color: #FFFFFF;"
                                    "border-radius: 9px")
        self.pausesong.clicked.connect(self.pausebutton)
        self.pausesong.setObjectName("pausesong")
        self.stopsong = QtWidgets.QPushButton(self.groupBox_2)
        self.stopsong.setGeometry(QtCore.QRect(10, 90, 141, 23))
        self.stopsong.setStyleSheet("color: #FFFFFF;"
                                    "border-style: solid;"
                                    "border-width: 2px;"
                                    "border-color: #FFFFFF;"
                                    "border-radius: 9px")
        self.stopsong.clicked.connect(self.stopbutton)
        self.stopsong.setObjectName("stopsong")
        self.beforesong = QtWidgets.QPushButton(self.groupBox_2)
        self.beforesong.setGeometry(QtCore.QRect(10, 120, 141, 23))
        self.beforesong.setStyleSheet("color: #FFFFFF;"
                                    "background-color: #FFFFFF;"
                                    "border-style: solid;"
                                    "border-width: 2px;"
                                    "border-color: #FFFFFF;"
                                    "border-radius: 9px")
        self.beforesong.clicked.connect(self.prevbutton)
        self.beforesong.setObjectName("beforesong")
        self.nextsong = QtWidgets.QPushButton(self.groupBox_2)
        self.nextsong.setGeometry(QtCore.QRect(10, 150, 141, 23))
        self.nextsong.setStyleSheet("color: #FFFFFF;"
                                    "border-style: solid;"
                                    "border-width: 2px;"
                                    "border-color: #FFFFFF;"
                                    "border-radius: 9px")
        self.nextsong.clicked.connect(self.nextbutton)
        self.nextsong.setObjectName("nextsong")
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(630, 10, 46, 191))
        self.gridLayoutWidget_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.gridLayoutWidget_3)
        self.groupBox_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_3.setAutoFillBackground(False)
        self.groupBox_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.volume = QtWidgets.QSlider(self.groupBox_3)
        self.volume.setGeometry(QtCore.QRect(10, 20, 22, 160))
        self.volume.setOrientation(QtCore.Qt.Vertical)
        self.volume.setStyleSheet("QSlider::handle:vertical {"
                                    "background: #E4F7BA;"
                                    "border: 2px solid #FFFFFF;"
                                    "}")
        self.volume.setRange(0, 100)
        self.volume.setValue(50)
        self.volume.valueChanged[int].connect(self.volumeChanged)
        self.volume.setObjectName("volume")
        self.gridLayout_3.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(10, 250, 661, 61))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox_5 = QtWidgets.QGroupBox(self.gridLayoutWidget_6)
        self.groupBox_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_5.setObjectName("groupBox_5")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_5)
        self.progressBar.setGeometry(QtCore.QRect(10, 20, 641, 23))
        self.progressBar.setProperty("value", 0)
        ## 프로그래스바 스타일시트
        self.progressBar.setStyleSheet("QProgressBar {"
                                            "border: 2px solid white;"
                                            "border-radius: 9px;"
                                            "text-align: center;"
                                        "}"
                                        "QProgressBar::chunk {"
                                            "background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #F15F5F, stop: 1 #E4F7BA);"
                                        "}")
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_6.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.gridLayoutWidget_7 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(10, 320, 441, 51))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_4 = QtWidgets.QGroupBox(self.gridLayoutWidget_7)
        self.groupBox_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_4.setObjectName("groupBox_4")
        self.onesong = QtWidgets.QRadioButton(self.groupBox_4)
        self.onesong.setGeometry(QtCore.QRect(10, 20, 90, 16))
        ## 라디오버튼 초기체크
        self.onesong.setChecked(True)
        self.onesong.clicked.connect(self.radClicked1)
        self.onesong.setObjectName("onesong")
        ## 기본적으로 한곡반복으로 설정
        self.playOption = 1
        self.player.updatePlayMode(1)
        self.allsong = QtWidgets.QRadioButton(self.groupBox_4)
        self.allsong.setGeometry(QtCore.QRect(180, 20, 90, 16))
        self.allsong.clicked.connect(self.radClicked2)
        self.allsong.setObjectName("allsong")
        self.randomsong = QtWidgets.QRadioButton(self.groupBox_4)
        self.randomsong.setGeometry(QtCore.QRect(340, 20, 90, 16))
        self.randomsong.clicked.connect(self.radClicked3)
        self.randomsong.setObjectName("randomsong")
        self.gridLayout_7.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(500, 340, 169, 23))
        ## 프로그램 종료버튼 클릭시 프로그램 종료
        self.pushButton.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton.setStyleSheet("color: #FFFFFF;"
                                    "background-color: #FFFFFF;"
                                    "border-style: solid;"
                                    "border-width: 2px;"
                                    "border-color: #FFFFFF;"
                                    "border-radius: 9px")
        self.pushButton.setObjectName("pushButton")
        self.deletesong = QtWidgets.QPushButton(Dialog)
        self.deletesong.setGeometry(QtCore.QRect(100, 210, 79, 23))
        self.deletesong.setStyleSheet("color: #FFFFFF;"
                                    "background-color: #FFFFFF;"
                                    "border-style: solid;"
                                    "border-width: 2px;"
                                    "border-color: #FFFFFF;"
                                    "border-radius: 9px")
        self.deletesong.clicked.connect(self.delsong)
        self.deletesong.setObjectName("deletesong")
        self.insertsong = QtWidgets.QPushButton(Dialog)
        self.insertsong.setGeometry(QtCore.QRect(10, 210, 79, 23))
        self.insertsong.setStyleSheet("color: #FFFFFF;"
                                    "background-color: #FFFFFF;"
                                    "border-style: solid;"
                                    "border-width: 2px;"
                                    "border-color: #FFFFFF;"
                                    "border-radius: 9px")
        self.insertsong.clicked.connect(self.addsong)
        self.insertsong.setObjectName("insertsong")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        ## 프로그램 배경 이미지
        Dialog.setStyleSheet("background-image: url(웨일1.png);")

    ## 재생
    def playbutton(self):
        if self.tableWidget.rowCount()>0:
                self.player.play(self.playlist, self.selectedList[0], self.playOption)

    ## 일시정지
    def pausebutton(self):
        self.player.pause()

    ## 정지
    def stopbutton(self):
        self.player.stop()

    ## 이전곡
    def prevbutton(self):
        self.player.prev()

    ## 다음곡
    def nextbutton(self):
        self.player.next()

    ## 음악추가
    def addsong(self):
        fname = QFileDialog.getOpenFileNames(None
                                             , '음악탐색'
                                             , ''
                                             , '음악파일 (*.mp3 *.wav *.ogg *.flac *.wma)')
        cnt = len(fname[0])       
        row = self.tableWidget.rowCount()        
        self.tableWidget.setRowCount(row + cnt)
        for i in range(row, row+cnt):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(fname[0][i-row]))

        self.createPlaylist()

    ## 테이블 클릭으로 음악 재생
    def tableDbClicked(self, e):
        self.player.play(self.playlist, self.selectedList[0], self.playOption)

    ## 볼륨 변경
    def volumeChanged(self):
        self.player.upateVolume(self.volume.value())

    ## 음악삭제
    def delsong(self):        
        row = self.tableWidget.rowCount()      
 
        index = []       
        for item in self.tableWidget.selectedIndexes():
            index.append(item.row())        
         
        index = list(set(index))        
        index.reverse()        
        for i in index:
            self.tableWidget.removeRow(i)
         
        self.createPlaylist()

    ## 테이블의 포커싱 변경
    def tableChanged(self):
        self.selectedList.clear()        
        for item in self.tableWidget.selectedIndexes():
            self.selectedList.append(item.row())
         
        self.selectedList = list(set(self.selectedList))
         
        if self.tableWidget.rowCount()!=0 and len(self.selectedList) == 0:
            self.selectedList.append(0)

    ## 플레이리스트 생성
    def createPlaylist(self):
        self.playlist.clear()
        for i in range(self.tableWidget.rowCount()):
            self.playlist.append(self.tableWidget.item(i,0).text())

    ## 라디오버튼 이벤트(한곡반복)
    def radClicked1(self):
        self.playOption = 1
        self.player.updatePlayMode(1)

    ## 라디오버튼 이벤트(전체반복)    
    def radClicked2(self):
        self.playOption = 3
        self.player.updatePlayMode(3)

    ## 라디오버튼 이벤트(랜덤재생)    
    def radClicked3(self):
        self.playOption = 4
        self.player.updatePlayMode(4)
        
    ## 노래변경시 테이블위젯의 포커스 변경 (테이블의 줄 선택을 바꿔줌)
    def updateMediaChanged(self, index):
         if index>=0:
            self.tableWidget.selectRow(index)            

    ## 노래의 재생시간 구하여 프로그래스바의 시작과 끝 설정
    def updateDurationChanged(self, index, msec):        
        if self.progressBar:
            self.progressBar.setRange(0, msec)       

    ## 현재 재생시간(위치) 업데이트
    def updatePositionChanged(self, index, msec):
        if self.progressBar:
            self.progressBar.setValue(msec)

    ## GUI
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "201611466 정원용 나만의 음악플레이어"))
        self.groupBox.setTitle(_translate("Dialog", "재생목록"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "제목"))
        self.groupBox_2.setTitle(_translate("Dialog", "컨트롤"))
        self.playsong.setText(_translate("Dialog", "재생"))
        self.pausesong.setText(_translate("Dialog", "일시정지"))
        self.stopsong.setText(_translate("Dialog", "정지"))
        self.beforesong.setText(_translate("Dialog", "이전 곡"))
        self.nextsong.setText(_translate("Dialog", "다음 곡"))
        self.groupBox_3.setTitle(_translate("Dialog", "볼륨"))
        self.groupBox_5.setTitle(_translate("Dialog", "경과시간"))
        self.groupBox_4.setTitle(_translate("Dialog", "플레이 설정"))
        self.onesong.setText(_translate("Dialog", "한곡 반복"))
        self.allsong.setText(_translate("Dialog", "전체 반복"))
        self.randomsong.setText(_translate("Dialog", "랜덤 재생"))
        self.pushButton.setText(_translate("Dialog", "프로그램 종료"))
        self.deletesong.setText(_translate("Dialog", "노래 삭제"))
        self.insertsong.setText(_translate("Dialog", "노래 추가"))

class Player:
    ## 생성자
    def __init__(self, parent):
        ## 윈도우 객체
        self.parent = parent
 
        self.player = QMediaPlayer()
        self.player.currentMediaChanged.connect(self.mediaChanged)
        self.player.durationChanged.connect(self.durationChanged)
        self.player.positionChanged.connect(self.positionChanged)
         
        self.playlist = QMediaPlaylist()
        
    ## 재생
    def play(self, playlists, startRow=0, option=QMediaPlaylist.Sequential):       
        if self.player.state() == QMediaPlayer.PausedState:
            self.player.play()
        else:              
            self.createPlaylist(playlists, startRow, option)            
            self.player.setPlaylist(self.playlist)
            self.playlist.setCurrentIndex(startRow)
            self.player.play()          

    ## 일시정지
    def pause(self):
        self.player.pause()         

    ## 정지
    def stop(self):
        self.player.stop()

    ## 이전곡
    def prev(self):        
        self.playlist.previous()     

    ## 다음곡
    def next(self):
        self.playlist.next()

    ## 플레이리스트 생성
    def createPlaylist(self, playlists, startRow=0, option=QMediaPlaylist.Sequential):        
        self.playlist.clear()      
 
        for path in playlists:
            url = QUrl.fromLocalFile(path)
            self.playlist.addMedia(QMediaContent(url))
 
        self.playlist.setPlaybackMode(option)

    ## 재생모드 업데이트
    def updatePlayMode(self, option):
        self.playlist.setPlaybackMode(option)

    ## 볼륨 업데이트
    def upateVolume(self, vol):
        self.player.setVolume(vol)

    ## 다음곡의 포커스 이동
    def mediaChanged(self, e):
        self.parent.updateMediaChanged(self.playlist.currentIndex())       

    ## 노래의 총 재생시간
    def durationChanged(self, msec):
        if msec>0:
            self.parent.updateDurationChanged(self.playlist.currentIndex(), msec)

    ## 현재 재생시간
    def positionChanged(self, msec):
        if msec>0:
            self.parent.updatePositionChanged(self.playlist.currentIndex(), msec)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
