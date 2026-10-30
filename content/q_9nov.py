# Quincena 9-22 nov 2026 · Healthspan Club. Datos verificados en research/facts_quincena_9nov.md
# Genera content/NN.json y content/schedule_9nov.json
import json
from pathlib import Path

D = Path(__file__).parent
END_TLW = "Medimos todo esto en The Longevity Weekend · enlace en la bio"
END_HH = "Cada martes, la noticia de longevidad de la semana"

P = []  # pieces


def car(id, date, cover, slides, caption, photo=True, end=END_TLW, **kw):
    d = {"id": id, "type": "carousel", "date": date, "cover": cover, "slides": slides, "caption": caption, "end_note": end}
    if photo:
        d["photo"] = f"img/{id}.jpg"
    d.update(kw)
    P.append(d)


def reel(id, date, frames, caption, **kw):
    d = {"id": id, "type": "reel", "date": date, "photo": f"img/{id}.jpg", "frames": frames, "caption": caption}
    d.update(kw)
    P.append(d)


# ------------------------------------------------------------------ semana 1
car("80", "2026-11-09T10:00:00",
    {"kicker": "Movember", "title": "Los hombres\nviven *5 años\nmenos*"},
    [{"kicker": "El dato", "title": "81,4 frente a\n*86,5 años*",
      "body": "Es la esperanza de vida al nacer en España en 2024, según el INE. **Más de 5 años de diferencia entre hombres y mujeres.**",
      "source": "INE, Movimiento Natural de la Población 2024"},
     {"kicker": "Por qué", "title": "Más riesgo,\n*menos médico*",
      "body": "Influye la biología, pero también los hábitos: los hombres fuman y beben más, tienen más accidentes y van menos al médico. **Eso sí se puede cambiar.**"},
     {"kicker": "Qué hacer", "title": "Tres cosas\n*este mes*",
      "body": "Mídete la tensión. Pide una analítica si hace años que no te la haces. **Y habla con alguien si no estás bien.**"},
     {"kicker": "Movember", "title": "Un bigote,\n*una conversación*",
      "body": "Movember nació para hablar de la salud de los hombres: próstata, testículos y salud mental. **Empieza por la tuya.**"}],
    "En España, los hombres viven más de 5 años menos que las mujeres.\n\nSegún el INE, la esperanza de vida al nacer en 2024 fue de 81,4 años en hombres y 86,5 en mujeres. Parte es biología. Pero otra parte son hábitos: más tabaco, más alcohol, más accidentes y menos visitas al médico.\n\nEste Movember, tres gestos: mídete la tensión, hazte una analítica si hace años que no la pides y habla con alguien si no estás bien. 🥸\n\nEnvíaselo a un hombre al que quieras ver a los 90.\n\n#longevidad #movember #saludmasculina #prevencion",
    pos="50% 25%")

reel("81", "2026-11-09T18:00:00",
     [{"kicker": "¿Mito o ciencia?", "title": "“Para bajar la\ntensión, *solo\nsirve correr*”"},
      {"stamp": "MITO", "body": "Lo que más la bajó fue el ejercicio isométrico: aguantar sin moverte."},
      {"title": "−8 puntos\n*de tensión*", "body": "De media en la máxima (y −4 en la mínima). 270 ensayos, 15.827 personas."},
      {"title": "*Espalda a la pared*,\nrodillas a 90°", "body": "Aguanta 2 minutos. Repite 4 veces, 3 días por semana."}],
     "¿Cardio para la tensión? Sí. Pero hay algo que funcionó todavía mejor.\n\nUn metaanálisis de 270 ensayos con 15.827 personas, publicado en el British Journal of Sports Medicine, comparó tipos de ejercicio. El entrenamiento isométrico (aguantar una postura sin moverte) bajó la tensión de media 8 mmHg la máxima y 4 la mínima. Y la sentadilla en pared fue de los que mejor funcionaron.\n\nPruébalo: espalda en la pared, rodillas a 90°, 2 minutos, 4 veces. Si tienes la tensión alta o problemas de corazón, consúltalo antes con tu médico. 🧱\n\nEtiqueta a quien tiene la tensión alta.\n\n#longevidad #tension #ejercicio #corazon")

reel("82", "2026-11-10T10:00:00",
     [{"kicker": "¿Mito o ciencia?", "size": 90, "title": "“Los abdominales\n*queman la grasa\nde la barriga*”"},
      {"stamp": "MITO", "body": "No puedes elegir de dónde pierdes grasa."},
      {"title": "6 semanas,\n*0 cambios*", "body": "Ni en la cintura ni en los pliegues. Ensayo con 24 adultos."},
      {"title": "Para la barriga:\n*todo el cuerpo*", "body": "Comida real, fuerza y moverte más cada día."}],
     "“Haz abdominales para quitarte la barriga”. Mito.\n\nEn un ensayo publicado en el Journal of Strength and Conditioning Research, 24 adultos hicieron 7 ejercicios de abdominales, 5 días por semana, durante 6 semanas. Resultado: la cintura y la grasa abdominal no cambiaron frente al grupo que no los hizo.\n\nLa grasa no se pierde por zonas. Para bajarla: comer mejor, entrenar fuerza de todo el cuerpo y moverte más. Los abdominales sí sirven para tener un tronco fuerte. 💪\n\nEnvíaselo a quien hace 100 abdominales cada noche.\n\n#longevidad #abdominales #mitoociencia #ejercicio")

