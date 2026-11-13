#!/usr/bin/env python3
"""Textos de la quincena 23 nov–6 dic 2026 (carpetas 108–135).
Genera spec.json + caption.txt en carruseles/NN o reels/NN. Los Healthspan Hoy 111 y 125 se hacen aparte.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CTA = {"kind": "cta"}
P = {}

def R(n, date, beats, caption):
    P[n] = dict(type="reel", date=date, beats=beats, caption=caption)

def C(n, date, slides, caption):
    P[n] = dict(type="carousel", date=date, slides=slides + [CTA], caption=caption)

# ---------- Lun 23 ----------
C("108", "2026-11-23T10:00:00", [
    {"kind": "cover", "kicker": "Campaña de la gripe", "title": "La vacuna de la gripe también <g>protege el corazón</g>", "sub": "Un ensayo con 2.571 personas que acababan de tener un infarto."},
    {"kind": "text", "kicker": "El ensayo", "big": "2.571", "title": "pacientes tras un infarto", "body": "En el ensayo IAMI recibieron la vacuna de la gripe o placebo en los días siguientes al infarto, y se les siguió un año.", "source": "Fröbert et al., Circulation, 2021"},
    {"kind": "text", "kicker": "El resultado", "big": "−41%", "title": "de muertes en un año", "body": "Con la vacuna hubo un 41% menos de muertes por cualquier causa y un 41% menos de muertes cardiovasculares que con placebo."},
    {"kind": "text", "kicker": "Por qué", "title": "La gripe <g>inflama</g> y sobrecarga el corazón", "body": "En los días después de una gripe sube el riesgo de infarto. Evitar la infección es también evitar ese pico."},
    {"kind": "text", "kicker": "Qué hacer", "title": "Si tienes 60 o más, <g>te toca</g>", "body": "En España se recomienda la vacuna a partir de los 60 años y en grupos de riesgo, como quien tiene enfermedad cardiaca. Pide cita en tu centro de salud."},
], """La vacuna de la gripe no solo evita pasar una semana en la cama. También protege el corazón.

En el ensayo IAMI, publicado en Circulation, 2.571 personas que acababan de tener un infarto recibieron la vacuna de la gripe o placebo. En el año siguiente, el grupo vacunado tuvo un 41% menos de muertes por cualquier causa y un 41% menos de muertes cardiovasculares.

La gripe inflama y sobrecarga el corazón, y en los días posteriores sube el riesgo de infarto. En España, la campaña recomienda la vacuna a partir de los 60 años y en grupos de riesgo. 💉

Envíaselo a quien todavía no se ha vacunado este año.

#longevidad #gripe #vacunas #corazon""")

R("109", "2026-11-23T18:00:00", [
    {"kicker": "Mito o ciencia", "title": "«A los 40 el metabolismo <g>se frena</g>»"},
    {"title": "<g>Mito</g>", "sub": "6.421 personas de 8 días a 95 años. Revista Science."},
    {"title": "Estable de los <g>20 a los 60</g>", "sub": "Después baja solo un 0,7% al año."},
    {"title": "Lo que cambia <g>es el músculo</g>", "sub": "Y lo que te mueves. Ahí sí puedes actuar."}],
"""«Es que a partir de los 40 el metabolismo se frena». Mito.

Un estudio publicado en Science midió el gasto energético de 6.421 personas de 29 países, desde los 8 días hasta los 95 años. Ajustado al tamaño del cuerpo, el metabolismo se mantuvo estable de los 20 a los 60 años. A partir de ahí baja, pero despacio: alrededor de un 0,7% al año.

Si a los 45 engordas, la causa suele estar en otra parte: menos músculo, menos movimiento y más comida. Y eso sí se puede cambiar. 💪

Envíaselo a quien culpa al metabolismo.

#longevidad #metabolismo #mitoociencia #fuerza""")

# ---------- Mar 24 ----------
R("110", "2026-11-24T10:00:00", [
    {"kicker": "Mito o ciencia", "title": "«Un multivitamínico al día <g>alarga la vida</g>»"},
    {"title": "<g>Mito</g>", "sub": "390.124 adultos sanos, seguidos más de 20 años."},
    {"title": "<g>No vivieron más</g>", "sub": "Al principio, incluso un 4% más de riesgo."},
    {"title": "Primero, <g>comida real</g>", "sub": "Suplementa solo lo que te falte, con tu médico."}],
"""Un multivitamínico al día «por si acaso». ¿Alarga la vida? Mito.

Un estudio del Instituto Nacional del Cáncer de EE. UU., publicado en JAMA Network Open, siguió durante más de 20 años a 390.124 adultos sanos. Quienes tomaban un multivitamínico a diario no vivieron más que quienes no lo tomaban. En los primeros años, incluso tuvieron un 4% más de riesgo de muerte.

Si tienes un déficit concreto, corrígelo con tu médico. Si no, la mejor «vitamina» sigue siendo un plato variado. 🥦

Envíaselo a quien tiene un cajón lleno de botes.

#longevidad #suplementos #mitoociencia #nutricion""")

