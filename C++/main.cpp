#include "mainwindow.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.setFixedHeight(559);
    w.setFixedWidth(452);
    w.show();
    return a.exec();
}
