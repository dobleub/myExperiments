#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4 import QtSql
from gui import Ui_MainWindow


class Programa(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.modelo = self.generaModelo()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tabla.setModel(self.modelo)
        self.reajusta()
        

        QtCore.QObject.connect(self.ui.action_Salir,QtCore.SIGNAL("activated()"),QtGui.qApp, QtCore.SLOT("quit()") )
        QtCore.QObject.connect(self.ui.refrescar,QtCore.SIGNAL("clicked()"),self.refrescar )
        QtCore.QObject.connect(self.ui.nuevaLinea,QtCore.SIGNAL("clicked()"),self.nuevaLinea )
        QtCore.QObject.connect(self.ui.eliminarLinea,QtCore.SIGNAL("clicked()"),self.eliminarLinea )


    def generaModelo(self):
        self.conectaDB()
        modelo = QtSql.QSqlTableModel(None, self.db)
        modelo.setTable("inventario")
        modelo.setSort(self.recordPrototipo.indexOf("ean13"),QtCore.Qt.AscendingOrder)
        modelo.select()
        return modelo

    def conectaDB(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QPSQL")
        self.db.setHostName("rufus")
        self.db.setDatabaseName("inventario")
        self.db.setUserName("josemaria")
        self.db.setPassword("")
        name = self.db.open()

        query = QtSql.QSqlQuery("select * from inventario",self.db)
        self.recordPrototipo = query.record()


    def reajusta(self):
        self.ui.tabla.resizeColumnsToContents()


    def nuevaLinea(self):
        fila = self.modelo.rowCount()
        self.modelo.insertRow(fila)
        self.reajusta()

        
    def eliminarLinea(self):
        index = self.ui.tabla.currentIndex()
        fila = index.row()
        ean13 = self.modelo.data(self.modelo.index(fila, self.recordPrototipo.indexOf("ean13"))).toString()
        nombre = self.modelo.data(self.modelo.index(fila, self.recordPrototipo.indexOf("nombre"))).toString()

        if QtGui.QMessageBox.question(self, "Borrar linea",
                                      QtCore.QString("¿Desea borrar el producto #%1, «%2»?").arg(ean13).arg(nombre),
                                      QtGui.QMessageBox.Yes|QtGui.QMessageBox.No) == QtGui.QMessageBox.Yes:
            self.modelo.removeRow(fila)
            self.reajusta()
        
     
        
        
    def refrescar(self):
        self.modelo.select()
        




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Programa()
    myapp.show()
    sys.exit(app.exec_())