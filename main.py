from instrutor import Instrutor
from aluno import Aluno
from aula import Aula
import psycopg2
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QLabel, QListWidget
from PyQt5 import QtGui
  


def EscolherUsuario():
    escolha = primeiratela.lineEdit.text()
    if(escolha != "Aluno" and escolha != "Instrutor"):
        QMessageBox.about(primeiratela, "Aviso", "Escolha entre Instrutor e Aluno")
        return 1
    
    if(escolha == "Aluno"):
        primeiratela.hide()
        Telaalunologincadastro.show()
        return 1

    primeiratela.hide()
    Telainstrutorlogincadastro.show()

def detelaescolhainstrutorparatelacadastroinstrutor():
    Telainstrutorlogincadastro.hide()
    Telainstrutor.show()
    
def detelaescolhainstrutorparatelalogininstrutor():
    Telainstrutorlogincadastro.hide()
    Telainstrutorlogin.show()

def detelaescolhaalunoparatelacadastroaluno():
    Telaalunologincadastro.hide()
    Telaaluno.show()
    
def detelaescolhaalunoparatelaloginaluno():
    Telaalunologincadastro.hide()
    Telaalunologin.show()

def detelaalterarcadastroinstrutorparatelainstrutorlogincadastro():
    Telaalterarcadastroinstrutor.hide()
    Telainstrutorlogincadastro.show()

def detelatelaprincipalinstrutorparatelainstrutorlogincadastro():
    TelaprincipalInstrutor.hide()
    Telainstrutorlogincadastro.show()

def detelaalunologinparatelaprincipalaluno():
    Telaalunologin.hide()
    Telaprincipalaluno.show()

def detelaprincipalalunoparatelamarcaraula():
    Telaprincipalaluno.hide()
    Telamarcaraula.show()

def detelaprincipalalunoparatelaalterarcadastroaluno():
    Telaprincipalaluno.hide()
    Telaalterarcadastroaluno.show()

