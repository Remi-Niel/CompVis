#include "utility.h"

ImageFile::ImageFile(QString const &file)
:   d_file(file)
{ }

bool ImageFile::operator<(ImageFile const &other)
{
    return d_file < other.d_file;
}

QString ImageFile::file() const
{
    return d_file;
}

QString ImageFile::name() const
{
    int index = d_file.lastIndexOf("/", -1);
    return d_file.right(d_file.size() - index - 1);
}

cv::Mat ImageFile::read_cv() const
{
    return cv::imread(d_file.toStdString());
}

QImage ImageFile::read_qt() const
{
    return QImage(d_file);
}

QImage ImageFile::thumbnail(size_t dim) const
{
    QImage original = read_qt();
    return original.scaled(dim, dim, Qt::IgnoreAspectRatio);
}