car("83", "2026-11-10T18:00:00",
    {"kicker": "Healthspan Hoy · Noticia", "big": "42", "big_size": 320,
     "title": "Minutos de luz\nintensa al día.\n*Menos demencia.*"},
    [{"kicker": "La noticia", "title": "87.577 personas\n*con un sensor*",
      "body": "Llevaron en la muñeca un sensor que medía la luz durante 7 días. Después se las siguió **8 años**. 741 desarrollaron demencia.",
      "source": "Zheng et al., General Psychiatry, 2026"},
     {"kicker": "El resultado", "title": "Más luz,\n*menos riesgo*",
      "body": "Quienes recibían de media más de 1.000 lux de día tenían **un 16% menos de riesgo**. Y unos 42 minutos al día de luz muy intensa se asociaron con un **17% menos**.",
      "source": "Zheng et al., General Psychiatry, 2026"},
     {"kicker": "Para que te hagas una idea", "title": "Dentro de casa\n*no llega*",
      "body": "Una casa bien iluminada ronda los 300–500 lux. **Fuera, un día nublado ya supera los 1.000**, y uno soleado pasa de 10.000."},
     {"kicker": "Ojo", "title": "Con\n*perspectiva*",
      "body": "Es un estudio observacional: muestra una asociación, no que la luz prevenga la demencia. **Pero salir a la luz cada mañana no tiene contras.**"}],
    "42 minutos de luz intensa al día. Ese es el dato de la semana.\n\nUn estudio del UK Biobank con 87.577 personas, publicado en General Psychiatry, midió la luz que recibían con un sensor en la muñeca y las siguió 8 años. Quienes recibían más luz de día (más de 1.000 lux de media) tenían un 16% menos de riesgo de demencia. Y unos 42 minutos diarios de luz muy intensa se asociaron con un 17% menos. La luz por la noche no mostró relación.\n\nEs observacional, así que no demuestra causa. Pero ahora que los días se acortan, el consejo es fácil: sal fuera cada mañana, aunque esté nublado. Dentro de casa no llegas. ☀️\n\n¿Cuántos minutos pasas al aire libre al día? Te leemos. 👇\n\n#longevidad #cerebro #demencia #luznatural",
    photo=False, end=END_HH)

car("84", "2026-11-11T10:00:00",
    {"kicker": "Fuerza", "title": "Tu apretón de\nmanos *predice\ncuánto vivirás*"},
    [{"kicker": "El estudio", "title": "139.691 personas\n*en 17 países*",
      "body": "El estudio PURE midió la fuerza de agarre con un dinamómetro y siguió a los participantes unos 4 años.",
      "source": "Leong et al., The Lancet, 2015"},
     {"kicker": "El dato", "title": "Cada 5 kg menos,\n*+16% de mortalidad*",
      "body": "Y un 17% más de muerte cardiovascular. **Predijo la mortalidad mejor que la tensión arterial.**",
      "source": "Leong et al., The Lancet, 2015"},
     {"kicker": "La explicación", "title": "No es\n*la mano*",
      "body": "La fuerza de agarre es un reflejo de tu fuerza muscular general. **Lo que importa es el músculo de todo el cuerpo.**"},
     {"kicker": "Qué hacer", "title": "Entrena\n*el agarre*",
      "body": "Fuerza 2 días por semana, peso muerto, remo y paseos del granjero con peso en cada mano. **Y cuelga de una barra.**"}],
    "Tu apretón de manos dice mucho de tu salud.\n\nEn el estudio PURE, publicado en The Lancet, se midió la fuerza de agarre de 139.691 personas de 17 países. Cada 5 kg menos de fuerza se asoció con un 16% más de mortalidad y un 17% más de muerte cardiovascular. Y predijo la mortalidad mejor que la tensión arterial.\n\nNo es por la mano: es un reflejo de tu fuerza general. Entrena fuerza 2 días por semana y añade peso muerto, remo y paseos con peso en las manos. ✊\n\nGuárdalo para tu próximo entrenamiento.\n\n#longevidad #fuerza #musculo #envejecimientosaludable",
    pos="50% 40%")

reel("85", "2026-11-11T18:00:00",
     [{"kicker": "Ciencia", "title": "*1 minuto*\nque alarga\nla vida"},
      {"stamp": "CIENCIA", "body": "Ráfagas cortas de esfuerzo intenso en el día a día. Sin gimnasio."},
      {"title": "3 al día,\n*−38–40% de mortalidad*", "body": "25.241 adultos que no hacían deporte, con sensor."},
      {"title": "Escaleras rápido,\n*bolsas de la compra*", "body": "Que te falte un poco el aire. 1–2 minutos, 3 veces al día."}],
     "¿No haces deporte? Este minuto cuenta.\n\nEn un estudio del UK Biobank publicado en Nature Medicine, 25.241 adultos que no hacían ejercicio llevaron un sensor. Quienes hacían unas 3 ráfagas diarias de 1–2 minutos de esfuerzo intenso en su día a día (subir escaleras rápido, cargar la compra, apretar el paso) tenían un 38–40% menos de mortalidad y un 48–49% menos de muerte cardiovascular.\n\nEs una asociación, pero la idea es sencilla: que te falte un poco el aire, varias veces al día. ⚡\n\nEtiqueta a quien dice que no tiene tiempo.\n\n#longevidad #ejercicio #escaleras #movimiento")