# ---------- Mié 25 ----------
R("112", "2026-11-25T10:00:00", [
    {"kicker": "Movimiento", "title": "Ir al trabajo <g>en bici</g>"},
    {"title": "<g>−41%</g> de mortalidad", "sub": "Más de 263.000 personas en Reino Unido. BMJ."},
    {"title": "<g>−45%</g> de cáncer", "sub": "Y un 46% menos de enfermedad cardiovascular."},
    {"title": "Si no puedes, <g>camina</g>", "sub": "Andar al trabajo también bajó el riesgo cardiovascular."}],
"""El gimnasio que te lleva a la oficina.

Un estudio de la Universidad de Glasgow con más de 263.000 personas del UK Biobank, publicado en el BMJ, encontró que quienes iban al trabajo en bici tenían un 41% menos de mortalidad, un 45% menos de cáncer y un 46% menos de enfermedad cardiovascular que quienes iban en coche o transporte público. Ir andando se asoció con un 27% menos de enfermedad cardiovascular.

Es observacional, pero el mensaje es fácil: si puedes convertir el trayecto en ejercicio, hazlo. 🚲

Etiqueta a quien ya va en bici.

#longevidad #bici #movimiento #corazon""")

R("113", "2026-11-25T18:00:00", [
    {"kicker": "Mito o ciencia", "title": "«Una copa me ayuda <g>a dormir</g>»"},
    {"title": "<g>Mito</g>", "sub": "4.098 personas con sensor de variabilidad cardiaca."},
    {"title": "Peor <g>recuperación nocturna</g>", "sub": "−9,3% con poco alcohol, −24% moderado, −39% mucho."},
    {"title": "Te duermes antes, <g>descansas peor</g>", "sub": "Esta Navidad, la última copa lejos de la cama."}],
"""«Una copa de vino y duermo como un bebé». Mito.

Un estudio finlandés publicado en JMIR Mental Health midió con un sensor la recuperación del cuerpo durante el sueño de 4.098 personas. Con poco alcohol, la recuperación fisiológica bajó un 9,3%. Con una cantidad moderada, un 24%. Y con mucho, un 39%.

El alcohol te ayuda a dormirte antes, pero el sueño que viene después es de peor calidad. Ahora que llegan las cenas de Navidad, deja la última copa lejos de la hora de dormir. 🍷

Envíaselo a quien toma «la del sueño».

#longevidad #sueño #alcohol #mitoociencia""")

# ---------- Jue 26 ----------
C("114", "2026-11-26T10:00:00", [
    {"kind": "cover", "kicker": "Analítica", "title": "El colesterol LDL: el número que <g>más pesa en tu corazón</g>", "sub": "Lo que dicen 26 ensayos con unas 170.000 personas."},
    {"kind": "text", "kicker": "Qué es", "title": "El colesterol <g>que se pega</g> a las arterias", "body": "El LDL transporta colesterol por la sangre. Cuanto más alto y durante más años, más placas en las arterias y más riesgo de infarto e ictus."},
    {"kind": "text", "kicker": "La evidencia", "big": "−22%", "title": "de infartos e ictus al bajar el LDL", "body": "Un análisis de 26 ensayos con unas 170.000 personas encontró que cada 1 mmol/L (unos 39 mg/dL) menos de LDL reducía un 22% los infartos, ictus y revascularizaciones.", "source": "Cholesterol Treatment Trialists, The Lancet, 2010"},
    {"kind": "text", "kicker": "Qué cifra", "title": "Depende de <g>tu riesgo</g>", "body": "No hay un número para todos: cuanto más riesgo cardiovascular tienes, más bajo conviene tenerlo. Pregúntale a tu médico cuál es tu objetivo."},
    {"kind": "text", "kicker": "Qué hacer", "title": "Lo que <g>lo baja</g>", "body": "Menos grasa saturada (embutidos, bollería, mantequilla), más fibra y legumbres, aceite de oliva, ejercicio y no fumar. Y si hace falta, medicación: funciona."},
], """Si solo miras un número de tu analítica para cuidar el corazón, que sea el colesterol LDL.

El LDL es el colesterol que acaba formando placas en las arterias. Un análisis de 26 ensayos con unas 170.000 personas, publicado en The Lancet, encontró que cada 1 mmol/L menos de LDL (unos 39 mg/dL) se traducía en un 22% menos de infartos, ictus y otros eventos graves.

No hay una cifra que valga para todos: cuanto más riesgo tienes, más bajo conviene tenerlo. Pregúntale a tu médico cuál es tu objetivo. 🩸

Guárdalo para tu próxima analítica.

#longevidad #colesterol #corazon #saludpreventiva""")

