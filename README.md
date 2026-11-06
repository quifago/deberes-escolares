# La semana, en claro

Web estática en español con los deberes de 1.º ESO A de las semanas del 2–6 y 9–13 de noviembre de 2026. Resumen familiar del Canva escolar revisado el 6 de noviembre. No es una comunicación oficial del colegio.

## Abrir y compartir

`index.html` funciona directamente al abrirlo, sin instalación ni conexión. Para tener una dirección web compartible, publica los archivos de esta carpeta en GitHub Pages, Vercel u otro alojamiento estático. No necesita compilación, servidor, cuenta de lector ni variables de entorno.

### GitHub Pages

1. Crea un repositorio y sube los archivos de esta carpeta a su raíz.
2. En Settings → Pages, selecciona Deploy from a branch, rama `main`, carpeta `/ (root)`.
3. GitHub mostrará la dirección una vez completado el despliegue.

### Vercel

Importa el repositorio como proyecto. Framework: Other. No hay comando de compilación. Directorio de salida: `.`. El archivo `vercel.json` incluye cabeceras para no indexar el contenido.

## Qué guarda

Las casillas se guardan únicamente en `localStorage` del navegador de cada familia. No existe una base de datos, seguimiento, analítica ni sincronización entre dispositivos. Las marcas originales de la familia no forman parte de esta copia. El selector permite consultar ambas semanas y el enlace `?semana=2026-11-09` abre una semana concreta. El botón de imprimir adapta la página al papel.

No se incluyen nombres de alumnos, credenciales, información familiar, enlaces privados de Alexia ni los PDF originales. La clase figura para que el alcance de los deberes esté claro. La web pide a los buscadores que no la indexen, pero eso no la convierte en privada: cualquier persona con la URL podrá abrirla y reenviarla.

## Actualizar el contenido

La información está duplicada en `data.json` (editable) y en el bloque `homework-data` de `index.html` para permitir abrir el HTML sin servidor. Tras cambiar `data.json`, ejecuta:

```sh
python3 build.py
```

Revisa también la fecha visible de actualización en `index.html`. Los cambios del widget de Wabi no se publican automáticamente aquí; esta copia se actualiza manualmente.

Las contradicciones del Canva se mantienen separadas de los deberes confirmados. No se resuelven suponiendo un capítulo, día o fecha.