car("86", "2026-11-12T10:00:00",
    {"kicker": "Mente", "title": "El ejercicio\n*también trata\nla depresión*"},
    [{"kicker": "El estudio", "title": "218 ensayos,\n*14.170 personas*",
      "body": "Un metaanálisis en red publicado en el BMJ comparó distintos tipos de ejercicio en personas con depresión.",
      "source": "Noetel et al., BMJ, 2024"},
     {"kicker": "Los que más ayudaron", "title": "Caminar, yoga\n*y fuerza*",
      "body": "Caminar o correr, el yoga y el entrenamiento de fuerza fueron los que más redujeron los síntomas. **Cuanto más intenso, mejor efecto.**",
      "source": "Noetel et al., BMJ, 2024"},
     {"kicker": "Ojo", "title": "Suma,\n*no sustituye*",
      "body": "La calidad de la evidencia es baja: hacen falta ensayos mejores. **Si estás en tratamiento, no lo dejes: el ejercicio se añade.**"},
     {"kicker": "Qué hacer", "title": "Empieza\n*por andar*",
      "body": "Un paseo rápido de 20–30 minutos, mejor con alguien. **Y pide ayuda profesional si lo necesitas.**"}],
    "Moverte también cuida tu cabeza.\n\nUn metaanálisis de 218 ensayos con 14.170 personas, publicado en el BMJ, comparó tipos de ejercicio en personas con depresión. Caminar o correr, el yoga y la fuerza fueron los que más redujeron los síntomas, y cuanto más intenso, mejor.\n\nCon perspectiva: la calidad de la evidencia es baja y el ejercicio suma, no sustituye. Si estás en tratamiento, no lo dejes. Y si lo estás pasando mal, pide ayuda. 💚\n\nEnvíaselo a alguien que necesite un paseo hoy.\n\n#longevidad #saludmental #ejercicio #bienestar",
    pos="50% 30%")

reel("87", "2026-11-12T18:00:00",
     [{"kicker": "¿Mito o ciencia?", "title": "“Un refresco\nal día *no hace\nnada*”"},
      {"stamp": "MITO", "body": "Cuantos más refrescos, más mortalidad. Dosis a dosis."},
      {"title": "2 al día,\n*+21% de mortalidad*", "body": "Y +31% de muerte cardiovascular. 118.363 adultos, hasta 34 años."},
      {"title": "Agua con gas\n*y limón*", "body": "Si te gustan las burbujas, sin azúcar."}],
     "Los refrescos no son un capricho inocente.\n\nEn un estudio de Harvard con 118.363 adultos seguidos hasta 34 años, publicado en Circulation, quienes tomaban 2 o más refrescos azucarados al día tenían un 21% más de mortalidad y un 31% más de muerte cardiovascular que quienes casi no los tomaban. Y el riesgo subía con cada dosis.\n\nEs una asociación, pero muy consistente. Cámbialos por agua, agua con gas y limón o infusiones frías. 🥤\n\nEnvíaselo a quien come con refresco.\n\n#longevidad #azucar #refrescos #nutricion")

car("88", "2026-11-13T10:00:00",
    {"kicker": "Movilidad", "title": "Una caída\n*se entrena*\nantes de que pase"},
    [{"kicker": "El problema", "title": "Las caídas, *el\nenemigo silencioso*",
      "body": "Con la edad, las caídas son una de las primeras causas de lesión y de pérdida de autonomía. **Y muchas se pueden prevenir.**"},
     {"kicker": "El estudio", "title": "108 ensayos,\n*23.407 personas*",
      "body": "Una revisión Cochrane analizó el ejercicio para prevenir caídas en mayores que viven en casa.",
      "source": "Sherrington et al., Cochrane, 2019"},
     {"kicker": "El resultado", "title": "*−24%*\nde caídas",
      "body": "Con ejercicios de equilibrio y funcionales. **Evidencia de certeza alta.**",
      "source": "Sherrington et al., Cochrane, 2019"},
     {"kicker": "Qué hacer", "title": "Equilibrio\n*cada día*",
      "body": "Lávate los dientes a una pierna, levántate de la silla sin manos y camina en línea recta. **Y añade fuerza de piernas.**"}],
    "Las caídas no son mala suerte: se pueden entrenar.\n\nUna revisión Cochrane de 108 ensayos con 23.407 mayores que viven en casa encontró que los ejercicios de equilibrio y funcionales reducen las caídas un 24%. La certeza de la evidencia es alta.\n\nEmpieza hoy: lávate los dientes a una pierna (cerca de un apoyo), levántate de la silla sin usar las manos y entrena fuerza de piernas 2 veces por semana. 🦶\n\nEnvíaselo a tus padres.\n\n#longevidad #equilibrio #caidas #envejecimientosaludable",
    pos="50% 35%")

