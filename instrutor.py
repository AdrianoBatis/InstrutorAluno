class Instrutor:
    
    def __init__(self, Nome, Cpf, DiaNascimento, MesNascimento, AnoNascimento, Graduacao, Horarios):
        self.Nome = Nome
        self.Cpf = Cpf
        self.DiaNascimento = DiaNascimento
        self.MesNascimento = MesNascimento
        self.AnoNascimento = AnoNascimento
        self.Graduacao = Graduacao
        self.Horarios = Horarios

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

    def SetGraduacao(self, Graduacao):
        self.Graduacao = Graduacao

    def GetGraduacao(self):
        return self.Graduacao

    def SetHorarios(self, Horarios):
        self.Horarios = Horarios

    def GetHorarios(self):
        return self.Horarios
