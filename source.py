import csv

# CODIGO,NOMBRE,CREDITOS,REQUISITOS,NIVEL,CICLO,BACHILLERATO
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


def load_cursos(nombre_archivo):
    cursos = []
    with open(nombre_archivo, newline='', encoding='utf8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv, delimiter=',', quotechar='|')
        for fila in lector_csv:
            cursos.append(Curso(
                fila["CODIGO"],
                fila["NOMBRE"],
                fila["CREDITOS"],
                fila["REQUISITOS"].split(';'),
                fila["NIVEL"],
                fila["CICLO"],
                fila["BACHILLERATO"]))
    return cursos

def load_estado(nombre_archivo):
    cursos = []
    with open(nombre_archivo, newline='', encoding='utf8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv, delimiter=',', quotechar='|')
        for fila in lector_csv:
            cursos.append(Curso(
                fila["CODIGO"],
                fila["NOMBRE"],
                fila["CREDITOS"],
                fila["REQUISITOS"].split(';'),
                fila["NIVEL"],
                fila["CICLO"],
                fila["BACHILLERATO"]))
    return cursos

def main():
    cursos = load_cursos("cursos.csv")
    estado = load_estado("estado.csv")
    aprobados = [f'[{c.codigo}]: "{c.nombre}"' for c in estado]
    for aprobado in aprobados:
        print(aprobado)


if __name__ == "__main__":
    main()
