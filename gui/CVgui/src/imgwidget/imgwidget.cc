#include "imgwidget.h"

ImgWidget::ImgWidget(QWidget *parent)
    : QLabel(parent)
{
    QPixmap pix = QPixmap("/home/jos/placeholder.png");

    this->setScaledContents(true);
    this->setPixmap(pix);
    this->setMinimumSize(600, 600);
}

ImgWidget::~ImgWidget()
{

}