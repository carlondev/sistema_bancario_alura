

class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...")
        self.__numero = numero
        self.__titular = titular.capitalize()
        self.__saldo = saldo
        self.__limite = limite
        
    def extrato(self):
        print("Saldo de R${:.2f} do titular {}".format(self.__saldo, self.__titular))
    
    def depositar(self, valor):
        self.__saldo += valor
        print("Você depositou R${:.2f} na conta de {}".format(valor, self.__titular))
        
    def __valor_a_sacar(self, valor_a_sacar):
        valor_total_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_total_disponivel
        
    def sacar(self, valor):
        if(self.__valor_a_sacar(valor)):
            self.__saldo -= valor
            print("Você sacou R${:.2f} da conta de {}".format(valor, self.__titular))
        else:
            print("O valor R${:.2f} é maior que o seu limite.".format(valor))
            print("Saque não permitido.")
        
    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property    
    def titular(self):
        return self.__titular
    
    @property    
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    
    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
    
    
        
    