R("115", "2026-11-26T18:00:00", [
    {"kicker": "Hábitos", "title": "Come <g>más despacio</g>"},
    {"title": "<g>−42%</g> de obesidad", "sub": "59.717 personas en Japón. BMJ Open."},
    {"title": "La saciedad <g>llega tarde</g>", "sub": "Tarda unos minutos en avisar al cerebro."},
    {"title": "Suelta el <g>tenedor</g>", "sub": "Entre bocado y bocado. Sin pantallas."}],
"""El truco más barato para comer menos: comer más despacio.

En un estudio con 59.717 personas con diabetes en Japón, publicado en BMJ Open, quienes comían despacio tenían un 42% menos de probabilidad de tener obesidad que quienes comían rápido. Los de ritmo normal, un 29% menos. Y quienes redujeron su velocidad a lo largo del seguimiento también bajaron de peso.

Es una asociación, pero tiene lógica: la sensación de saciedad tarda en llegar. Suelta el tenedor entre bocado y bocado, y come sin pantallas. 🍽️

Etiqueta a quien termina siempre el primero.

#longevidad #nutricion #habitos #comerconsciente""")

# ---------- Vie 27 ----------
R("116", "2026-11-27T10:00:00", [
    {"kicker": "Sueño", "title": "La siesta, <g>con datos</g>"},
    {"title": "<g>−37%</g> de muerte coronaria", "sub": "23.681 adultos griegos. Archives of Internal Medicine."},
    {"title": "Corta: <g>20–30 minutos</g>", "sub": "Si te despiertas aturdido, ha sido larga."},
    {"title": "Y no a <g>última hora</g>", "sub": "Para no robarle sueño a la noche."}],
"""La siesta española, con datos.

En un estudio con 23.681 adultos griegos sanos, publicado en Archives of Internal Medicine, quienes dormían siesta de forma regular tenían un 37% menos de muerte coronaria que quienes no la dormían. El efecto fue más claro en hombres que trabajaban.

Es observacional y la clave está en el formato: corta, de 20 a 30 minutos, y no a última hora de la tarde para no robarle sueño a la noche. 😴

Etiqueta a tu compañero de siesta.

#longevidad #siesta #sueño #corazon""")

R("117", "2026-11-27T18:00:00", [
    {"kicker": "Mito o ciencia", "title": "«A los 90 ya <g>no se gana músculo</g>»"},
    {"title": "<g>Mito</g>", "sub": "Personas de 86 a 96 años. Revista JAMA."},
    {"title": "<g>+174%</g> de fuerza", "sub": "En solo 8 semanas de entrenamiento."},
    {"title": "Nunca es <g>tarde</g>", "sub": "Pero cuanto antes empieces, mejor."}],
"""«A mi edad ya no se gana músculo». Mito.

En un estudio clásico publicado en JAMA, personas de entre 86 y 96 años que vivían en una residencia entrenaron fuerza con cargas altas durante 8 semanas. Su fuerza aumentó de media un 174%, el músculo del muslo creció un 9% y caminaban casi un 50% más rápido.

Era un grupo pequeño, pero el mensaje se ha confirmado muchas veces: el músculo responde a cualquier edad. Con supervisión y empezando poco a poco. 🏋️

Envíaselo a tu abuela o a tu padre.

#longevidad #fuerza #musculo #mitoociencia""")

