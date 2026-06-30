# Explicaion de la solucion

Al empezar la prueba no tenia experiencia en extraccion de informacion desde un PDF asi que el primer paso fue investigar que herramientas podian servirpara resolver el problema.

Elegi usar **PyMuPDF** para leer el contenido del PDF, porque permite obtener el texto de forma facil y funcionaba correctamente con las recetas de ejemplo.

Para poder extraer la informacion importante (paciente, medico, medicamentos, etc) utilice un modelo de lenguaje (**Google Gemini**) acompañado de un prompt que indica que información debe extraer y en que formato devolverla.

El prompt fue separado del codigo, en un archivo independiente para facilitar mantenimiento y modificaciones futuras.

Fui probando ambos PDF de ejemplo para verificar que la lectura era correcta independientemente del numero de recetas brindadas en un solo PDF, ya que el primer ejemplo tenia 1 y el segundo 2.

Al principio el programa se ejecutaba desde un archivo "main.py" para probar cosas rapido. Luego mude las funcionalidades a una API desarrollada con **FastAPI** logrando enviar un PDF y recibir informacion en formato JSON.

Tambien agregue validaciones basicas como que el archivo sea un PDF antes de empezar, devolviendo error en caso de no serlo.

El resultado final es una API simple que recibe un PDF mediante POST, extrae su contenido, procesa la informacion mediante IA y deuvelve una respuesta estructurada en JSON lista para ser usada en otras apps o almacenada en una BD.