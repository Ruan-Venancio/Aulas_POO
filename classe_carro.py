class Carro:
    
    def __init__(self, modelo, ano, cor, velocidade_max):
        self.modelo = modelo
        self.ano = ano 
        self.cor = cor 
        self.vel = 0
        self.vel_max = velocidade_max
    
    
    def imprimir(self):
        print(f"\nModelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        print(f"Velocidade atual: {self.vel}")
        print(f"Velocidade Maxíma: {self.vel_max}")
    
    def acelerar(self,velocidade_modificada):
        
        try:
            int(velocidade_modificada)
        except:
            print("Entre com um número")
        else:

            velocidade_modificada = int(velocidade_modificada)

            if self.vel == self.vel_max:
                print("Velocidade está no maxímo")
            elif velocidade_modificada > self.vel_max:
                print("Velocidade acima que a maxíma")
            else:
                self.vel += velocidade_modificada
    
    def parar(self):
        if self.vel == 0:
            print("O carro já está parado")
        else:
            self.vel = 0

toyota = Carro("rapido", 1917, "silver", 360)