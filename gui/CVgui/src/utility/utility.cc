#include "utility.h"

std::vector<ImageFile> list_images(QString folder)
{
    std::vector<ImageFile> rval;
    QDirIterator it{folder, QDir::Files};

    while (it.hasNext())
    {
        QString file = it.next();
        // qDebug() << file;
        rval.push_back(file);
    }

    std::sort(rval.begin(), rval.end());
    return rval;
}
