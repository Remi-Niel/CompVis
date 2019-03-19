#include "mainwindow/mainwindow.h"
#include <QApplication>

#include "imgmanip/imgmanip.h"
#include "utility/utility.h"

int main(int argc, char *argv[])
{
    std::vector<ImageFile> files = list_images("/home/jos/Downloads/lunar_eclipse/");
    for (ImageFile const &file : files)
    {
        qDebug() << file.name();
    }

    QApplication a(argc, argv);
    MainWindow w;
    w.show();

    return a.exec();
}
