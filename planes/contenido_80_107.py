#!/usr/bin/env python3
"""Textos verificados de la quincena 9–22 nov 2026 (carpetas 80–107).
Genera spec.json + caption.txt en carruseles/NN o reels/NN.
Las imágenes (portada.png / imagen.png) se añaden cuando se generan en ChatGPT.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CTA = {"kind": "cta"}

P = {}

P["80"] = dict(type="carousel", date="2026-11-09T10:00:00", slides=[
    {"kind": "cover", "kicker": "Movember", "title": "¿Por qué los hombres viven <g>5 años menos</g>?", "sub": "En España, 81,3 años frente a 86,7."},
    {"kind": "text", "kicker": "El dato", "big": "5,4", "title": "años de diferencia", "body": "En 2023, las mujeres vivieron de media 86,7 años en España y los hombres 81,3. En 1990 la brecha era de 7,3 años.", "source": "Funcas, datos de 2023"},
    {"kind": "text", "kicker": "Por qué", "title": "Más riesgos, <g>menos chequeos</g>", "body": "Buena parte de la diferencia se explica por hábitos: más tabaco y alcohol, más accidentes y menos visitas al médico."},
    {"kind": "text", "kicker": "Qué hacer", "title": "Este noviembre, <g>revísate</g>", "body": "Mídete la tensión, hazte una analítica y pregunta a tu médico qué revisiones te tocan por edad. Y si algo te preocupa, habla de ello."},
    CTA],
    caption="""Los hombres viven unos 5 años menos que las mujeres. Y no es solo genética.

En España, la esperanza de vida en 2023 fue de 86,7 años para ellas y 81,3 para ellos. La brecha se ha reducido (en 1990 era de 7,3 años), pero sigue ahí. Buena parte se explica por hábitos: más tabaco y alcohol, más accidentes y menos visitas al médico.

Noviembre es el mes de Movember, dedicado a la salud masculina. Buen momento para medirte la tensión, hacerte una analítica y preguntar qué revisiones te tocan. 🥸

Etiqueta a ese amigo que lleva años sin ir al médico.

#longevidad #movember #saludmasculina #prevencion""")

P["81"] = dict(type="reel", date="2026-11-09T18:00:00", beats=[
    {"kicker": "Tensión alta", "title": "El ejercicio que <g>más la baja</g>"},
    {"title": "<g>Sentadilla</g> en pared", "sub": "Isométrico: aguantar la postura sin moverte."},
    {"title": "<g>−8 puntos</g> de tensión", "sub": "270 ensayos, 15.827 personas. El cardio: −4,5."},
    {"title": "Súmalo a <g>tu rutina</g>", "sub": "Sin dejar el cardio ni la medicación."}],
    caption="""¿El ejercicio que más baja la tensión? Probablemente no es el que piensas.

Un metaanálisis publicado en el British Journal of Sports Medicine, con 270 ensayos y 15.827 personas, comparó tipos de ejercicio. Los isométricos (aguantar una postura sin moverte, como la sentadilla en pared) bajaron la tensión en reposo una media de 8,2/4,0 mmHg. El cardio, 4,5/2,5.

No sustituye al cardio ni a la medicación: se suma. Y si tienes la tensión muy alta, consulta antes. 🧱

Envíaselo a quien se mide la tensión cada mañana.

#longevidad #tensionarterial #isometricos #ejercicio""")

P["82"] = dict(type="reel", date="2026-11-10T10:00:00", beats=[
    {"kicker": "Mito", "title": "Abdominales para <g>quemar barriga</g>"},
    {"title": "6 semanas de <g>abdominales</g>", "sub": "24 adultos, 5 días a la semana."},
    {"title": "La grasa abdominal <g>no bajó</g>", "sub": "Ganaron resistencia, no perdieron barriga."},
    {"title": "Lo que funciona: <g>todo el cuerpo</g>", "sub": "Comer mejor, moverte más y entrenar fuerza."}],
    caption="""Hacer abdominales para perder barriga. Mito.

En un ensayo publicado en el Journal of Strength and Conditioning Research, 24 adultos hicieron 7 ejercicios de abdominales, 5 días a la semana, durante 6 semanas. La grasa del abdomen no bajó frente al grupo control. Lo que sí mejoró fue su resistencia abdominal.

La grasa no se quema por zonas. Baja con el conjunto: comer mejor, moverte más y entrenar fuerza de todo el cuerpo. 🔥

Envíaselo a quien hace 100 abdominales cada noche.

#longevidad #abdominales #mitoociencia #entrenamiento""")

