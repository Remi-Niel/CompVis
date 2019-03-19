#include "listentry.h"

ListEntry::ListEntry(ImageFile const &imgfile)
:   QWidget(0),
    d_file(imgfile)
{
    QVBoxLayout *layout = new QVBoxLayout;
    
    QPixmap pixmap = QPixmap::fromImage(imgfile.thumbnail());
    QLabel *img = new QLabel();
    img->setPixmap(pixmap);

    QLabel *label = new QLabel();
    label->setText(imgfile.name());

    img->setMinimumSize(100, 100);
    img->setMaximumSize(100, 100);
    label->setMinimumSize(100, 20);
    label->setMaximumSize(100, 20);

    layout->addWidget(img);
    layout->addWidget(label);
    
    this->setMinimumSize(100, 120);
    this->setMaximumSize(100, 120);
    this->setLayout(layout);
}