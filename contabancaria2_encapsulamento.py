class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor} realizado. ")
        else:
            print("Valor de depósito inválido.")
    def sacar (self,valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R$ {valor} realizado.")
    def versaldo(self):
        return f"O saldo disponível é de R$ {self.__saldo}"
    
conta = ContaBancaria("João", 500000)

print(conta.versaldo())

conta.depositar(50)

print(conta.versaldo())

conta.sacar(200)

conta.sacar(70)

print(conta.versaldo())