P["84"] = dict(type="carousel", date="2026-11-11T10:00:00", slides=[
    {"kind": "cover", "kicker": "El dato", "title": "Tu <g>fuerza de agarre</g> dice cuánto vivirás", "sub": "139.691 personas de 17 países."},
    {"kind": "text", "kicker": "El estudio", "big": "17", "title": "países, 139.691 personas", "body": "El estudio PURE midió la fuerza de la mano a adultos de 35 a 70 años y los siguió una mediana de 4 años.", "source": "Leong et al., The Lancet, 2015"},
    {"kind": "text", "kicker": "El resultado", "big": "+16%", "title": "de mortalidad por cada 5 kg menos", "body": "La fuerza de agarre predijo la mortalidad mejor que la tensión arterial sistólica."},
    {"kind": "text", "kicker": "Con perspectiva", "title": "No es la mano: <g>es todo el cuerpo</g>", "body": "El agarre refleja tu fuerza general. Entrena fuerza 2 veces por semana: peso muerto, remo y paseos del granjero con peso."},
    CTA],
    caption="""Apretar la mano con fuerza dice mucho de cuánto vas a vivir.

El estudio PURE, publicado en The Lancet, midió la fuerza de agarre a 139.691 adultos de 17 países. Por cada 5 kg menos de fuerza, el riesgo de muerte subía un 16%. Y predijo la mortalidad mejor que la tensión arterial sistólica.

Es una asociación: el agarre refleja tu fuerza general. La buena noticia es que se entrena. Peso muerto, remo y paseos del granjero, 2 veces por semana. 🤝

¿Alguna vez te has medido el agarre? Cuéntanos. 👇

#longevidad #fuerza #fuerzadeagarre #envejecimientosaludable""")

P["85"] = dict(type="reel", date="2026-11-11T18:00:00", beats=[
    {"kicker": "Sin gimnasio", "title": "<g>1 minuto</g> intenso, 3 veces al día"},
    {"title": "25.241 personas <g>sin deporte</g>", "sub": "Con sensor en la muñeca, casi 7 años."},
    {"title": "<g>−38%</g> de mortalidad", "sub": "Y casi la mitad de muerte cardiovascular."},
    {"title": "Escaleras, cuestas, <g>la compra</g>", "sub": "Cuando puedas, aprieta un minuto."}],
    caption="""No tienes tiempo para el gimnasio. ¿Tienes 3 minutos?

Un estudio publicado en Nature Medicine siguió casi 7 años a 25.241 adultos del UK Biobank que no hacían deporte, con un sensor en la muñeca. Quienes hacían unas 3 ráfagas diarias de actividad intensa de 1–2 minutos en su vida normal (subir escaleras rápido, cargar la compra, correr a por el autobús) tenían un 38–40% menos de mortalidad y un 48–49% menos de muerte cardiovascular.

Es observacional, pero el mensaje es fácil: cuando puedas, aprieta un minuto. ⚡

Etiqueta a quien siempre coge el ascensor.

#longevidad #ejercicio #vilpa #movimiento""")

P["86"] = dict(type="carousel", date="2026-11-12T10:00:00", slides=[
    {"kind": "cover", "kicker": "Salud mental", "title": "El ejercicio también <g>trata la depresión</g>", "sub": "218 ensayos, 14.170 personas."},
    {"kind": "text", "kicker": "El estudio", "big": "218", "title": "ensayos con 14.170 personas", "body": "Un metaanálisis comparó distintos tipos de ejercicio en personas con depresión.", "source": "Noetel et al., BMJ, 2024"},
    {"kind": "text", "kicker": "Lo que mejor funcionó", "title": "Caminar o correr, <g>yoga</g> y <g>fuerza</g>", "body": "Caminar o correr fue lo más eficaz, seguido del yoga y el entrenamiento de fuerza."},
    {"kind": "text", "kicker": "Con perspectiva", "title": "Suma, <g>no sustituye</g>", "body": "La calidad de muchos estudios es baja. Si tienes depresión, el ejercicio ayuda junto a tu médico o psicólogo, no en su lugar."},
    CTA],
    caption="""Moverte también es tratar la depresión.

Un metaanálisis publicado en el BMJ reunió 218 ensayos con 14.170 personas con depresión. Caminar o correr fue lo que mejor funcionó, seguido del yoga y el entrenamiento de fuerza, con efectos claros frente a los grupos control.

Ojo: la calidad de muchos estudios es baja, y el ejercicio no sustituye a la ayuda profesional. Se suma a ella. 🌿

Envíaselo a alguien a quien le venga bien un paseo hoy. Y acompáñale.

#longevidad #saludmental #depresion #ejercicio""")

