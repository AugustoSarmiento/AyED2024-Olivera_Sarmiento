from datetime import datetime

class Node:
    def __init__(self, date, temperature):
        self.date = date
        self.temperature = temperature
        self.left = None
        self.right = None
        self.height = 1

class Temperaturas_DB:
    def __init__(self):
        self.root = None

    def guardar_temperatura(self, temperatura, fecha):
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        self.root = self.insert(self.root, fecha_dt, temperatura)

    def devolver_temperatura(self, fecha):
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        return self.search(self.root, fecha_dt)

    def max_temp_rango(self, fecha1, fecha2):
        fecha1_dt = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_dt = datetime.strptime(fecha2, "%d/%m/%Y")
        return self.range_max(self.root, fecha1_dt, fecha2_dt, float('-inf'))

    def min_temp_rango(self, fecha1, fecha2):
        fecha1_dt = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_dt = datetime.strptime(fecha2, "%d/%m/%Y")
        return self.range_min(self.root, fecha1_dt, fecha2_dt, float('inf'))

    def temp_extremos_rango(self, fecha1, fecha2):
        max_temp = self.max_temp_rango(fecha1, fecha2)
        min_temp = self.min_temp_rango(fecha1, fecha2)
        return min_temp, max_temp

    def borrar_temperatura(self, fecha):
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        self.root = self.delete(self.root, fecha_dt)

    def devolver_temperaturas(self, fecha1, fecha2):
        fecha1_dt = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_dt = datetime.strptime(fecha2, "%d/%m/%Y")
        temperaturas = []
        self.range_search(self.root, fecha1_dt, fecha2_dt, temperaturas)
        return temperaturas

    def cantidad_muestras(self):
        return self.count_nodes(self.root)

    # Métodos auxiliares internos para el AVL y operaciones de rango

    def insert(self, root, date, temperature):
        if not root:
            return Node(date, temperature)

        if date < root.date:
            root.left = self.insert(root.left, date, temperature)
        elif date > root.date:
            root.right = self.insert(root.right, date, temperature)
        else:
            raise ValueError("Ya existe una temperatura registrada en esa fecha.")

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and date < root.left.date:
            return self.right_rotate(root)
        if balance < -1 and date > root.right.date:
            return self.left_rotate(root)
        if balance > 1 and date > root.left.date:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and date < root.right.date:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, date):
        if not root:
            return root

        if date < root.date:
            root.left = self.delete(root.left, date)
        elif date > root.date:
            root.right = self.delete(root.right, date)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = self.get_min_value_node(root.right)
            root.date, root.temperature = temp.date, temp.temperature
            root.right = self.delete(root.right, temp.date)

        if not root:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def search(self, root, date):
        if not root:
            return None
        if root.date == date:
            return root.temperature
        elif date < root.date:
            return self.search(root.left, date)
        else:
            return self.search(root.right, date)

    def range_search(self, root, fecha1, fecha2, temperaturas):
        if not root:
            return
        if fecha1 <= root.date <= fecha2:
            temperaturas.append(f"{root.date.strftime('%d/%m/%Y')}: {root.temperature} ºC")
        if fecha1 < root.date:
            self.range_search(root.left, fecha1, fecha2, temperaturas)
        if root.date < fecha2:
            self.range_search(root.right, fecha1, fecha2, temperaturas)

    def range_max(self, root, fecha1, fecha2, max_val):
        if not root:
            return max_val
        if fecha1 <= root.date <= fecha2:
            max_val = max(max_val, root.temperature)
        if fecha1 < root.date:
            max_val = self.range_max(root.left, fecha1, fecha2, max_val)
        if root.date < fecha2:
            max_val = self.range_max(root.right, fecha1, fecha2, max_val)
        return max_val

    def range_min(self, root, fecha1, fecha2, min_val):
        if not root:
            return min_val
        if fecha1 <= root.date <= fecha2:
            min_val = min(min_val, root.temperature)
        if fecha1 < root.date:
            min_val = self.range_min(root.left, fecha1, fecha2, min_val)
        if root.date < fecha2:
            min_val = self.range_min(root.right, fecha1, fecha2, min_val)
        return min_val

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def get_min_value_node(self, root):
        while root.left:
            root = root.left
        return root

    def count_nodes(self, root):
        if not root:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)
