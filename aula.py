from instrutor import Instrutor

class Aula:

    def __init__(self, Id, DataAula, Instrutor, Inicio, Fim):
        self.Id = Id
        self.Data = DataAula
        self.Instrutor = Instrutor

    def SetId(self, Id):
        self.Id = Id

    def GetId(self):
        return self.Id

    def SetDataAula(self, DataAula):
        self.DataAula = DataAula

    def GetDataAula(self):
        return self.DataAula

    def SetInstrutor(self, Instrutor):
        self.Instrutor = Instrutor

    def GetInstrutor(self):
        return self.Instrutor

    def SetInicio(self, Inicio):
        self.Inicio = Inicio

    def GetInicio(self):
        return self.Inicio

    def SetFim(self, Fim):
        self.Fim = Fim

    def GetFim(self):
        return self.Fim
