import random
from datetime import datetime, timedelta

class Node:
    def __init__(self, label):
        self.label = label
        self._parent = None
        self._left = None
        self._right = None
        self.height = 1

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node
        if node is not None:
            node._parent = self

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node
        if node is not None:
            node._parent = self

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        self._parent = node
        self.update_height()

    def update_height(self):
        left_height = self._left.height if self._left else 0
        right_height = self._right.height if self._right else 0
        self.height = 1 + max(left_height, right_height)

class TemperatureNode:
    def __init__(self, temperatura, fecha):
        self.temperatura = temperatura
        self.fecha = fecha
        # Agregar otras propiedades necesarias


class AVL:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        node = value
        if self.root is None:
            self.root = node
            self.size = 1
        else:
            self._insert_node(self.root, node)
            self.size += 1

    def _insert_node(self, curr_node, new_node):
        if new_node.label < curr_node.label:
            if curr_node.left is None:
                curr_node.left = new_node
                new_node.parent = curr_node
            else:
                self._insert_node(curr_node.left, new_node)
        else:
            if curr_node.right is None:
                curr_node.right = new_node
                new_node.parent = curr_node
            else:
                self._insert_node(curr_node.right, new_node)
        self.rebalance(curr_node)

    def rebalance(self, node):
        while node:
            node.update_height()
            balance_factor = self.get_balance(node)

            if balance_factor > 1:
                if self.get_balance(node.left) < 0:
                    node.left = self.rotate_left(node.left)
                node = self.rotate_right(node)

            elif balance_factor < -1:
                if self.get_balance(node.right) > 0:
                    node.right = self.rotate_right(node.right)
                node = self.rotate_left(node)

            node = node.parent

    def get_balance(self, node):
        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0
        return left_height - right_height

    def rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left:
            right_child.left.parent = node
        right_child.parent = node.parent
        if not node.parent:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child
        node.update_height()
        right_child.update_height()

    def rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right:
            left_child.right.parent = node
        left_child.parent = node.parent
        if not node.parent:
            self.root = left_child
        elif node == node.parent.left:
            node.parent.left = left_child
        else:
            node.parent.right = left_child
        left_child.right = node
        node.parent = left_child
        node.update_height()
        left_child.update_height()

    def search(self, node, date):
        if node is None or node.label == date:
            return node
        elif date < node.label:
            return self.search(node.left, date)
        else:
            return self.search(node.right, date)

    def delete(self, date):
        self.root = self._delete_node(self.root, date)

    def _delete_node(self, node, date):
        if node is None:
            return node

        if date < node.label:
            node.left = self._delete_node(node.left, date)
        elif date > node.label:
            node.right = self._delete_node(node.right, date)
        else:
            if node.left is None or node.right is None:
                temp = node.left if node.left else node.right
                node = temp
            else:
                temp = self.get_min_value_node(node.right)
                node.label = temp.label
                node.temperature = temp.temperature
                node.right = self._delete_node(node.right, temp.label)

        if node is None:
            return node

        node.update_height()
        balance_factor = self.get_balance(node)

        if balance_factor > 1:
            if self.get_balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance_factor < -1:
            if self.get_balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def get_min_value_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def range_search(self, node, start_date, end_date, result):
        if node is None:
            return
        if start_date <= node.label:
            self.range_search(node.left, start_date, end_date, result)
        if start_date <= node.label <= end_date:
            result.append(node)
        if end_date >= node.label:
            self.range_search(node.right, start_date, end_date, result)

            #aca termina el arbol y su balanceo 

class Temperaturas_DB:
    def __init__(self):
        self.tree = AVL()

    def guardar_temperatura(self, temperatura, fecha):
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        nuevo_nodo = TemperatureNode(temperatura, fecha_dt)
        self.tree.insert(nuevo_nodo)

    def devolver_temperatura(self, fecha):
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        nodo = self.tree.search(self.tree.root, fecha_dt)
        return nodo.temperature if nodo else None

    def borrar_temperatura(self, fecha):
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        self.tree.delete(fecha_dt)

    def devolver_temperaturas(self, fecha1, fecha2):
        fecha_dt1 = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha_dt2 = datetime.strptime(fecha2, "%d/%m/%Y")
        temperaturas = []
        self.tree.range_search(self.tree.root, fecha_dt1, fecha_dt2, temperaturas)
        return [f"{nodo.label.strftime('%d/%m/%Y')}: {nodo.temperature} ºC" for nodo in temperaturas]

    def max_temp_rango(self, fecha1, fecha2):
        fecha_dt1 = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha_dt2 = datetime.strptime(fecha2, "%d/%m/%Y")
        temperaturas = []
        self.tree.range_search(self.tree.root, fecha_dt1, fecha_dt2, temperaturas)
        return max(nodo.temperature for nodo in temperaturas) if temperaturas else None

    def min_temp_rango(self, fecha1, fecha2):
        fecha_dt1 = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha_dt2 = datetime.strptime(fecha2, "%d/%m/%Y")
        temperaturas = []
        self.tree.range_search(self.tree.root, fecha_dt1, fecha_dt2, temperaturas)
        return min(nodo.temperature for nodo in temperaturas) if temperaturas else None

    def temp_extremos_rango(self, fecha1, fecha2):
        fecha_dt1 = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha_dt2 = datetime.strptime(fecha2, "%d/%m/%Y")
        temperaturas = []
        self.tree.range_search(self.tree.root, fecha_dt1, fecha_dt2, temperaturas)
        if temperaturas:
            return (min(nodo.temperature for nodo in temperaturas), 
                    max(nodo.temperature for nodo in temperaturas))
        return None

    def cantidad_muestras(self):
        return self.tree.size

# Función para generar fechas aleatorias
def generar_fechas_aleatorias(n, start_date, end_date):
    fechas = []
    delta = end_date - start_date
    for _ in range(n):
        random_days = random.randint(0, delta.days)
        random_date = start_date + timedelta(days=random_days)
        fechas.append(random_date.strftime("%d/%m/%Y"))
    return fechas

