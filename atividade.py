class ContaBancária:
    def __init__(self,saldo,numero,TipoConta):
            self.saldo = saldo
            self.numero = numero
            self.TipoConta = TipoConta
    def getSaldo(self):
          return (self.saldo)
    def setSaldo(self, saldo):
          self.saldo = saldo
    def getNumero(self):
          return (self.numero)
    def setNumero(self, numero):
          self.numero = numero
    def getTipoConta(self):
          return (self.TipoConta)
    def setTipoConta(self, TipoConta):
          self.TipoConta = TipoConta
    def verificar_situacao(self):
        if self.saldo > 0:
            print(f"O saldo da conta {self.numero} está positivo.")
        elif self.saldo < 0:
            print(f"O saldo da conta {self.numero} está negativo.")
        else:
            print(f"A conta {self.numero} está sem saldo.")
def executor():
    numero = int(input("Digite o número da conta: "))
    saldo = float(input("Digite o saldo inicial da conta: "))
    TipoConta = input("Digite o tipo de conta (corrente ou poupança): ")
    conta = ContaBancária(saldo, numero,TipoConta)
    conta.verificar_situacao()
    newsald = float(input("Digite o novo saldo para a conta: "))
    conta.setSaldo(newsald)
    print(f"O saldo atual da conta número {conta.getNumero()} é: {conta.getSaldo()} reais.")
    newbie = input("Digite o novo tipo de conta: ")
    conta.setTipoConta(newbie)
    print(f"O novo tipo de conta é: {conta.getTipoConta()}")
executor()