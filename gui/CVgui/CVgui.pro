#-------------------------------------------------
#
# Project created by QtCreator 2019-03-19T10:49:47
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = CVgui
TEMPLATE = app

# The following define makes your compiler emit warnings if you use
# any feature of Qt which has been marked as deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS

# You can also make your code fail to compile if you use deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

CONFIG += c++17

# These work for linux (Antergos specifically, might differ per distro)
INCLUDEPATH     += /usr/include/opencv4
LIBS            += -L/lib -lopencv_core -lopencv_highgui -lopencv_imgproc -lopencv_imgcodecs

SOURCES += \
        src/imgmanip/imgmanip.cc \
        \
        src/imgwidget/imgwidget.cc \
        \
        src/listentry/listentry.cc \
        \
        src/mainwindow/mainwindow.cc \
        src/mainwindow/uibuilders.cc \
        \
        src/utility/imagefile.cc \
        src/utility/utility.cc \
        \
        src/main.cc

HEADERS += \
        src/imgmanip/imgmanip.h \
        src/imgwidget/imgwidget.h \
        src/listentry/listentry.h \
        src/mainwindow/mainwindow.h \
        src/utility/utility.h

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

FORMS +=