# ---------- Sáb 28 ----------
C("118", "2026-11-28T10:00:00", [
    {"kind": "cover", "kicker": "Guía práctica", "title": "Rutina de fuerza en casa <g>en 20 minutos</g>", "sub": "Sin máquinas. Dos veces por semana."},
    {"kind": "text", "kicker": "Por qué", "big": "30–60", "title": "minutos de fuerza a la semana", "body": "Es la dosis que más beneficio se asoció con la mortalidad en un análisis de 16 estudios. Dos sesiones de 20–30 minutos bastan.", "source": "Momma et al., British Journal of Sports Medicine, 2022"},
    {"kind": "text", "kicker": "La rutina", "title": "3 vueltas, <g>4 ejercicios</g>", "body": "1. Sentadilla a una silla: 10–12<br>2. Flexiones con las manos en la mesa: 8–10<br>3. Remo con una mochila cargada: 10–12<br>4. Puente de glúteo: 12–15<br>Descansa 1 minuto entre vueltas."},
    {"kind": "text", "kicker": "Cómo progresar", "title": "Cuando sea fácil, <g>súbele</g>", "body": "Más peso en la mochila, más repeticiones o más lento al bajar. Las últimas 2 repeticiones deberían costarte."},
    {"kind": "text", "kicker": "Con cuidado", "title": "Técnica <g>antes que peso</g>", "body": "Espalda neutra, sin dolor articular. Si tienes una lesión o enfermedad del corazón, consulta antes."},
], """No necesitas gimnasio para entrenar fuerza. Necesitas 20 minutos, una silla y una mochila.

Un análisis de 16 estudios publicado en el British Journal of Sports Medicine encontró el mayor beneficio con 30–60 minutos de fuerza a la semana. Dos sesiones cortas bastan.

La rutina, 3 vueltas:
1. Sentadilla a una silla: 10–12
2. Flexiones con las manos en la mesa: 8–10
3. Remo con una mochila cargada: 10–12
4. Puente de glúteo: 12–15

Cuando sea fácil, pon más peso en la mochila o baja más despacio. 🎒

Guárdalo y hazlo hoy.

#longevidad #fuerza #entrenamientoencasa #musculo""")

R("119", "2026-11-28T18:00:00", [
    {"kicker": "Movimiento", "title": "El deporte que <g>más años suma</g>"},
    {"title": "Tenis: <g>+9,7 años</g>", "sub": "8.577 daneses seguidos hasta 25 años."},
    {"title": "Gimnasio: <g>+1,5</g>", "sub": "Bádminton +6,2, fútbol +4,7, bici +3,7."},
    {"title": "La clave: <g>jugar con otros</g>", "sub": "Es observacional, pero el juego en grupo suma."}],
"""¿El deporte que más años de vida se asocia? El tenis.

En el estudio Copenhagen City Heart, publicado en Mayo Clinic Proceedings, se siguió hasta 25 años a 8.577 adultos. Frente a los sedentarios, quienes jugaban al tenis vivían 9,7 años más; bádminton, 6,2; fútbol, 4,7; bici, 3,7; natación, 3,4; correr, 3,2; y gimnasio, 1,5.

Ojo: es observacional, y quien juega al tenis suele tener más dinero y salud. Pero los autores apuntan a algo interesante: los deportes que más suman son los que se juegan con otras personas. 🎾

¿Con quién juegas tú? 👇

#longevidad #tenis #deporte #movimiento""")

# ---------- Dom 29 ----------
R("120", "2026-11-29T10:00:00", [
    {"kicker": "Hábitos", "title": "Un huerto también <g>es salud</g>"},
    {"title": "Ensayo con <g>291 adultos</g>", "sub": "La mitad recibió un huerto urbano. Lancet Planetary Health."},
    {"title": "<g>+42 min</g> de actividad", "sub": "A la semana, y +1,4 g de fibra al día."},
    {"title": "Y <g>menos estrés</g>", "sub": "Sobre todo en quienes más lo tenían."}],
"""Plantar lechugas también cuenta como salud.

En un ensayo de la Universidad de Colorado publicado en The Lancet Planetary Health, 291 adultos que nunca habían cultivado se repartieron al azar: la mitad recibió un huerto urbano y la otra mitad esperó un año. En una temporada, los hortelanos comían 1,4 g más de fibra al día, se movían 42 minutos más a la semana y tenían menos estrés y ansiedad.

Si no tienes huerto, unas macetas en el balcón también enganchan. 🌱

Etiqueta a quien tiene mano para las plantas.

#longevidad #huerto #habitos #bienestar""")

R("121", "2026-11-29T18:00:00", [
    {"kicker": "Mito o ciencia", "title": "«Hay que hacer <g>5 comidas</g> al día»"},
    {"title": "<g>Mito</g>", "sub": "Ensayo de 8 semanas. British Journal of Nutrition."},
    {"title": "3 o 6 comidas: <g>igual</g>", "sub": "Mismas calorías, misma pérdida de peso."},
    {"title": "Come <g>cuando te vaya bien</g>", "sub": "Lo que cuenta es el total y la calidad."}],
"""«Hay que hacer 5 comidas al día para activar el metabolismo». Mito.

En un ensayo publicado en el British Journal of Nutrition, 16 adultos con obesidad siguieron 8 semanas la misma dieta con las mismas calorías. Unos repartidas en 3 comidas y otros en 6. Perdieron lo mismo: 5,3 kg frente a 4,6 kg, una diferencia que no fue significativa.

Es un estudio pequeño, pero coincide con el resto: lo que cuenta es cuánto y qué comes, no cuántas veces. Si picar entre horas te hace comer de más, no lo necesitas. 🍽️

Envíaselo a quien come cada 3 horas con alarma.

#longevidad #nutricion #mitoociencia #metabolismo""")

