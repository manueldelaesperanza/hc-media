# Healthspan Club · operación de RRSS (para cualquier sesión de Claude)

Este repo es la copia persistente de todo lo que produce Claude para @healthspanclub.es.
El espacio de trabajo de Claude se reinicia sin aviso: TODO lo que haga falta después
(scripts, imágenes, carruseles, reels, textos) se sube aquí en cuanto se genera.

- Metricool: brandId 7133099, zona Europe/Madrid. Instagram + Facebook (página 1302909262913530).
- Carruseles: autoPublish true, 10:00. Reels: autoPublish false (Manuel los publica a mano con música), 18:00; martes 10:00.
- Martes 18:00: "Healthspan Hoy" (noticia de la semana), carrusel tipográfico.
- Medios para Metricool: URLs públicas de este repo (raw.githubusercontent.com/manueldelaesperanza/hc-media/main/...).
  Antes se usaba Netlify (candid-valkyrie-0f0b9d.netlify.app), que exigía que Manuel arrastrara carpetas.
- Imágenes: Claude las genera en el ChatGPT de Manuel (proyecto HEALTHSPAN CLUB, chat "Imágenes RRSS")
  desde el navegador integrado de la app de Claude, y las extrae por JavaScript (canvas → base64 en trozos).
- Estilo: fondo #141814, dorado #F2C14E, tipografía Outfit; 1080×1350 carruseles, 1080×1920 reels (12 s, 5 planos).
- Pérdida del 28-oct-2026: se perdieron scripts y medios de la quincena 26 oct–8 nov (carpetas 52–79).
  Metricool conserva sus copias; Manuel tiene HC_media_26oct-8nov.zip en su Mac.