def CadastroInstrutor():
#Nome, Cpf, DiaNascimento, MesNascimento, AnoNascimento, Graduacao, Aluno, Horarios, Senha

    horarios = [[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
    Nome = Telainstrutor.lineEdit.text()
    Cpf = Telainstrutor.lineEdit_2.text()
    Graduacao = Telainstrutor.lineEdit_3.text()
    Senha = Telainstrutor.lineEdit_11.text()
    data = Telainstrutor.calendarWidget.selectedDate()
    DiaNascimento = data.day()
    MesNascimento = data.month()
    AnoNascimento = data.year()

    
    if(len(Nome) < 5 or len(Nome) > 50):
        QMessageBox.about(Telainstrutor, "Aviso", "Nome invalido(Para um nome ser considerado valido ele deve conter de 5 a 50 caracteres)")
        return "Nome invalido(Para um nome ser considerado valido ele deve conter de 5 a 50 caracteres)"

    if(len(Cpf) != 11):
        QMessageBox.about(Telainstrutor, "Aviso", "CPF invalido")
        return "CPF invalido"

    for i in Cpf:
        if(not i.isdigit()):
            QMessageBox.about(Telainstrutor, "Aviso", "CPF invalido")
            return "CPF invalido"

    if(AnoNascimento > 2002):
        QMessageBox.about(Telainstrutor, "Aviso", "Voce deve ter mais de 18 anos para se cadastrar")
        return "Voce deve ter mais de 18 anos para se cadastrar"

    if(AnoNascimento < 1900):
        QMessageBox.about(Telainstrutor, "Aviso", "Ano invalido")
        return "Ano invalido"

    if(len(Graduacao) > 500):
        QMessageBox.about(Telainstrutor, "Aviso", "O comprimento da graduacao deve conter no maximo 500 caracteres")
        return "O comprimento da graduacao deve conter no maximo 500 caracteres"
            
    con = psycopg2.connect(database='sistema', user='postgres', password='henry')
    cur = con.cursor()
    cur.execute("insert into instrutor values('%s', '%s', %d, %d, %d, '%s', %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %s)"%(Nome, Cpf, DiaNascimento, MesNascimento, AnoNascimento, Graduacao, horarios[0][0], horarios[0][1], horarios[1][0], horarios[1][1], horarios[2][0], horarios[2][1], horarios[3][0],horarios[3][1], horarios[4][0], horarios[4][1], horarios[5][0], horarios[5][1], horarios[6][0], horarios[6][1], Senha))
    con.commit()
    con.close()
    Telainstrutor.hide()
    Telainstrutorlogincadastro.show()
    return "Instrutor Cadastrado com sucesso"


def CadastroAluno():
#Nome, Cpf, DiaNascimento,MesNascimento, AnoNascimento, Endereco, NumeroContato, Senha

    Nome = Telaaluno.lineEdit.text()
    Cpf = Telaaluno.lineEdit_2.text()
    data = Telaaluno.calendarWidget.selectedDate()
    DiaNascimento = data.day()
    MesNascimento = data.month()
    AnoNascimento = data.year()
    Endereco = Telaaluno.lineEdit_3.text()
    NumeroContato = Telaaluno.lineEdit_4.text()
    Senha = Telaaluno.lineEdit_5.text()
    
    if(len(Nome) < 5 or len(Nome) > 50):
        QMessageBox.about(Telaaluno, "Aviso", "Nome invalido(Para um nome ser considerado valido ele deve conter de 5 a 50 caracteres)")
        return "Nome invalido(Para um nome ser considerado valido ele deve conter de 5 a 50 caracteres)"

    if(len(Cpf) != 11):
        QMessageBox.about(Telaaluno, "Aviso", "CPF invalido")
        return "CPF invalido"

    for i in Cpf:
        if(not i.isdigit()):
            QMessageBox.about(Telaaluno, "Aviso", "CPF invalido")
            return "CPF invalido"

    if(AnoNascimento > 2002):
        QMessageBox.about(Telaaluno, "Aviso", "Voce deve ter mais de 18 anos para se cadastrar")
        return "Voce deve ter mais de 18 anos para se cadastrar"

    if(AnoNascimento < 1900):
        QMessageBox.about(Telaaluno, "Aviso", "Ano invalido")
        return "Ano invalido"

    if(len(Endereco) < 5 or len(Endereco) > 800):
        QMessageBox.about(Telaaluno, "Aviso", "Endereco invalido(Para um Endereco ser considerado valido ele deve conter de 5 a 800 caracteres)")
        return "Endereco invalido(Para um Endereco ser considerado valido ele deve conter de 5 a 800 caracteres)"

    if(len(NumeroContato) != 11):
        QMessageBox.about(Telaaluno, "Aviso", "Numero para contato invalido")
        return "Numero para contato invalido"

    for i in NumeroContato:
        if(not i.isdigit()):
            QMessageBox.about(Telaaluno, "Aviso", "Numero para contato invalido")
            return "Numero para contato invalido"

    con = psycopg2.connect(database='sistema', user='postgres', password='henry')
    cur = con.cursor()
    cur.execute("insert into aluno values('%s', '%s', %d, %d, %d, '%s', '%s', '%s')"%(Nome, Cpf, DiaNascimento, MesNascimento, AnoNascimento, Endereco, NumeroContato, Senha))
    con.commit()
    con.close()
    Telaaluno.hide()
    Telaalunologincadastro.show()
    return "Aluno Cadastrado com sucesso"

def DisponibilidadeInstrutor():
#CpfInstrutor, inseg, fimseg, inter, fimter, inqua, fimqua, inqui, fimqui, insex, fimsex, insab, fimsab, indom, fimdom

    if(len(Teladisponibilidadeinstrutor.lineEdit.text())!=5):
        QMessageBox.about(Teladisponibilidadeinstrutor, "Aviso", "O campo 'segunda' deve conter 5 digitos na forma horainicio/horafinal")
        return 2

    if(len(Teladisponibilidadeinstrutor.lineEdit_2.text())!=5):
        QMessageBox.about(Teladisponibilidadeinstrutor, "Aviso", "O campo 'terça' deve conter 5 digitos na forma horainicio/horafinal")
        return 2

    if(len(Teladisponibilidadeinstrutor.lineEdit_3.text())!=5):
        QMessageBox.about(Teladisponibilidadeinstrutor, "Aviso", "O campo 'quarta' deve conter 5 digitos na forma horainicio/horafinal")
        return 2

    if(len(Teladisponibilidadeinstrutor.lineEdit_4.text())!=5):
        QMessageBox.about(Teladisponibilidadeinstrutor, "Aviso", "O campo 'quinta' deve conter 5 digitos na forma horainicio/horafinal")
        return 2

    if(len(Teladisponibilidadeinstrutor.lineEdit_5.text())!=5):
        QMessageBox.about(Teladisponibilidadeinstrutor, "Aviso", "O campo 'sexta' deve conter 5 digitos na forma horainicio/horafinal")
        return 2

    if(len(Teladisponibilidadeinstrutor.lineEdit_6.text())!=5):
        QMessageBox.about(Teladisponibilidadeinstrutor, "Aviso", "O campo 'sábado' deve conter 5 digitos na forma horainicio/horafinal")
        return 2

    if(len(Teladisponibilidadeinstrutor.lineEdit_7.text())!=5):
        QMessageBox.about(Teladisponibilidadeinstrutor, "Aviso", "O campo 'domingo' deve conter 5 digitos na forma horainicio/horafinal")
        return 2

    segunda = Teladisponibilidadeinstrutor.lineEdit.text()
    terca = Teladisponibilidadeinstrutor.lineEdit_2.text()
    quarta = Teladisponibilidadeinstrutor.lineEdit_3.text()
    quinta = Teladisponibilidadeinstrutor.lineEdit_4.text()
    sexta = Teladisponibilidadeinstrutor.lineEdit_5.text()
    sabado = Teladisponibilidadeinstrutor.lineEdit_6.text()
    domingo = Teladisponibilidadeinstrutor.lineEdit_7.text()

    inseg  = int(segunda[0]+segunda[1])
    fimseg = int(segunda[3]+segunda[4])

    inter  = int(terca[0]+terca[1])
    fimter = int(terca[3]+terca[4])

    inqua = int(quarta[0]+quarta[1])
    fimqua = int(quarta[3]+quarta[4])

    inqui = int(quinta[0]+quinta[1])
    fimqui = int(quinta[3]+quinta[4])

    insex = int(sexta[0]+sexta[1])
    fimsex = int(sexta[3]+sexta[4])

    insab = int(sabado[0]+sabado[1])
    fimsab = int(sabado[3]+sabado[4])

    indom = int(domingo[0]+domingo[1])
    fimdom = int(domingo[3]+domingo[4])

    CpfInstrutor = i.GetCpf()
    
    con = psycopg2.connect(database='sistema', user='postgres', password='henry')
    cur = con.cursor()
    cur.execute("UPDATE instrutor SET inseg = %d WHERE cpf = '%s';"%(inseg, CpfInstrutor))
    con.commit()
    cur.execute("UPDATE instrutor SET fimseg = %d WHERE cpf = '%s';"%(fimseg, CpfInstrutor))
    con.commit()
    cur.execute("UPDATE instrutor SET inter = %d WHERE cpf = '%s';"%(inter, CpfInstrutor))
    con.commit()
    cur.execute("UPDATE instrutor SET fimter = %d WHERE cpf = '%s';"%(fimter, CpfInstrutor))
    con.commit()
    cur.execute("UPDATE instrutor SET inqua = %d WHERE cpf = '%s';"%(inqua, CpfInstrutor))
    con.commit()
    cur.execute("UPDATE instrutor SET fimqua = %d WHERE cpf = '%s';"%(fimqua, CpfInstrutor))
    con.commit()
    cur.execute("UPDATE instrutor SET inqui = %d WHERE cpf = '%s';"%(inqui, CpfInstrutor))
    con.commit()
    cur.execute("UPDATE instrutor SET fimqui = %d WHERE cpf = '%s';"%(fimqui, CpfInstrutor))
    con.commit()
    cur.execute("UPDATE instrutor SET insex = %d WHERE cpf = '%s';"%(insex, CpfInstrutor))
    con.commit()
    cur.execute("UPDATE instrutor SET fimsex = %d WHERE cpf = '%s';"%(fimsex, CpfInstrutor))
    con.commit()
    cur.execute("UPDATE instrutor SET insab = %d WHERE cpf = '%s';"%(insab, CpfInstrutor))
    con.commit()
    cur.execute("UPDATE instrutor SET fimsab = %d WHERE cpf = '%s';"%(fimsab, CpfInstrutor))
    con.commit()
    cur.execute("UPDATE instrutor SET indom = %d WHERE cpf = '%s';"%(indom, CpfInstrutor))
    con.commit()
    cur.execute("UPDATE instrutor SET fimdom = %d WHERE cpf = '%s';"%(fimdom, CpfInstrutor))
    con.commit()
    con.close()
    
    QMessageBox.about(Teladisponibilidadeinstrutor, "Aviso", "Os Horários foram alterados com sucesso")
    Teladisponibilidadeinstrutor.hide()
    TelaprincipalInstrutor.show()


def MarcarAula():
    
    Data = Telamarcaraula.calendarWidget.selectedDate().toPyDate()
    DiaSemana = Data.weekday()
    HoraInicio = Telamarcaraula.lineEdit.text()
    HoraFinal = Telamarcaraula.lineEdit_2.text()
    Instrutor = Telamarcaraula.comboBox.text()
    print (Data)
    if DiaSemana == 0:
        con = psycopg2.connect(database='sistema', user='postgres', password='henry')
        cur = con.cursor()
        Resultado = cur.execute("SELECT inseg, fimseg FROM instrutor WHERE cpfaluno = '%s' "%(a.GetCpf()))

        print (Resultado)
        con.commit()
        con.close()

    Telamarcaraula.hide()
    Telaprincipalaluno.show()
    return "Aulas marcadas com sucesso"

    con = psycopg2.connect(database='sistema', user='postgres', password='henry')
    cur = con.cur()
    for i in range

#CpfAluno, inseg, fimseg, inter, fimter, inqua, fimqua, inqui, fimqui, insex, fimsex, insab, fimsab, indom, fimdom
    
def LoginInstrutor():

    Cpf   = Telainstrutorlogin.lineEdit.text()
    Senha = Telainstrutorlogin.lineEdit_2.text()

	#1 Sucesso
	#2 Cpf não cadastrado
	#3 Senha errada

    con = psycopg2.connect(database='sistema', user='postgres', password='henry')
    cur = con.cursor()
    cur.execute("select cpf,senha from instrutor where cpf='%s';"%(Cpf))
    l = cur.fetchall()
    con.close()

    if(len(l)==0):
        QMessageBox.about(Telainstrutorlogin, "Aviso", "Este CPF não foi cadastrado")
        return 2

    if(Senha != l[0][1]):
        QMessageBox.about(Telainstrutorlogin, "Aviso", "Voce digitou a senha errada")
        return 3

    Telainstrutorlogin.hide()
    TelaprincipalInstrutor.show()
    i.SetCpf(Cpf)
    return 1

def LoginAluno():

    Cpf   = Telaalunologin.lineEdit.text()
    Senha = Telaalunologin.lineEdit_2.text()

	#1 Sucesso
	#2 Cpf não cadastrado
	#3 Senha errada

    con = psycopg2.connect(database='sistema', user='postgres', password='henry')
    cur = con.cursor()
    cur.execute("select cpf,senha from aluno where cpf='%s';"%(Cpf))
    l = cur.fetchall()
    con.close()

    if(len(l)==0):
        QMessageBox.about(Telaalunologin, "Aviso", "Este CPF não foi cadastrado")
        return 2

    if(Senha != l[0][1]):
        QMessageBox.about(Telaalunologin, "Aviso", "Voce digitou a senha errada")
        return 3

    Telaalunologin.hide()
    Telaalunologin.show() 
    a.SetCpf(Cpf)
    return 1


def AlterarCadastroInstrutor():

    Nome = Telaalterarcadastroinstrutor.lineEdit.text()
    Cpf = Telaalterarcadastroinstrutor.lineEdit_2.text()
    CpfdoAluno = Telaalterarcadastroinstrutor.lineEdit_5.text()
    Graduacao = Telaalterarcadastroinstrutor.lineEdit_4.text()
    Senha = Telaalterarcadastroinstrutor.lineEdit_6.text()
    Data = Telaalterarcadastroinstrutor.calendarWidget.selectedDate()
    DiaNascimento = Data.day()
    MesNascimento = Data.month()
    AnoNascimento = Data.year()


    con = psycopg2.connect(database='sistema', user='postgres', password='henry')
    cur = con.cursor()
    cur.execute("UPDATE instrutor SET nome = '%s', cpf  = '%s', cpfaluno = '%s', graduacao = '%s', senha = '%s', dianascimento = '%i', mesnascimento = '%i', anonascimento = '%i' WHERE cpf = '%s' "%(Nome, Cpf, CpfdoAluno, Graduacao, Senha, DiaNascimento, MesNascimento, AnoNascimento, i.GetCpf()))
    con.commit()
    con.close()
    Telaalterarcadastroinstrutor.hide()
    Telainstrutorlogincadastro.show()
    return "Alterações feitas com sucesso"

def RemoverContaInstrutor():

    con = psycopg2.connect(database='sistema', user='postgres', password='henry')
    cur = con.cursor()
    cur.execute("DELETE FROM instrutor WHERE cpf = '%s' "%(i.GetCpf()))
    con.commit()
    con.close()
    TelaprincipalInstrutor.hide()
    Telainstrutorlogincadastro.show()
    return "Instrutor removido com sucesso"

def AlterarCadastroAluno():

    Nome = Telaalterarcadastroaluno.lineEdit.text()
    Cpf = Telaalterarcadastroinstrutor.lineEdit_2.text()
    Endereco = Telaalterarcadastroaluno.lineEdit_3.text()
    NumeroContato = Telaalterarcadastroaluno.lineEdit_4.text()
    Senha = Telaalterarcadastroaluno.lineEdit_5.text()
    Data = Telaalterarcadastroaluno.calendarWidget.selectedDate()
    DiaNascimento = Data.day()
    MesNascimento = Data.month()
    AnoNascimento = Data.year()

    con = psycopg2.connect(database='sistema', user='postgres', password='henry')
    cur = con.cursor()
    cur.execute("UPDATE aluno SET nome = '%s', cpf  = '%s', endereco = '%s', numerocontato = '%s', senha = '%s', dianascimento = '%i', mesnascimento = '%i', anonascimento = '%i' WHERE cpf = '%s' "%(Nome, Cpf, Endereco, NumeroContato, Senha, DiaNascimento, MesNascimento, AnoNascimento, a.GetCpf()))
    con.commit()
    con.close()
    Telaalterarcadastroaluno.hide()
    Telaalunologincadastro.show()
    return "Alterações feitas com sucesso"

def RemoverContaAluno():

    con = psycopg2.connect(database='sistema', user='postgres', password='henry')
    cur = con.cursor()
    cur.execute("DELETE FROM aluno WHERE cpf = '%s' "%(a.GetCpf()))
    con.commit()
    con.close()
    Telaprincipalaluno.hide()
    Telaalunologincadastro.show()
    return "Instrutor removido com sucesso"

def PrincipalDisponibilidade():
    TelaprincipalInstrutor.hide()
    Teladisponibilidadeinstrutor.show()

def PrincipalAlterar():
    TelaprincipalInstrutor.hide()
    Telaalterarcadastroinstrutor.show()
    
#cria a aplicação
app = QtWidgets.QApplication([])

#carrega todas as telas criadas
#exemplo
primeiratela     = uic.loadUi("Telas/primeiratela.ui")
Telaalunologin     = uic.loadUi("Telas/Telaalunologin.ui")
Telaalunologincadastro     = uic.loadUi("Telas/Telaalunologincadastro.ui")
Telaaluno     = uic.loadUi("Telas/Telaaluno.ui")
Telainstrutorlogin     = uic.loadUi("Telas/Telainstrutorlogin.ui")
Telainstrutorlogincadastro     = uic.loadUi("Telas/Telainstrutorlogincadastro.ui")
Telainstrutor     = uic.loadUi("Telas/Telainstrutor.ui")
Telamarcaraula     = uic.loadUi("Telas/Telamarcaraula.ui")
Telaprincipalaluno     = uic.loadUi("Telas/Telaprincipalaluno.ui")
TelaprincipalInstrutor     = uic.loadUi("Telas/TelaprincipalInstrutor.ui")
Teladisponibilidadeinstrutor = uic.loadUi("Telas/Teladisponibilidadeinstrutor.ui")
Telamarcaraula = uic.loadUi("Telas/Telamarcaraula.ui")
Telaalterarcadastroinstrutor = uic.loadUi("Telas/Telaalterarcadastroinstrutor.ui")
Telaalterarcadastroaluno = uic.loadUi("Telas/Telaalterarcadastroaluno.ui")

primeiratela.pushButton.clicked.connect(EscolherUsuario)

Telainstrutorlogincadastro.pushButton.clicked.connect(detelaescolhainstrutorparatelacadastroinstrutor)
Telainstrutorlogincadastro.pushButton_2.clicked.connect(detelaescolhainstrutorparatelalogininstrutor)

Telaalunologincadastro.pushButton.clicked.connect(detelaescolhaalunoparatelacadastroaluno)
Telaalunologincadastro.pushButton_2.clicked.connect(detelaescolhaalunoparatelaloginaluno)

Telaalterarcadastroinstrutor.pushButton.clicked.connect(detelaalterarcadastroinstrutorparatelainstrutorlogincadastro)

Telaprincipalaluno.pushButton_2.clicked.connect(detelaprincipalalunoparatelaalterarcadastroaluno)

Telainstrutor.pushButton.clicked.connect(CadastroInstrutor)

Telaaluno.pushButton.clicked.connect(CadastroAluno)

Telainstrutorlogin.pushButton.clicked.connect(LoginInstrutor)

Telaalunologin.pushButton.clicked.connect(LoginAluno)

TelaprincipalInstrutor.pushButton.clicked.connect(PrincipalDisponibilidade)
TelaprincipalInstrutor.pushButton_2.clicked.connect(PrincipalAlterar)

Teladisponibilidadeinstrutor.pushButton.clicked.connect(DisponibilidadeInstrutor)

Telaalterarcadastroinstrutor.pushButton.clicked.connect(AlterarCadastroInstrutor)

Telaalterarcadastroaluno.pushButton.clicked.connect(AlterarCadastroAluno)

TelaprincipalInstrutor.pushButton_3.clicked.connect(RemoverContaInstrutor)

Telaprincipalaluno.pushButton_3.clicked.connect(RemoverContaAluno)

Telamarcaraula.pushButton.clicked.connect(MarcarAula)

Telaalunologin.pushButton.clicked.connect(detelaalunologinparatelaprincipalaluno)

Telaprincipalaluno.pushButton.clicked.connect(detelaprincipalalunoparatelamarcaraula)

i = Instrutor("", "", "", "", "", "", [])
#cria o instrutor que está usando o programa

a = Aluno("", "", "", "", "", "", "", "")
#cria o aluno que está usando o programa

#chama a tela em que o programa deve começar
primeiratela.show()

#começa o programa
app.exec()



