class Entidad:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def __str__(self):
        return f"Entidad(nombre={self.nombre}, tipo={self.tipo})"

class Cliente(Entidad):
    def __init__(self, nombre, tipo, cedula, correo, saldo=0):
        super().__init__(nombre, tipo)
        self.cedula = cedula
        self.correo = correo
        self.saldo = saldo

    def __str__(self):
        return f"Cliente(nombre={self.nombre}, tipo={self.tipo}, cedula={self.cedula}, correo={self.correo}, saldo={self.saldo})"

    def actualizar_saldo(self, monto):
        try:
            if monto < 0 and abs(monto) > self.saldo:
                raise ValueError("Saldo insuficiente para realizar la operación.")
        except ValueError as e:
            return f"Error: {e}"
        else:
            self.saldo += monto
            return f"Saldo actualizado. Nuevo saldo: {self.saldo}"

class Servicio(Entidad):
    def __init__(self, nombre, tipo, descripcion, precio_hora, cliente, duracion, estado):
        super().__init__(nombre, tipo)
        self.descripcion = descripcion
        self.precio_hora = precio_hora
        self.cliente = cliente.cedula  # Guardamos la cédula del cliente en lugar del objeto completo
        self.duracion = duracion
        self.estado = estado

    def __str__(self):
        return f"Servicio(nombre={self.nombre}, tipo={self.tipo}, descripcion={self.descripcion}, precio_hora={self.precio_hora}, cliente={self.cliente}, duracion={self.duracion}, estado={self.estado})"

    def calcular_costo(self):
        return self.precio_hora * self.duracion

    def confirmar(self):
        reporte = f"Confirmando servicio: {self.nombre}, Tipo: {self.tipo}, Cédula del cliente: {self.cliente}, Estado actual: {self.estado}"
        try:
            if self.estado != "Pendiente":
                raise ValueError("El servicio no está en estado Pendiente.")
            for cliente in clientela:
                if cliente.cedula == self.cliente:
                    aux = cliente.saldo
                    break
            if aux < self.calcular_costo():
                raise ValueError("Saldo insuficiente para confirmar el servicio.")
        except ValueError as e:
            reporte += f"Error: {e}"
        else:
            self.estado = "Confirmado"
            aux -= self.calcular_costo()
            for cliente in clientela:
                if cliente.cedula == self.cliente:
                    cliente.saldo = aux  # Actualizamos el saldo del cliente en la lista
                    break
            reporte += f"Servicio confirmado. Nuevo saldo del cliente: {aux}"
        finally:
            with open("log.txt", "a", encoding="utf-8") as archivo_reporte:
                archivo_reporte.write(reporte + "\n")
        return reporte

    def cancelar(self):
        reporte = f"Cancelando servicio: {self.nombre}, Tipo: {self.tipo}, Cédula del cliente: {self.cliente}, Estado actual: {self.estado}"
        try:
            if self.estado != "Confirmado":
                raise ValueError("El servicio no está en estado Confirmado.")
        except ValueError as e:
            reporte += f"Error: {e}"
        else:
            self.estado = "Cancelado"
            for cliente in clientela:
                if cliente.cedula == self.cliente:
                    cliente.saldo += self.calcular_costo()
                    aux = cliente.saldo
                    break
            reporte += f"Servicio cancelado. Nuevo saldo del cliente: {aux}"
        finally:
            with open("log.txt", "a", encoding="utf-8") as archivo_reporte:
                archivo_reporte.write(reporte + "\n")
        return reporte
        