P["87"] = dict(type="reel", date="2026-11-12T18:00:00", beats=[
    {"kicker": "El dato", "title": "<g>2 refrescos</g> al día"},
    {"title": "118.363 adultos, <g>décadas</g> de seguimiento", "sub": "Estudio de Harvard en Circulation."},
    {"title": "<g>+21%</g> de mortalidad", "sub": "Y un 31% más de muerte cardiovascular."},
    {"title": "Cámbialo por <g>agua con gas</g>", "sub": "Con limón o hielo, sin azúcar."}],
    caption="""Dos refrescos azucarados al día pasan factura.

Un estudio de Harvard publicado en Circulation siguió durante décadas a 118.363 adultos. Quienes tomaban 2 o más bebidas azucaradas al día tenían un 21% más de riesgo de muerte que quienes casi no las tomaban (menos de una al mes), y un 31% más de muerte cardiovascular.

Es una asociación, pero va en la línea de todo lo que sabemos del azúcar añadido. Mejor agua, agua con gas o infusiones. 🥤

Envíaselo a quien no come sin su refresco.

#longevidad #azucar #refrescos #nutricion""")

P["88"] = dict(type="carousel", date="2026-11-13T10:00:00", slides=[
    {"kind": "cover", "kicker": "Prevención", "title": "Las caídas se pueden <g>prevenir</g>", "sub": "108 ensayos, 23.407 personas mayores."},
    {"kind": "text", "kicker": "El estudio", "big": "108", "title": "ensayos, 23.407 personas", "body": "Una revisión Cochrane analizó programas de ejercicio en personas mayores que viven en su casa.", "source": "Sherrington et al., Cochrane, 2019"},
    {"kind": "text", "kicker": "El resultado", "big": "−23%", "title": "de caídas con ejercicio", "body": "Equilibrio y ejercicios funcionales: −24%. Combinados con fuerza: −34%. Taichí: −19%."},
    {"kind": "text", "kicker": "Qué hacer", "title": "Entrena el <g>equilibrio</g>", "body": "Ponte a una pierna mientras te lavas los dientes, levántate de la silla sin manos y entrena fuerza de piernas 2 veces por semana."},
    CTA],
    caption="""Una caída puede cambiarte la vida. Y se pueden prevenir.

Una revisión Cochrane con 108 ensayos y 23.407 personas mayores que vivían en su casa encontró que el ejercicio reduce un 23% las caídas. Los programas de equilibrio y ejercicios funcionales, un 24%. Si además incluyen fuerza, hasta un 34%. El taichí, un 19%.

El equilibrio se entrena a cualquier edad, y cuanto antes empieces, mejor. 🧘

Envíaselo a tus padres.

#longevidad #equilibrio #caidas #envejecimientosaludable""")

P["89"] = dict(type="reel", date="2026-11-13T18:00:00", beats=[
    {"kicker": "Mito", "title": "El cardio en ayunas <g>quema más grasa</g>"},
    {"title": "4 semanas, <g>mismo plan</g>", "sub": "20 mujeres: unas en ayunas, otras tras comer."},
    {"title": "<g>Mismo resultado</g>", "sub": "Ambos grupos perdieron peso y grasa por igual."},
    {"title": "Entrena <g>cuando te venga bien</g>", "sub": "Lo que cuenta es la constancia."}],
    caption="""¿Correr en ayunas quema más grasa? No hay pruebas.

En un ensayo publicado en el Journal of the International Society of Sports Nutrition, 20 mujeres hicieron 1 hora de cardio 3 días por semana durante 4 semanas, con la misma dieta. La mitad entrenaba en ayunas y la otra mitad después de comer. Ambos grupos perdieron peso y grasa, sin diferencias entre ellos.

Es un estudio pequeño, pero coincide con el resto: entrena cuando mejor te venga. Lo que cuenta es la constancia. 🏃

Envíaselo a quien sale a correr sin desayunar por obligación.

#longevidad #cardio #ayuno #mitoociencia""")