# ---------- Lun 30 ----------
R("122", "2026-11-30T10:00:00", [
    {"kicker": "Invierno", "title": "Un baño caliente <g>para el corazón</g>"},
    {"title": "<g>−28%</g> de enfermedad cardiovascular", "sub": "30.076 japoneses seguidos unos 20 años. Heart."},
    {"title": "<g>−26%</g> de ictus", "sub": "En quienes se bañaban a diario en agua caliente."},
    {"title": "Agua caliente, <g>no ardiendo</g>", "sub": "Con cuidado si tienes la tensión baja."}],
"""En Japón, el baño caliente de cada noche es casi un ritual. Y los datos lo acompañan.

Un estudio con 30.076 adultos japoneses seguidos unos 20 años, publicado en Heart, encontró que quienes se bañaban a diario en agua caliente tenían un 28% menos de enfermedad cardiovascular y un 26% menos de ictus que quienes se bañaban una o dos veces por semana o menos.

Es observacional, y el calor dilata los vasos de forma parecida a un ejercicio suave. Agua caliente, no ardiendo, y cuidado si tienes la tensión baja o problemas de corazón. 🛁

Etiqueta a quien no perdona su baño.

#longevidad #corazon #bienestar #invierno""")

R("123", "2026-11-30T18:00:00", [
    {"kicker": "Mito o ciencia", "title": "«Mucha proteína <g>daña los riñones</g>»"},
    {"title": "<g>Mito</g> si estás sano", "sub": "Metaanálisis de 28 estudios. Journal of Nutrition."},
    {"title": "Sin efecto en la <g>función renal</g>", "sub": "Incluso con 1,5 g por kilo al día o más."},
    {"title": "Si tienes <g>enfermedad renal</g>", "sub": "Ahí sí, consulta con tu médico."}],
"""«Tanta proteína te va a destrozar los riñones». Mito, si tus riñones están sanos.

Un metaanálisis de la Universidad McMaster, publicado en The Journal of Nutrition, reunió 28 estudios con más de 1.300 personas. Comer mucha proteína (1,5 g por kilo al día o más) no empeoró la función renal en personas sin enfermedad del riñón.

Si tienes enfermedad renal, es distinto: ahí la cantidad la marca tu médico. Si no, la proteína suficiente es clave para conservar músculo con los años. 🥚

Envíaselo a quien teme a los batidos de proteína.

#longevidad #proteina #mitoociencia #nutricion""")

# ---------- Mar 1 ----------
R("124", "2026-12-01T10:00:00", [
    {"kicker": "Nutrición", "title": "El picante y <g>la longevidad</g>"},
    {"title": "<g>−23%</g> de mortalidad", "sub": "22.811 italianos seguidos 8 años. JACC."},
    {"title": "<g>4 veces</g> por semana o más", "sub": "Guindilla en la comida habitual."},
    {"title": "Con <g>perspectiva</g>", "sub": "Es una asociación. Si te sienta mal, no hace falta."}],
"""Un toque de guindilla en el plato. ¿Ayuda a vivir más?

En el estudio Moli-sani, publicado en el Journal of the American College of Cardiology, se siguió durante unos 8 años a 22.811 adultos del sur de Italia. Quienes tomaban guindilla 4 o más veces por semana tenían un 23% menos de mortalidad que quienes casi no la tomaban, y menos muertes cardiovasculares.

Es una asociación, y probablemente va de la mano de una dieta mediterránea. Si te gusta, adelante. Si te sienta mal, no hace falta. 🌶️

Etiqueta a quien le echa picante a todo.

#longevidad #picante #dietamediterranea #nutricion""")

