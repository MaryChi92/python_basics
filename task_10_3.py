class Cell:

    def __init__(self, cellule):
        self.cellule = int(cellule)

    def __add__(self, other):
        total_cellule = self.cellule + other.cellule
        return total_cellule

    def __sub__(self, other):
        if self.cellule > other.cellule:
            dif_cellule = self.cellule - other.cellule
        else:
            dif_cellule = 'Разность количества ячеек двух клеток не может быть меньше нуля'
        return dif_cellule

    def __mul__(self, other):
        new_cell_mul = Cell(self.cellule * other.cellule)
        return new_cell_mul

    def __floordiv__(self, other):
        new_cell_div = Cell(self.cellule // other.cellule) if self.cellule > other.cellule else Cell(other.cellule // self.cellule)
        return new_cell_div

    def __str__(self):
        return f'{self.cellule}'

    def make_order(self, cell_in_row):
        rows = ''
        for i in range(self.cellule // cell_in_row):
            rows += f'{"*" * cell_in_row} \n'
        rows += '*' * (self.cellule % cell_in_row)
        return rows


c_1 = Cell(5)
c_2 = Cell(16)

print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 // c_2)
print(c_2.make_order(3))
