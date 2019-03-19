#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include "../imgwidget/imgwidget.h"

#include <QGroupBox>
#include <QHBoxLayout>
#include <QMainWindow>
#include <QPushButton>
#include <QScrollArea>
#include <QWidget>

class MainWindow : public QMainWindow
{
    Q_OBJECT

    /* GUI PARTS */
    QScrollArea *d_list;

    public:
        MainWindow(QWidget *parent = 0);
        ~MainWindow();

    private:
        QScrollArea *create_image_list();
        QWidget *create_control_panel();
};

#endif // MAINWINDOW_H