P["90"] = dict(type="carousel", date="2026-11-14T10:00:00", slides=[
    {"kind": "cover", "kicker": "Día Mundial de la Diabetes", "title": "La prediabetes <g>tiene vuelta atrás</g>", "sub": "El ensayo que lo demostró."},
    {"kind": "text", "kicker": "El estudio", "big": "3.234", "title": "personas con prediabetes", "body": "El Diabetes Prevention Program comparó cambios de hábitos, metformina y placebo durante casi 3 años.", "source": "DPP Research Group, NEJM, 2002"},
    {"kind": "text", "kicker": "El resultado", "big": "−58%", "title": "de diabetes con hábitos", "body": "La metformina la redujo un 31%. Los hábitos funcionaron casi el doble."},
    {"kind": "text", "kicker": "Los objetivos", "title": "<g>7%</g> de peso y <g>150 minutos</g> de ejercicio", "body": "Perder un 7% del peso y moverse al menos 150 minutos a la semana. Si tu glucosa sale alta, empieza por ahí y habla con tu médico."},
    CTA],
    caption="""Hoy es el Día Mundial de la Diabetes. Una buena noticia: la prediabetes tiene vuelta atrás.

El Diabetes Prevention Program, publicado en el NEJM, siguió a 3.234 personas con prediabetes durante casi 3 años. Perder un 7% del peso y moverse 150 minutos a la semana redujo un 58% el riesgo de diabetes. La metformina, un 31%. Los hábitos funcionaron casi el doble que el fármaco.

Si en tu analítica la glucosa sale en el límite, no lo dejes pasar. 🩸

Guárdalo y compártelo con quien tenga la glucosa alta.

#longevidad #diabetes #prediabetes #diamundialdeladiabetes""")

P["91"] = dict(type="reel", date="2026-11-14T18:00:00", beats=[
    {"kicker": "Mito", "title": "El azúcar moreno <g>es más sano</g>"},
    {"title": "Mismas <g>calorías</g>", "sub": "190 frente a 194 kcal por cada 50 g."},
    {"title": "Minerales: <g>casi nada</g>", "sub": "Una cucharada no llega al 1% de lo que necesitas."},
    {"title": "Azúcar es <g>azúcar</g>", "sub": "Lo que importa es cuánto tomas."}],
    caption="""“El azúcar moreno es más sano”. Mito.

Según el Consejo Europeo de Información sobre la Alimentación (EUFIC), 50 g de azúcar moreno tienen 190 kcal y 50 g de blanco, 194. Sí tiene algo más de minerales, pero tan poco que una cucharada no llega al 1% de lo que necesitas al día.

Moreno o blanco, lo que cuenta es la cantidad de azúcar añadido. Cuanto menos, mejor. 🥄

Envíaselo a quien pide el sobre de azúcar moreno "para cuidarse".

#longevidad #azucar #mitoociencia #nutricion""")

P["92"] = dict(type="reel", date="2026-11-15T10:00:00", beats=[
    {"kicker": "Biohacking", "title": "¿Sirven las <g>duchas frías</g>?"},
    {"title": "3.018 personas, <g>30 días</g>", "sub": "Terminaban la ducha con 30–90 s de agua fría."},
    {"title": "<g>−29%</g> de bajas laborales", "sub": "Pero no enfermaron menos días."},
    {"title": "Pruébalo si <g>te sienta bien</g>", "sub": "Si tienes problemas de corazón, consulta antes."}],
    caption="""¿Las duchas frías sirven para algo? Algo sí, pero menos de lo que se vende.

En un ensayo publicado en PLOS ONE, 3.018 personas en los Países Bajos terminaron su ducha diaria con entre 30 y 90 segundos de agua fría durante 30 días. Tuvieron un 29% menos de bajas laborales que el grupo control. Pero no enfermaron menos días: se encontraban mejor para ir a trabajar. Y daba igual cuánto durara el frío.

Si te sienta bien, adelante. Si tienes problemas de corazón, consulta antes. 🚿

¿Te atreves a terminar la ducha en frío? 👇

#longevidad #duchafria #biohacking #mitoociencia""")

P["93"] = dict(type="reel", date="2026-11-15T18:00:00", beats=[
    {"kicker": "Sueño", "title": "¿Sirve <g>recuperar</g> el finde?"},
    {"title": "Más de 38.000 suecos, <g>13 años</g>", "sub": "Estudio en el Journal of Sleep Research."},
    {"title": "≤5 h todos los días: <g>+65%</g>", "sub": "de mortalidad, en menores de 65 años."},
    {"title": "Recuperar el finde <g>compensó</g>", "sub": "Pero lo ideal es dormir bien toda la semana."}],
    caption="""¿Se puede recuperar el sueño el fin de semana? Parece que algo sí.

Un estudio publicado en el Journal of Sleep Research siguió hasta 13 años a más de 38.000 adultos suecos. En los menores de 65, quienes dormían 5 horas o menos todos los días tenían un 65% más de mortalidad que quienes dormían 6–7 horas. Pero quienes dormían poco entre semana y recuperaban el fin de semana no tenían más riesgo.

Es una asociación y no es una licencia para dormir poco: la regularidad sigue siendo lo mejor. 😴

Envíaselo a quien se pasa el sábado durmiendo.

#longevidad #sueño #descanso #mitoociencia""")