# ---------- Mié 2 ----------
C("126", "2026-12-02T10:00:00", [
    {"kind": "cover", "kicker": "Guía práctica", "title": "Empezar a correr después de los 40: <g>plan de 8 semanas</g>", "sub": "De caminar a 20 minutos seguidos."},
    {"kind": "text", "kicker": "Por qué", "big": "−27%", "title": "de mortalidad en quienes corren", "body": "Un análisis de 14 estudios con 232.149 personas encontró beneficio incluso corriendo una vez por semana y menos de 50 minutos.", "source": "Pedisic et al., British Journal of Sports Medicine, 2020"},
    {"kind": "text", "kicker": "Semanas 1–4", "title": "Alterna <g>andar y trotar</g>", "body": "3 días por semana, 25 minutos.<br>Semana 1: 1 min trotando, 2 andando<br>Semana 2: 2 y 2<br>Semana 3: 3 y 2<br>Semana 4: 5 y 2"},
    {"kind": "text", "kicker": "Semanas 5–8", "title": "Hacia <g>20 minutos seguidos</g>", "body": "Semana 5: 8 trotando, 2 andando<br>Semana 6: 10 y 1<br>Semana 7: 15 seguidos<br>Semana 8: 20 seguidos<br>Si una semana cuesta, repítela."},
    {"kind": "text", "kicker": "Las reglas", "title": "Despacio, <g>pudiendo hablar</g>", "body": "Ritmo en el que puedas hablar. Un día de descanso entre sesiones y fuerza de piernas. Si tienes problemas de corazón o hace años que no haces deporte, consulta antes."},
], """¿Más de 40 y nunca has corrido? Este plan te lleva de cero a 20 minutos seguidos en 8 semanas.

Un análisis de 14 estudios con 232.149 personas, publicado en el British Journal of Sports Medicine, encontró que quienes corrían tenían un 27% menos de mortalidad, incluso corriendo una vez por semana y menos de 50 minutos.

El plan: 3 días por semana, alternando trotar y andar, y subiendo poco a poco hasta 20 minutos seguidos. A un ritmo en el que puedas hablar. Si una semana cuesta, repítela. 🏃‍♀️

Guárdalo y empieza el lunes.

#longevidad #correr #running #empezaracorrer""")

R("127", "2026-12-02T18:00:00", [
    {"kicker": "Mito o ciencia", "title": "«Hay una dieta <g>mejor</g> para adelgazar»"},
    {"title": "<g>Mito</g>", "sub": "Ensayo DIETFITS: 609 adultos, 12 meses. JAMA."},
    {"title": "<g>−5,3 kg</g> frente a <g>−6,0 kg</g>", "sub": "Baja en grasa o baja en hidratos: sin diferencia."},
    {"title": "La mejor es <g>la que mantienes</g>", "sub": "Comida real, menos ultraprocesados."}],
"""¿Baja en grasa o baja en hidratos? Da igual.

En el ensayo DIETFITS de la Universidad de Stanford, publicado en JAMA, 609 adultos con sobrepeso siguieron durante 12 meses una dieta saludable baja en grasa o una saludable baja en hidratos. Perdieron de media 5,3 kg y 6,0 kg. La diferencia no fue significativa.

Las dos tenían lo mismo en común: más verdura, comida real y menos azúcar, harinas refinadas y ultraprocesados. La mejor dieta es la que puedes mantener. 🥗

Envíaselo a quien cambia de dieta cada mes.

#longevidad #nutricion #mitoociencia #adelgazar""")

# ---------- Jue 3 ----------
R("128", "2026-12-03T10:00:00", [
    {"kicker": "Hábitos", "title": "2 horas a la semana <g>en la naturaleza</g>"},
    {"title": "<g>120 minutos</g>", "sub": "19.806 personas en Inglaterra. Scientific Reports."},
    {"title": "Mejor <g>salud y bienestar</g>", "sub": "Por debajo de 2 horas, sin diferencia clara."},
    {"title": "Parque, monte <g>o playa</g>", "sub": "En una salida o en varias."}],
"""¿Cuánta naturaleza necesitas? Unas 2 horas a la semana.

Un estudio de la Universidad de Exeter con 19.806 personas en Inglaterra, publicado en Scientific Reports, encontró que quienes pasaban al menos 120 minutos a la semana en espacios naturales tenían mejor salud y bienestar. Por debajo de 2 horas no había una ventaja clara, y el beneficio se estabilizaba hacia las 3–5 horas.

Vale un parque, el monte o la playa, de una vez o en varias salidas. Este finde, plan al aire libre. 🌳

Etiqueta a quien te vas a llevar.

#longevidad #naturaleza #bienestar #saludmental""")

R("129", "2026-12-03T18:00:00", [
    {"kicker": "Mito o ciencia", "title": "«El aceite de coco <g>es sano</g>»"},
    {"title": "<g>Mito</g>", "sub": "16 ensayos. Revista Circulation."},
    {"title": "Sube el <g>colesterol LDL</g>", "sub": "Unos 10 mg/dL más que otros aceites vegetales."},
    {"title": "Para cocinar, <g>aceite de oliva</g>", "sub": "Lo de siempre, con evidencia."}],
"""«El aceite de coco es un superalimento». Mito.

Un metaanálisis de 16 ensayos, publicado en Circulation, encontró que el aceite de coco subía el colesterol LDL (el «malo») unos 10 mg/dL más que los aceites vegetales no tropicales. Y no mejoraba el peso, la glucosa ni la inflamación.

Tiene un 80–90% de grasa saturada. Para cocinar y aliñar, el de siempre: aceite de oliva virgen extra. 🫒

Envíaselo a quien hace todo con aceite de coco.

#longevidad #aceitedeoliva #colesterol #mitoociencia""")

