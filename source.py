import csv

# CODIGO,NOMBRE,CRÉDITOS,REQUISITOS,NIVEL,CICLO,BACHILLERATO
class Curso:
    def __init__(self, codigo, nombre, creditos, requisitos, nivel, ciclo, bachillerato) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.requisitos = requisitos
        self.nivel = nivel
        self.ciclo = ciclo
        self.bachillerato = bachillerato

    def __repr__(self) -> str:
        return f"Curso({self.codigo}, {self.nombre}, {self.creditos}, {self.requisitos}, {self.nivel}, {self.ciclo}, {self.bachillerato})"

    def __str__(self) -> str:
        return f"[{self.codigo}]({self.nombre})"

