#ifndef __INCLUDED_LISTENTRY_H
#define __INCLUDED_LISTENTRY_H

#include <QLabel>
#include <QPixmap>
#include <QVBoxLayout>
#include <QWidget>
#include "../utility/utility.h"

class ListEntry : public QWidget
{
    ImageFile d_file;

    public:
        ListEntry(ImageFile const &imgfile);

        ImageFile &file();
};

#endif