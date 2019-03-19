#include "mainwindow.h"

#include "../imgwidget/imgwidget.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    // central
    QWidget *central = new QWidget;
    QVBoxLayout *layout = new QVBoxLayout;

    // top part
    QWidget *top = new QWidget;
    QHBoxLayout *toplayout = new QHBoxLayout;

    // bottom bar
    QWidget *buttons = new QWidget;
    QHBoxLayout *buttonlayout = new QHBoxLayout;

    d_list = create_image_list();

    top->setLayout(toplayout);
    toplayout->addWidget(d_list);
    toplayout->addWidget(new ImgWidget);
    toplayout->addWidget(create_control_panel());

    buttons->setLayout(buttonlayout);
    buttonlayout->addWidget(new QPushButton("Load folder"));
    buttonlayout->addWidget(new QPushButton("output video"));

    central->setLayout(layout);
    layout->addWidget(top);
    layout->addWidget(buttons);

    this->setCentralWidget(central);
    this->setVisible(true);
}

MainWindow::~MainWindow()
{

}