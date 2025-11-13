class Veiculo:
    def __init__(self, marca, modelo, velocidademax):
        self.marca = marca
        self.modelo = modelo
        self.__velocidademax = velocidademax   #    protegido
        self.__codigointerno = 'ABC123' # privado

    def _calcular_desempenho(self):
        #   método protegido, ocultar a complexidade
        return f"O veículo pode atingir até {self.__velocidademax} km/h"
    
    def mostrarinfos(self):
        #   interface pública que abstrai os detalhes internos
        desempenho = self._calcular_desempenho()
        return f"Marca: {self.marca}, Modelo: {self.modelo}, {desempenho}"
    def __metodoprivado(self):
        return "Esse método é privado."
    
#   leitura dos dados pelo user
marca = input("Insira a marca do veículo: ")
modelo = input("Insira o modelo do veículo: ")
velocidademax = float(input("Insira a velocidade máxima do veículo: "))
veiculo = Veiculo(marca, modelo, velocidademax)
print(veiculo.mostrarinfos())

#   método PROTEGIDO = apenas UM underline (_) - destinado ao uso interno da classe ou subclasse, ou seja, pode ser puxado FORA da classe
#   método PRIVADO = tem DOIS underlines (__) - dificulta o acesso acidental ou externo direto ao método 