class Reserva(Servicio):
    def __init__(self, nombre, tipo, descripcion, precio_hora, cliente, duracion, estado):
        super().__init__(nombre, tipo, descripcion, precio_hora, cliente, duracion, estado)

    def __str__(self):
        return f"Reserva(nombre={self.nombre}, tipo={self.tipo}, descripcion={self.descripcion}, precio_hora={self.precio_hora}, cliente={self.cliente}, duracion={self.duracion}, estado={self.estado})"

    def calcular_costo(self):
        return super().calcular_costo() * 1.1  # Aplica un recargo del 10% para reservas

    def confirmar(self):
        reporte = f"Confirmando reserva: {self.nombre}, Tipo: {self.tipo}, Cédula del cliente: {self.cliente}, Estado actual: {self.estado}"
        try:
            if self.estado != "Pendiente":
                raise ValueError("La reserva no está en estado Pendiente.")
            for cliente in clientela:
                if cliente.cedula == self.cliente:
                    aux = cliente.saldo
                    break
            if aux < self.calcular_costo():
                raise ValueError("Saldo insuficiente para confirmar la reserva.")
        except ValueError as e:
            reporte += f"Error: {e}"
        else:
            self.estado = "Confirmado"
            aux -= self.calcular_costo()
            for cliente in clientela:
                if cliente.cedula == self.cliente:
                    cliente.saldo = aux  # Actualizamos el saldo del cliente en la lista
                    break
            reporte += f"Reserva confirmada. Nuevo saldo del cliente: {aux}"
        finally:
            with open("log.txt", "a", encoding="utf-8") as archivo_reporte:
                archivo_reporte.write(reporte + "\n")
        return reporte

    def cancelar(self):
        reporte = f"Cancelando reserva: {self.nombre}, Tipo: {self.tipo}, Cédula del cliente: {self.cliente}, Estado actual: {self.estado}"
        try:
            if self.estado != "Confirmado":
                raise ValueError("La reserva no está en estado Confirmado.")
        except ValueError as e:
            reporte += f"Error: {e}"
        else:
            self.estado = "Cancelado"
            for cliente in clientela:
                if cliente.cedula == self.cliente:
                    cliente.saldo += self.calcular_costo()
                    aux = cliente.saldo
                    break
            reporte += f"Reserva cancelada. Nuevo saldo del cliente: {aux}"
        finally:
            with open("log.txt", "a", encoding="utf-8") as archivo_reporte:
                archivo_reporte.write(reporte + "\n")
        return reporte

class Alquiler(Servicio):
    def __init__(self, nombre, tipo, descripcion, precio_hora, cliente, duracion, estado):
        super().__init__(nombre, tipo, descripcion, precio_hora, cliente, duracion, estado)

    def __str__(self):
        return f"Alquiler(nombre={self.nombre}, tipo={self.tipo}, descripcion={self.descripcion}, precio_hora={self.precio_hora}, cliente={self.cliente}, duracion={self.duracion}, estado={self.estado})"

    def calcular_costo(self):
        return super().calcular_costo() * 1.2  # Aplica un recargo del 20% para alquileres

    def confirmar(self):
        reporte = f"Confirmando alquiler: {self.nombre}, Tipo: {self.tipo}, Cédula del cliente: {self.cliente}, Estado actual: {self.estado}"
        try:
            if self.estado != "Pendiente":
                raise ValueError("El alquiler no está en estado Pendiente.")
            for cliente in clientela:
                if cliente.cedula == self.cliente:
                    aux = cliente.saldo
                    break
            if aux < self.calcular_costo():
                raise ValueError("Saldo insuficiente para confirmar el alquiler.")
        except ValueError as e:
            reporte += f"Error: {e}"
        else:
            self.estado = "Confirmado"
            aux -= self.calcular_costo()
            for cliente in clientela:
                if cliente.cedula == self.cliente:
                    cliente.saldo = aux  # Actualizamos el saldo del cliente en la lista
                    break
            reporte += f"Alquiler confirmado. Nuevo saldo del cliente: {aux}"
        finally:
            with open("log.txt", "a", encoding="utf-8") as archivo_reporte:
                archivo_reporte.write(reporte + "\n")
        return reporte

    def cancelar(self):
        reporte = f"Cancelando alquiler: {self.nombre}, Tipo: {self.tipo}, Cédula del cliente: {self.cliente}, Estado actual: {self.estado}"
        try:
            if self.estado != "Confirmado":
                raise ValueError("El alquiler no está en estado Confirmado.")
        except ValueError as e:
            reporte += f"Error: {e}"
        else:
            self.estado = "Cancelado"
            for cliente in clientela:
                if cliente.cedula == self.cliente:
                    cliente.saldo += self.calcular_costo()
                    aux = cliente.saldo
                    break
            reporte += f"Alquiler cancelado. Nuevo saldo del cliente: {aux}"
        finally:
            with open("log.txt", "a", encoding="utf-8") as archivo_reporte:
                archivo_reporte.write(reporte + "\n")
        return reporte

