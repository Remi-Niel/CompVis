#ifndef __INCLUDED_UTILITY_H
#define __INCLUDED_UTILITY_H

#include <QDebug>
#include <QDirIterator>
#include <QImage>
#include <QString>

#include <vector>
#include <opencv2/opencv.hpp>

class ImageFile
{
    QString d_file;

    public:
        ImageFile(QString const &file);
        bool operator<(ImageFile const &other);


        QString file() const;
        QString name() const;

        cv::Mat read_cv() const;
        QImage read_qt() const;
        QImage thumbnail(size_t dim = 100) const;
};

std::vector<ImageFile> list_images(QString folder);

#endif