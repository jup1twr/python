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
        return f"Marca: {self.marca}, Modelo {self.modelo}, {desempenho}"
    def __metodoprivado(self):
        return "Esse método é privado."
    
carro = Veiculo("Toyota", "Corolla", 180)
print(carro.mostrarinfos())
#   print(carro._calcular_desempenho) - ERRO, NÃO VAI FUNCIONAR!
#   método PROTEGIDO = apenas UM underline (_) - destinado ao uso interno da classe ou subclasse, ou seja, pode ser puxado FORA da classe
#   método PRIVADO = tem DOIS underlines (__) - dificulta o acesso acidental ou externo direto ao método 