reel("89", "2026-11-13T18:00:00",
     [{"kicker": "¿Mito o ciencia?", "title": "“El cardio en\nayunas *quema\nmás grasa*”"},
      {"stamp": "MITO", "body": "La misma grasa perdida, en ayunas o habiendo comido."},
      {"title": "4 semanas,\n*sin diferencias*", "body": "Mismo cardio y misma dieta. Solo cambió el momento de comer."},
      {"title": "Lo que cuenta:\n*el total*", "body": "Entrena cuando mejor te siente."}],
     "“Entrena en ayunas para quemar más grasa”. Mito.\n\nEn un ensayo publicado en el Journal of the International Society of Sports Nutrition, 20 mujeres hicieron 1 hora de cardio 3 veces por semana durante 4 semanas, con la misma dieta. Unas entrenaban en ayunas y otras después de comer. Las dos perdieron peso y grasa, y no hubo diferencias entre grupos.\n\nEs un estudio pequeño y corto, pero encaja con lo demás: lo que cuenta es el total. Entrena cuando mejor te siente. 🏃\n\nEnvíaselo a quien sale a correr sin desayunar \"para quemar\".\n\n#longevidad #ayuno #cardio #mitoociencia")

car("90", "2026-11-14T10:00:00",
    {"kicker": "Día Mundial de la Diabetes", "title": "La prediabetes\n*tiene vuelta\natrás*"},
    [{"kicker": "El estudio", "title": "3.234 personas\n*con prediabetes*",
      "body": "El Diabetes Prevention Program comparó cambios de hábitos, metformina y placebo durante casi 3 años.",
      "source": "Knowler et al., NEJM, 2002"},
     {"kicker": "El resultado", "title": "Hábitos:\n*−58% de diabetes*",
      "body": "Más del doble que el fármaco, que la redujo un 31%. **Con dos objetivos sencillos.**",
      "source": "Knowler et al., NEJM, 2002"},
     {"kicker": "Los objetivos", "title": "−7% de peso,\n*150 minutos*",
      "body": "Perder un 7% del peso y moverse al menos 150 minutos a la semana. **No hacía falta más.**"},
     {"kicker": "Qué hacer", "title": "Mírate\n*la glucosa*",
      "body": "Si tienes barriga, antecedentes familiares o hace años que no te haces una analítica, **pide que te miren la glucosa y la hemoglobina glicada.**"}],
    "La prediabetes tiene vuelta atrás.\n\nEn el Diabetes Prevention Program, publicado en el NEJM, 3.234 personas con la glucosa alterada siguieron un programa de hábitos, tomaron metformina o placebo. Los objetivos del programa eran perder un 7% del peso y moverse 150 minutos a la semana. Resultado en casi 3 años: un 58% menos de diabetes con los hábitos y un 31% menos con el fármaco.\n\nHoy es el Día Mundial de la Diabetes. Si hace años que no te haces una analítica, pídela. 🩸\n\nCompártelo con quien tenga \"el azúcar un poco alto\".\n\n#longevidad #diabetes #prediabetes #glucosa",
    pos="50% 40%")

reel("91", "2026-11-14T18:00:00",
     [{"kicker": "¿Mito o ciencia?", "title": "“El azúcar\nmoreno *es más\nsano*”"},
      {"stamp": "MITO", "body": "Es azúcar con un poco de melaza. Casi lo mismo."},
      {"title": "194 frente a\n*190 kcal*", "body": "Por cada 50 g. Y una cucharada da menos del 1% de los minerales que necesitas."},
      {"title": "Menos azúcar,\n*del color que sea*", "body": "Y más fruta entera."}],
     "“Uso azúcar moreno porque es más sano”. Mito.\n\nEl azúcar moreno es azúcar con un poco de melaza, que le da el color y el sabor. Según el Consejo Europeo de Información sobre la Alimentación (EUFIC), 50 g de blanco aportan unas 194 kcal y 50 g de moreno, unas 190. Y una cucharada de moreno da menos del 1% de los minerales que necesitas al día.\n\nEl problema no es el color: es la cantidad. Reduce el azúcar añadido, del tipo que sea. 🥄\n\nEnvíaselo a quien pide el sobre de azúcar moreno.\n\n#longevidad #azucar #mitoociencia #nutricion")

reel("92", "2026-11-15T10:00:00",
     [{"kicker": "¿Mito o ciencia?", "title": "“Las duchas\nfrías *te hacen\nenfermar menos*”"},
      {"stamp": "A MEDIAS", "size": 120, "body": "No enfermaron menos. Pero faltaron menos al trabajo."},
      {"title": "*−29%*\nde bajas", "body": "Ensayo con 3.018 adultos. Terminar la ducha con 30–90 s de agua fría."},
      {"title": "Si te gusta,\n*30 segundos*", "body": "Al final de tu ducha. Si tienes problemas de corazón, consulta antes."}],
     "¿Las duchas frías te hacen enfermar menos? A medias.\n\nEn un ensayo publicado en PLOS ONE, 3.018 adultos terminaron su ducha caliente con 30, 60 o 90 segundos de agua fría durante un mes. No enfermaron menos días. Pero pidieron un 29% menos de bajas laborales que el grupo que no lo hizo. Sin efectos adversos graves.\n\nSi te gusta, prueba con 30 segundos al final de la ducha. Si tienes problemas de corazón, consúltalo antes. 🚿\n\nEtiqueta a quien no se atrevería.\n\n#longevidad #duchafria #biohacking #mitoociencia")

