#include "mainwindow.h"
#include "ui_mainwindow.h"
#include<QLineEdit>
#include<QIntValidator>
#include "sudoku.h"

using namespace std;

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QLineEdit* temp[9][9] = {
    {ui->l00, ui->l01, ui->l02, ui->l03, ui->l04, ui->l05, ui->l06, ui->l07, ui->l08},
    {ui->l10, ui->l11, ui->l12, ui->l13, ui->l14, ui->l15, ui->l16, ui->l17, ui->l18},
    {ui->l20, ui->l21, ui->l22, ui->l23, ui->l24, ui->l25, ui->l26, ui->l27, ui->l28},
    {ui->l30, ui->l31, ui->l32, ui->l33, ui->l34, ui->l35, ui->l36, ui->l37, ui->l38},
    {ui->l40, ui->l41, ui->l42, ui->l43, ui->l44, ui->l45, ui->l46, ui->l47, ui->l48},
    {ui->l50, ui->l51, ui->l52, ui->l53, ui->l54, ui->l55, ui->l56, ui->l57, ui->l58},
    {ui->l60, ui->l61, ui->l62, ui->l63, ui->l64, ui->l65, ui->l66, ui->l67, ui->l68},
    {ui->l70, ui->l71, ui->l72, ui->l73, ui->l74, ui->l75, ui->l76, ui->l77, ui->l78},
    {ui->l80, ui->l81, ui->l82, ui->l83, ui->l84, ui->l85, ui->l86, ui->l87, ui->l88}
};
    for (int i=0;i<9;i++)
        for (int j=0;j<9;j++)
            grid[i][j] = temp[i][j];

    for (int i=0;i<9;i++)
        for (int j=0;j<9;j++)
        {
            grid[i][j]->setAlignment(Qt::AlignHCenter);
            grid[i][j]->setValidator((new QIntValidator(1,9,this)));
            grid[i][j]->setMaxLength(1);
        }

}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_solveButton_clicked()
{
   for (int i=0; i<9; i++)
       for (int j=0; j<9; j++)
           solved[i][j] = grid[i][j]->text().toInt();

   Sudoku s(solved);
   if (s.solve())
   {
       ui->label->setStyleSheet("color:green");
       ui->label->setText("Solved!!");
       for (int i=0;i<9;i++)
           for (int j=0;j<9;j++)
           {
               grid[i][j]->setText(QVariant(solved[i][j]).toString());
           }
   }
   else
   {
    ui->label->setStyleSheet("color:red");
    ui->label->setText("No solution available");
   }
}

void MainWindow :: on_clearButton_clicked()
{
    ui->label->setText("");
    for (int i=0;i<9;i++)
        for (int j=0;j<9;j++)
        {
            grid[i][j]->setText("");
        }
}