class Asesoria(Servicio):
    def __init__(self, nombre, tipo, descripcion, precio_hora, cliente, duracion, estado):
        super().__init__(nombre, tipo, descripcion, precio_hora, cliente, duracion, estado)

    def __str__(self):
        return f"Asesoria(nombre={self.nombre}, tipo={self.tipo}, descripcion={self.descripcion}, precio_hora={self.precio_hora}, cliente={self.cliente}, duracion={self.duracion}, estado={self.estado})"

    def confirmar(self):
        reporte = f"Confirmando asesoría: {self.nombre}, Tipo: {self.tipo}, Cédula del cliente: {self.cliente}, Estado actual: {self.estado}"
        try:
            if self.estado != "Pendiente":
                raise ValueError("La asesoría no está en estado Pendiente.")
            for cliente in clientela:
                if cliente.cedula == self.cliente:
                    aux = cliente.saldo
                    break
            if aux < self.calcular_costo():
                raise ValueError("Saldo insuficiente para confirmar la asesoría.")
        except ValueError as e:
            reporte += f"Error: {e}"
        else:
            self.estado = "Confirmado"
            aux -= self.calcular_costo()
            for cliente in clientela:
                if cliente.cedula == self.cliente:
                    cliente.saldo = aux
                    break
            reporte += f"Asesoría confirmada. Nuevo saldo del cliente: {aux}"
        finally:
            with open("log.txt", "a", encoding="utf-8") as archivo_reporte:
                archivo_reporte.write(reporte + "\n")
        return reporte

    def cancelar(self):
        reporte = f"Cancelando asesoría: {self.nombre}, Tipo: {self.tipo}, Cédula del cliente: {self.cliente}, Estado actual: {self.estado}"
        try:
            if self.estado != "Confirmado":
                raise ValueError("La asesoría no está en estado Confirmado.")
        except ValueError as e:
            reporte += f"Error: {e}"
        else:
            self.estado = "Cancelado"
            for cliente in clientela:
                if cliente.cedula == self.cliente:
                    cliente.saldo += self.calcular_costo()
                    aux = cliente.saldo
                    break
            reporte += f"Asesoría cancelada. Nuevo saldo del cliente: {aux}"
        finally:
            with open("log.txt", "a", encoding="utf-8") as archivo_reporte:
                archivo_reporte.write(reporte + "\n")
        return reporte

clientela=[]
servicios=[]

def agregar_cliente(nombre, tipo, cedula, correo, saldo=0):
    reporte = f"Agregando cliente: {nombre}, Tipo: {tipo}, Cédula: {cedula}, Correo: {correo}, Saldo: {saldo}"
    try:
        cedula_int = int(cedula)
        for cliente in clientela:
            if cliente.cedula == cedula_int:
                raise ValueError("Ya existe un cliente con esa cédula.")
    except ValueError as e:
        reporte += f"\nError: {e}"
    else:
        cliente = Cliente(nombre, tipo, cedula, correo, saldo)
        clientela.append(cliente)
        reporte += f"\nCliente agregado exitosamente: {cliente}"
    finally:
        with open("log.txt", "a", encoding="utf-8") as archivo_reporte:
            archivo_reporte.write(reporte + "\n")
        print(reporte)

def eliminar_cliente(cedula):
    reporte = f"Eliminando cliente con cédula: {cedula}"
    try:
        cedula_int = int(cedula)
        for cliente in clientela:
            if cliente.cedula == cedula_int:
                clientela.remove(cliente)
                reporte += f"\nCliente eliminado exitosamente: {cliente}"
                break
        else:
            raise ValueError("No se encontró un cliente con esa cédula.")
    except ValueError as e:
        reporte += f"\nError: {e}"
    finally:
        with open("log.txt", "a", encoding="utf-8") as archivo_reporte:
            archivo_reporte.write(reporte + "\n")
        print(reporte)

def actualizar_saldo_cliente(cedula, monto):
    reporte = f"Actualizando saldo del cliente con cédula: {cedula}, Monto: {monto}"
    try:
        cedula_int = int(cedula)
        for cliente in clientela:
            if cliente.cedula == cedula_int:
                resultado = cliente.actualizar_saldo(monto)
                reporte += f"\n{resultado}"
                break
        else:
            raise ValueError("No se encontró un cliente con esa cédula.")
    except ValueError as e:
        reporte += f"\nError: {e}"
    finally:
        with open("log.txt", "a", encoding="utf-8") as archivo_reporte:
            archivo_reporte.write(reporte + "\n")
        print(reporte)