reel("93", "2026-11-15T18:00:00",
     [{"kicker": "¿Mito o ciencia?", "title": "“El sueño\n*no se recupera\nel finde*”"},
      {"stamp": "A MEDIAS", "size": 120, "body": "Mejor no deberlo. Pero recuperar parece ayudar."},
      {"title": "Dormir poco siempre:\n*+65% de mortalidad*", "body": "En menores de 65. Dormir poco entre semana y recuperar el finde: sin diferencia. 43.880 suecos."},
      {"title": "Primero,\n*la regularidad*", "body": "Si un día no puedes, recupera. Pero no lo conviertas en tu rutina."}],
     "¿Sirve recuperar sueño el fin de semana? A medias.\n\nEn un estudio sueco con 43.880 personas seguidas 13 años, publicado en el Journal of Sleep Research, los menores de 65 que dormían 5 horas o menos todos los días tenían un 65% más de mortalidad que quienes dormían 6–7. Pero quienes dormían poco entre semana y recuperaban el finde no tenían más riesgo.\n\nEs una asociación. Lo ideal sigue siendo dormir lo suficiente y con horarios regulares. Si una semana no puedes, recupera. 😴\n\nEnvíaselo a quien vive con sueño atrasado.\n\n#longevidad #sueño #descanso #mitoociencia")

# ------------------------------------------------------------------ semana 2
car("94", "2026-11-16T10:00:00",
    {"kicker": "Sueño", "title": "Si roncas,\n*mira esto*"},
    [{"kicker": "El dato", "title": "936 millones\n*de adultos*",
      "body": "Tienen apnea del sueño en el mundo, entre los 30 y los 69 años. **425 millones, moderada o grave.**",
      "source": "Benjafield et al., Lancet Respir Med, 2019"},
     {"kicker": "Qué es", "title": "Pausas\n*al respirar*",
      "body": "La vía aérea se cierra mientras duermes y el oxígeno baja una y otra vez. **La mayoría no lo sabe.**"},
     {"kicker": "Las señales", "title": "Ronquidos,\n*pausas, cansancio*",
      "body": "Roncar fuerte, que te digan que dejas de respirar, despertarte cansado o dormirte de día. **Y la tensión alta difícil de controlar.**"},
     {"kicker": "Qué hacer", "title": "Pide\n*un estudio*",
      "body": "Cuéntaselo a tu médico: una prueba de sueño lo confirma. **Tiene tratamiento, y se nota.**"}],
    "Si roncas fuerte, esto te interesa.\n\nUn análisis publicado en The Lancet Respiratory Medicine estimó que 936 millones de adultos de 30 a 69 años tienen apnea del sueño en el mundo, y 425 millones de forma moderada o grave. La mayoría no lo sabe.\n\nSeñales: roncar fuerte, pausas al respirar mientras duermes, despertarte cansado, dormirte de día o tener la tensión alta difícil de controlar. Si te suena, cuéntaselo a tu médico: una prueba de sueño lo confirma y tiene tratamiento. 😴\n\nEnvíaselo a quien no te deja dormir.\n\n#longevidad #sueño #apnea #ronquidos",
    pos="50% 40%")

reel("95", "2026-11-16T18:00:00",
     [{"kicker": "¿Mito o ciencia?", "title": "“Correr\n*destroza las\nrodillas*”"},
      {"stamp": "MITO", "body": "Correr por afición se asoció con menos artrosis, no más."},
      {"title": "3,5% frente\n*a 10,2%*", "body": "Artrosis de cadera o rodilla: corredores frente a sedentarios. 114.829 personas."},
      {"title": "Empieza suave,\n*sube poco a poco*", "body": "Y entrena fuerza de piernas."}],
     "“No corras, que te vas a cargar las rodillas”. Mito.\n\nUn metaanálisis de 17 estudios con 114.829 personas, publicado en el Journal of Orthopaedic & Sports Physical Therapy, encontró artrosis de cadera o rodilla en el 3,5% de los corredores por afición, frente al 10,2% de las personas sedentarias. En corredores de competición subía al 13,3%.\n\nCorrer con cabeza no castiga tus articulaciones: empieza suave, sube poco a poco y entrena fuerza de piernas. 🏃‍♂️\n\nEnvíaselo a quien te dice que correr es malo.\n\n#longevidad #correr #rodillas #mitoociencia")

reel("96", "2026-11-17T10:00:00",
     [{"kicker": "¿Mito o ciencia?", "title": "“La sal marina\n*es más sana*”"},
      {"stamp": "MITO", "body": "Tiene prácticamente el mismo sodio que la de mesa."},
      {"title": "Alrededor de\n*un 40% de sodio*", "body": "En las dos. Sus minerales son trazas."},
      {"title": "Menos sal,\n*más hierbas*", "body": "Limón, especias y ajo dan sabor sin sodio."}],
     "“Uso sal marina, que es más sana”. Mito.\n\nSegún la American Heart Association, la sal de mesa y la mayoría de sales marinas tienen alrededor de un 40% de sodio. Los minerales de la marina están en cantidades tan pequeñas que no aportan nada que no te dé una dieta normal.\n\nEl problema es la cantidad, sobre todo la que viene escondida en pan, embutidos y comida preparada. Prueba con limón, hierbas y especias. 🧂\n\nEnvíaselo a quien compra sal marina «porque es más sana».\n\n#longevidad #sal #tension #mitoociencia")

