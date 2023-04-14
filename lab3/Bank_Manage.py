#import MySQLdb
from PyQt5 import QtCore,QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTreeWidgetItem
from PyQt5.QtCore import QDate, QTime, Qt
import sys
from numpy import double
import pymysql
from sympy import N, Id, false

from Ui_bank import Ui_MainWindow


class BankManger(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, Connect_bank_Manage) -> None:
        super(BankManger,self).__init__()
        self.conn = Connect_bank_Manage
        self.curso = conn.cursor()
        self.setupUi(self)
        self.setWindowTitle('银行业务管理系统')
        self.display(display_kind='Bank')
        self.display(display_kind='Customer')
        self.display(display_kind='Customer_worker')
        self.display(display_kind='Department')
        self.display(display_kind='Employee')
        self.display(display_kind='check_account')
        self.display(display_kind='saving_account')
        self.display(display_kind='loan')
        self.display(display_kind='pay')
        self.signal_slot()
        
    def signal_slot(self):
        self.Bank_Add.clicked.connect(self.bank_add)
        self.Bank_Del.clicked.connect(self.bank_del)
        self.Bank_Change.clicked.connect(self.bank_change)
        self.Bank_Query.clicked.connect(self.bank_query)
        
        self.Department_Add.clicked.connect(self.department_add)
        self.Department_Del.clicked.connect(self.department_del)
        self.Department_Change.clicked.connect(self.department_change)
        self.Department_Query.clicked.connect(self.department_query)
        
        self.Worker_Add.clicked.connect(self.worker_add)
        self.Worker_Del.clicked.connect(self.worker_del)
        self.Worker_Change.clicked.connect(self.worker_change)
        self.Worker_Query.clicked.connect(self.worker_query)
        
        self.Customer_Add.clicked.connect(self.customer_add)
        self.Customer_Del.clicked.connect(self.customer_del)
        self.Customer_Change.clicked.connect(self.customer_change)
        self.Customer_Query.clicked.connect(self.customer_query)
        
        self.Customer_Add_2.clicked.connect(self.customer_worker_add)
        self.Customer_Del_2.clicked.connect(self.customer_worker_del)
        self.Customer_Change_2.clicked.connect(self.customer_worker_change)
        self.Customer_Query_2.clicked.connect(self.customer_worker_query)
        
        self.Account_Open_Save.clicked.connect(self.account_open_save)
        self.Account_Del_Save.clicked.connect(self.account_del_save)
        self.Account_Change_Save.clicked.connect(self.account_change_save)
        self.Account_Query_Save.clicked.connect(self.account_query_save)
        
        self.Account_Open_Check.clicked.connect(self.account_open_check)
        self.Account_Del_Check.clicked.connect(self.account_del_check)
        self.Account_Change_Check.clicked.connect(self.account_change_check)
        self.Account_Query_Check.clicked.connect(self.account_query_check)
        
        self.Loan_Add.clicked.connect(self.loan_add)
        self.Loan_Del.clicked.connect(self.loan_del)
        self.Loan_Query.clicked.connect(self.loan_query)
        
        self.Loan_Pay.clicked.connect(self.loan_pay)
        
        self.Query_Year.clicked.connect(self.query_year)
        self.Query_Season.clicked.connect(self.query_season)
        self.Query_Month.clicked.connect(self.query_month)
        
    def display(self,display_kind, query = False):
        self.conn.commit()  # 事务的提交
        if display_kind == 'Customer':
            self.CustomerTableWidget.clearContents()
            if query == False:
                self.curso.execute('select * from Customer')
            rows = self.curso.fetchall()
            
            row = self.curso.rowcount
            if row == 0:
                return
            vol = len(rows[0])
            self.CustomerTableWidget.setRowCount(row)
            self.CustomerTableWidget.setColumnCount(vol)
            for i in range(row):
                for j in range(vol):
                    temp_data = rows[i][j]
                    data = QtWidgets.QTableWidgetItem(str(temp_data))
                    self.CustomerTableWidget.setItem(i, j, data)
                    
        if display_kind == 'Customer_worker':
            self.Customer_WorkerTableWidget.clearContents()
            if query == False:
                self.curso.execute('select * from Responsible')
            rows = self.curso.fetchall()
            row = self.curso.rowcount
            if row == 0:
                return
            vol = len(rows[0])
            self.Customer_WorkerTableWidget.setRowCount(row)
            self.Customer_WorkerTableWidget.setColumnCount(vol)
            for i in range(row):
                for j in range(vol):
                    temp_data = rows[i][j]
                    data = QtWidgets.QTableWidgetItem(str(temp_data))
                    self.Customer_WorkerTableWidget.setItem(i, j, data)
                    
        if display_kind == 'Bank':
            self.Bank_TableWidget.clearContents()
            if query == False:
                self.curso.execute('select * from Bank')
            rows = self.curso.fetchall()
            row = self.curso.rowcount
            if row == 0:
                return
            vol = len(rows[0])
            self.Bank_TableWidget.setRowCount(row)
            self.Bank_TableWidget.setColumnCount(vol)
            for i in range(row):
                for j in range(vol):
                    temp_data = rows[i][j]
                    data = QtWidgets.QTableWidgetItem(str(temp_data))
                    self.Bank_TableWidget.setItem(i, j, data)
                    
        if display_kind == 'Department':
            self.Department_TableWidget.clearContents()
            if query == False:
                self.curso.execute('select * from Department')
            rows = self.curso.fetchall()
            row = self.curso.rowcount
            if row == 0:
                return
            vol = len(rows[0])
            self.Department_TableWidget.setRowCount(row)
            self.Department_TableWidget.setColumnCount(vol)
            for i in range(row):
                for j in range(vol):
                    temp_data = rows[i][j]
                    data = QtWidgets.QTableWidgetItem(str(temp_data))
                    self.Department_TableWidget.setItem(i, j, data)
        
        if display_kind == 'Employee':
            self.Worker_TableWidget.clearContents()
            if query == False:
                self.curso.execute('select * from Employee')
            rows = self.curso.fetchall()
            row = self.curso.rowcount
            if row == 0:
                return
            vol = len(rows[0])
            self.Worker_TableWidget.setRowCount(row)
            self.Worker_TableWidget.setColumnCount(vol)
            for i in range(row):
                for j in range(vol):
                    temp_data = rows[i][j]
                    data = QtWidgets.QTableWidgetItem(str(temp_data))
                    self.Worker_TableWidget.setItem(i, j, data)
                
        
        if display_kind == 'check_account':
            self.Check_tableWidget.clearContents()
            if query == False:
                self.curso.execute('select Checking_Account.Account_Id, Checking_Account.Bank_Name, Checking_Account.Account_Balance, Checking_Account.Account_OpenDate, Checking_Account.Overdraft, have_visit.Customer_Id, have_visit.RecentVisit_Date  from Checking_Account INNER JOIN have_visit ON Checking_Account.Account_Id = have_visit.Account_Id ')
            rows = self.curso.fetchall()
            row = self.curso.rowcount
            if row == 0:
                return
            vol = len(rows[0])
            self.Check_tableWidget.setRowCount(row)
            self.Check_tableWidget.setColumnCount(vol)
            for i in range(row):
                for j in range(vol):
                    temp_data = rows[i][j]
                    data = QtWidgets.QTableWidgetItem(str(temp_data))
                    self.Check_tableWidget.setItem(i, j, data)
            
        if display_kind == 'saving_account':
            self.Save_tableWidget.clearContents()
            if query == False:
                self.curso.execute('select Saving_Account.Account_Id, Saving_Account.Bank_Name, Saving_Account.Account_Balance, Saving_Account.Account_OpenDate, Saving_Account.Interest_Rate, Saving_Account.Currency_Type , have_visit.Customer_Id, have_visit.RecentVisit_Date  from Saving_Account INNER JOIN have_visit ON Saving_Account.Account_Id = have_visit.Account_Id ')
            rows = self.curso.fetchall()
            row = self.curso.rowcount
            if row == 0:
                return
            vol = len(rows[0])
            self.Save_tableWidget.setRowCount(row)
            self.Save_tableWidget.setColumnCount(vol)
            for i in range(row):
                for j in range(vol):
                    temp_data = rows[i][j]
                    data = QtWidgets.QTableWidgetItem(str(temp_data))
                    self.Save_tableWidget.setItem(i, j, data)
                    
        if display_kind == 'loan':
            self.Loan_tableWidget.clearContents()
            if query == True and  self.state_query != '':
                rows = self.curso.fetchall()
                row = self.curso.rowcount
                if row == 0:
                    return
                vol = len(rows[0])
                self.Loan_tableWidget.setRowCount(row)
                self.Loan_tableWidget.setColumnCount(vol + 1)
                m = 0
                for i in range(row):
                    money = double(rows[i][2])
                    query = 'select sum(Pay_Money) from Payment where Loan_Id = ' + '\'' + rows[i][0] + '\''
                    self.curso.execute(query)
                    sum = self.curso.fetchone()[0]
                    if sum is None:
                        if self.state_query == '未开始发放':
                            for j in range(vol):
                                temp_data = rows[i][j]
                                data = QtWidgets.QTableWidgetItem(str(temp_data))
                                self.Loan_tableWidget.setItem(m, j, data)
                            self.Loan_tableWidget.setItem(m, vol, QtWidgets.QTableWidgetItem('未开始发放'))    
                            m = m +1    
                    else:
                        sum = double(sum)
                        if sum == 0:
                            if self.state_query == '未开始发放':
                                for j in range(vol):
                                    temp_data = rows[i][j]
                                    data = QtWidgets.QTableWidgetItem(str(temp_data))
                                    self.Loan_tableWidget.setItem(m, j, data)
                                self.Loan_tableWidget.setItem(m, vol, QtWidgets.QTableWidgetItem('未开始发放'))    
                                m = m +1 
                        elif sum < money:
                            if self.state_query == '发放中':
                                for j in range(vol):
                                    temp_data = rows[i][j]
                                    data = QtWidgets.QTableWidgetItem(str(temp_data))
                                    self.Loan_tableWidget.setItem(m, j, data)
                                self.Loan_tableWidget.setItem(m, vol, QtWidgets.QTableWidgetItem('发放中'))    
                                m = m +1 
                        elif sum == money:
                            if self.state_query == '已全部发放':
                                for j in range(vol):
                                    temp_data = rows[i][j]
                                    data = QtWidgets.QTableWidgetItem(str(temp_data))
                                    self.Loan_tableWidget.setItem(m, j, data)
                                self.Loan_tableWidget.setItem(m, vol, QtWidgets.QTableWidgetItem('已全部发放'))    
                                m = m +1 
                return                            
            if query == False:
                self.curso.execute('select * from Loan')
            rows = self.curso.fetchall()
            row = self.curso.rowcount
            if row == 0:
                return
            vol = len(rows[0])
            self.Loan_tableWidget.setRowCount(row)
            self.Loan_tableWidget.setColumnCount(vol + 1)
            for i in range(row):
                for j in range(vol):
                    temp_data = rows[i][j]
                    data = QtWidgets.QTableWidgetItem(str(temp_data))
                    self.Loan_tableWidget.setItem(i, j, data)
                money = double(rows[i][2])
                query = 'select sum(Pay_Money) from Payment where Loan_Id = ' + '\'' + rows[i][0] + '\''
                self.curso.execute(query)
                sum = self.curso.fetchone()[0]
                if sum is None:
                    self.Loan_tableWidget.setItem(i, vol, QtWidgets.QTableWidgetItem('未开始发放'))
                else:
                    sum = double(sum)
                    if sum == 0:
                        self.Loan_tableWidget.setItem(i, vol, QtWidgets.QTableWidgetItem('未开始发放'))
                    elif sum < money:
                        self.Loan_tableWidget.setItem(i, vol, QtWidgets.QTableWidgetItem('发放中'))
                    elif sum == money:
                        self.Loan_tableWidget.setItem(i, vol, QtWidgets.QTableWidgetItem('已全部发放'))
        
        if display_kind == 'pay':
            self.Pay_tableWidget.clearContents()
            self.Pay_tableWidget.setRowCount(1)
            if query == False:
                self.curso.execute('select * from Payment')
            rows = self.curso.fetchall()
            row = self.curso.rowcount
            if row == 0:
                return
            vol = len(rows[0])
            self.Pay_tableWidget.setRowCount(row)
            self.Pay_tableWidget.setColumnCount(vol)
            for i in range(row):
                for j in range(vol):
                    temp_data = rows[i][j]
                    data = QtWidgets.QTableWidgetItem(str(temp_data))
                    self.Pay_tableWidget.setItem(i, j, data)
                    
        if display_kind == 'result':
            self.Business_tableWidget.clearContents()
            if query == False:
                self.curso.execute('select * from Payment')
            rows = self.curso.fetchall()
            row = self.curso.rowcount
            if row == 0:
                return
            vol = len(rows[0])
            self.Business_tableWidget.setRowCount(row)
            self.Business_tableWidget.setColumnCount(vol)
            for i in range(row):
                for j in range(vol):
                    temp_data = rows[i][j]
                    data = QtWidgets.QTableWidgetItem(str(temp_data))
                    self.Business_tableWidget.setItem(i, j, data)
                        
    def cursor_bank(self,request, display_kind, query = False):
        try:
            self.curso.execute(request)
        except:
            return False
        
        self.display(display_kind=display_kind, query = query)
        
    def department_add(self):
        if self.Department_Id.text().isspace():
            department_id = ''
        else:
            department_id = self.Department_Id.text()
        if self.Department_BankName.text().isspace():
            bank_name = ''
        else:
            bank_name = self.Department_BankName.text()
        if self.Department_Name.text().isspace():
            department_name = ''
        else:
            department_name = self.Department_Name.text()
        if self.Department_Type.text().isspace():
            department_type = ''
        else:
            department_type = self.Department_Type.text()
        if self.Department_LeaderId.text().isspace():
            department_leaderid = ''
        else:
            department_leaderid = self.Department_LeaderId.text()
        
        if (department_id == '' or department_name == '' or bank_name == '' or department_type == '' or department_leaderid == ''):
            QMessageBox.information(self,'错误','部门信息填写不完整！暂无领导可填\'无\'')
            return
        
        question = QMessageBox.question(self, '确定', "插入部门信息: \n" +
                                                      "\n部门号: " + department_id +
                                                      "\n部门所在支行名: " + bank_name +
                                                      "\n部门名: " + department_name +
                                                      "\n部门类型: " + department_type +
                                                      "\n部门领导: " + department_leaderid , QMessageBox.No | QMessageBox.Yes , QMessageBox.Yes)
        
        if question == QMessageBox.No:
            return
        
        self.curso.execute('select * from Department where Department_Id = ' + '\'' + department_id + '\'')
        query = self.curso.fetchone()
        if query is not None:
            QMessageBox.information(self,'错误','部门已存在！')
            return
        
        self.curso.execute('select * from Bank where Bank_Name = ' + '\'' + bank_name + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','银行不存在！')
            return
        
        if department_leaderid != '无':
            self.curso.execute('select * from Employee where Employee_Id = ' + '\'' + department_leaderid + '\'')
            query = self.curso.fetchone()
            if query is None:
                QMessageBox.information(self,'错误','员工不存在！')
                return
        add = 'insert into Department Values(' + '\''+ department_id + '\'' + ', ' + '\''+ bank_name + '\'' + ', ' + '\'' + department_name + '\''  + ','  + '\'' + department_type + '\'' +',' +  '\''  +department_leaderid + '\''   +')'
        reply = self.cursor_bank(add,'Department',False)
        if reply == False:
            QMessageBox.information(self,'错误','输入不合法')
            return
        
    def department_del(self):
        if self.Department_Id.text().isspace():
            department_id = ''
        else:
            department_id = self.Department_Id.text()
            
        if (department_id == ''):
            QMessageBox.information(self,'错误','部门删除信息不完整')
            return
        
        question = QMessageBox.question(self, '确定', '是否删除部门号为: '+ department_id + '的部门', QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if question == QMessageBox.No:
            return 
        
        self.curso.execute('select * from Department where Department_Id = ' + '\'' + department_id + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','部门不存在！')
            return
        
        dele = 'delete from Department WHERE  Department_Id = ' + '\'' + department_id + '\''
        reply = self.cursor_bank(dele,'Department',False)
        if reply == False:
            QMessageBox.information(self,'错误','输入不合法')
            return
        
    def department_change(self):
        if self.Department_Id.text().isspace():
            department_id = ''
        else:
            department_id = self.Department_Id.text()
        if self.Bank_Name.text().isspace():
            bank_name = ''
        else:
            bank_name = self.Bank_Name.text()
        if self.Department_Name.text().isspace():
            department_name = ''
        else:
            department_name = self.Department_Name.text()
        if self.Department_Type.text().isspace():
            department_type = ''
        else:
            department_type = self.Department_Type.text()
        if self.Department_LeaderId.text().isspace():
            department_leaderid = ''
        else:
            department_leaderid = self.Department_LeaderId.text()
            
        
        if (department_id == '' or (department_name == '' and  bank_name == '' and  department_type == '' and  department_leaderid == '')):
            QMessageBox.information(self,'错误','部门信息填写不完整！暂无领导可填\'无\'')
            return
        change = 'update Department set '
        index = 0
        
        question = QMessageBox.question(self, '确定', '是否更改部门号为: '+ department_id + '的部门信息', QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if question == QMessageBox.No:
            return 
        
        self.curso.execute('select * from Department where Department_Id = ' + '\'' + department_id + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','部门不存在！')
            return
        
        
        
        if bank_name != '' :
            print(bank_name)
            if index != 0:
                change = change + ', '
            index = index + 1
            change = change + 'Bank_Name = ' + '\'' + bank_name + '\''
            self.curso.execute('select * from Bank where Bank_Name = ' + '\'' + bank_name + '\'')
            query = self.curso.fetchone()
            if query is None:
                QMessageBox.information(self,'错误','银行不存在！')
                return
        if  department_name!= '' :
            if index != 0:
                change = change + ', '
            index = index + 1
            change = change + 'Department_Name = ' + '\'' + department_name + '\''
        if  department_type!= '' :
            if index != 0:
                change = change + ', '
            index = index + 1
            change = change + 'Department_Type = ' + '\'' + department_type + '\''
        if  department_leaderid!= '' :
            if index != 0:
                change = change + ', '
            index = index + 1
            change = change + 'Department_LeaderID = ' + '\'' + department_leaderid + '\''
            if department_leaderid != '无':
                self.curso.execute('select * from Employee where Employee_Id = ' + '\'' + department_leaderid + '\'')
                query = self.curso.fetchone()
                if query is None:
                    QMessageBox.information(self,'错误','员工不存在！')
                    return
            
        
        change = change + 'where Department_Id = ' + '\'' + department_id + '\''
        reply = self.cursor_bank(change,'Department',False)
        if reply == False:
            QMessageBox.information(self,'错误','输入不合法')
            return
        
    def department_query(self):
        if self.Department_Id.text().isspace():
            department_id = ''
        else:
            department_id = self.Department_Id.text()
        if self.Bank_Name.text().isspace():
            bank_name = ''
        else:
            bank_name = self.Bank_Name.text()
        if self.Department_Name.text().isspace():
            department_name = ''
        else:
            department_name = self.Department_Name.text()
        if self.Department_Type.text().isspace():
            department_type = ''
        else:
            department_type = self.Department_Type.text()
        if self.Department_LeaderId.text().isspace():
            department_leaderid = ''
        else:
            department_leaderid = self.Department_LeaderId.text()
            
        
        if (department_id == '' and  department_name == '' and  bank_name == '' and  department_type == '' and  department_leaderid == ''):
            self.cursor_bank('Select * from Department','Department',True)
            return
        change = 'Select * from Department Where '
        index = 0
        
        question = QMessageBox.question(self, '确定', '是否进行查询', QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if question == QMessageBox.No:
            return 
        
        if department_id != '' :
            if index != 0:
                change = change + 'and  '
            index = index + 1
            change = change + 'Department_Id = ' + '\'' + department_id + '\''
        if bank_name != '' :
            if index != 0:
                change = change + 'and  '
            index = index + 1
            change = change + 'Bank_Name = ' + '\'' + bank_name + '\''
        if  department_name!= '' :
            if index != 0:
                change = change + 'and  '
            index = index + 1
            change = change + 'Department_Name = ' + '\'' + department_name + '\''
        if  department_type!= '' :
            if index != 0:
                change = change + 'and  '
            index = index + 1
            change = change + 'Department_Type = ' + '\'' + department_type + '\''
        if  department_leaderid!= '' :
            if index != 0:
                change = change + 'and  '
            index = index + 1
            change = change + 'Department_LeaderID = ' + '\'' + department_leaderid + '\''
        
        
        reply = self.cursor_bank(change,'Department',True)
        if reply == False:
            QMessageBox.information(self,'错误','输入不合法')
            return
        
    def worker_add(self):
        if self.Worker_Id.text().isspace():
            id = ''
        else:
            id = self.Worker_Id.text()
        if self.Worker_DepartmentId.text().isspace():
            department_id = ''
        else:
            department_id = self.Worker_DepartmentId.text()
        if self.Worker_Name.text().isspace():
            name = ''
        else:
            name = self.Worker_Name.text()
        if self.Worker_Phone.text().isspace():
            phone = ''
        else:
            phone = self.Worker_Phone.text()
        if self.Worker_Address.text().isspace():
            address = ''
        else:
            address = self.Worker_Address.text()
        
        enterdate = self.Worker_EnterDate.date()
            
        enterdate = str(enterdate).split('(')
        enterdate = enterdate[-1].split(')')
        enterdate = enterdate[0].split(', ')
        enterdate = enterdate[0] + '-' + enterdate[1] + '-' + enterdate[2]
        
        if (department_id == '' or id == '' or name == '' or address == '' or phone == '' or enterdate == ''):
            QMessageBox.information(self,'错误','员工信息填写不完整！')
            return
        
        
        question = QMessageBox.question(self, '确定', "插入员工信息: \n" +
                                                      "\n员工号: " + id +
                                                      "\n员工所在部门号: " + department_id +
                                                      "\n员工名: " + name +
                                                      "\n员工电话号码: " + phone +
                                                      "\n员工地址: " + address +
                                                      "\n员工入职日期: " + enterdate , QMessageBox.No | QMessageBox.Yes , QMessageBox.Yes)
        
        if question == QMessageBox.No:
            return
        
        self.curso.execute('select * from Employee where Employee_Id = ' + '\'' + id + '\'')
        query = self.curso.fetchone()
        if query is not None:
            QMessageBox.information(self,'错误','员工号已存在！')
            return
        
        self.curso.execute('select * from Department where Department_Id = ' + '\'' + department_id + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','部门不存在！')
            return
        
        
        
        add = 'insert into Employee Values(' + '\''+ id + '\'' + ', ' + '\''+ department_id + '\'' + ', ' + '\'' + name + '\''  + ','  + '\'' + phone + '\'' +',' +  '\''  +address + '\'' +',' +  '\''  +enterdate + '\''   +')'
        reply = self.cursor_bank(add,'Employee',False)
        if reply == False:
            QMessageBox.information(self,'错误','输入不合法')
            return
        None
        
    def worker_del(self):
        if self.Worker_Id.text().isspace():
            id = ''
        else:
            id = self.Worker_Id.text()
            
        if (id == ''):
            QMessageBox.information(self,'错误','员工删除信息不完整')
            return
        
        question = QMessageBox.question(self, '确定', '是否删除员工身份证号为: '+ id + '的员工', QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if question == QMessageBox.No:
            return 
        
        self.curso.execute('select * from Employee where Employee_Id = ' + '\'' + id + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','员工不存在！')
            return
        
        dele = 'delete from Employee WHERE  Employee_Id = ' + '\'' + id + '\''
        reply = self.cursor_bank(dele,'Employee',False)
        if reply == False:
            QMessageBox.information(self,'错误','输入不合法')
            return
        
    def worker_change(self):
        if self.Worker_Id.text().isspace():
            id = ''
        else:
            id = self.Worker_Id.text()
        if self.Worker_DepartmentId.text().isspace():
            department_id = ''
        else:
            department_id = self.Worker_DepartmentId.text()
        if self.Worker_Name.text().isspace():
            name = ''
        else:
            name = self.Worker_Name.text()
        if self.Worker_Phone.text().isspace():
            phone = ''
        else:
            phone = self.Worker_Phone.text()
        if self.Worker_Address.text().isspace():
            address = ''
        else:
            address = self.Worker_Address.text()
        
        enterdate = self.Worker_EnterDate.date()
        
        enterdate = str(enterdate).split('(')
        enterdate = enterdate[-1].split(')')
        enterdate = enterdate[0].split(', ')
        
        enterdate = enterdate[0] + '-' + enterdate[1] + '-' + enterdate[2]
        
        if (id == '' or (department_id == '' and  name == '' and  address == '' and  phone == '' and  enterdate == '')):
            QMessageBox.information(self,'错误','员工信息填写不完整！')
            return
        
        
        change = 'update Employee set '
        index = 0
        
        question = QMessageBox.question(self, '确定', '是否更改身份证号为: '+ id + '的员工信息', QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if question == QMessageBox.No:
            return 
        
        self.curso.execute('select * from Employee where Employee_Id = ' + '\'' + id + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','员工不存在！')
            return
        
        if department_id != '' :
            if index != 0:
                change = change + ', '
            index = index + 1
            change = change + 'Department_Id = ' + '\'' + department_id + '\''
            self.curso.execute('select * from Department where Department_Id = ' + '\'' + department_id + '\'')
            query = self.curso.fetchone()
            if query is None:
                QMessageBox.information(self,'错误','部门不存在！')
                return
        if  name!= '' :
            if index != 0:
                change = change + ', '
            index = index + 1
            change = change + 'Employee_Name = ' + '\'' + name + '\''
        if  phone!= '' :
            if index != 0:
                change = change + ', '
            index = index + 1
            change = change + 'Employee_Phone = ' + '\'' + phone + '\''
        if  address!= '' :
            if index != 0:
                change = change + ', '
            index = index + 1
            change = change + 'Employee_Address = ' + '\'' + address + '\''
        if  enterdate!= '' :
            if index != 0:
                change = change + ', '
            index = index + 1
            change = change + 'Employee_EnterDate = ' + '\'' + enterdate + '\''
            
        
        change = change + 'where Employee_Id = ' + '\'' + id + '\''
        print(change)
        reply = self.cursor_bank(change,'Employee',False)
        if reply == False:
            QMessageBox.information(self,'错误','输入不合法')
            return
        None
    def worker_query(self):
        if self.Worker_Id.text().isspace():
            id = ''
        else:
            id = self.Worker_Id.text()
        if self.Worker_DepartmentId.text().isspace():
            department_id = ''
        else:
            department_id = self.Worker_DepartmentId.text()
        if self.Worker_Name.text().isspace():
            name = ''
        else:
            name = self.Worker_Name.text()
        if self.Worker_Phone.text().isspace():
            phone = ''
        else:
            phone = self.Worker_Phone.text()
        if self.Worker_Address.text().isspace():
            address = ''
        else:
            address = self.Worker_Address.text()
        
        enterdate = self.Worker_EnterDate.date()
        enterdate = str(enterdate).split('(')
        enterdate = enterdate[-1].split(')')
        enterdate = enterdate[0].split(', ')
        enterdate = enterdate[0] + '-' + enterdate[1] + '-' + enterdate[2]
        
        if (id == '' and  department_id == '' and  name == '' and  address == '' and  phone == '' and  enterdate == ''):
            self.cursor_bank('Select * from Employee','Employee',True)
            return
        
        change = 'Select * from Employee Where '
        index = 0
        
        question = QMessageBox.question(self, '确定', '是否进行查询 ', QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if question == QMessageBox.No:
            return 
        
        
        if id != '' :
            if index != 0:
                change = change + 'and  '
            index = index + 1
            change = change + 'Employee_Id = ' + '\'' + id + '\''
        if  department_id!= '' :
            if index != 0:
                change = change + 'and  '
            index = index + 1
            change = change + 'Department_Id = ' + '\'' + department_id + '\''
        if  name!= '' :
            if index != 0:
                change = change + 'and  '
            index = index + 1
            change = change + 'Employee_Name = ' + '\'' + name + '\''
        if  phone!= '' :
            if index != 0:
                change = change + 'and  '
            index = index + 1
            change = change + 'Employee_Phone = ' + '\'' + phone + '\''
        if address!= '':
            if index != 0:
                change = change + 'and '
            index = index + 1
            change = change + 'Employee_Address = ' + '\'' + address + '\''
        if enterdate!= '':
            if index != 0:
                change = change + 'and '
            index = index + 1
            change = change + 'Employee_EnterDate = ' + '\'' + enterdate + '\''
            
        
        
        reply = self.cursor_bank(change,'Employee',True)
        if reply == False:
            QMessageBox.information(self,'错误','输入不合法')
            return
        None
        
    def bank_add(self):
        if self.Bank_Name.text().isspace():
            Name = ''
        else:
            Name = self.Bank_Name.text()
        if self.Bank_city.text().isspace():
            City = ''
        else:
            City = self.Bank_city.text()
        if self.Bank_Possion.text().isspace():
            Possion = ''
        else:
            Possion = self.Bank_Possion.text()
        
        
        if (Name == '' or City == '' or Possion == ''):
            QMessageBox.information(self,'错误','银行信息填写不完整！')
            return
        
        
        question = QMessageBox.question(self, '确定', "插入银行信息: \n" +
                                                      "\n支行名字: " + Name +
                                                      "\n支行所在城市: " + City +
                                                      "\n支行资产: " + Possion , QMessageBox.No | QMessageBox.Yes , QMessageBox.Yes)
        
        if question == QMessageBox.No:
            return
        
        self.curso.execute('select * from Bank where Bank_Name = ' + '\'' + Name + '\'')
        query = self.curso.fetchone()
        if query is not None:
            QMessageBox.information(self,'错误','支行已存在！')
            return
        
        add = 'insert into Bank Values(' + '\''+ Name + '\'' + ', ' + '\''+ City + '\'' + ', ' + '\'' + Possion + '\''    + ')'
        reply = self.cursor_bank(add,'Bank',False)
        if reply == False:
            QMessageBox.information(self,'错误','输入不合法')
            return
        
    def bank_del(self):
        if self.Bank_Name.text().isspace():
            Name = ''
        else:
            Name = self.Bank_Name.text()
            
        if (Name == ''):
            QMessageBox.information(self,'错误','银行删除信息不完整')
            return
        
        question = QMessageBox.question(self, '确定', '是否删除银行名字为: '+ Name + '的客户', QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if question == QMessageBox.No:
            return 
        
        self.curso.execute('select * from Bank where Bank_Name = ' + '\'' + Name + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','银行不存在！')
            return
        
        dele = 'delete from Bank WHERE  Bank_Name= ' + '\'' + Name + '\''
        reply = self.cursor_bank(dele,'Bank',False)
        if reply == False:
            QMessageBox.information(self,'错误','输入不合法')
            return
        
    def bank_change(self):
        if self.Bank_Name.text().isspace():
            Name = ''
        else:
            Name = self.Bank_Name.text()
        if self.Bank_city.text().isspace():
            City = ''
        else:
            City = self.Bank_city.text()
        if self.Bank_Possion.text().isspace():
            Possion = ''
        else:
            Possion = self.Bank_Possion.text()
            
        
        if (Name == '' or (City == '' and  Possion == '' )):
            QMessageBox.information(self,'错误','银行信息填写不完整！')
            return
        change = 'update Bank set '
        index = 0
        
        question = QMessageBox.question(self, '确定', '是否更改名字为: '+ Name + '的支行信息', QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if question == QMessageBox.No:
            return 
        
        self.curso.execute('select * from Bank where Bank_Name = ' + '\'' + Name + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','支行不存在！')
            return
        
        if City != '' :
            if index != 0:
                change = change + ', '
            index = index + 1
            change = change + 'Bank_Name = ' + '\'' + City + '\''
        if  Possion!= '' :
            if index != 0:
                change = change + ', '
            index = index + 1
            change = change + 'Bank_possession = ' + '\'' + Possion + '\''
        change = change + 'where Bank_Name = ' + '\'' + Name + '\''
        reply = self.cursor_bank(change,'Bank',False)
        if reply == False:
            QMessageBox.information(self,'错误','输入不合法')
            return
        
        
    def bank_query(self):
        if self.Bank_Name.text().isspace():
            Name = ''
        else:
            Name = self.Bank_Name.text()
        if self.Bank_city.text().isspace():
            City = ''
        else:
            City = self.Bank_city.text()
        if self.Bank_Possion.text().isspace():
            Possion = ''
        else:
            Possion = self.Bank_Possion.text()
            
        
        if (Name == '' and  City == '' and  Possion == '' ):
            change = 'select * from Bank '
            self.cursor_bank(change,'Bank',True)
            return
        change = 'select * from Bank where '
        index = 0
        
        question = QMessageBox.question(self, '确定', '是否进行查询', QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if question == QMessageBox.No:
            return 
        
        if Name != '' :
            if index != 0:
                change = change + 'and  '
            index = index + 1
            change = change + 'Bank_Name = ' + '\'' + Name + '\''
        if City != '' :
            if index != 0:
                change = change + 'and  '
            index = index + 1
            change = change + 'Bank_City = ' + '\'' + City + '\''
        if  Possion!= '' :
            if index != 0:
                change = change + 'and  '
            index = index + 1
            change = change + 'Bank_possession = ' + '\'' + Possion + '\''
        
        
        reply = self.cursor_bank(change,'Bank',True)
        if reply == False:
            QMessageBox.information(self,'错误','输入不合法')
            return
    
    def customer_add(self):
        
        if self.Customer_Id.text().isspace():
            Id = ''
        else:
            Id = self.Customer_Id.text()
        if self.Customer_Name.text().isspace():
            Name = ''
        else:
            Name = self.Customer_Name.text()
            if '\'' in Name:
                k = ''
                for i in Name:
                    if i != '\'':
                        k = k + i
                    else:
                        k = k +'\'\''
                Name = k
        if self.Customer_Phone.text().isspace():
            Phone = ''
        else:
            Phone = self.Customer_Phone.text()
        if self.Customer_Address.text().isspace():
            Address = ''
        else:
            Address = self.Customer_Address.text()
            
        if self.Co_Name.text().isspace():
            CoName = ''
        else:
            CoName = self.Co_Name.text()
            if '\'' in CoName:
                k = ''
                for i in CoName:
                    if i != '\'':
                        k = k + i
                    else:
                        k = k +'\'\''
                CoName = k
        if self.Co_Phone.text().isspace():
            CoPhone = ''
        else:
            CoPhone = self.Co_Phone.text()
        if self.Co_Email.text().isspace():
            CoEmail = ''
        else:
            CoEmail = self.Co_Email.text()
        if self.Relationship.text().isspace():
            Relationship = ''
        else:
            Relationship = self.Relationship.text()
            
            
        
        if (Id == '' or Name == '' or Phone == '' or Address == '' or
             CoName == '' or CoPhone == '' or CoEmail == '' or Relationship == ''):
            QMessageBox.information(self,'错误','用户信息填写不完整！')
            return
        
        
        
            
        question = QMessageBox.question(self, '确定', "插入客户信息: \n客户身份证号码: " + Id +
                                                      "\n客户姓名: " + Name +
                                                      "\n客户电话号码: " + Phone +
                                                      "\n客户地址: " + Address +
                                                      "\n联系人姓名: " + CoName+ 
                                                      "\n联系人电话号码: " + CoPhone+
                                                      "\n联系人Email: " + CoEmail + 
                                                      "\n联系人与客户关系: " + Relationship, QMessageBox.No | QMessageBox.Yes , QMessageBox.Yes)
        if question == QMessageBox.No:
            return
        
        self.curso.execute('select * from Customer where Customer_Id = ' + '\'' + Id + '\'')
        query = self.curso.fetchone()
        if query is not None:
            QMessageBox.information(self,'错误','用户已存在！')
            return
        
        add = 'insert into Customer Values(' + '\''+ Id + '\'' +  ', ' + '\''+ Name + '\'' + ', ' + '\''+ Phone + '\'' + ', ' + '\'' + Address + '\''  + ', ' + '\'' + CoName + '\'' +  ', ' + '\'' + CoPhone + '\'' + ', ' + '\''+ CoEmail + '\'' + ', ' + '\'' + Relationship + '\''  + ')'
        reply = self.cursor_bank(add,'Customer',False)
        if reply == False:
            QMessageBox.information(self,'错误','输入不合法')
            return
        
    def customer_del(self):
        if self.Customer_Id.text().isspace():
            Id = ''
        else:
            Id = self.Customer_Id.text()
            
        if (Id == ''):
            QMessageBox.information(self,'Error','Information Error')
            return
        
        question = QMessageBox.question(self, '确定', '是否删除身份证号码为: '+ Id + '的客户', QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if question == QMessageBox.No:
            return 
        
        self.curso.execute('select * from Customer where Customer_Id = ' + '\'' + Id + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','用户不存在！')
            return
        
        dele = 'delete from Customer WHERE Customer_Id = ' + '\'' + Id + '\''
        success = self.cursor_bank(dele,'Customer',False)
        if success == False:
            QMessageBox.information(self,'错误','用户存在关联账户或贷款记录！')
            return
        
    def customer_change(self):
        if self.Customer_Id.text().isspace():
            Id = ''
        else:
            Id = self.Customer_Id.text()
        if self.Customer_Name.text().isspace():
            Name = ''
        else:
            Name = self.Customer_Name.text()
            if '\'' in Name:
                k = ''
                for i in Name:
                    if i != '\'':
                        k = k + i
                    else:
                        k = k +'\'\''
                Name = k
        if self.Customer_Phone.text().isspace():
            Phone = ''
        else:
            Phone = self.Customer_Phone.text()
        if self.Customer_Address.text().isspace():
            Address = ''
        else:
            Address = self.Customer_Address.text()
            
        if self.Co_Name.text().isspace():
            CoName = ''
        else:
            CoName = self.Co_Name.text()
            if '\'' in CoName:
                k = ''
                for i in CoName:
                    if i != '\'':
                        k = k + i
                    else:
                        k = k +'\'\''
                CoName = k
        if self.Co_Phone.text().isspace():
            CoPhone = ''
        else:
            CoPhone = self.Co_Phone.text()
        if self.Co_Email.text().isspace():
            CoEmail = ''
        else:
            CoEmail = self.Co_Email.text()
        if self.Relationship.text().isspace():
            Relationship = ''
        else:
            Relationship = self.Relationship.text()
            
        
        if (Id == '' or (Phone == '' and  Address == '' and  Name == '' and  CoPhone == '' and  CoEmail == '' and  CoName == '' and  Relationship == '')):
            QMessageBox.information(self,'错误','用户信息填写不完整！')
            return
        change = 'update Customer set '
        index = 0
        
        question = QMessageBox.question(self, '确定', '是否更改身份证号码为: '+ Id + '的客户信息', QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if question == QMessageBox.No:
            return 
        
        self.curso.execute('select * from Customer where Customer_Id = ' + '\'' + Id + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','用户不存在！')
            return
        
        if Name != '' :
            if index != 0:
                change = change + ', '
            index = index + 1
            change = change + 'Customer_Name = ' + '\'' + Name + '\''
        if  Phone!= '' :
            if index != 0:
                change = change + ', '
            index = index + 1
            change = change + 'Customer_Phone = ' + '\'' + Phone + '\''
        if  Address!= '' :
            if index != 0:
                change = change + ', '
            index = index + 1
            change = change + 'Customer_Address = ' + '\'' + Address + '\''
        if  CoName!= '' :
            if index != 0:
                change = change + ', '
            index = index + 1
            change = change + 'Contact_Name = ' + '\'' + CoName + '\''
        if  CoPhone!= '' :
            if index != 0:
                change = change + ', '
            index = index + 1
            change = change + 'Contact_Phone = ' + '\'' + CoPhone + '\''
        if  CoEmail!= '' :
            if index != 0:
                change = change + ', '
            index = index + 1
            change = change + 'Contact_Email = ' + '\'' + CoEmail + '\''
        if  Relationship!= '' :
            if index != 0:
                change = change + ', '
            index = index + 1
            change = change + 'Relationship = ' + '\'' + Relationship + '\''
        change = change + 'where Customer_Id = ' + '\'' + Id + '\''
        reply = self.cursor_bank(change,'Customer',False)
        if reply == False:
            QMessageBox.information(self,'错误','输入不合法')
            return
    
    
    
    
    
    def customer_query(self):
        if self.Customer_Id.text().isspace():
            Id = ''
        else:
            Id = self.Customer_Id.text()
        if self.Customer_Name.text().isspace():
            Name = ''
        else:
            Name = self.Customer_Name.text()
            if '\'' in Name:
                k = ''
                for i in Name:
                    if i != '\'':
                        k = k + i
                    else:
                        k = k +'\'\''
                Name = k
        if self.Customer_Phone.text().isspace():
            Phone = ''
        else:
            Phone = self.Customer_Phone.text()
        if self.Customer_Address.text().isspace():
            Address = ''
        else:
            Address = self.Customer_Address.text()
            
        if self.Co_Name.text().isspace():
            CoName = ''
        else:
            CoName = self.Co_Name.text()
            if '\'' in CoName:
                k = ''
                for i in CoName:
                    if i != '\'':
                        k = k + i
                    else:
                        k = k +'\'\''
                CoName = k
        if self.Co_Phone.text().isspace():
            CoPhone = ''
        else:
            CoPhone = self.Co_Phone.text()
        if self.Co_Email.text().isspace():
            CoEmail = ''
        else:
            CoEmail = self.Co_Email.text()
        if self.Relationship.text().isspace():
            Relationship = ''
        else:
            Relationship = self.Relationship.text()
            
        
        if (Id == '' and  Phone == '' and  Address == '' and  Name == '' and  CoPhone == '' and  CoEmail == '' and  CoName == '' and  Relationship == ''):
            change = 'select * from Customer '
            self.cursor_bank(change,'Customer',True)
            return
        change = 'select * from Customer where '
        index = 0
        
        question = QMessageBox.question(self, '确定', '是否进行查询', QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if question == QMessageBox.No:
            return 
        
        if Id != '' :
            if index != 0:
                change = change + 'and  '
            index = index + 1
            change = change + 'Customer_Id = ' + '\'' + Id + '\''
        if Name != '' :
            if index != 0:
                change = change + 'and  '
            index = index + 1
            change = change + 'Customer_Name = ' + '\'' + Name + '\''
        if  Phone!= '' :
            if index != 0:
                change = change + 'and  '
            index = index + 1
            change = change + 'Customer_Phone = ' + '\'' + Phone + '\''
        if  Address!= '' :
            if index != 0:
                change = change + 'and  '
            index = index + 1
            change = change + 'Customer_Address = ' + '\'' + Address + '\''
        if  CoName!= '' :
            if index != 0:
                change = change + 'and  '
            index = index + 1
            change = change + 'Contact_Name = ' + '\'' + CoName + '\''
        if  CoPhone!= '' :
            if index != 0:
                change = change + 'and  '
            index = index + 1
            change = change + 'Contact_Phone = ' + '\'' + CoPhone + '\''
        if  CoEmail!= '' :
            if index != 0:
                change = change + 'and  '
            index = index + 1
            change = change + 'Contact_Email = ' + '\'' + CoEmail + '\''
        if  Relationship!= '' :
            if index != 0:
                change = change + 'and  '
            index = index + 1
            change = change + 'Relationship = ' + '\'' + Relationship + '\''
        
        reply = self.cursor_bank(change,'Customer',True)
        if reply == False:
            QMessageBox.information(self,'错误','输入不合法')
            return
        print('query')
        
    def customer_worker_add(self):
        if self.Customer_ReId.text().isspace():
            Id = ''
        else:
            Id = self.Customer_ReId.text()
        if self.Customer_InchargeWorker.text().isspace():
            Worker = ''
        else:
            Worker = self.Customer_InchargeWorker.text()
        if self.Customer_WorkChargeType.text().isspace():
            Type = ''
        else:
            Type = self.Customer_WorkChargeType.text()
        
            
            
        
        if (Id == '' or Worker == '' or Type == '') :
            QMessageBox.information(self,'错误','用户信息填写不完整！')
            return
        
        
        
            
        question = QMessageBox.question(self, '确定', "插入客户员工服务信息: \n客户身份证号码: " + Id +
                                                      "\n员工身份证号: " + Worker +
                                                      "\n客户与员工服务关系: " + Type , QMessageBox.No | QMessageBox.Yes , QMessageBox.Yes)
        if question == QMessageBox.No:
            return
        
        self.curso.execute('select * from Customer where Customer_Id = ' + '\'' + Id + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','用户不存在！')
            return
        
        self.curso.execute('select * from Employee where Employee_Id = ' + '\'' + Worker + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','员工不存在！')
            return
        
        self.curso.execute('select Department_Id from Employee where Employee_Id = ' + '\'' + Worker + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','部门号不存在！')
            return
        department = query[0]
        
        self.curso.execute('select Department_Name from Department where Department_Id = ' + '\'' + department + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','部门类型不存在！')
            return
        department = query[0]
        if Type == '账户负责人':
            if department != '账户部门':
                QMessageBox.information(self,'错误','请选择正确的部门员工！')
                return
        if Type == '贷款负责人':
            if department != '贷款部门':
                QMessageBox.information(self,'错误','请选择正确的部门员工！')
                return
        
        self.curso.execute('select * from Responsible where Employee_Id = ' + '\'' + Worker + '\'' +'and  Customer_Id = ' + '\'' + Id + '\'')
        query = self.curso.fetchone()
        if query is not None:
            QMessageBox.information(self,'错误','该用户与员工的服务关系已存在！')
            return
        
        add = 'insert into Responsible Values(' + '\''+ Id + '\'' +  ', ' + '\''+ Worker + '\'' + ', ' + '\''+ Type + '\'' +')'
        reply = self.cursor_bank(add,"Customer_worker",False)
        if reply == False:
            QMessageBox.information(self,'错误','输入不合法')
            return
        
    def customer_worker_del(self):
        if self.Customer_ReId.text().isspace():
            Id = ''
        else:
            Id = self.Customer_ReId.text()
        if self.Customer_InchargeWorker.text().isspace():
            Worker = ''
        else:
            Worker = self.Customer_InchargeWorker.text()
        if self.Customer_WorkChargeType.text().isspace():
            Type = ''
        else:
            Type = self.Customer_WorkChargeType.text()
            
        if (Id == '' and  Worker == ''):
            QMessageBox.information(self,'Error','Information Error')
            return
        
        question = QMessageBox.question(self, '确定', '是否删除信息', QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if question == QMessageBox.No:
            return 
        
        
        
        index = 0
        dele = 'delete from Responsible WHERE '
        
        if Id != '':
            if index != 0:
                dele = dele + 'and  '
            index = index + 1
            dele = dele + 'Customer_Id = ' + '\'' + Id + '\''
            self.curso.execute('select * from Responsible where Customer_Id = ' + '\'' + Id + '\'')
            query = self.curso.fetchone()
            if query is None:
                QMessageBox.information(self,'错误','该用户不存在！')
                return
        if Worker != '':
            if index != 0:
                dele = dele + 'and  '
            index = index + 1
            dele = dele + 'Employee_Id = ' + '\'' + Worker + '\''
            self.curso.execute('select * from Responsible where Employee_Id = ' + '\'' + Worker + '\'')
            query = self.curso.fetchone()
            if query is None:
                QMessageBox.information(self,'错误','该员工不存在！')
                return
        
        reply = self.cursor_bank(dele,'Customer_worker',False)
        if reply == False:
            QMessageBox.information(self,'错误','输入不合法')
            return
        
    def customer_worker_change(self):
        if self.Customer_ReId.text().isspace():
            Id = ''
        else:
            Id = self.Customer_ReId.text()
        if self.Customer_InchargeWorker.text().isspace():
            Worker = ''
        else:
            Worker = self.Customer_InchargeWorker.text()
        if self.Customer_WorkChargeType.text().isspace():
            Type = ''
        else:
            Type = self.Customer_WorkChargeType.text()
        
        
            
        if ((Id == '' or Worker == '') or Type == ''):
            QMessageBox.information(self,'错误','更改信息填写不完整')
            return
        
        
        
        question = QMessageBox.question(self, '确定', '是否更改信息', QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if question == QMessageBox.No:
            return 
        
        
            
        self.curso.execute('select * from Responsible where Customer_Id = ' + '\'' + Id + '\''+  ' and  Employee_Id = ' + '\'' + Worker + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','该客户与该员工不存在关系！')
            return
            
        self.curso.execute('select Department_Id from Employee where Employee_Id = ' + '\'' + Worker + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','部门号不存在！')
            return
        department = query[0]
        
        self.curso.execute('select Department_Name from Department where Department_Id = ' + '\'' + department + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','部门类型不存在！')
            return
        department = query[0]
        if Type == '账户负责人':
            if department != '账户部门':
                QMessageBox.information(self,'错误','请选择正确的部门员工！')
                return
        if Type == '贷款负责人':
            print(department)
            if department != '贷款部门':
                QMessageBox.information(self,'错误','请选择正确的部门员工！')
                return
        change = 'update Responsible set Responsible_Type = ' + '\'' + Type +'\'' + 'where Customer_Id = ' + '\'' + Id + '\''+  ' and  Employee_Id = ' + '\'' + Worker + '\''
        
        
        
        reply = self.cursor_bank(change,'Customer_worker',False)
        if reply == False:
            QMessageBox.information(self,'错误','输入不合法')
            return
    
    def customer_worker_query(self):
        if self.Customer_ReId.text().isspace():
            Id = ''
        else:
            Id = self.Customer_ReId.text()
        if self.Customer_InchargeWorker.text().isspace():
            Worker = ''
        else:
            Worker = self.Customer_InchargeWorker.text()
        if self.Customer_WorkChargeType.text().isspace():
            Type = ''
        else:
            Type = self.Customer_WorkChargeType.text()
        
        
            
        if (Id == '' and  Worker == '' and  Type == ''):
            query = 'select * from Responsible'
            self.cursor_bank(query,'Customer_worker',True)
            return
        
         
        question = QMessageBox.question(self, '确定', '是否进行查询信息', QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if question == QMessageBox.No:
            return 
        index = 0
        query = 'select * from Responsible WHERE '
        
        if Id != '':
            if index != 0:
                query = query + 'and  '
            index = index + 1
            query = query + 'Customer_Id = ' + '\'' + Id + '\''
        if Worker != '':
            if index != 0:
                query = query + 'and  '
            index = index + 1
            query = query + 'Employee_Id = ' + '\'' + Worker + '\''
        if Type != '':
            if index != 0:
                query = query + 'and  '
            index = index + 1
            query = query + 'Responsible_Type = ' + '\'' + Type + '\''
        reply = self.cursor_bank(query,'Customer_worker',True)
        if reply == False:
            QMessageBox.information(self,'错误','输入不合法')
            return
        
    def account_open_check(self):
        if self.Account_Id_Check.text().isspace():
            Account_Id = ''
        else:
            Account_Id = self.Account_Id_Check.text()
        if self.Account_BankName_Check.text().isspace():
            BankName = ''
        else:
            BankName = self.Account_BankName_Check.text()
        if self.Account_Balance_Check.text().isspace():
            Balance = ''
        else:
            Balance = self.Account_Balance_Check.text()
        opendate = self.Account_OpenDate_Check.date()
        opendate = str(opendate).split('(')
        opendate = opendate[-1].split(')')
        opendate = opendate[0].split(', ')
        opendate = opendate[0] + '-' + opendate[1] + '-' + opendate[2]
        
        if self.Account_InterestRate_Check.text().isspace():
            Overdraft = ''
        else:
            Overdraft = self.Account_InterestRate_Check.text()
        if self.Account_CustomerId_Check.text().isspace():
            CustomerId = ''
        else:
            CustomerId = self.Account_CustomerId_Check.text()
        visitdate = self.Account_RecentVisitDate_Check.date()
        visitdate = str(visitdate).split('(')
        visitdate = visitdate[-1].split(')')
        visitdate = visitdate[0].split(', ')
        visitdate = visitdate[0] + '-' + visitdate[1] + '-' + visitdate[2]
        
        self.curso.execute('select * from setupAccount WHERE Customer_Id = ' + '\'' + CustomerId + '\'' + 'and  Bank_Name = ' + '\'' + BankName + '\'' + 'and  Account_type =  \'支票账户\'' )
        query = self.curso.fetchone()
        if query is not None:
            QMessageBox.information(self,'错误','该客户已到该银行创建过此类账户！')
            return
        
        self.curso.execute('select * from Customer where Customer_Id = ' + '\'' + CustomerId + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','用户不存在！')
            return
        
        self.curso.execute('select * from Bank where Bank_Name = ' + '\'' + BankName + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','支行不存在！')
            return
        
        
        
        self.curso.execute('select * from Account where Account_Id = ' + '\'' + Account_Id + '\'')
        query = self.curso.fetchone()
        
        if query is None:
            if (Account_Id == '' or BankName == '' or opendate == '' or Balance == '' or Overdraft == '' or CustomerId == '' ) :
                QMessageBox.information(self,'错误','账户信息填写不完整！')
                return
            question = QMessageBox.question(self, '确定', '是否插入账户信息' , QMessageBox.No | QMessageBox.Yes , QMessageBox.Yes)
            if question == QMessageBox.No:
                return
            add = 'insert into Account  Values(' + '\''+ Account_Id + '\'' +  ', ' + '\''+ BankName + '\'' + ', ' + '\''+ Balance + '\'' + ', ' + '\''+ opendate + '\'' +')'
            reply = self.cursor_bank(add,"Account",False)
            if reply == False:
                QMessageBox.information(self,'错误','输入不合法')
                return
            
            add = 'insert  into Checking_Account  Values(' + '\''+ Account_Id + '\'' +  ', ' + '\''+ BankName + '\'' + ', ' + '\''+ Balance + '\'' + ', ' + '\''+ opendate + '\'' + ','+ '\'' + Overdraft +'\'' +')'
            reply = self.cursor_bank(add,"Checking_Account",False)
            if reply == False:
                QMessageBox.information(self,'错误','输入不合法')
                return
        else: 
            if (Account_Id == '' or CustomerId == '' ) :
                QMessageBox.information(self,'错误','账户信息填写不完整！')
                return
            self.curso.execute('select Bank_Name from Account WHERE Account_Id = ' + '\'' + Account_Id + '\'')
            
            bank = self.curso.fetchone()
            if bank == None:
                QMessageBox.information(self,'错误','银行不存在！')
                return  
            bank = bank[0]
            self.curso.execute('select Customer_Id from have_visit WHERE Account_Id = ' + '\'' + Account_Id + '\'')
            customer = self.curso.fetchone()
            if customer == None:
                QMessageBox.information(self,'错误','访问不存在！')
                return
            customer = customer[0]
            self.curso.execute('select Account_type from setupAccount WHERE Bank_Name = ' + '\'' + bank + '\'' + 'and  Customer_Id = ' + '\'' + customer + '\'')
            type = self.curso.fetchone()
            if type == None:
                QMessageBox.information(self,'错误','信息错误')
            type = type[0]
            if type != '支票账户':
                QMessageBox.information(self,'错误','该账户号为储蓄账户类型！')
                return    
            question = QMessageBox.question(self, '确定', '是否插入账户信息' , QMessageBox.No | QMessageBox.Yes , QMessageBox.Yes)
            if question == QMessageBox.No:
                return
        
        
        add = 'insert into have_visit   Values(' + '\''+ CustomerId + '\'' +  ', ' + '\''+ Account_Id + '\''   + ', ' + '\''+ visitdate + '\'' +')'
        reply = self.cursor_bank(add,"have_visit",False)
        if reply == False:
            QMessageBox.information(self,'错误','该客户已创建过该账户号')
            return
        
        add = 'insert into setupAccount   Values(' + '\''+ CustomerId + '\'' +  ', ' + '\''+ BankName + '\''   + ', ' + '\''+ '支票账户' + '\'' +')'
        reply = self.cursor_bank(add,"setupAccount",False)
        if reply == False:
            QMessageBox.information(self,'错误','输入不合法')
            return
       
        
        self.display('check_account',False)
        
    def account_del_check(self):
        if self.Account_Id_Check.text().isspace():
            Id = ''
        else:
            Id = self.Account_Id_Check.text()
        if self.Account_CustomerId_Check.text().isspace():
            CustomerId = ''
        else:
            CustomerId = self.Account_CustomerId_Check.text()
            
        if ((Id == '' and  CustomerId == '' )or Id == ''):
            QMessageBox.information(self,'错误','未填写删除的账户号或账户号与客户号')
            return
        
        question = QMessageBox.question(self, '确定', '是否删除信息', QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if question == QMessageBox.No:
            return 
        
        if CustomerId == '':
            select = 'select Bank_Name from Checking_Account WHERE Account_Id = ' + '\'' + Id + '\''
            self.curso.execute(select)
            self.conn.commit()  # 事务的提交
            query = self.curso.fetchone()
            if query is not None:
                bank = query[0]
                select = 'select Customer_Id from have_visit WHERE Account_Id = ' + '\'' + Id + '\'' 
                self.curso.execute(select)
                self.conn.commit()  # 事务的提交
                for query in self.curso.fetchall():
                    if query is not None:
                        customer = query[0]
                        select = 'select * from setupAccount WHERE Customer_Id = ' + '\'' + customer + '\'' + 'and  Bank_Name = ' + '\'' + bank + '\'' + 'and  Account_type =  \'支票账户\'' 
                        self.curso.execute(select)
                        query = self.curso.fetchone()
                        if query is None:
                            QMessageBox.information(self,'错误','要删除的setupAccount信息不存在！')
                            return
                        dele = 'delete from setupAccount WHERE Customer_Id = ' + '\'' + customer + '\'' + 'and  Bank_Name = ' + '\'' + bank + '\'' + 'and  Account_type =  \'支票账户\'' 
                        reply = self.cursor_bank(dele,'setupAccount',False)
                        if reply == False:
                            QMessageBox.information(self,'错误','输入不合法')
                            return
            
            select = 'select * from Checking_Account WHERE Account_Id = ' + '\'' + Id + '\''
            self.curso.execute(select)
            query = self.curso.fetchone()
            if query is None:
                QMessageBox.information(self,'错误','要删除的Checking_Account信息不存在！')
                return
            dele = 'delete from Checking_Account WHERE Account_Id = ' + '\'' + Id + '\''
            reply = self.cursor_bank(dele,'Checking_Account',False)
            if reply == False:
                QMessageBox.information(self,'错误','输入不合法')
                return
            
            select = 'select * from have_visit WHERE Account_Id = ' + '\'' + Id + '\''
            self.curso.execute(select)
            query = self.curso.fetchone()
            if query is None:
                QMessageBox.information(self,'错误','要删除的have_visit信息不存在！')
                return
            dele = 'delete from have_visit WHERE Account_Id = ' + '\'' + Id + '\''
            reply = self.cursor_bank(dele,'have_visit',False)
            if reply == False:
                QMessageBox.information(self,'错误','输入不合法')
                return
            
            select = 'select * from Account WHERE Account_Id = ' + '\'' + Id + '\''
            self.curso.execute(select)
            query = self.curso.fetchone()
            if query is None:
                QMessageBox.information(self,'错误','要删除的Account信息不存在！')
                return
            dele = 'delete from Account WHERE Account_Id = ' + '\'' + Id + '\''
            reply = self.cursor_bank(dele,'Account',False)
            if reply == False:
                QMessageBox.information(self,'错误','输入不合法')
                return
        else:
            select = 'select Bank_Name from Checking_Account WHERE Account_Id = ' + '\'' + Id + '\''
            self.curso.execute(select)
            self.conn.commit()  # 事务的提交
            query = self.curso.fetchone()
            if query is None:
                QMessageBox.information(self,'错误','要删除的Bank_Name信息不存在！')
                return
            if query is not None:
                bank = query[0]
                select = 'select Customer_Id from have_visit WHERE Account_Id = ' + '\'' + Id + '\'' 
                self.curso.execute(select)
                row = self.curso.rowcount
                if row > 1:
                    select = 'select * from setupAccount WHERE Customer_Id = ' + '\'' +  CustomerId + '\'' + 'and  Bank_Name = ' + '\'' + bank + '\'' + 'and  Account_type =  \'支票账户\'' 
                    self.curso.execute(select)
                    query = self.curso.fetchone()
                    if query is None:
                        QMessageBox.information(self,'错误','要删除的setupAccount信息不存在！')
                        return
                    dele = 'delete from setupAccount WHERE Customer_Id = ' + '\'' + CustomerId + '\'' + 'and  Bank_Name = ' + '\'' + bank + '\'' + 'and  Account_type =  \'支票账户\'' 
                    reply = self.cursor_bank(dele,'setupAccount',False)
                    if reply == False:
                        QMessageBox.information(self,'错误','输入不合法')
                        return
                    
                    select = 'select * from have_visit WHERE Customer_Id = ' + '\'' + CustomerId + '\'' + 'and  Account_Id = ' + '\'' + Id + '\''  
                    self.curso.execute(select)
                    query = self.curso.fetchone()
                    if query is None:
                        QMessageBox.information(self,'错误','要删除的 have_visit 信息不存在！')
                        return
                    dele = 'delete from have_visit WHERE Customer_Id = ' + '\'' + CustomerId + '\'' + 'and  Account_Id = ' + '\'' + Id + '\''  
                    reply = self.cursor_bank(dele,'have_visit',False)
                    if reply == False:
                        QMessageBox.information(self,'错误','输入不合法')
                        return
                elif row == 1:
                    print(row)
                    select = 'select * from setupAccount WHERE Customer_Id = ' + '\'' +  CustomerId + '\'' + 'and  Bank_Name = ' + '\'' + bank + '\'' + 'and  Account_type =  \'支票账户\'' 
                    self.curso.execute(select)
                    query = self.curso.fetchone()
                    if query is None:
                        QMessageBox.information(self,'错误','要删除的 setupAccount 信息不存在！')
                        return
                    dele = 'delete from setupAccount WHERE Customer_Id = ' + '\'' + CustomerId + '\'' + 'and  Bank_Name = ' + '\'' + bank + '\'' + 'and  Account_type =  \'支票账户\'' 
                    reply = self.cursor_bank(dele,'setupAccount',False)
                    if reply == False:
                        QMessageBox.information(self,'错误','输入不合法')
                        return
            
                    select = 'select * from Checking_Account WHERE Account_Id = ' + '\'' + Id + '\''
                    self.curso.execute(select)
                    query = self.curso.fetchone()
                    if query is None:
                        QMessageBox.information(self,'错误','要删除的 Checking_Account 信息不存在！')
                        return
                    dele = 'delete from Checking_Account WHERE Account_Id = ' + '\'' + Id + '\''
                    reply = self.cursor_bank(dele,'Checking_Account',False)
                    if reply == False:
                        QMessageBox.information(self,'错误','输入不合法')
                        return
            
                    select = 'select * from have_visit WHERE Account_Id = ' + '\'' + Id + '\'' + 'and  Customer_Id = ' + '\'' + CustomerId + '\''
                    self.curso.execute(select)
                    query = self.curso.fetchone()
                    if query is None:
                        QMessageBox.information(self,'错误','要删除的have_visit信息不存在！')
                        return
                    dele = 'delete from have_visit WHERE Account_Id = ' + '\'' + Id + '\''  + 'and  Customer_Id = ' + '\'' + CustomerId + '\''
                    reply = self.cursor_bank(dele,'have_visit',False)
                    if reply == False:
                        QMessageBox.information(self,'错误','输入不合法')
                        return
                        
                    select = 'select * from Account WHERE Account_Id = ' + '\'' + Id + '\''
                    self.curso.execute(select)
                    query = self.curso.fetchone()
                    if query is None:
                        QMessageBox.information(self,'错误','要删除的Account信息不存在！')
                        return
                    dele = 'delete from Account WHERE Account_Id = ' + '\'' + Id + '\''
                    reply = self.cursor_bank(dele,'Account',False)
                    if reply == False:
                        QMessageBox.information(self,'错误','输入不合法')
                        return
                else:
                    QMessageBox.information(self,'错误','要删除的Customer_Id信息不存在！')
                    return
        self.display('check_account',False)
        print('del check')
        
    def account_change_check(self):
        if self.Account_Id_Check.text().isspace():
            Account_Id = ''
        else:
            Account_Id = self.Account_Id_Check.text()
        if self.Account_BankName_Check.text().isspace():
            BankName = ''
        else:
            BankName = self.Account_BankName_Check.text()
        if self.Account_Balance_Check.text().isspace():
            Balance = ''
        else:
            Balance = self.Account_Balance_Check.text()
        opendate = self.Account_OpenDate_Check.date()
        opendate = str(opendate).split('(')
        opendate = opendate[-1].split(')')
        opendate = opendate[0].split(', ')
        opendate = opendate[0] + '-' + opendate[1] + '-' + opendate[2]
        
        if self.Account_InterestRate_Check.text().isspace():
            Overdraft = ''
        else:
            Overdraft = self.Account_InterestRate_Check.text()
        if self.Account_CustomerId_Check.text().isspace():
            CustomerId = ''
        else:
            CustomerId = self.Account_CustomerId_Check.text()
        visitdate = self.Account_RecentVisitDate_Check.date()
        visitdate = str(visitdate).split('(')
        visitdate = visitdate[-1].split(')')
        visitdate = visitdate[0].split(', ')
        visitdate = visitdate[0] + '-' + visitdate[1] + '-' + visitdate[2]
        
        
        if (Account_Id == '' ) :
            QMessageBox.information(self,'错误','要更改的账户信息填写不完整！')
            return
        
        question = QMessageBox.question(self, '确定', '是否更改账户信息' , QMessageBox.No | QMessageBox.Yes , QMessageBox.Yes)
        if question == QMessageBox.No:
            return
        
        self.curso.execute('select * from Checking_Account where Account_Id = ' + '\'' + Account_Id + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','该账户不存在！')
            return
        
        QMessageBox.information(self,'提醒','不允许更改用户号或支行名，如有需求请进行销户和开户！')
    
            
        QMessageBox.information(self,'提醒','不允许更改开户日期，如有需求请进行销户和开户！')
       
        question = QMessageBox.question(self, '问题', '是否更改最近访问日期' , QMessageBox.No | QMessageBox.Yes , QMessageBox.Yes)
        if question == QMessageBox.Yes:
            if CustomerId == '':
                QMessageBox.information(self,'错误','需要指定访问用户！')
                return 
            self.curso.execute('select * from have_visit where Customer_Id = ' +'\''+ CustomerId +'\'' + 'and  Account_Id = ' + '\'' + Account_Id + '\'')
            query = self.curso.fetchone()
            if query is None:
                QMessageBox.information(self,'错误','该用户不存在！')
                return
            change = 'update have_visit set RecentVisit_Date = ' + '\''+ visitdate + '\'' + 'where Customer_Id = ' +'\''+ CustomerId +'\'' + 'and  Account_Id = ' + '\'' + Account_Id + '\''
            ret = self.cursor_bank(change,"have_visit",False)
            if ret == False:
                QMessageBox.information(self,'错误','该用户不存在')
                return 
        else :
            if (Balance == '' and  Overdraft == ''):
                QMessageBox.information(self,'错误','要更改的账户信息填写不完整！')
                return
        
        if  (Balance != '' or Overdraft != ''):
            change = 'update Checking_Account set '
            index = 0
            if  Balance!= '' :
                if index != 0:
                    change = change + ', '
                index = index + 1
                change = change + 'Account_Balance = ' + '\'' + Balance + '\''
            if  Overdraft!= '' :
                if index != 0:
                    change = change + ', '
                index = index + 1
                change = change + 'Overdraft = ' + '\'' + Overdraft + '\''
            change = change + 'where Account_Id = ' + '\'' + Account_Id + '\''
            print(change) 
        
            ret = self.cursor_bank(change,"Checking_Account",False)
            if ret == False:
                QMessageBox.information(self,'错误','要修改的账户不存在')
                return
        
            change = 'update Account set '
            index = 0
            if  Balance!= '' :
                if index != 0:
                    change = change + ', '
                index = index + 1
                change = change + 'Account_Balance = ' + '\'' + Balance + '\''
                change = change + 'where Account_Id = ' + '\'' + Account_Id + '\'' 
                ret = self.cursor_bank(change,"Account",False)
                if ret == False:
                    QMessageBox.information(self,'错误','要修改的账户不存在')
                    return
        
        
        self.display('check_account',False)
        print('change check')
        
    def account_query_check(self):
        if self.Account_Id_Check.text().isspace():
            Account_Id = ''
        else:
            Account_Id = self.Account_Id_Check.text()
        if self.Account_BankName_Check.text().isspace():
            BankName = ''
        else:
            BankName = self.Account_BankName_Check.text()
        if self.Account_Balance_Check.text().isspace():
            Balance = ''
        else:
            Balance = self.Account_Balance_Check.text()
        opendate = self.Account_OpenDate_Check.date()
        opendate = str(opendate).split('(')
        opendate = opendate[-1].split(')')
        opendate = opendate[0].split(', ')
        opendate = opendate[0] + '-' + opendate[1] + '-' + opendate[2]
        
        if self.Account_InterestRate_Check.text().isspace():
            Overdraft = ''
        else:
            Overdraft = self.Account_InterestRate_Check.text()
        if self.Account_CustomerId_Check.text().isspace():
            CustomerId = ''
        else:
            CustomerId = self.Account_CustomerId_Check.text()
        visitdate = self.Account_RecentVisitDate_Check.date()
        visitdate = str(visitdate).split('(')
        visitdate = visitdate[-1].split(')')
        visitdate = visitdate[0].split(', ')
        visitdate = visitdate[0] + '-' + visitdate[1] + '-' + visitdate[2]
        
        question = QMessageBox.question(self, '问题', '是否进行查询' , QMessageBox.No | QMessageBox.Yes , QMessageBox.Yes)
        if question == QMessageBox.No:
            return
        
        query = 'select Checking_Account.Account_Id, Checking_Account.Bank_Name, Checking_Account.Account_Balance, Checking_Account.Account_OpenDate, Checking_Account.Overdraft, have_visit.Customer_Id, have_visit.RecentVisit_Date  from Checking_Account INNER JOIN have_visit ON Checking_Account.Account_Id = have_visit.Account_Id '
        
        index = 0
        question = QMessageBox.question(self, '问题', '是否查询最近访问日期' , QMessageBox.No | QMessageBox.Yes , QMessageBox.Yes)
        if question == QMessageBox.Yes:
            if index == 0:
                query = query + 'where '
            else:
                query = query + 'and  '
            index = index + 1
            query = query + 'have_visit.RecentVisit_Date = ' + '\'' + visitdate + '\''
        
        question = QMessageBox.question(self, '问题', '是否查询开户日期' , QMessageBox.No | QMessageBox.Yes , QMessageBox.Yes)
        if question == QMessageBox.Yes:
            if index == 0:
                query = query + 'where '
            else:
                query = query + 'and  '
            index = index + 1
            query = query + 'Checking_Account.Account_OpenDate = ' + '\'' + opendate + '\''
        
        if Account_Id != '':
            if index == 0:
                query = query + 'where '
            else:
                query = query + 'and  '
            index = index + 1
            query = query + 'Checking_Account.Account_Id = ' + '\'' + Account_Id + '\''
        if BankName != '':
            if index == 0:
                query = query + 'where '
            else:
                query = query + 'and  '
            index = index + 1
            query = query + 'Checking_Account.Bank_Name = ' + '\'' + BankName + '\''
        if  Balance!= '':
            if index == 0:
                query = query + 'where '
            else:
                query = query + 'and  '
            index = index + 1
            query = query + 'Checking_Account.Account_Balance = ' + '\'' + Balance + '\''
        if Overdraft != '':
            if index == 0:
                query = query + 'where '
            else:
                query = query + 'and  '
            index = index + 1
            query = query + 'Checking_Account.Overdraft = ' + '\'' + Overdraft + '\''
        if CustomerId != '':
            if index == 0:
                query = query + 'where '
            else:
                query = query + 'and  '
            index = index + 1
            query = query + 'have_visit.Customer_Id = ' + '\'' + CustomerId + '\''
        ret = self.cursor_bank(query,"Account",False)
        if ret == False:
            print(query)
            QMessageBox.information(self,'错误','查询信息错误')
            return
        
        self.display('check_account',True)
    
    def account_open_save(self):
        if self.Account_Id_Save.text().isspace():
            Account_Id = ''
        else:
            Account_Id = self.Account_Id_Save.text()
        if self.Account_BankName_Save.text().isspace():
            BankName = ''
        else:
            BankName = self.Account_BankName_Save.text()
        if self.Account_Balance_Save.text().isspace():
            Balance = ''
        else:
            Balance = self.Account_Balance_Save.text()
        opendate = self.Account_OpenDate_Save.date()
        opendate = str(opendate).split('(')
        opendate = opendate[-1].split(')')
        opendate = opendate[0].split(', ')
        opendate = opendate[0] + '-' + opendate[1] + '-' + opendate[2]
        
        if self.Account_InterestRate_Save.text().isspace():
            Rate = ''
        else:
            Rate = self.Account_InterestRate_Save.text()
        if self.Account_CurrencyType_Save.text().isspace():
            Type = ''
        else:
            Type = self.Account_CurrencyType_Save.text()
        if self.Account_CustomerId_Save.text().isspace():
            CustomerId = ''
        else:
            CustomerId = self.Account_CustomerId_Save.text()
        
        visitdate = self.Account_RecentVisitDate_Save.date()
        visitdate = str(visitdate).split('(')
        visitdate = visitdate[-1].split(')')
        visitdate = visitdate[0].split(', ')
        visitdate = visitdate[0] + '-' + visitdate[1] + '-' + visitdate[2]
        
        
        self.curso.execute('select * from setupAccount WHERE Customer_Id = ' + '\'' + CustomerId + '\'' + 'and  Bank_Name = ' + '\'' + BankName + '\'' + 'and  Account_type =  \'储蓄账户\'' )
        query = self.curso.fetchone()
        if query is not None:
            QMessageBox.information(self,'错误','该客户已到该银行创建过此类账户！')
            return
        
        self.curso.execute('select * from Customer where Customer_Id = ' + '\'' + CustomerId + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','用户不存在！')
            return
        
        self.curso.execute('select * from Bank where Bank_Name = ' + '\'' + BankName + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','支行不存在！')
            return
        
        
        
        self.curso.execute('select * from Account where Account_Id = ' + '\'' + Account_Id + '\'')
        query = self.curso.fetchone()
        if query is None:
            if (Account_Id == '' or BankName == '' or opendate == '' or Balance == '' or Rate == '' or Type == '' or CustomerId == '' ) :
                QMessageBox.information(self,'错误','账户信息填写不完整！')
                return
            question = QMessageBox.question(self, '确定', '是否插入账户信息' , QMessageBox.No | QMessageBox.Yes , QMessageBox.Yes)
            if question == QMessageBox.No:
                return
            add = 'insert into Account  Values(' + '\''+ Account_Id + '\'' +  ', ' + '\''+ BankName + '\'' + ', ' + '\''+ Balance + '\'' + ', ' + '\''+ opendate + '\'' +')'
            
            reply = self.cursor_bank(add,"Account",False)
            if reply == False:
                QMessageBox.information(self,'错误','输入信息不合法')
                return
            add = 'insert  into  Saving_Account Values(' + '\''+ Account_Id + '\'' +  ', ' + '\''+ BankName + '\'' + ', ' + '\''+ Balance + '\'' + ', ' + '\''+ opendate + '\'' + ','+ '\'' + Rate +'\'' + ',' + '\'' + Type + '\'' ')'
            reply = self.cursor_bank(add,"Saving_Account",False)
            if reply == False:
                QMessageBox.information(self,'错误','输入信息不合法')
                return
        else:
            if (Account_Id == '' or CustomerId == '' ) :
                QMessageBox.information(self,'错误','账户信息填写不完整！')
                return
            self.curso.execute('select Bank_Name from Account WHERE Account_Id = ' + '\'' + Account_Id + '\'')
            bank = self.curso.fetchone()[0]
            self.curso.execute('select Customer_Id from have_visit WHERE Account_Id = ' + '\'' + Account_Id + '\'')
            customer = self.curso.fetchone()[0]
            self.curso.execute('select Account_type from setupAccount WHERE Bank_Name = ' + '\'' + bank + '\'' + 'and  Customer_Id = ' + '\'' + customer + '\'')
            type = self.curso.fetchone()[0]
            if type != '储蓄账户':
                QMessageBox.information(self,'错误','该账户号为支票账户类型！')
                return    
            question = QMessageBox.question(self, '确定', '是否插入账户信息' , QMessageBox.No | QMessageBox.Yes , QMessageBox.Yes)
            if question == QMessageBox.No:
                return
            BankName = bank
        
        
        
        add = 'insert into have_visit   Values(' + '\''+ CustomerId + '\'' +  ', ' + '\''+ Account_Id + '\''   + ', ' + '\''+ visitdate + '\'' +')'
        ret  = self.cursor_bank(add,"have_visit",False)
        if ret == False:
            QMessageBox.information(self,'错误','该客户已创建过该账户号！')
            return
        
        
        add = 'insert into setupAccount   Values(' + '\''+ CustomerId + '\'' +  ', ' + '\''+ BankName + '\''   + ', ' + '\''+ '储蓄账户' + '\'' +')'
        reply = self.cursor_bank(add,"setupAccount",False)
        if reply == False:
            QMessageBox.information(self,'错误','输入信息不合法')
            return
        
        
       
        
        self.display('saving_account',False)
        print('open save')
        
        
    def account_del_save(self):
        if self.Account_Id_Save.text().isspace():
            Id = ''
        else:
            Id = self.Account_Id_Save.text()
        if self.Account_CustomerId_Save.text().isspace():
            CustomerId = ''
        else:
            CustomerId = self.Account_CustomerId_Save.text()
            
        if ((Id == '' and  CustomerId == '') or Id == '' ):
            QMessageBox.information(self,'错误','未填写删除的账户号或账户号与客户号')
            return
        
        question = QMessageBox.question(self, '确定', '是否删除信息', QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if question == QMessageBox.No:
            return 
        
        if CustomerId == '':
            select = 'select Bank_Name from Saving_Account WHERE Account_Id = ' + '\'' + Id + '\''
            self.curso.execute(select)
            self.conn.commit()  # 事务的提交
            query = self.curso.fetchone()
            if query is not None:
                bank = query[0]
                select = 'select Customer_Id from have_visit WHERE Account_Id = ' + '\'' + Id + '\'' 
                self.curso.execute(select)
                self.conn.commit()  # 事务的提交
                for query in self.curso.fetchall():
                    if query is not None:
                        customer = query[0]
                        select = 'select * from setupAccount WHERE Customer_Id = ' + '\'' + customer + '\'' + 'and  Bank_Name = ' + '\'' + bank + '\'' + 'and  Account_type =  \'储蓄账户\'' 
                        self.curso.execute(select)
                        query = self.curso.fetchone()
                        if query is None:
                            QMessageBox.information(self,'错误','要删除的setupAccount信息不存在！')
                            return
                        dele = 'delete from setupAccount WHERE Customer_Id = ' + '\'' + customer + '\'' + 'and  Bank_Name = ' + '\'' + bank + '\'' + 'and  Account_type =  \'储蓄账户\'' 
                        reply = self.cursor_bank(dele,'setupAccount',False)
                        if reply == False:
                            QMessageBox.information(self,'错误','输入信息不合法')
                            return
            
            select = 'select * from Saving_Account WHERE Account_Id = ' + '\'' + Id + '\''
            self.curso.execute(select)
            query = self.curso.fetchone()
            if query is None:
                QMessageBox.information(self,'错误','要删除的Saving_Account信息不存在！')
                return
            dele = 'delete from Saving_Account WHERE Account_Id = ' + '\'' + Id + '\''
            reply = self.cursor_bank(dele,'Saving_Account',False)
            if reply == False:
                QMessageBox.information(self,'错误','输入信息不合法')
                return
            
            select = 'select * from have_visit WHERE Account_Id = ' + '\'' + Id + '\''
            self.curso.execute(select)
            query = self.curso.fetchone()
            if query is None:
                QMessageBox.information(self,'错误','要删除的have_visit信息不存在！')
                return
            dele = 'delete from have_visit WHERE Account_Id = ' + '\'' + Id + '\''
            reply = self.cursor_bank(dele,'have_visit',False)
            if reply == False:
                QMessageBox.information(self,'错误','输入信息不合法')
                return
            
            select = 'select * from Account WHERE Account_Id = ' + '\'' + Id + '\''
            self.curso.execute(select)
            query = self.curso.fetchone()
            if query is None:
                QMessageBox.information(self,'错误','要删除的Account信息不存在！')
                return
            dele = 'delete from Account WHERE Account_Id = ' + '\'' + Id + '\''
            reply = self.cursor_bank(dele,'Account',False)
            if reply == False:
                QMessageBox.information(self,'错误','输入信息不合法')
                return
        else:
            select = 'select Bank_Name from Saving_Account WHERE Account_Id = ' + '\'' + Id + '\''
            self.curso.execute(select)
            self.conn.commit()  # 事务的提交
            query = self.curso.fetchone()
            if query is None:
                QMessageBox.information(self,'错误','要删除的Bank_Name信息不存在！')
                return
            if query is not None:
                bank = query[0]
                select = 'select Customer_Id from have_visit WHERE Account_Id = ' + '\'' + Id + '\'' 
                self.curso.execute(select)
                row = self.curso.rowcount
                if row > 1:
                    select = 'select * from setupAccount WHERE Customer_Id = ' + '\'' +  CustomerId + '\'' + 'and  Bank_Name = ' + '\'' + bank + '\'' + 'and  Account_type =  \'储蓄账户\'' 
                    self.curso.execute(select)
                    query = self.curso.fetchone()
                    if query is None:
                        QMessageBox.information(self,'错误','要删除的setupAccount信息不存在！')
                        return
                    dele = 'delete from setupAccount WHERE Customer_Id = ' + '\'' + CustomerId + '\'' + 'and  Bank_Name = ' + '\'' + bank + '\'' + 'and  Account_type =  \'储蓄账户\'' 
                    reply = self.cursor_bank(dele,'setupAccount',False)
                    if reply == False:
                        QMessageBox.information(self,'错误','输入信息不合法')
                        return
                    
                    select = 'select * from have_visit WHERE Customer_Id = ' + '\'' + CustomerId + '\'' + 'and  Account_Id = ' + '\'' + Id + '\''  
                    self.curso.execute(select)
                    query = self.curso.fetchone()
                    if query is None:
                        QMessageBox.information(self,'错误','要删除的 have_visit 信息不存在！')
                        return
                    dele = 'delete from have_visit WHERE Customer_Id = ' + '\'' + CustomerId + '\'' + 'and  Account_Id = ' + '\'' + Id + '\''  
                    reply = self.cursor_bank(dele,'have_visit',False)
                    if reply == False:
                        QMessageBox.information(self,'错误','输入信息不合法')
                        return
                elif row == 1:
                    print(row)
                    select = 'select * from setupAccount WHERE Customer_Id = ' + '\'' +  CustomerId + '\'' + 'and  Bank_Name = ' + '\'' + bank + '\'' + 'and  Account_type =  \'储蓄账户\'' 
                    self.curso.execute(select)
                    query = self.curso.fetchone()
                    if query is None:
                        QMessageBox.information(self,'错误','要删除的 setupAccount 信息不存在！')
                        return
                    dele = 'delete from setupAccount WHERE Customer_Id = ' + '\'' + CustomerId + '\'' + 'and  Bank_Name = ' + '\'' + bank + '\'' + 'and  Account_type =  \'储蓄账户\'' 
                    reply = self.cursor_bank(dele,'setupAccount',False)
                    if reply == False:
                        QMessageBox.information(self,'错误','输入信息不合法')
                        return
            
                    select = 'select * from Saving_Account WHERE Account_Id = ' + '\'' + Id + '\''
                    self.curso.execute(select)
                    query = self.curso.fetchone()
                    if query is None:
                        QMessageBox.information(self,'错误','要删除的 Saving_Account 信息不存在！')
                        return
                    dele = 'delete from Saving_Account WHERE Account_Id = ' + '\'' + Id + '\''
                    reply = self.cursor_bank(dele,'Saving_Account',False)
                    if reply == False:
                        QMessageBox.information(self,'错误','输入信息不合法')
                        return
            
                    select = 'select * from have_visit WHERE Account_Id = ' + '\'' + Id + '\'' + 'and  Customer_Id = ' + '\'' + CustomerId + '\''
                    self.curso.execute(select)
                    query = self.curso.fetchone()
                    if query is None:
                        QMessageBox.information(self,'错误','要删除的have_visit信息不存在！')
                        return
                    dele = 'delete from have_visit WHERE Account_Id = ' + '\'' + Id + '\''  + 'and  Customer_Id = ' + '\'' + CustomerId + '\''
                    reply = self.cursor_bank(dele,'have_visit',False)
                    if reply == False:
                        QMessageBox.information(self,'错误','输入信息不合法')
                        return
            
                    select = 'select * from Account WHERE Account_Id = ' + '\'' + Id + '\''
                    self.curso.execute(select)
                    query = self.curso.fetchone()
                    if query is None:
                        QMessageBox.information(self,'错误','要删除的Account信息不存在！')
                        return
                    dele = 'delete from Account WHERE Account_Id = ' + '\'' + Id + '\''
                    relpy = self.cursor_bank(dele,'Account',False)
                    if reply == False:
                        QMessageBox.information(self,'错误','输入信息不合法')
                        return
                else:
                    QMessageBox.information(self,'错误','要删除的Customer_Id信息不存在！')
                    return
        self.display('saving_account',False)
        print('del save')
        
    def account_change_save(self):
        if self.Account_Id_Save.text().isspace():
            Account_Id = ''
        else:
            Account_Id = self.Account_Id_Save.text()
        if self.Account_BankName_Save.text().isspace():
            BankName = ''
        else:
            BankName = self.Account_BankName_Save.text()
        if self.Account_Balance_Save.text().isspace():
            Balance = ''
        else:
            Balance = self.Account_Balance_Save.text()
        opendate = self.Account_OpenDate_Save.date()
        opendate = str(opendate).split('(')
        opendate = opendate[-1].split(')')
        opendate = opendate[0].split(', ')
        opendate = opendate[0] + '-' + opendate[1] + '-' + opendate[2]
        
        if self.Account_InterestRate_Save.text().isspace():
            Rate = ''
        else:
            Rate = self.Account_InterestRate_Save.text()
        if self.Account_CurrencyType_Save.text().isspace():
            Type = ''
        else:
            Type = self.Account_CurrencyType_Save.text()
        if self.Account_CustomerId_Save.text().isspace():
            CustomerId = ''
        else:
            CustomerId = self.Account_CustomerId_Save.text()
        visitdate = self.Account_RecentVisitDate_Save.date()
        visitdate = str(visitdate).split('(')
        visitdate = visitdate[-1].split(')')
        visitdate = visitdate[0].split(', ')
        visitdate = visitdate[0] + '-' + visitdate[1] + '-' + visitdate[2]
        
        
        if (Account_Id == '' ) :
            QMessageBox.information(self,'错误','要更改的账户信息填写不完整！')
            return
        
        question = QMessageBox.question(self, '确定', '是否更改账户信息' , QMessageBox.No | QMessageBox.Yes , QMessageBox.Yes)
        if question == QMessageBox.No:
            return
        
        self.curso.execute('select * from Saving_Account where Account_Id = ' + '\'' + Account_Id + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','该账户不存在！')
            return
        
        QMessageBox.information(self,'提醒','不允许更改用户号或支行名，如有需求请进行销户和开户！')
    
            
        QMessageBox.information(self,'提醒','不允许更改开户日期，如有需求请进行销户和开户！')
       
        question = QMessageBox.question(self, '问题', '是否更改最近访问日期' , QMessageBox.No | QMessageBox.Yes , QMessageBox.Yes)
        if question == QMessageBox.Yes:
            if CustomerId == '':
                QMessageBox.information(self,'错误','需要指定访问用户！')
                return 
            self.curso.execute('select * from have_visit where Customer_Id = ' +'\''+ CustomerId +'\'' + 'and  Account_Id = ' + '\'' + Account_Id + '\'')
            query = self.curso.fetchone()
            if query is None:
                QMessageBox.information(self,'错误','该用户不存在！')
                return
            change = 'update have_visit set RecentVisit_Date = ' + '\''+ visitdate + '\'' + 'where Customer_Id = ' +'\''+ CustomerId +'\'' + 'and  Account_Id = ' + '\'' + Account_Id + '\''
            ret = self.cursor_bank(change,"have_visit",False)
            if ret == False:
                QMessageBox.information(self,'错误','该用户不存在')
                return 
        else :
            if (Balance == '' and  Rate == '' and   Type == ''):
                QMessageBox.information(self,'错误','要更改的账户信息填写不完整！')
                return
        
        if  (Balance != '' or Rate != '' or Type != ''):
            change = 'update Saving_Account set '
            index = 0
            if  Balance!= '' :
                if index != 0:
                    change = change + ', '
                index = index + 1
                change = change + 'Account_Balance = ' + '\'' + Balance + '\''
            if  Rate!= '' :
                if index != 0:
                    change = change + ', '
                index = index + 1
                change = change + 'Interest_Rate = ' + '\'' + Rate + '\''
            if  Type!= '' :
                if index != 0:
                    change = change + ', '
                index = index + 1
                change = change + 'Currency_Type = ' + '\'' + Type + '\''
            change = change + 'where Account_Id = ' + '\'' + Account_Id + '\''
            print(change) 
        
            ret = self.cursor_bank(change,"Saving_Account",False)
            if ret == False:
                QMessageBox.information(self,'错误','要修改的账户不存在')
                return
        
            change = 'update Account set '
            index = 0
            if  Balance!= '' :
                if index != 0:
                    change = change + ', '
                index = index + 1
                change = change + 'Account_Balance = ' + '\'' + Balance + '\''
                change = change + 'where Account_Id = ' + '\'' + Account_Id + '\'' 
                ret = self.cursor_bank(change,"Account",False)
                if ret == False:
                    QMessageBox.information(self,'错误','要修改的账户不存在')
                    return
              
        self.display('saving_account',False)
        print('change Save')
    def account_query_save(self):
        if self.Account_Id_Save.text().isspace():
            Account_Id = ''
        else:
            Account_Id = self.Account_Id_Save.text()
        if self.Account_BankName_Save.text().isspace():
            BankName = ''
        else:
            BankName = self.Account_BankName_Save.text()
        if self.Account_Balance_Save.text().isspace():
            Balance = ''
        else:
            Balance = self.Account_Balance_Save.text()
        opendate = self.Account_OpenDate_Save.date()
        opendate = str(opendate).split('(')
        opendate = opendate[-1].split(')')
        opendate = opendate[0].split(', ')
        opendate = opendate[0] + '-' + opendate[1] + '-' + opendate[2]
        
        if self.Account_InterestRate_Save.text().isspace():
            Rate = ''
        else:
            Rate = self.Account_InterestRate_Save.text()
        if self.Account_CurrencyType_Save.text().isspace():
            Type = ''
        else:
            Type = self.Account_CurrencyType_Save.text()
        
        if self.Account_CustomerId_Save.text().isspace():
            CustomerId = ''
        else:
            CustomerId = self.Account_CustomerId_Save.text()
        visitdate = self.Account_RecentVisitDate_Save.date()
        visitdate = str(visitdate).split('(')
        visitdate = visitdate[-1].split(')')
        visitdate = visitdate[0].split(', ')
        visitdate = visitdate[0] + '-' + visitdate[1] + '-' + visitdate[2]
        
        question = QMessageBox.question(self, '问题', '是否进行查询' , QMessageBox.No | QMessageBox.Yes , QMessageBox.Yes)
        if question == QMessageBox.No:
            return
        
        query = 'select Saving_Account.Account_Id, Saving_Account.Bank_Name, Saving_Account.Account_Balance, Saving_Account.Account_OpenDate, Saving_Account.Interest_Rate, Saving_Account.Currency_Type , have_visit.Customer_Id, have_visit.RecentVisit_Date  from Saving_Account INNER JOIN have_visit ON Saving_Account.Account_Id = have_visit.Account_Id '
        
        index = 0
        question = QMessageBox.question(self, '问题', '是否查询最近访问日期' , QMessageBox.No | QMessageBox.Yes , QMessageBox.Yes)
        if question == QMessageBox.Yes:
            if index == 0:
                query = query + 'where '
            else:
                query = query + 'and  '
            index = index + 1
            query = query + 'have_visit.RecentVisit_Date = ' + '\'' + visitdate + '\''
        
        question = QMessageBox.question(self, '问题', '是否查询开户日期' , QMessageBox.No | QMessageBox.Yes , QMessageBox.Yes)
        if question == QMessageBox.Yes:
            if index == 0:
                query = query + 'where '
            else:
                query = query + 'and  '
            index = index + 1
            query = query + 'Saving_Account.Account_OpenDate = ' + '\'' + opendate + '\''
        
        if Account_Id != '':
            if index == 0:
                query = query + 'where '
            else:
                query = query + 'and  '
            index = index + 1
            query = query + 'Saving_Account.Account_Id = ' + '\'' + Account_Id + '\''
        if BankName != '':
            if index == 0:
                query = query + 'where '
            else:
                query = query + 'and  '
            index = index + 1
            query = query + 'Saving_Account.Bank_Name = ' + '\'' + BankName + '\''
        if  Balance!= '':
            if index == 0:
                query = query + 'where '
            else:
                query = query + 'and   '
            index = index + 1
            query = query + 'Saving_Account.Account_Balance = ' + '\'' + Balance + '\''
        if Rate != '':
            if index == 0:
                query = query + 'where '
            else:
                query = query + 'and   '
            index = index + 1
            query = query + 'Saving_Account.Interest_Rate = ' + '\'' + Rate + '\''
        if Type != '':
            if index == 0:
                query = query + 'where '
            else:
                query = query + 'and   '
            index = index + 1
            query = query + 'Saving_Account.Currency_Type = ' + '\'' + Type + '\''
        if CustomerId != '':
            if index == 0:
                query = query + 'where '
            else:
                query = query + 'and   '
            index = index + 1
            query = query + 'have_visit.Customer_Id = ' + '\'' + CustomerId + '\''
        ret = self.cursor_bank(query,"Account",False)
        if ret == False:
            QMessageBox.information(self,'错误','查询信息错误')
            return
        
        self.display('saving_account',True)
        
        
        
    def loan_add(self):
        if self.Loan_Id.text().isspace():
            Loan_Id = ''
        else:
            Loan_Id = self.Loan_Id.text()
        if self.Loan_BankName.text().isspace():
            BankName = ''
        else:
            BankName = self.Loan_BankName.text()
        if self.Loan_Money.text().isspace():
            Loan_Money = ''
        else:
            Loan_Money = self.Loan_Money.text()
        if self.Loan_State.text().isspace():
            Loan_State = ''
        else:
            Loan_State = self.Loan_State.text()
        
        if (Loan_Id == '' or BankName == '' or Loan_Money == '' ):
            QMessageBox.information(self,'错误','贷款信息填写不完整！')
            return
        QMessageBox.information(self,'提醒','贷款状态为自动生成，无法自定义！')
        
        question = QMessageBox.question(self, '确定', "插入贷款信息", QMessageBox.No | QMessageBox.Yes , QMessageBox.Yes)
        
        if question == QMessageBox.No:
            return
        
        self.curso.execute('select * from Loan where Loan_Id = ' + '\'' + Loan_Id + '\'')
        query = self.curso.fetchone()
        if query is not None:
            QMessageBox.information(self,'错误','贷款号已存在！')
            return
        
        self.curso.execute('select * from Bank where Bank_Name = ' + '\'' + BankName + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','银行不存在！')
            return
        
        
        add = 'insert into Loan Values(' + '\''+ Loan_Id + '\'' + ', ' + '\''+ BankName + '\'' + ', ' + '\'' + Loan_Money + '\''  +')'
        self.curso.execute(add)
        self.conn.commit()
        self.display('loan',False)
        
        
        print('loan add')
        
    def loan_del(self):
        if self.Loan_Id.text().isspace():
            Id = ''
        else:
            Id = self.Loan_Id.text()
            
        if (Id == ''):
            QMessageBox.information(self,'错误','删除信息未填写完整')
            return
        
        question = QMessageBox.question(self, '确定', '是否删除贷款号为: '+ Id + '的贷款', QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if question == QMessageBox.No:
            return 
        
        self.curso.execute('select * from Loan where Loan_Id = ' + '\'' + Id + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','贷款号不存在！')
            return
        
        self.curso.execute('select Loan_Money from Loan where Loan_Id = ' + '\'' + Id + '\'')
        money = self.curso.fetchone()[0]
        money = double(money)
        
        query = 'select sum(Pay_Money) from Payment where Loan_Id = ' + '\'' + Id + '\''
        self.curso.execute(query)
        sum = self.curso.fetchone()[0]
        print(sum)
        if sum is None:
            print('eeeee')
            dele = 'delete from Loan WHERE Loan_Id = ' + '\'' + Id + '\''
            self.curso.execute(dele)
            self.conn.commit()  # 事务的提交
        else:
            sum = double(sum)
            if sum == 0:
                dele = 'delete from Payment WHERE Loan_Id = ' + '\'' + Id + '\'' 
                self.curso.execute(dele)
                self.display('pay')
                dele = 'delete from Loan WHERE Loan_Id = ' + '\'' + Id + '\'' 
                self.curso.execute(dele)
                self.conn.commit()
            elif sum < money:
                QMessageBox.information(self,'错误','贷款在发放中！')
                return
            elif sum == money:
                dele = 'delete from Payment WHERE Loan_Id = ' + '\'' + Id + '\'' 
                self.curso.execute(dele)
                self.display('pay')
                dele = 'delete from Loan WHERE Loan_Id = ' + '\'' + Id + '\'' 
                self.curso.execute(dele)
                self.conn.commit()
        self.display('loan',False)
        print('loan del')
        
    def loan_query(self):
        if self.Loan_Id.text().isspace():
            Id = ''
        else:
            Id = self.Loan_Id.text()
        if self.Loan_BankName.text().isspace():
            BankName = ''
        else:
            BankName = self.Loan_BankName.text()
        if self.Loan_Money.text().isspace():
            Loan_Money = ''
        else:
            Loan_Money = self.Loan_Money.text()
        if self.Loan_State.text().isspace():
            Loan_State = ''
        else:
            Loan_State = self.Loan_State.text()
        
        
        if (Id == '' and   BankName == ''  and   Loan_Money == ''):
            change = 'select * from Loan'
            self.state_query = Loan_State
            self.cursor_bank(change,'loan',True)
            return
        query = 'select * from Loan where '
        index = 0
        
        question = QMessageBox.question(self, '确定', '是否进行查询', QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if question == QMessageBox.No:
            return 
        
        if Id != '' :
            if index != 0:
                query = query + 'and   '
            index = index + 1
            query = query + 'Loan_Id = ' + '\'' + Id + '\''
        if BankName != '' :
            if index != 0:
                query = query + 'and   '
            index = index + 1
            query = query + 'Bank_Name = ' + '\'' + BankName + '\''
        if  Loan_Money!= '' :
            if index != 0:
                query = query + 'and   '
            index = index + 1
            query = query + 'Loan_Money = ' + '\'' + Loan_Money + '\''
        self.state_query = Loan_State
        reply = self.cursor_bank(query,'loan',True)
        if reply == False:
            QMessageBox.information(self,'错误','输入信息不合法')
            return
        
        print('query')
        
    def loan_pay(self):
        if self.Loan_PayId.text().isspace():
            Pay_Id = ''
        else:
            Pay_Id = self.Loan_PayId.text()
        if self.Loan_CustomerId.text().isspace():
            Customer_Id = ''
        else:
            Customer_Id = self.Loan_CustomerId.text()
        Pay_Date = self.Loan_PayDate.date()
        Pay_Date = str(Pay_Date).split('(')
        Pay_Date = Pay_Date[-1].split(')')
        Pay_Date = Pay_Date[0].split(', ')
        Pay_Date = Pay_Date[0] + '-' + Pay_Date[1] + '-' + Pay_Date[2]
        
        
        if self.Loan_Pay_Id.text().isspace():
            Loan_Id = ''
        else:
            Loan_Id = self.Loan_Pay_Id.text()
        
        if self.Loan_PayMoney.text().isspace():
            PayMoney = ''
        else:
            PayMoney = self.Loan_PayMoney.text()
        
        if (Loan_Id == '' or  Customer_Id== '' or Pay_Id == '' or Pay_Date == '' or PayMoney == ''):
            QMessageBox.information(self,'错误','贷款发放信息填写不完整！')
            return
        
        
        question = QMessageBox.question(self, '确定', "插入贷款发放信息", QMessageBox.No | QMessageBox.Yes , QMessageBox.Yes)
        
        if question == QMessageBox.No:
            return
        
        self.curso.execute('select * from Customer where  Customer_Id= ' + '\'' + Customer_Id + '\'')
        query = self.curso.fetchone()
        if query is None:
            QMessageBox.information(self,'错误','客户不存在！')
            return
        
        self.curso.execute('select * from Loan where  Loan_Id= ' + '\'' + Loan_Id + '\'')
        query = self.curso.fetchone()
        print(query)
        if query is None:
            QMessageBox.information(self,'错误','贷款号不存在！')
            return
        
        self.curso.execute('select * from Payment where Loan_Id = ' + '\'' + Loan_Id + '\'' + ' and   Customer_Id = ' + '\'' +Customer_Id + '\'' +' and   Pay_ID = '  + '\'' + Pay_Id + '\'')
        query = self.curso.fetchone()
        if query is not None:
            QMessageBox.information(self,'错误','此笔发放已存在！')
            return
        
        
        self.curso.execute('select Loan_Money from Loan where Loan_Id = ' +'\'' + Loan_Id + '\'')
        money = self.curso.fetchone()[0]
        money = double(money)
        
        self.curso.execute('select sum(Pay_Money) from Payment where Loan_Id = ' +'\'' + Loan_Id + '\'')
        sum = self.curso.fetchone()[0]
        if sum is not None:
            sum = double(sum)
            print(sum)
            if money < sum + double(PayMoney):
                QMessageBox.information(self,'错误','发放金额过大！')
                return
        else:
            if money < double(PayMoney):
                QMessageBox.information(self,'错误','发放金额过大！')
                return
            
        
        
        add = 'insert into Payment Values(' + '\''+ Loan_Id + '\'' + ', ' + '\''+ Customer_Id + '\'' + ', ' + '\'' + Pay_Date + '\''  +', ' + '\'' + PayMoney + '\''  +', ' + '\'' + Pay_Id + '\''  +')'
        reply = self.cursor_bank(add,'pay',False)
        if reply == False:
            QMessageBox.information(self,'错误','输入信息不合法')
            return
        self.display('loan')
        
        
    def query_year(self):
        if self.Year.text().isspace():
            year = ''
        else:
            year = self.Year.text()
        if self.Query_AccountType.text().isspace():
            type = ''
        else:
            type = self.Query_AccountType.text()
        if(year == '' or type == '' or (type != '贷款业务' and   type != '储蓄业务')):
            QMessageBox.information(self,'错误','查询信息错误，账户类型请填写贷款业务或储蓄业务！')
            return
        if type == '贷款业务':
            query = 'select Loan.Bank_Name, count(DISTINCT Payment.Customer_Id) ,sum(Payment.Pay_Money) from  Loan,Payment where Loan.Loan_Id =  Payment.Loan_Id and   EXTRACT(YEAR FROM Payment.Pay_Date) = ' + '\'' + year + '\'' + 'group by Loan.Bank_Name'
            reply = self.cursor_bank(query, 'result',True)
            if reply == False:
                QMessageBox.information(self,'错误','输入信息不合法')
                return
        if type == '储蓄业务':
            query = 'select bala.Bank_Name, bala.reslut,cus.num from  (select Saving_Account.Bank_Name , sum(Saving_Account.Account_Balance) as reslut from Saving_Account where EXTRACT(YEAR FROM Account_OpenDate) = '  + '\''+ year + '\'' +' group by Saving_Account.Bank_Name) bala, (select Saving_Account.Bank_Name, count(have_visit.Customer_Id) as num from Saving_Account, have_visit  where Saving_Account.Account_Id = have_visit.Account_Id and   EXTRACT(YEAR FROM Saving_Account.Account_OpenDate) = '  + '\''+ year + '\'' + 'group by  Saving_Account.Bank_Name) cus where bala.Bank_Name = cus.Bank_Name  '
            reply = self.cursor_bank(query, 'result',True)
            if reply == False:
                QMessageBox.information(self,'错误','输入信息不合法')
                return
        
    def query_season(self):
        if self.Year.text().isspace():
            year = ''
        else:
            year = self.Year.text()
        if self.Season.text().isspace():
            season = ''
        else:
            season = self.Season.text()
        if self.Query_AccountType.text().isspace():
            type = ''
        else:
            type = self.Query_AccountType.text()
        if(year == '' or type == '' or (type != '贷款业务' and   type != '储蓄业务')):
            QMessageBox.information(self,'错误','查询信息错误，账户类型请填写贷款业务或储蓄业务！')
            return
        if type == '贷款业务':
            query = 'select Loan.Bank_Name, count(DISTINCT Payment.Customer_Id) ,sum(Payment.Pay_Money) from  Loan,Payment where Loan.Loan_Id =  Payment.Loan_Id and   EXTRACT(YEAR FROM Payment.Pay_Date) = ' + '\'' + year + '\'' + 'and   EXTRACT(QUARTER FROM Payment.Pay_Date ) = ' + '\'' + season + '\'' +'group by Loan.Bank_Name'
            reply = self.cursor_bank(query, 'result',True)
            if reply == False:
                QMessageBox.information(self,'错误','输入信息不合法')
                return
        if type == '储蓄业务':
            query = 'select bala.Bank_Name, bala.reslut,cus.num from  (select Saving_Account.Bank_Name , sum(Saving_Account.Account_Balance) as reslut from Saving_Account where EXTRACT(YEAR FROM Account_OpenDate) = '  + '\''+ year + '\'' + 'and   EXTRACT(QUARTER FROM Account_OpenDate) = '+ '\''+ season + '\''+ ' group by Saving_Account.Bank_Name) bala, (select Saving_Account.Bank_Name, count(have_visit.Customer_Id) as num from Saving_Account, have_visit  where Saving_Account.Account_Id = have_visit.Account_Id and   EXTRACT(YEAR FROM Saving_Account.Account_OpenDate) = '  + '\''+ year + '\'' + 'and   EXTRACT(QUARTER FROM Saving_Account.Account_OpenDate) = ' +'\'' + season + '\'' + 'group by  Saving_Account.Bank_Name) cus where bala.Bank_Name = cus.Bank_Name  '
            reply = self.cursor_bank(query, 'result',True)
            if reply == False:
                QMessageBox.information(self,'错误','输入信息不合法')
                return
        print('query season')
        
    def query_month(self):
        if self.Year.text().isspace():
            year = ''
        else:
            year = self.Year.text()
        if self.Month.text().isspace():
            month = ''
        else:
            month = self.Month.text()
        if self.Query_AccountType.text().isspace():
            type = ''
        else:
            type = self.Query_AccountType.text()
        if(year == '' or type == '' or (type != '贷款业务' and   type != '储蓄业务')):
            QMessageBox.information(self,'错误','查询信息错误，账户类型请填写贷款业务或储蓄业务！')
            return
        if type == '贷款业务':
            query = 'select Loan.Bank_Name, count(DISTINCT Payment.Customer_Id) ,sum(Payment.Pay_Money) from  Loan,Payment where Loan.Loan_Id =  Payment.Loan_Id and   EXTRACT(YEAR FROM Pay_Date) = ' + '\'' + year + '\'' +  'and   EXTRACT(MONTH FROM Payment.Pay_Date ) = ' + '\'' + month + '\'' +'group by Loan.Bank_Name'
            reply = self.cursor_bank(query, 'result',True)
            if reply == False:
                QMessageBox.information(self,'错误','输入信息不合法')
                return
        if type == '储蓄业务':
            query = 'select bala.Bank_Name, bala.reslut,cus.num from  (select Saving_Account.Bank_Name , sum(Saving_Account.Account_Balance) as reslut from Saving_Account where EXTRACT(YEAR FROM Account_OpenDate) = '  + '\''+ year + '\'' + 'and   EXTRACT( MONTH FROM Account_OpenDate) = '+ '\''+ month + '\''+ ' group by Saving_Account.Bank_Name) bala, (select Saving_Account.Bank_Name, count(have_visit.Customer_Id) as num from Saving_Account, have_visit  where Saving_Account.Account_Id = have_visit.Account_Id and   EXTRACT(YEAR FROM Saving_Account.Account_OpenDate) = '  + '\''+ year + '\'' + 'and  EXTRACT(MONTH FROM Saving_Account.Account_OpenDate) = ' +'\'' + month + '\'' + 'group by  Saving_Account.Bank_Name) cus where bala.Bank_Name = cus.Bank_Name  '
            reply = self.cursor_bank(query, 'result',True)
            if reply == False:
                QMessageBox.information(self,'错误','输入信息不合法')
                return
        print('query season')
        print('query month')
        
    
    
    
if  __name__=="__main__":
    conn = pymysql.connect(host='127.0.0.1',user='root',passwd='12345678',port=3306,db='bank',charset='utf8')
    app=QtWidgets.QApplication(sys.argv)
    bank = BankManger(Connect_bank_Manage = conn)
    
    bank.show()
    sys.exit(app.exec_())



