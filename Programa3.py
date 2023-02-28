class Inventario:
    def __init__(self,referencia,cantidad):
        self.referencia=referencia
        self.cantidad=cantidad
    
    #Metodos 
    def ObtenerReferencia(self):
        return self.referencia
    def ObtenerCantidad(self):
        return self.cantidad
    
    def MostrarInventario(self):
        print("\nReferencia: "+self.ObtenerReferencia()+"\nCantidad:"+str(self.ObtenerCantidad()))
referencia= input("Favor de ingresar la referencia del producto: ")
cantidad= input("Favor de ingresar la cantidad: ")

x=Inventario(referencia,cantidad)
x.MostrarInventario()