car("98", "2026-11-18T10:00:00",
    {"kicker": "Cerebro", "title": "Una vacuna\nque podría\n*proteger tu cerebro*"},
    [{"kicker": "El estudio", "title": "Un experimento\n*natural en Gales*",
      "body": "La vacuna del herpes zóster se ofreció solo a quienes nacieron a partir del 2 de septiembre de 1933. **Personas casi iguales, con y sin vacuna.**",
      "source": "Eyting et al., Nature, 2025"},
     {"kicker": "El resultado", "title": "*−20%*\nde demencia",
      "body": "En 7 años, los que pudieron vacunarse tuvieron un 20% menos de nuevos diagnósticos de demencia. **Más claro en mujeres.**",
      "source": "Eyting et al., Nature, 2025"},
     {"kicker": "Ojo", "title": "Prometedor,\n*no definitivo*",
      "body": "Es un diseño muy sólido, pero hacen falta ensayos que lo confirmen. **La vacuna, además, protege del herpes zóster, que es muy doloroso.**"},
     {"kicker": "Qué hacer", "title": "Pregunta\n*en tu centro*",
      "body": "En España se ofrece a partir de cierta edad o con algunas enfermedades. **Pregunta si te toca.**"}],
    "Una vacuna que podría proteger tu cerebro.\n\nEn Gales, la vacuna del herpes zóster se ofreció solo a quienes habían nacido a partir del 2 de septiembre de 1933. Eso creó un experimento natural: personas casi iguales, unas con vacuna y otras sin ella. El estudio, publicado en Nature, encontró que en 7 años los que pudieron vacunarse tuvieron un 20% menos de nuevos diagnósticos de demencia, con un efecto más claro en mujeres.\n\nEs prometedor, pero faltan ensayos que lo confirmen. Pregunta en tu centro de salud si te corresponde. 💉\n\nEnvíaselo a tus padres.\n\n#longevidad #demencia #vacunas #cerebro",
    pos="50% 35%")

reel("99", "2026-11-18T18:00:00",
     [{"kicker": "Ciencia", "title": "Yogur, kéfir\n*y chucrut*"},
      {"stamp": "CIENCIA", "body": "Más fermentados, más variedad de bacterias en tu intestino."},
      {"title": "Más diversidad,\n*menos inflamación*", "body": "Ensayo de Stanford con 36 adultos. La fibra sola no lo consiguió."},
      {"title": "Una ración\n*al día*", "body": "Yogur natural, kéfir, chucrut o encurtidos sin azúcar."}],
     "Tu intestino también come.\n\nEn un ensayo de Stanford publicado en Cell, 36 adultos siguieron una dieta rica en fermentados o rica en fibra. Con los fermentados (yogur, kéfir, chucrut, kimchi), la diversidad de su microbiota fue subiendo y bajaron varios marcadores de inflamación. Con la fibra, la diversidad no cambió en ese tiempo.\n\nEs un estudio pequeño, pero apunta en una dirección fácil: añade un fermentado al día, sin azúcar. 🥛\n\nGuárdalo para tu próxima compra.\n\n#longevidad #microbiota #fermentados #nutricion")

car("100", "2026-11-19T10:00:00",
    {"kicker": "Día Internacional del Hombre", "title": "8 hábitos,\n*hasta 24 años\nmás de vida*"},
    [{"kicker": "El estudio", "title": "719.147\n*veteranos*",
      "body": "El Million Veteran Program de EE. UU. calculó cuánto vivía la gente según cuántos hábitos sanos tenía.",
      "source": "Nguyen et al., Am J Clin Nutr, 2024"},
     {"kicker": "Los 8 hábitos", "title": "Lo de\n*siempre*",
      "body": "No fumar, moverse, no beber en exceso, dormir bien, comer bien, gestionar el estrés, cuidar las relaciones **y no tener adicción a los opioides.**"},
     {"kicker": "El resultado", "title": "*+24 años* ellos,\n+20,5 ellas",
      "body": "Es la esperanza de vida extra a los 40 años con los 8 hábitos frente a ninguno. **Cada hábito suma.**",
      "source": "Nguyen et al., Am J Clin Nutr, 2024"},
     {"kicker": "Ojo", "title": "Con\n*perspectiva*",
      "body": "Es una estimación en veteranos, con hábitos declarados por ellos. **Pero el mensaje es claro: no hace falta hacerlo todo para ganar.**"}],
    "8 hábitos. Hasta 24 años más de vida.\n\nUn estudio con 719.147 veteranos de EE. UU., publicado en el American Journal of Clinical Nutrition, calculó la esperanza de vida según 8 hábitos: no fumar, moverse, no beber en exceso, dormir bien, comer bien, gestionar el estrés, cuidar las relaciones y no tener adicción a los opioides. Con los 8 frente a ninguno, a los 40 años: 24 años más en hombres y 20,5 en mujeres.\n\nEs una estimación y en un grupo concreto, pero cada hábito sumaba. Hoy, Día Internacional del Hombre, elige uno y empieza. 💪\n\n¿Cuántos de los 8 cumples? Te leemos. 👇\n\n#longevidad #habitos #saludmasculina #diadelhombre",
    pos="50% 30%")