# ---------- Vie 4 ----------
C("130", "2026-12-04T10:00:00", [
    {"kind": "cover", "kicker": "Guía práctica", "title": "Navidad sin culpa: <g>5 reglas</g>", "sub": "Disfrutar las fiestas sin empezar enero cuesta arriba."},
    {"kind": "text", "kicker": "El dato", "big": "+0,8", "title": "kilos en Navidad, y la mitad se queda", "body": "Un estudio con unas 3.000 personas que se pesaban a diario vio subidas de 0,8 kg en Alemania, 0,6 en EE. UU. y 0,5 en Japón. La mitad se perdía pronto; el resto seguía meses después.", "source": "Helander et al., NEJM, 2016"},
    {"kind": "text", "kicker": "Reglas 1 y 2", "title": "Fiesta, <g>no temporada</g>", "body": "1. Disfruta los días señalados; el resto, vida normal. 2. En las cenas, empieza por verdura y proteína, y sirve el turrón en plato pequeño."},
    {"kind": "text", "kicker": "Reglas 3 y 4", "title": "Muévete y <g>vigila la copa</g>", "body": "3. Paseo de 10–15 minutos después de comer: baja la glucosa. 4. Alterna cada copa con un vaso de agua, y la última lejos de la hora de dormir."},
    {"kind": "text", "kicker": "Regla 5", "title": "No <g>compenses</g>", "body": "Nada de ayunos castigo ni dietas de enero. Vuelve a tus rutinas al día siguiente: sueño, fuerza y comida real."},
], """Las fiestas no engordan en un día. Engordan cuando duran tres semanas.

Un estudio publicado en el NEJM con unas 3.000 personas que se pesaban a diario vio que en Navidad se ganan unos 0,8 kg en Alemania, 0,6 en EE. UU. y 0,5 en Japón. La mitad se perdía pronto, pero el resto seguía ahí meses después.

5 reglas para disfrutar sin empezar enero cuesta arriba:
1. Fiesta los días señalados; el resto, vida normal
2. Primero verdura y proteína; el turrón, en plato pequeño
3. Paseo de 10–15 minutos después de comer
4. Una copa, un vaso de agua, y la última lejos de la cama
5. Nada de castigos: al día siguiente, a tus rutinas 🎄

Guárdalo y compártelo con tu familia.

#longevidad #navidad #habitos #nutricion""")

R("131", "2026-12-04T18:00:00", [
    {"kicker": "Mito o ciencia", "title": "«Saltarse el desayuno <g>engorda</g>»"},
    {"title": "<g>Mito</g>", "sub": "Metaanálisis de 13 ensayos. BMJ."},
    {"title": "Desayunar: <g>+260 kcal</g> al día", "sub": "Y 0,44 kg más de peso de media."},
    {"title": "Desayuna <g>si tienes hambre</g>", "sub": "Y si lo haces, que sea comida real."}],
"""«El desayuno es la comida más importante del día». Para adelgazar, no.

Un metaanálisis de 13 ensayos de la Universidad de Monash, publicado en el BMJ, encontró que quienes desayunaban comían unas 260 kcal más al día y pesaban de media 0,44 kg más que quienes se lo saltaban.

No significa que desayunar sea malo: si tienes hambre por la mañana, desayuna, y que sea comida real. Pero no hace falta forzarlo para adelgazar. ☕

Envíaselo a quien desayuna sin hambre.

#longevidad #desayuno #mitoociencia #nutricion""")

# ---------- Sáb 5 ----------
R("132", "2026-12-05T10:00:00", [
    {"kicker": "Relaciones", "title": "Los abuelos que cuidan <g>viven más</g>"},
    {"title": "Más de <g>500 personas</g>", "sub": "De 70 a 103 años, en Berlín. Evolution and Human Behavior."},
    {"title": "<g>10 años</g> frente a <g>5</g>", "sub": "La mitad de los que cuidaban seguía viva 10 años después."},
    {"title": "Cuidar <g>a ratos</g>", "sub": "Ayudar suma; agotarse, no."}],
"""Cuidar de los nietos podría ser bueno para la salud de los abuelos.

Un estudio con más de 500 personas de 70 a 103 años en Berlín, publicado en Evolution and Human Behavior, encontró que la mitad de los abuelos que cuidaban de sus nietos de vez en cuando seguían vivos 10 años después. En cambio, la mitad de quienes no ayudaban a nadie había muerto en 5 años.

Es observacional, y los autores avisan: el beneficio está en ayudar con moderación, no en hacerse cargo de todo. Propósito y compañía, dos pilares de la longevidad. 👴👦

Etiqueta a tus padres.

#longevidad #abuelos #proposito #relaciones""")