P["94"] = dict(type="carousel", date="2026-11-16T10:00:00", slides=[
    {"kind": "cover", "kicker": "Sueño", "title": "Si roncas, <g>mira esto</g>", "sub": "Casi 1.000 millones de adultos tienen apnea del sueño."},
    {"kind": "text", "kicker": "El dato", "big": "936", "title": "millones de adultos", "body": "Es la estimación mundial de personas de 30 a 69 años con apnea obstructiva del sueño. Muchos no lo saben.", "source": "Benjafield et al., Lancet Respir Med, 2019"},
    {"kind": "text", "kicker": "Señales", "title": "Ronquidos, <g>pausas</g> y cansancio", "body": "Roncar fuerte, que te digan que dejas de respirar, despertarte cansado o con dolor de cabeza y dormirte de día."},
    {"kind": "text", "kicker": "Qué hacer", "title": "Coméntalo con <g>tu médico</g>", "body": "Hay pruebas de sueño sencillas y tratamientos que funcionan. Dormir bien es uno de los pilares de la longevidad."},
    CTA],
    caption="""Si roncas fuerte y te levantas cansado, puede que no sea solo cansancio.

Una estimación publicada en The Lancet Respiratory Medicine calcula que unos 936 millones de adultos de 30 a 69 años en el mundo tienen apnea obstructiva del sueño: pausas en la respiración mientras duermes. Muchos no lo saben.

Señales: ronquidos fuertes, pausas que nota tu pareja, despertarte cansado y dormirte de día. Si te suena, coméntalo con tu médico. 😴

Etiqueta a quien ronca a tu lado (con cariño).

#longevidad #apnea #sueño #saludpreventiva""")

P["95"] = dict(type="reel", date="2026-11-16T18:00:00", beats=[
    {"kicker": "Mito", "title": "Correr <g>destroza las rodillas</g>"},
    {"title": "Más de <g>100.000 personas</g>", "sub": "Metaanálisis sobre correr y artrosis."},
    {"title": "Artrosis: <g>3,5%</g> en corredores", "sub": "10% en sedentarios y 13% en competición."},
    {"title": "Corre <g>con cabeza</g>", "sub": "Sube poco a poco y entrena fuerza."}],
    caption="""“Correr destroza las rodillas”. Mito, al menos si corres por placer.

Un metaanálisis publicado en el Journal of Orthopaedic & Sports Physical Therapy, con más de 100.000 personas, encontró artrosis de cadera o rodilla en el 3,5% de los corredores recreativos, frente al 10% de los sedentarios y el 13% de los corredores de competición.

Es observacional, pero tranquiliza: correr con cabeza no parece dañar las articulaciones. Sube el volumen poco a poco y entrena fuerza. 🏃‍♂️

Envíaselo a quien te dice que vas a acabar con las rodillas mal.

#longevidad #correr #rodillas #mitoociencia""")

P["96"] = dict(type="reel", date="2026-11-17T10:00:00", beats=[
    {"kicker": "Mito", "title": "La sal marina <g>es más sana</g>"},
    {"title": "<g>40%</g> de sodio", "sub": "La de mesa y casi todas las marinas."},
    {"title": "<g>6 de cada 10</g> creen lo contrario", "sub": "Encuesta de la American Heart Association."},
    {"title": "Reduce <g>la cantidad</g>", "sub": "Hierbas, limón y especias para dar sabor."}],
    caption="""“Uso sal marina, que es más sana”. Mito.

Según la American Heart Association, la sal de mesa y la mayoría de sales marinas tienen alrededor de un 40% de sodio. En una encuesta suya, el 61% creía que la sal marina tenía menos. No es así.

Lo que importa es cuánta sal tomas, y buena parte viene de procesados como embutidos, pan y platos preparados. Para dar sabor: hierbas, limón y especias. 🧂

Envíaselo a quien echa escamas de sal a todo.

#longevidad #sal #mitoociencia #nutricion""")

