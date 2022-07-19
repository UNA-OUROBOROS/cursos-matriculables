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

    def __eq__(self, other):
        if isinstance(other, Curso):
            return self.codigo == other.codigo
        if isinstance(other, str):
            return self.codigo == other
        return False


def load_cursos(nombre_archivo):
    cursos = []
    with open(nombre_archivo, newline='', encoding='utf8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv, delimiter=',', quotechar='|')
        for fila in lector_csv:
            cursos.append(load_curso(fila))
    return cursos

def load_estado(nombre_archivo):
    cursos = []
    with open(nombre_archivo, newline='', encoding='utf8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv, delimiter=',', quotechar='|')
        for fila in lector_csv:
            cursos.append(load_curso(fila))
    return cursos

def load_curso(fila) -> Curso:
    requisitos = fila["REQUISITOS"]
    return Curso(
        fila["CODIGO"],
        fila["NOMBRE"],
        fila["CREDITOS"],
        [] if requisitos == '' else requisitos.split(';'),
        fila["NIVEL"],
        fila["CICLO"],
        fila["BACHILLERATO"])

def cursos_restantes(cursos, aprobados):
    restantes = []
    for curso in cursos:
        if curso not in aprobados:
            restantes.append(curso)
    return restantes

def cursos_matriculables(aprobados, restantes):
    matriculables = []
    for curso in restantes:
        matriculable = True
        for requisito in curso.requisitos:
            if requisito not in aprobados:
                matriculable = False
                break
        if matriculable:
            matriculables.append(curso)
    return matriculables

def main():
    cursos = load_cursos("cursos.csv")
    aprobados = load_estado("estado.csv")
    restantes = cursos_restantes(cursos, aprobados)
    matriculables = cursos_matriculables(aprobados, restantes)
    listado = [f'[{c.codigo}]: "{c.nombre}"' for c in matriculables]
    print(f"cursos restantes: {len(restantes)}")
    print("cursos matriculables")
    for curso in listado:
        print(curso)


if __name__ == "__main__":
    main()
