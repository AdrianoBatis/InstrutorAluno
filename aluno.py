class Aluno:
    def __init__(self, Nome, Cpf, DiaNascimento,MesNascimento, AnoNascimento, Endereco, NumeroContato, FormaPagamento):
        self.Nome = Nome
        self.Cpf = Cpf
        self.DataNascimento = DataNascimento
        self.Endereco = Endereco
        self.NumeroContato = NumeroContato
        self.FormaPagamento = FormaPagamento

    def SetNome(self, Nome):
        self.Nome = Nome

    def GetNome(self):
        return self.Nome

    def SetCpf(self, Cpf):
        self.Cpf = Cpf

    def GetCpf(self):
        return self.Cpf

    def SetDiaNascimento(self, DiaNascimento):
        self.DiaNascimento = DiaNascimento

    def GetDiaNascimento(self):
        return self.DiaNascimento

    def SetMesNascimento(self, MesNascimento):
        self.MesNascimento = MesNascimento

    def GetMesNascimento(self):
        return self.MesNascimento

    def SetAnoNascimento(self, AnoNascimento):
        self.AnoNascimento = AnoNascimento

    def GetAnoNascimento(self):
        return self.AnoNascimento

    def SetEndereco(self, Endereco):
        self.Endereco = Endereco

    def GetEndereco(self):
        return self.Endereco

    def SetNumeroContato(self, NumeroContato):
        self.NumeroContato = NumeroContato

    def GetNumeroContato(self):
        return self.NumeroContato
    
    def SetFormaPagamento(self, FormaPagamento):
        self.FormaPagamento = FormaPagamento

    def GetFormaPagamento(self):
        return self.FormaPagamento