P["98"] = dict(type="carousel", date="2026-11-18T10:00:00", slides=[
    {"kind": "cover", "kicker": "Cerebro", "title": "La vacuna del zóster y <g>la demencia</g>", "sub": "Un experimento natural en Gales."},
    {"kind": "text", "kicker": "El experimento", "title": "Una fecha <g>lo decidió</g>", "body": "En 2013, Gales vacunó del herpes zóster solo a quienes habían nacido a partir del 2 de septiembre de 1933. Así se pudo comparar a personas casi iguales, separadas por semanas de edad.", "source": "Eyting et al., Nature, 2025"},
    {"kind": "text", "kicker": "El resultado", "big": "−20%", "title": "de nuevos diagnósticos de demencia", "body": "en los 7 años siguientes, en quienes pudieron vacunarse."},
    {"kind": "text", "kicker": "Qué hacer", "title": "Pregunta en <g>tu centro de salud</g>", "body": "En España se ofrece por edad y a grupos de riesgo. Falta confirmar el efecto en ensayos, pero la vacuna ya merece la pena por sí misma."},
    CTA],
    caption="""¿Una vacuna que podría proteger del deterioro cognitivo? Hay datos que apuntan a ello.

En 2013, Gales empezó a vacunar del herpes zóster solo a quienes habían nacido a partir del 2 de septiembre de 1933. Investigadores de Stanford aprovecharon ese corte para comparar a personas casi idénticas, separadas por pocas semanas de edad. En los 7 años siguientes, poder vacunarse se asoció con un 20% menos de nuevos diagnósticos de demencia. Lo publicó Nature.

Faltan ensayos que lo confirmen, pero la vacuna ya tiene sentido por sí misma: el zóster duele, y mucho. Pregunta en tu centro de salud si te toca. 💉

Envíaselo a tus padres.

#longevidad #demencia #vacunas #cerebro""")

P["99"] = dict(type="reel", date="2026-11-18T18:00:00", beats=[
    {"kicker": "Microbiota", "title": "Fermentados contra <g>la inflamación</g>"},
    {"title": "36 adultos, <g>10 semanas</g>", "sub": "Yogur, kéfir, kimchi, kombucha…"},
    {"title": "Bajaron <g>19</g> marcadores de inflamación", "sub": "Y la microbiota se volvió más diversa."},
    {"title": "Añade <g>fermentados</g> a tu día", "sub": "Naturales y sin azúcar añadido."}],
    caption="""Yogur, kéfir, chucrut, kimchi. Tu microbiota lo agradece.

En un ensayo de Stanford publicado en Cell, 36 adultos siguieron durante 10 semanas una dieta rica en fermentados o una rica en fibra. Con los fermentados, la microbiota se volvió más diversa y bajaron 19 marcadores de inflamación, entre ellos la interleucina 6. Con la fibra, en ese tiempo, no.

Es un estudio pequeño, pero prometedor. Elige fermentados naturales, sin azúcar añadido. 🥛

¿Cuál es tu fermentado favorito? 👇

#longevidad #microbiota #fermentados #nutricion""")

P["100"] = dict(type="carousel", date="2026-11-19T10:00:00", slides=[
    {"kind": "cover", "kicker": "Día Internacional del Hombre", "title": "8 hábitos, hasta <g>24 años más</g>", "sub": "719.147 veteranos de EE. UU."},
    {"kind": "text", "kicker": "El estudio", "big": "719.147", "bigsize": 180, "title": "veteranos de 40 a 99 años", "body": "Se analizaron sus hábitos y su supervivencia. Se presentó en el congreso Nutrition 2023 y aún no está publicado en revista.", "source": "Nguyen et al., Nutrition 2023"},
    {"kind": "text", "kicker": "Los 8 hábitos", "title": "Lo que <g>sumaba años</g>", "body": "Moverse · no fumar · no abusar de opioides · gestionar el estrés · comer bien · no beber en exceso · dormir bien · tener buenas relaciones."},
    {"kind": "text", "kicker": "El resultado", "big": "+24", "title": "años a los 40, en hombres", "body": "Con los 8 hábitos frente a ninguno. En mujeres, +21. Es una estimación observacional, pero cada hábito suma."},
    CTA],
    caption="""8 hábitos que, juntos, se asocian con hasta 24 años más de vida.

Investigadores del sistema de veteranos de EE. UU. analizaron a 719.147 personas. A los 40 años, los hombres con estos 8 hábitos tenían una esperanza de vida 24 años mayor que los que no tenían ninguno; las mujeres, 21 años más. Los hábitos: moverse, no fumar, no abusar de opioides, gestionar el estrés, comer bien, no beber en exceso, dormir bien y tener buenas relaciones.

Ojo: se presentó en el congreso Nutrition 2023 y aún no está publicado en revista. Es una estimación, pero la lista no tiene secretos. 💪

¿Cuántos de los 8 cumples? 👇

#longevidad #habitossaludables #diadelhombre #saludmasculina""")

