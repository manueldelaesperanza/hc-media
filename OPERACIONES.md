# Healthspan Club · operación de RRSS (para cualquier sesión de Claude)

Este repo es la copia persistente de todo lo que produce Claude para @healthspanclub.es.
El espacio de trabajo de Claude se reinicia sin aviso: TODO lo que haga falta después
(scripts, imágenes, carruseles, reels, textos) se sube aquí en cuanto se genera.

- Metricool: brandId 7133099, zona Europe/Madrid. Instagram + Facebook (página 1302909262913530).
- Carruseles: autoPublish true, 10:00. Reels: autoPublish false (Manuel los publica a mano con música), 18:00; martes 10:00.
- Martes 18:00: "Healthspan Hoy" (noticia de la semana), carrusel tipográfico.
- Medios para Metricool: URLs públicas de este repo (raw.githubusercontent.com/manueldelaesperanza/hc-media/main/...).
  PROBADO el 31-oct-2026 con el carrusel 83: Metricool las acepta y las copia a static.metricool.com. Ya no hace falta Netlify.
- Imágenes: Claude las genera en el ChatGPT de Manuel (proyecto HEALTHSPAN CLUB, chat "Imágenes RRSS")
  desde el navegador integrado de la app de Claude, y las extrae por JavaScript (canvas → base64 en trozos).
- Estilo: fondo #141814, dorado #F2C14E, tipografía Outfit; 1080×1350 carruseles, 1080×1920 reels (12 s, 5 planos).
- Pérdida del 28-oct-2026: se perdieron scripts y medios de la quincena 26 oct–8 nov (carpetas 52–79).
  Metricool conserva sus copias; Manuel tiene HC_media_26oct-8nov.zip en su Mac.
- Plantillas: tools/hc_render.py (ver tools/README.md). Reel = 1 imagen vertical 2:3 arriba con fundido + 4 frases + cierre
  «SÍGUENOS PARA VIVIR MÁS», 2,4 s cada parte, 12 s. Carrusel 1080x1350: portada, diapositivas de texto y cierre.
- Estructura: carruseles/NN/{spec.json,caption.txt,slide_XX.jpg}, reels/NN/{spec.json,caption.txt,imagen.png,reel.mp4,portada.jpg}.
- Desde 31-oct: más reels (los reels llegan a ~3 veces más gente). El reparto de formatos se revisa cada viernes con las métricas.
- 02-nov-2026: quincena 9–22 nov (80–107) completa y programada en Metricool: 10 carruseles (autoPublish) + 16 reels
  (autoPublish false) + Healthspan Hoy 83. Vídeos desde raw.githubusercontent también funcionan en Metricool.
  Recordatorios de reels: send_later 15 min antes de cada uno. Pendiente: Healthspan Hoy 97 (mar 17), se elige el vie 13.
- Imágenes: tools/img_assemble.py reconstruye las imágenes de ChatGPT (canvas → JPEG base64 en trozos de 250k).
- 09-nov-2026: DUPLICADOS. En Metricool había una segunda tanda de la quincena 9–22 nov creada el 30-oct (ids 4110xxxxx),
  además de la buena (2-nov, ids 41430xxxx/41431xxxx + HH 412275778, la que coincide con este repo y las cifras verificadas).
  El 9-nov a las 10:00 se publicaron los DOS carruseles de Movember. Las 25 piezas pendientes de la tanda del 30-oct
  se pasaron a BORRADOR (draft) en Metricool, no se borraron. Antes de programar, comprobar siempre con getScheduledPosts
  que no hay piezas ya programadas en esas fechas.
