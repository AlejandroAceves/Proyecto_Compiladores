# Lenguaje y Compilador Especializados en Organización de Carpetas

## Resumen
Este proyecto consiste en el desarrollo de un lenguaje y un compilador especializados en la organización de archivos dentro de una carpeta seleccionada. La herramienta permite clasificar archivos por fecha de creación, tamaño, palabras en el nombre del archivo y tipo de archivo. Además, ofrece funciones para modificar carpetas mediante comandos como `move`, `delete`, `duplicate`, y `copy`.

## Motivación y Problema a Resolver

### Descripción del Problema
El proyecto busca enseñar a los usuarios, a través de un lenguaje sencillo, una nueva forma de organizar archivos en su dispositivo local, facilitando la gestión y manipulación de archivos sin la necesidad de conocimientos previos en programación.

### Importancia
En el ámbito laboral, muchas personas no saben utilizar terminales para organizar archivos debido a la complejidad del lenguaje y la falta de conocimientos en programación, lo que puede resultar en pérdida de tiempo en el manejo de archivos.

### Casos de Uso
La herramienta permitirá a los usuarios organizar archivos de manera más eficiente. Algunos casos de uso incluyen:
- Modificar la localización y cantidad de documentos disponibles (cambiando la posición en el directorio, eliminando, duplicando o copiando archivos).
- Organizar documentos dentro de una carpeta según las preferencias del usuario.

## Objetivos del Proyecto
- **Objetivo 1:** Mejorar la eficiencia en la organización y gestión de archivos.
- **Objetivo 2:** Proveer una herramienta accesible para usuarios sin experiencia en programación.
- **Objetivo 3:** Reducir el tiempo y esfuerzo dedicados a la gestión manual de archivos.
- **Objetivo 4:** Facilitar la implementación de operaciones complejas sobre archivos y carpetas con comandos simples.

## Comparación con Compiladores y Herramientas Similares

### Batch y Shell Scripts
Lenguajes de scripting como Batch en Windows y Shell (Bash) en Unix/Linux permiten automatizar la gestión de archivos a través de comandos como `move`, `copy`, `rm`, y `cp`. Son flexibles y ampliamente utilizados en entornos de desarrollo y administración de sistemas.

### PowerShell
PowerShell es una herramienta avanzada en Windows que permite la automatización de tareas administrativas, incluida la organización de archivos, utilizando comandos como `Move-Item`, `Remove-Item`, `Copy-Item`, y funciones avanzadas de scripting.

### Python
Python, con bibliotecas como `os` y `shutil`, permite escribir scripts para gestionar archivos y carpetas. Es un lenguaje versátil que puede ser utilizado para tareas complejas de organización y manipulación de archivos.

### Herramientas Automatizadas de Gestión de Archivos
Existen aplicaciones con interfaces gráficas para organizar archivos, como Hazel en macOS, que permite a los usuarios definir reglas para la clasificación automática de archivos. Sin embargo, estas herramientas suelen estar limitadas a plataformas específicas y no ofrecen la flexibilidad de un lenguaje de programación.

## Limitaciones de Soluciones Actuales
- **Curva de Aprendizaje Elevada:** Herramientas como Bash, PowerShell y Python requieren conocimientos de programación o scripting, lo que puede ser un obstáculo para usuarios no técnicos.
- **Falta de Simplicidad y Usabilidad:** Las soluciones existentes no están diseñadas específicamente para la organización de archivos de manera intuitiva.
- **Compatibilidad Limitada:** Muchas herramientas están restringidas a ciertos sistemas operativos o requieren software adicional.
- **Flexibilidad vs. Usabilidad:** Las herramientas con interfaces gráficas carecen de la flexibilidad necesaria para satisfacer necesidades específicas o complejas.

## Justificación del Nuevo Compilador
- **Accesibilidad para Usuarios No Técnicos:** Ofrecerá un lenguaje sencillo y accesible para la organización de archivos, reduciendo la barrera de entrada para usuarios sin conocimientos técnicos.
- **Enfoque Específico en la Organización de Archivos:** Diseñado específicamente para optimizar la experiencia del usuario en la gestión de archivos.
- **Multiplataforma y Fácil de Usar:** Compatible con múltiples sistemas operativos, priorizando la usabilidad y eliminando la necesidad de aprender comandos complejos.
- **Solución Flexible y Personalizable:** Proporciona suficiente flexibilidad para que los usuarios personalicen la organización de archivos según sus necesidades, permitiendo tanto tareas sencillas como operaciones avanzadas.

## Arquitectura y Diseño del Compilador
- **Diagrama de bloques:**
    - https://drive.google.com/file/d/1n5fFAuvSHq6quBxfa6XKAuDULbauceNO/view?usp=drive_link
    - https://www.canva.com/design/DAGP2JyK5CQ/OI_ijP0oY6DJ0F-oxyt2jQ/edit?utm_content=DAGP2JyK5CQ&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton 

- **Explicación del flujo de datos:**

- **Decisiones de diseño:**
    - Identifier: `Organize`,`Modify`
    - OPERATOR: `+`,`-`,`=`
    - KEYWORDS: `Date`, `Size`, `Text`, `Move`, `Delete`, `Copy`, `FILETYPE`
    - PUNCTUATORS: `/`, `.`, `;`