P["101"] = dict(type="reel", date="2026-11-19T18:00:00", beats=[
    {"kicker": "Mito", "title": "Con la edad, <g>nada de pesas</g>"},
    {"title": "101 mujeres de <g>unos 65 años</g>", "sub": "Baja masa ósea. 8 meses, 2 sesiones de 30 min."},
    {"title": "Columna: <g>+2,9%</g> de hueso", "sub": "El grupo control perdió un 1,2%."},
    {"title": "Con técnica y <g>supervisión</g>", "sub": "Solo 1 molestia leve en 8 meses."}],
    caption="""“A tu edad, nada de pesas”. Mito.

En el ensayo LIFTMOR, publicado en el Journal of Bone and Mineral Research, 101 mujeres de unos 65 años con baja masa ósea entrenaron fuerza intensa con supervisión, 2 sesiones de 30 minutos por semana durante 8 meses. La densidad ósea de la columna subió un 2,9%, mientras el grupo control perdió un 1,2%. Y solo hubo una molestia leve de espalda.

Con buena técnica y alguien que te guíe, levantar peso protege el hueso. 🏋️‍♀️

Envíaselo a tu madre.

#longevidad #fuerza #osteoporosis #mujer""")

P["102"] = dict(type="carousel", date="2026-11-20T10:00:00", slides=[
    {"kind": "cover", "kicker": "Prevención", "title": "Moverte se asocia con menos riesgo de <g>13 cánceres</g>", "size": 88, "sub": "1,44 millones de personas."},
    {"kind": "text", "kicker": "El estudio", "big": "1,44", "title": "millones de personas", "body": "Datos de EE. UU. y Europa reunidos por el Instituto Nacional del Cáncer de EE. UU., con una mediana de 11 años de seguimiento.", "source": "Moore et al., JAMA Intern Med, 2016"},
    {"kind": "text", "kicker": "El resultado", "big": "13", "title": "tipos de cáncer con menos riesgo", "body": "Entre ellos, esófago, hígado, riñón, colon, mama y endometrio. En 7, el riesgo era al menos un 20% menor."},
    {"kind": "text", "kicker": "Con perspectiva", "title": "Con <g>cualquier peso</g>", "body": "La relación se mantuvo en personas con normopeso y con sobrepeso. Es observacional, pero suma razones para moverte."},
    CTA],
    caption="""Moverte se asocia con menos riesgo de 13 tipos de cáncer.

Un análisis del Instituto Nacional del Cáncer de EE. UU., publicado en JAMA Internal Medicine, reunió a 1,44 millones de personas seguidas una mediana de 11 años. Quienes más se movían en su tiempo libre tenían menos riesgo de 13 cánceres, como esófago, hígado, riñón, colon, mama o endometrio. En 7 de ellos, al menos un 20% menos.

Es observacional, y la relación se mantuvo con normopeso y con sobrepeso. Una razón más para moverte. 🚴‍♀️

Guárdalo y compártelo.

#longevidad #cancer #ejercicio #prevencion""")

P["103"] = dict(type="reel", date="2026-11-20T18:00:00", beats=[
    {"kicker": "Mito", "title": "Sin gluten <g>es más sano</g>"},
    {"title": "Más de <g>100.000 personas</g>", "sub": "Sin celiaquía, seguidas más de 20 años."},
    {"title": "El gluten <g>no se asoció</g> con infartos", "sub": "Y quitar integrales podría salir caro."},
    {"title": "Si eres celíaco, <g>sí</g>", "sub": "Si no, apuesta por el grano integral."}],
    caption="""“Me quito el gluten para estar más sano”. Si no eres celíaco, mito.

Un estudio de Harvard publicado en el BMJ siguió durante más de 20 años a más de 100.000 personas sin celiaquía. El gluten no se asoció con más riesgo de enfermedad coronaria. Y los autores avisan: quitarlo puede hacer que comas menos cereales integrales, que sí protegen el corazón.

Si eres celíaco o tu médico te lo indica, sin gluten. Si no, mejor integral. 🍞

Envíaselo a quien compra todo "sin gluten".

#longevidad #gluten #mitoociencia #nutricion""")

P["104"] = dict(type="reel", date="2026-11-21T10:00:00", beats=[
    {"kicker": "El dato", "title": "Dos <g>tazas de té</g> al día"},
    {"title": "498.043 personas, <g>11 años</g>", "sub": "UK Biobank, de 40 a 69 años."},
    {"title": "<g>−9 a −13%</g> de mortalidad", "sub": "Con leche o azúcar, más o menos caliente."},
    {"title": "Té sí, <g>azúcar poco</g>", "sub": "Es una asociación, no un elixir."}],
    caption="""El té de las 5 tiene algo de razón.

Un estudio del Instituto Nacional del Cáncer de EE. UU. publicado en Annals of Internal Medicine siguió 11 años a 498.043 adultos de 40 a 69 años del UK Biobank. Quienes tomaban 2 o más tazas de té al día, sobre todo negro, tenían entre un 9 y un 13% menos de riesgo de muerte. Daba igual que lo tomaran con leche, con azúcar o más o menos caliente.

Es observacional, no un elixir. Pero si te gusta, buen hábito. 🍵

¿Té o café? 👇

#longevidad #te #nutricion #habitossaludables""")

