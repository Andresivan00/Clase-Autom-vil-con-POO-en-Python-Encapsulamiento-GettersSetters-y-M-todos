# Definimos la clase Automovil, que representa un automóvil con atributos y comportamientos
class Automovil: 
    # Constructor (__init__) se ejecuta al crear un objeto de la clase Automovil
    # Inicializa los atributos del automóvil con los valores pasados como parámetros
    def __init__(self, marca, modelo, motor, numPuertas, cantAsientos, velMaxima, color, velActual, tipoCombustible, tipoAutomovil):
        self._marca = marca                # Marca del automóvil (ej. Toyota)
        self._modelo = modelo              # Modelo del automóvil (ej. 2025)
        self._motor = motor                # Motor (ej. 2 litros)
        self._numPuertas = numPuertas      # Número de puertas
        self._cantAsientos = cantAsientos  # Cantidad de asientos
        self._velMaxima = velMaxima        # Velocidad máxima
        self._color = color                # Color del automóvil
        self._velActual = velActual        # Velocidad actual del automóvil
        self._tipoCombustible = tipoCombustible  # Tipo de combustible (ej: Gasolina, Diésel, Eléctrico)
        self._tipoAutomovil = tipoAutomovil      # Tipo de automóvil (ej: SUV, Sedán, Deportivo)

    # ----- MÉTODOS GETTER Y SETTER -----
    # Estos métodos permiten obtener (get) o modificar (set) los atributos privados del automóvil
    
    def get_marca(self):  # Devuelve la marca
        return self._marca
    
    def set_marca(self, marca):  # Cambia la marca
        self._marca = marca
    
    def get_modelo(self):  # Devuelve el modelo
        return self._modelo
    
    def set_modelo(self, modelo):  # Cambia el modelo
        self._modelo = modelo
    
    def get_motor(self):  # Devuelve el motor
        return self._motor
    
    def set_motor(self, motor):  # Cambia el motor
        self._motor = motor
    
    def get_numPuertas(self):  # Devuelve el número de puertas
        return self._numPuertas
    
    def set_numPuertas(self, numPuertas):  # Cambia el número de puertas
        self._numPuertas = numPuertas
    
    def get_cantAsientos(self):  # Devuelve la cantidad de asientos
        return self._cantAsientos
    
    def set_cantAsientos(self, cantAsientos):  # Cambia la cantidad de asientos
        self._cantAsientos = cantAsientos
    
    def get_velMaxima(self):  # Devuelve la velocidad máxima
        return self._velMaxima
    
    def set_velMaxima(self, velMaxima):  # Cambia la velocidad máxima
        self._velMaxima = velMaxima
    
    def get_color(self):  # Devuelve el color
        return self._color
    
    def set_color(self, color):  # Cambia el color
        self._color = color
    
    def get_velActual(self):  # Devuelve la velocidad actual
        return self._velActual   
    
    def set_velActual(self, velActual):  # Cambia la velocidad actual
        self._velActual = velActual
        
    # Devuelve el tipo de combustible
    def get_tipoCombustible(self):
        return self._tipoCombustible

    # Devuelve el tipo de automóvil
    def get_tipoAutomovil(self):
        return self._tipoAutomovil
    
    # Permite cambiar el tipo de combustible
    def set_tipoCombustible(self, tipoCombustible):
        self._tipoCombustible = tipoCombustible

    # Permite cambiar el tipo de automóvil
    def set_tipoAutomovil(self, tipoAutomovil):
        self._tipoAutomovil = tipoAutomovil


        
    # ----- MÉTODOS DE COMPORTAMIENTO -----
    # Acciones que puede realizar el automóvil
    
    
    def acelerar(self, incremento):
        # Aumenta la velocidad actual en la cantidad indicada
        self._velActual = self._velActual + incremento
        
    def desacelerar(self, decremento):
        # Disminuye la velocidad actual en la cantidad indicada
        self._velActual = self._velActual - decremento
        
    def frenar(self):
        # Detiene completamente el automóvil (velocidad = 0)
        self._velActual = 0
        
    def tiempoLlegada(self, distancia):
        # Calcula el tiempo de llegada en función de la velocidad actual y la distancia
        # Fórmula: tiempo = distancia / velocidad
        if self._velActual > 0:
            tiempo = distancia / self._velActual
            return tiempo
        else:
            return float('inf')  # Si está detenido, el tiempo de llegada es infinito
    
    def imprimir(self):
        # Muestra en formato de texto la información principal del automóvil
        return f'''La marca es: {self._marca}
                    El modelo es: {self._modelo}
                    El color es: {self._color}
                    La velocidad actual es: {self._velActual}
                    La velocidad máxima es: {self._velMaxima}
                    La cantidad de asientos es: {self._cantAsientos}
                    El motor es: {self._motor}
                    El tipo de combustible es: {self._tipoCombustible}
                    El tipo de automóvil es: {self._tipoAutomovil}
    '''

# ----- PROGRAMA PRINCIPAL -----
# Creamos un objeto 'a' de la clase Automovil con datos iniciales
a = Automovil("Toyota", "2025", 2, 5, 7, 300, "Blanco", 80, "Gasolina", "SUV")

# Imprimimos la información inicial del automóvil
print(a.imprimir())

# Cambiamos el modelo con un setter y lo mostramos con el getter
a.set_modelo(2006)
print("El nuevo modelo es: ", a.get_modelo())

# Cambiar el tipo de combustible usando el SET
a.set_tipoCombustible("Eléctrico")
print("El nuevo tipo de combustible es:", a.get_tipoCombustible())

# Aceleramos el automóvil +20 km/h
a.acelerar(20) 
print("Nueva velocidad:", a.get_velActual())

# Desaceleramos el automóvil -10 km/h
a.desacelerar(10) 
print("Nueva velocidad:", a.get_velActual())

# Calculamos el tiempo de llegada a un lugar a 13 km de distancia
print("Tiempo de llegada al Buenavista:", a.tiempoLlegada(13))

# Frenamos el automóvil (velocidad = 0)
a.frenar()
print(a.imprimir())