reel("101", "2026-11-19T18:00:00",
     [{"kicker": "¿Mito o ciencia?", "title": "“A partir de\ncierta edad, *nada\nde pesas*”"},
      {"stamp": "MITO", "body": "Bien supervisadas, las pesas fortalecieron el hueso en mujeres de 65 años."},
      {"title": "+2,9% de hueso\n*en la columna*", "body": "Frente a −1,2% sin entrenar. Mujeres de 65 años con baja masa ósea, 8 meses."},
      {"title": "Fuerza,\n*con técnica*", "body": "2 sesiones de 30 minutos a la semana. Con un profesional."}],
     "“A tu edad, nada de pesas”. Mito.\n\nEn el ensayo LIFTMOR, publicado en el Journal of Bone and Mineral Research, participaron 101 mujeres de unos 65 años con baja masa ósea. La mitad entrenó fuerza intensa y supervisada 2 veces por semana, 30 minutos, durante 8 meses. Su densidad ósea en la columna subió un 2,9%, mientras en el grupo control bajó un 1,2%. Solo hubo un efecto adverso leve.\n\nLa clave es la técnica y la supervisión. Si tienes osteoporosis, empieza con un profesional. 🏋️‍♀️\n\nEnvíaselo a tu madre.\n\n#longevidad #fuerza #osteoporosis #mitoociencia")

car("102", "2026-11-20T10:00:00",
    {"kicker": "Movimiento", "title": "Moverte se asocia\ncon menos riesgo de\n*13 tipos de cáncer*"},
    [{"kicker": "El estudio", "title": "1,44 millones\n*de personas*",
      "body": "12 estudios de EE. UU. y Europa compararon la actividad física en el tiempo libre con 26 tipos de cáncer.",
      "source": "Moore et al., JAMA Intern Med, 2016"},
     {"kicker": "El resultado", "title": "Menos riesgo\n*en 13 de 26*",
      "body": "Entre los más y los menos activos: **−42% en esófago, −27% en hígado, −26% en pulmón, −23% en riñón, −16% en colon.**",
      "source": "Moore et al., JAMA Intern Med, 2016"},
     {"kicker": "Ojo", "title": "Con\n*perspectiva*",
      "body": "Es una asociación, y en algunos cánceres influye el peso. **Pero 10 de las 13 relaciones se mantuvieron al tener en cuenta el peso.**"},
     {"kicker": "Qué hacer", "title": "150 minutos\n*a la semana*",
      "body": "Lo que recomienda la OMS, como mínimo. **Camina rápido, pedalea, nada o entrena: lo que vayas a mantener.**"}],
    "Moverte también es prevenir el cáncer.\n\nUn análisis de 12 estudios con 1,44 millones de personas, publicado en JAMA Internal Medicine, encontró que los más activos en su tiempo libre tenían menos riesgo en 13 de los 26 tipos de cáncer estudiados: un 42% menos de cáncer de esófago, 27% de hígado, 26% de pulmón, 23% de riñón y 16% de colon, entre otros.\n\nEs una asociación, pero muy amplia. Apunta a 150 minutos a la semana como mínimo, de lo que te guste. 🚴‍♀️\n\nCompártelo con quien dice que el ejercicio es solo para adelgazar.\n\n#longevidad #cancer #ejercicio #prevencion",
    pos="50% 35%")

reel("103", "2026-11-20T18:00:00",
     [{"kicker": "¿Mito o ciencia?", "title": "“Quitar el gluten\n*es más sano*”"},
      {"stamp": "MITO", "body": "Sin celiaquía, no se ha visto que proteja tu corazón."},
      {"title": "110.017 personas,\n*26 años*", "body": "Más o menos gluten: el mismo riesgo de infarto."},
      {"title": "Lo que sí cuenta:\n*integrales*", "body": "Quitar el gluten puede quitarte cereales integrales."}],
     "“Como sin gluten porque es más sano”. Mito (si no eres celíaco).\n\nEn un estudio de Harvard con 110.017 adultos sin celiaquía seguidos 26 años, publicado en el BMJ, la cantidad de gluten no se relacionó con el riesgo de infarto. Y los autores avisan: evitarlo sin necesidad puede hacerte comer menos cereales integrales, que sí se asocian con menos riesgo.\n\nSi sospechas celiaquía, no lo quites antes de hacerte las pruebas. 🌾\n\nEnvíaselo a quien compra todo \"sin gluten\".\n\n#longevidad #gluten #nutricion #mitoociencia")