P["105"] = dict(type="reel", date="2026-11-21T18:00:00", beats=[
    {"kicker": "Truco", "title": "¿Caminas a <g>100 pasos por minuto</g>?"},
    {"title": "Ese es el ritmo <g>moderado</g>", "sub": "El que cuenta para los 150 minutos semanales."},
    {"title": "<g>130</g> pasos por minuto: <g>vigoroso</g>"},
    {"title": "Cuenta <g>15 segundos</g>", "sub": "25 pasos o más: vas a buen ritmo."}],
    caption="""¿Cómo saber si caminas lo bastante rápido? Cuenta tus pasos.

Un estudio publicado en el International Journal of Behavioral Nutrition and Physical Activity midió la intensidad de la marcha en 80 adultos de 21 a 40 años. Unos 100 pasos por minuto ya es intensidad moderada, la que cuenta para los 150 minutos semanales recomendados. A partir de unos 130, es vigorosa.

Pruébalo: cuenta los pasos en 15 segundos. Si das 25 o más, vas a buen ritmo. 👟

Cuéntanos cuántos te salen. 👇

#longevidad #caminar #pasos #movimiento""")

P["106"] = dict(type="carousel", date="2026-11-22T10:00:00", slides=[
    {"kind": "cover", "kicker": "Hábitos", "title": "Un hábito tarda <g>66 días</g>, no 21", "sub": "Y saltarte un día no lo arruina."},
    {"kind": "text", "kicker": "El estudio", "big": "96", "title": "voluntarios, 84 días", "body": "Investigadores del University College London pidieron a cada uno repetir un hábito nuevo a diario y medir cuánto les salía en automático.", "source": "Lally et al., Eur J Soc Psychol, 2010"},
    {"kind": "text", "kicker": "El resultado", "big": "66", "title": "días de mediana", "body": "Con mucha variación: de 18 a 254 días según la persona y el hábito."},
    {"kind": "text", "kicker": "La buena noticia", "title": "Saltarte un día <g>no lo rompe</g>", "body": "Fallar una vez no cambió el resultado. Empieza pequeño, átalo a algo que ya haces y no te castigues."},
    CTA],
    caption="""¿21 días para crear un hábito? Más bien 66. Y saltarte uno no pasa nada.

En un estudio del University College London publicado en el European Journal of Social Psychology, 96 voluntarios repitieron a diario un hábito nuevo durante 84 días. La mediana para que les saliera en automático fue de 66 días, con mucha variación: de 18 a 254. Y fallar un día suelto no estropeó el proceso.

Empieza pequeño, átalo a algo que ya haces y ten paciencia. 📆

¿Qué hábito vas a empezar esta semana? 👇

#longevidad #habitos #constancia #bienestar""")

P["107"] = dict(type="reel", date="2026-11-22T18:00:00", beats=[
    {"kicker": "Mito", "title": "Crujirse los nudillos <g>da artrosis</g>"},
    {"title": "215 personas de <g>50 a 89 años</g>", "sub": "Con y sin artrosis en las manos."},
    {"title": "Artrosis: <g>18%</g> frente a <g>22%</g>", "sub": "En quienes los crujían y quienes no. Sin diferencia."},
    {"title": "Cruje <g>tranquilo</g>", "sub": "Si duele o se hincha, consulta."}],
    caption="""“No te crujas los nudillos, que te va a dar artrosis”. Mito.

Un estudio publicado en el Journal of the American Board of Family Medicine comparó a 215 personas de 50 a 89 años. Tenían artrosis en las manos el 18% de quienes se crujían los nudillos y el 22% de quienes no. Sin diferencias.

Eso sí, si te duele o se hincha la articulación, consúltalo. 🖐️

Etiqueta a quien no para de crujirse los dedos.

#longevidad #articulaciones #artrosis #mitoociencia""")


def main():
    for nn, p in P.items():
        d = ROOT / ("reels" if p["type"] == "reel" else "carruseles") / nn
        d.mkdir(parents=True, exist_ok=True)
        if p["type"] == "reel":
            spec = {"type": "reel", "image": "imagen.png", "beats": p["beats"]}
        else:
            spec = {"type": "carousel", "image": "portada.png", "slides": p["slides"]}
        spec["publish"] = p["date"]
        (d / "spec.json").write_text(json.dumps(spec, ensure_ascii=False, indent=1))
        (d / "caption.txt").write_text(p["caption"].strip() + "\n")
    print(len(P), "piezas")


if __name__ == "__main__":
    main()
