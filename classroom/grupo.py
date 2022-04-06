from asignatura import Asignatura

class Grupo:

    grado = "Grado 12"

    def _init_(self, grupo="grupo predeterminado", asignaturas=[], estudiantes=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
    def _str_(self):
      cadena= "Grupo de estudiantes: " + self._grupo
      return cadena

    def listadoAsignaturas(self, **kwargs):
        for asasa in kwargs.values():
          
          self._asignaturas.append(Asignatura(asasa))
    
    def agregarAlumno(self, alumno, lista=None):
      if(lista is None):
        lista=[]
      lista.append(alumno)
      self.listadoAlumnos = self.listadoAlumnos + lista
      
   
     

    @classmethod
    def asignarNombre(*args):
      for arg in args:
        if arg == "Grado 1":
          Grupo.grado="Grado 1"
        else:
          Grupo.grado="Grado"