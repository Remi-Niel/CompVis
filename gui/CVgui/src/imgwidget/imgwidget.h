#ifndef __INCLUDED_IMGWIDGET_H
#define __INCLUDED_IMGWIDGET_H

#include <QLabel>
#include <QPixmap>

class ImgWidget : public QLabel
{
    Q_OBJECT

    QLabel *d_label;

    public:
        ImgWidget(QWidget *parent = 0);
        ~ImgWidget();


};

#endif