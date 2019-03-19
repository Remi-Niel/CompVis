#include "mainwindow.h"

#include "../utility/utility.h"
#include "../listentry/listentry.h"

QScrollArea *MainWindow::create_image_list()
{
    QScrollArea *area = new QScrollArea;
    area->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
    area->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOn);
    
    QWidget *widget = new QWidget;
    widget->setLayout(new QVBoxLayout);
    widget->setMinimumSize(120, 600);
    widget->setMaximumSize(120, 16777215);
    widget->sizePolicy().setVerticalStretch(1);

    std::vector<ImageFile> files = list_images("/home/jos/Downloads/lunar_eclipse/");
    for (ImageFile const &file : files)
        widget->layout()->addWidget(new ListEntry(file));

    area->setWidget(widget);
    area->setMaximumSize(120, 16777215);
    return area;
}

QWidget *MainWindow::create_control_panel()
{
    QWidget *widget = new QGroupBox(QString("Controls:"));

    widget->setMinimumSize(225, 600);
    widget->setMaximumSize(225, 10000);

    QVBoxLayout *layout = new QVBoxLayout;
    layout->addWidget(new QLabel("Komen hiero"));
    layout->addStretch(0);
    widget->setLayout(layout);
    

    return widget;
}   