R("133", "2026-12-05T18:00:00", [
    {"kicker": "A medias", "title": "¿El chocolate <g>protege el corazón</g>?"},
    {"title": "Ensayo COSMOS: <g>21.442</g> personas", "sub": "Extracto de cacao o placebo, unos 3,6 años."},
    {"title": "<g>−27%</g> de muerte cardiovascular", "sub": "Pero el total de eventos (−10%) no fue significativo."},
    {"title": "Era <g>extracto</g>, no tableta", "sub": "Si comes chocolate, negro y en onzas."}],
"""¿El chocolate es bueno para el corazón? A medias.

En el ensayo COSMOS, publicado en el American Journal of Clinical Nutrition, 21.442 adultos tomaron durante unos 3,6 años un extracto con 500 mg de flavanoles de cacao o placebo. Hubo un 27% menos de muertes cardiovasculares, pero el total de eventos cardiovasculares bajó solo un 10% y no fue significativo.

Y la clave: era un extracto en cápsulas, no chocolate. Su directora lo dejó claro: «COSMOS no fue un ensayo de chocolate». Si lo comes, que sea negro y en onzas. 🍫

Envíaselo a quien justifica la tableta con «antioxidantes».

#longevidad #chocolate #corazon #mitoociencia""")

# ---------- Dom 6 ----------
R("134", "2026-12-06T10:00:00", [
    {"kicker": "Mito o ciencia", "title": "«Todo el pan <g>integral</g> lo es»"},
    {"title": "<g>Mito</g>", "sub": "Hay que mirar la etiqueta."},
    {"title": "Integral = <g>100% harina integral</g>", "sub": "Lo exige la norma del pan desde 2019."},
    {"title": "Si no, verás <g>el %</g>", "sub": "«Elaborado con harina integral» y el porcentaje."}],
"""«Compro pan de molde integral, que es más sano». ¿Seguro que es integral?

Desde la norma de calidad del pan de 2019, en España solo se puede llamar «pan integral» al elaborado con un 100% de harina integral. Si lleva menos, la etiqueta tiene que indicar el porcentaje, por ejemplo «elaborado con harina integral (30%)».

Gira el paquete y mira dos cosas: que ponga 100% integral y que el primer ingrediente sea harina integral. La fibra de verdad está ahí. 🍞

Envíaselo a quien compra «integral» sin mirar.

#longevidad #pan #mitoociencia #nutricion""")

R("135", "2026-12-06T18:00:00", [
    {"kicker": "A medias", "title": "¿Intervalos <g>a los 70</g>?"},
    {"title": "Ensayo Generation 100", "sub": "1.567 noruegos de 70 a 77 años, 5 años. BMJ."},
    {"title": "Mortalidad: <g>3%</g> con intervalos", "sub": "4,7% en el grupo control. No significativo."},
    {"title": "Es <g>seguro</g> y suma", "sub": "Dos días por semana, adaptado a tu forma."}],
"""¿Entrenar con intervalos a los 70? Se puede, y sienta bien.

En el ensayo Generation 100, publicado en el BMJ, 1.567 noruegos de 70 a 77 años se repartieron en tres grupos durante 5 años: intervalos 2 veces por semana, ejercicio moderado o las recomendaciones generales. La mortalidad fue del 3% con intervalos, del 4,7% en el grupo control y del 6% con ejercicio moderado. La diferencia no fue significativa, pero los intervalos fueron seguros y mejoraron la forma física.

Con la edad, la intensidad también tiene sitio. Adaptada a tu forma y, si tienes problemas de corazón, consultada antes. 🚴

Envíaselo a quien cree que a cierta edad solo toca pasear.

#longevidad #ejercicio #intervalos #envejecimientosaludable""")


def main():
    for n, d in P.items():
        base = ROOT / ("carruseles" if d["type"] == "carousel" else "reels") / n
        base.mkdir(parents=True, exist_ok=True)
        spec = {"type": d["type"], "image": None}
        if d["type"] == "carousel":
            spec["slides"] = d["slides"]
            for p in ("portada.jpg",):
                if (base / p).exists(): spec["image"] = p
        else:
            spec["beats"] = d["beats"]
            if (base / "imagen.jpg").exists(): spec["image"] = "imagen.jpg"
        spec["publish"] = d["date"]
        (base / "spec.json").write_text(json.dumps(spec, ensure_ascii=False, indent=1))
        (base / "caption.txt").write_text(d["caption"].strip() + "\n")
    print(len(P), "piezas")

if __name__ == "__main__":
    main()