reel("104", "2026-11-21T10:00:00",
     [{"kicker": "Ciencia", "title": "*2 tazas de té*\nal día"},
      {"stamp": "CIENCIA", "body": "Té negro y mortalidad: una asociación modesta pero clara."},
      {"title": "*−13%*\nde mortalidad", "body": "Con 2–3 tazas al día. 498.043 personas del UK Biobank, 11 años."},
      {"title": "Sin azúcar\n*y sin prisa*", "body": "Y si te quita el sueño, antes de comer."}],
     "¿Eres más de té? Buenas noticias.\n\nEn un estudio del UK Biobank con 498.043 personas seguidas 11 años, publicado en Annals of Internal Medicine, quienes tomaban 2–3 tazas de té al día (sobre todo negro) tenían un 13% menos de mortalidad que quienes no tomaban. Daba igual si también tomaban café.\n\nEs una asociación y el efecto es modesto. Tómalo sin azúcar, y si te quita el sueño, mejor antes de comer. 🍵\n\nEtiqueta a tu compañero de té.\n\n#longevidad #te #nutricion #habitossaludables",
     top=0, pos="50% 80%")

reel("105", "2026-11-21T18:00:00",
     [{"kicker": "Ciencia", "title": "¿Caminas a\n*100 pasos\npor minuto*?"},
      {"stamp": "CIENCIA", "body": "Es la cadencia que marca el paso a intensidad moderada."},
      {"title": "100 pasos/min:\n*moderada*", "body": "130: vigorosa. Estudio de laboratorio con 76 adultos."},
      {"title": "Cuenta 15 segundos:\n*25 pasos*", "body": "Si llegas, estás caminando con intensidad."}],
     "No es solo cuánto caminas. Es a qué ritmo.\n\nEn un estudio de laboratorio con 76 adultos, publicado en el International Journal of Behavioral Nutrition and Physical Activity, caminar a unos 100 pasos por minuto marcó la intensidad moderada, la que cuenta para los 150 minutos semanales. Y 130 pasos por minuto, la vigorosa.\n\nPruébalo: cuenta tus pasos durante 15 segundos. Si llegas a 25, vas bien. 👟\n\nEtiqueta a quien camina demasiado despacio.\n\n#longevidad #caminar #pasos #movimiento",
     top=0, pos="50% 85%")

car("106", "2026-11-22T10:00:00",
    {"kicker": "Hábitos", "title": "Un hábito tarda\n*66 días*,\nno 21"},
    [{"kicker": "El estudio", "title": "96 personas,\n*un hábito nuevo*",
      "body": "Eligieron algo sencillo (beber agua, comer fruta, correr) y lo repitieron cada día durante 12 semanas.",
      "source": "Lally et al., Eur J Soc Psychol, 2010"},
     {"kicker": "El resultado", "title": "De media,\n*66 días*",
      "body": "Es lo que tardó en volverse automático. **Pero varió mucho: de 18 a unos 254 días.**",
      "source": "Lally et al., Eur J Soc Psychol, 2010"},
     {"kicker": "La buena noticia", "title": "Fallar un día\n*no lo rompe*",
      "body": "Saltarse un día no afectó al resultado. **Lo que cuenta es volver al día siguiente.**"},
     {"kicker": "Qué hacer", "title": "Pequeño\n*y diario*",
      "body": "Ata el hábito a algo que ya haces: después del café, 10 sentadillas. **Y date 2 meses, no 3 semanas.**"}],
    "Los 21 días para crear un hábito son un mito.\n\nEn un estudio publicado en el European Journal of Social Psychology, 96 personas eligieron un hábito sencillo y lo repitieron cada día durante 12 semanas. De media tardaron 66 días en hacerlo de forma automática, con mucha variación: de 18 a unos 254 días. Y saltarse un día no estropeaba el resultado.\n\nEmpieza pequeño, átalo a algo que ya haces y date 2 meses, no 3 semanas. 📅\n\n¿Qué hábito empiezas hoy? Cuéntanoslo. 👇\n\n#longevidad #habitos #constancia #bienestar",
    pos="50% 35%")

reel("107", "2026-11-22T18:00:00",
     [{"kicker": "¿Mito o ciencia?", "title": "“Crujirte los\nnudillos *da\nartrosis*”"},
      {"stamp": "MITO", "body": "No se encontró relación con la artrosis de la mano."},
      {"title": "18,1% frente\n*a 21,5%*", "body": "Artrosis en quienes se crujen y en quienes no. 215 personas de 50 a 89 años."},
      {"title": "Puedes crujir\n*tranquilo*", "body": "Si duele o se hincha, eso sí, consulta."}],
     "“No te crujas los nudillos, que te va a dar artrosis”. Mito.\n\nEn un estudio publicado en el Journal of the American Board of Family Medicine, con 215 personas de 50 a 89 años y radiografía de la mano, la artrosis apareció en el 18,1% de quienes se crujían los nudillos y en el 21,5% de quienes no. Ni los años ni la frecuencia cambiaban el resultado.\n\nPuedes seguir haciéndolo. Si te duele o se hincha la articulación, consulta. 🤚\n\nEtiqueta a quien no para de crujirse los dedos.\n\n#longevidad #articulaciones #mitoociencia #salud")

for d in P:
    (D / f"{d['id']}.json").write_text(json.dumps(d, ensure_ascii=False, indent=1))
(D / "schedule_9nov.json").write_text(json.dumps([{k: d[k] for k in ("id", "type", "date")} for d in P], ensure_ascii=False, indent=1))
print(len(P), "piezas")