def agregar_servicio(nombre, tipo, descripcion, precio_hora, cedula_cliente, duracion, estado):
    reporte = f"Agregando servicio: {nombre}, Tipo: {tipo}, Descripción: {descripcion}, Precio por hora: {precio_hora}, Cédula del cliente: {cedula_cliente}, Duración: {duracion}, Estado: {estado}"
    try:
        cedula_int = int(cedula_cliente)
        cliente_encontrado = None
        for cliente in clientela:
            if cliente.cedula == cedula_int:
                cliente_encontrado = cliente
                break
        if not cliente_encontrado:
            raise ValueError("No se encontró un cliente con esa cédula.")
        
        if tipo == "Reserva":
            servicio = Reserva(nombre, tipo, descripcion, precio_hora, cliente_encontrado, duracion, estado)
        elif tipo == "Alquiler":
            servicio = Alquiler(nombre, tipo, descripcion, precio_hora, cliente_encontrado, duracion, estado)
        elif tipo == "Asesoria":
            servicio = Asesoria(nombre, tipo, descripcion, precio_hora, cliente_encontrado, duracion, estado)
        else:
            raise ValueError("Tipo de servicio no válido. Debe ser 'Reserva', 'Alquiler' o 'Asesoria'.")
        
        servicios.append(servicio)
        reporte += f"\nServicio agregado exitosamente: {servicio}"
    except ValueError as e:
        reporte += f"\nError: {e}"
    finally:
        with open("log.txt", "a", encoding="utf-8") as archivo_reporte:
            archivo_reporte.write(reporte + "\n")
        print(reporte)

def eliminar_servicio(nombre):
    reporte = f"Eliminando servicio con nombre: {nombre}"
    try:
        for servicio in servicios:
            if servicio.nombre == nombre:
                servicios.remove(servicio)
                reporte += f"\nServicio eliminado exitosamente: {servicio}"
                break
        else:
            raise ValueError("No se encontró un servicio con ese nombre.")
    except ValueError as e:
        reporte += f"\nError: {e}"
    finally:
        with open("log.txt", "a", encoding="utf-8") as archivo_reporte:
            archivo_reporte.write(reporte + "\n")
        print(reporte)

def confirmar_servicio(nombre):
    reporte = f"Confirmando servicio con nombre: {nombre}"
    try:
        for servicio in servicios:
            if servicio.nombre == nombre:
                resultado = servicio.confirmar()
                reporte += f"\n{resultado}"
                break
        else:
            raise ValueError("No se encontró un servicio con ese nombre.")
    except ValueError as e:
        reporte += f"\nError: {e}"
    finally:
        with open("log.txt", "a", encoding="utf-8") as archivo_reporte:
            archivo_reporte.write(reporte + "\n")
        print(reporte)

def cancelar_servicio(nombre):
    reporte = f"Cancelando servicio con nombre: {nombre}"
    try:
        for servicio in servicios:
            if servicio.nombre == nombre:
                resultado = servicio.cancelar()
                reporte += f"\n{resultado}"
                break
        else:
            raise ValueError("No se encontró un servicio con ese nombre.")
    except ValueError as e:
        reporte += f"\nError: {e}"
    finally:
        with open("log.txt", "a", encoding="utf-8") as archivo_reporte:
            archivo_reporte.write(reporte + "\n")
        print(reporte)

def main():
    agregar_cliente("Juan Pérez", "Regular", 124875936, "juan@example.com")
    agregar_cliente("María López", "Premium", 124875936, "maria@example.com")
    agregar_servicio("Servicio de Reserva", "Reserva", "Reserva de sala de reuniones", 100, 124875936, 2, "Pendiente")
    confirmar_servicio("Servicio de Reserva")
    actualizar_saldo_cliente(124875936, 300)
    confirmar_servicio("Servicio de Reserva")
    cancelar_servicio("Servicio de Reserva")
    agregar_servicio("Servicio de Alquiler", "Alquiler", "Alquiler de equipo audiovisual", 150, 27356894, 3, "Pendiente")
    agregar_cliente("Pedro Gómez", "Regular", 27356894, "pedro@example.com")
    agregar_servicio("Servicio de Alquiler", "Alquiler", "Alquiler de equipo audiovisual", 150, 27356894, 3, "Pendiente")

main()