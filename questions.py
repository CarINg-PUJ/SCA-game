patients = [
    {
        "name": "Juan Pérez", "age": 58, "gender": "Masculino",
        "symptoms": "Dolor torácico opresivo de 45 minutos, sudoración",
        "vitals": {
            'FC': { 'value': '110 lpm', 'critical': True },
            'PA': { 'value': '90/60 mmHg', 'critical': True },
            'SatO2': { 'value': '92%', 'critical': True },
            'Temp': { 'value': '36.5°C', 'critical': False }
        }
    },
    {
        "name": "María González", "age": 65, "gender": "Femenino",
        "symptoms": "Dolor torácico atípico, náuseas, fatiga",
        "vitals": {
            'FC': { 'value': '95 lpm', 'critical': False },
            'PA': { 'value': '140/90 mmHg', 'critical': False },
            'SatO2': { 'value': '94%', 'critical': False },
            'Temp': { 'value': '36.8°C', 'critical': False }
        }
    },
    {
        "name": "Carlos Ruiz", "age": 72, "gender": "Masculino",
        "symptoms": "Disnea y molestias torácicas leves de 6 horas",
        "vitals": {
            'FC': { 'value': '88 lpm', 'critical': False },
            'PA': { 'value': '160/95 mmHg', 'critical': False },
            'SatO2': { 'value': '96%', 'critical': False },
            'Temp': { 'value': '37°C', 'critical': False }
        }
    }
]

question_bank = [
    {
        "title": "Evaluación Inicial STEMI", "type": "stemi",
        "scenario": "Paciente con dolor torácico intenso de inicio súbito hace 30 minutos",
        "ecg": "⚡ ECG: Elevación del ST >2mm en V1-V4 (STEMI anterior) ⚡",
        "question": "¿Cuál es tu primera acción según AHA 2025?",
        "options": [
            { "text": "ECG de 12 derivaciones en <10 minutos", "correct": True, "feedback": "Correcto! ECG <10min es clase I AHA 2025" },
            { "text": "Troponinas inmediatas", "correct": False, "feedback": "El ECG tiene prioridad absoluta" },
            { "text": "Rx tórax", "correct": False, "feedback": "No retrasar ECG por imagen" },
            { "text": "TC torácico", "correct": False, "feedback": "ECG es la prioridad" }
        ]
    },
    {
        "title": "Protocolo MONA STEMI", "type": "stemi",
        "scenario": "STEMI confirmado, dolor 9/10, SatO2 88%",
        "ecg": "⚡ STEMI inferior (II, III, aVF) ⚡",
        "question": "¿Protocolo MONA correcto según AHA 2025?",
        "options": [
            { "text": "Morfina PRN + O2 si SatO2<90% + Nitroglicerina + ASA 325mg", "correct": True, "feedback": "Perfecto! MONA actualizado AHA 2025" },
            { "text": "Morfina + O2 100% + Nitroglicerina + ASA", "correct": False, "feedback": "O2 solo si SatO2<90%" },
            { "text": "Solo analgesia", "correct": False, "feedback": "Protocolo incompleto" },
            { "text": "MONA sin morfina", "correct": False, "feedback": "Morfina PRN para dolor severo" }
        ]
    },
    {
        "title": "Tiempo Puerta-Balón", "type": "stemi",
        "scenario": "STEMI con síntomas de 1 hora, hospital con ICP disponible",
        "ecg": "⚡ STEMI anterior extenso ⚡",
        "question": "¿Tiempo objetivo puerta-balón AHA 2025?",
        "options": [
            { "text": "<90 minutos", "correct": True, "feedback": "Correcto! Meta <90min para ICP primaria" },
            { "text": "<120 minutos", "correct": False, "feedback": "Muy tardío para ICP primaria" },
            { "text": "<60 minutos", "correct": False, "feedback": "Ideal pero no siempre realista" },
            { "text": "<180 minutos", "correct": False, "feedback": "Inaceptablemente tardío" }
        ]
    },
    {
        "title": "Fibrinólisis vs ICP", "type": "stemi",
        "scenario": "STEMI, hospital sin ICP, transferencia tomaría 3 horas",
        "ecg": "⚡ STEMI de 2 horas de evolución ⚡",
        "question": "¿Estrategia de reperfusión óptima?",
        "options": [
            { "text": "Fibrinólisis inmediata", "correct": True, "feedback": "Correcto! Si transferencia >120min, fibrinólisis" },
            { "text": "Transferir para ICP", "correct": False, "feedback": "Tiempo excesivo, >120min" },
            { "text": "Tratamiento médico", "correct": False, "feedback": "Reperfusión es mandatoria" },
            { "text": "Esperar 6 horas", "correct": False, "feedback": "Ventana terapéutica crítica" }
        ]
    },
    {
        "title": "Contraindicaciones Fibrinólisis", "type": "stemi",
        "scenario": "STEMI, paciente con ACV hemorrágico hace 2 meses",
        "ecg": "⚡ STEMI lateral (I, aVL, V5-V6) ⚡",
        "question": "¿Conducta apropiada?",
        "options": [
            { "text": "ICP primaria urgente", "correct": True, "feedback": "Correcto! ACV hemorrágico contraindica fibrinólisis" },
            { "text": "Fibrinólisis con alteplase", "correct": False, "feedback": "Contraindicación absoluta" },
            { "text": "Tratamiento médico conservador", "correct": False, "feedback": "Requiere reperfusión" },
            { "text": "Fibrinólisis con reteplase", "correct": False, "feedback": "Cualquier fibrinolítico está contraindicado" }
        ]
    },
    {
        "title": "Antiagregación Dual STEMI", "type": "stemi",
        "scenario": "STEMI, preparando ICP primaria",
        "ecg": "⚡ STEMI posterior (V7-V9) ⚡",
        "question": "¿Antiagregación dual óptima pre-ICP?",
        "options": [
            { "text": "ASA 325mg + Ticagrelor 180mg", "correct": True, "feedback": "Perfecto! DAPT potente para STEMI" },
            { "text": "ASA 81mg + Clopidogrel 75mg", "correct": False, "feedback": "Dosis insuficientes para agudo" },
            { "text": "Solo ASA 325mg", "correct": False, "feedback": "Monoterapia insuficiente" },
            { "text": "ASA + Prasugrel 10mg", "correct": False, "feedback": "Dosis de Prasugrel incorrecta" }
        ]
    },
    {
        "title": "STEMI en Diabético", "type": "stemi",
        "scenario": "STEMI en diabético de 68 años, sin contraindicaciones",
        "ecg": "⚡ STEMI anterior con Q patológicas ⚡",
        "question": "¿Inhibidor P2Y12 preferido según AHA 2025?",
        "options": [
            { "text": "Ticagrelor 180mg carga", "correct": True, "feedback": "Correcto! Ticagrelor preferido en diabéticos" },
            { "text": "Prasugrel 60mg carga", "correct": False, "feedback": "Ticagrelor mejor evidencia en diabéticos" },
            { "text": "Clopidogrel 600mg", "correct": False, "feedback": "Menos potente en diabéticos" },
            { "text": "Cangrelor IV", "correct": False, "feedback": "No primera línea" }
        ]
    },
    {
        "title": "Shock Cardiogénico STEMI", "type": "stemi",
        "scenario": "STEMI con PA 70/40, frialdad distal, lactato 4.5",
        "ecg": "⚡ STEMI anterior extenso + shock ⚡",
        "question": "¿Manejo inicial prioritario?",
        "options": [
            { "text": "ICP primaria URGENTE + soporte hemodinámico", "correct": True, "feedback": "Correcto! Revascularización urgente es clave" },
            { "text": "Estabilizar primero, luego ICP", "correct": False, "feedback": "ICP urgente mejora supervivencia" },
            { "text": "IABP primero", "correct": False, "feedback": "ICP tiene prioridad" },
            { "text": "Solo soporte médico", "correct": False, "feedback": "Revascularización es vital" }
        ]
    },
    {
        "title": "STEMI en Anciano >80 años", "type": "stemi",
        "scenario": "STEMI en mujer de 85 años, independiente, buena calidad de vida",
        "ecg": "⚡ STEMI inferior con bloqueo AV ⚡",
        "question": "¿Estrategia de reperfusión?",
        "options": [
            { "text": "ICP primaria (edad no es contraindicación)", "correct": True, "feedback": "Correcto! Edad sola no contraindica ICP" },
            { "text": "Solo tratamiento médico", "correct": False, "feedback": "Discriminación por edad inapropiada" },
            { "text": "Fibrinólisis preferible", "correct": False, "feedback": "Mayor riesgo hemorrágico en ancianos" },
            { "text": "Cuidados paliativos", "correct": False, "feedback": "Paciente con buena funcionalidad" }
        ]
    },
    {
        "title": "Rescate post-Fibrinólisis", "type": "stemi",
        "scenario": "Post-fibrinólisis, dolor persiste, ST sin resolución >50% a los 90min",
        "ecg": "⚡ ST persistentemente elevado post-líticos ⚡",
        "question": "¿Siguiente paso según AHA 2025?",
        "options": [
            { "text": "ICP de rescate inmediata", "correct": True, "feedback": "Correcto! Fibrinólisis fallida requiere ICP rescate" },
            { "text": "Segunda dosis de fibrinolítico", "correct": False, "feedback": "No recomendado, aumenta riesgo" },
            { "text": "Esperar 24 horas", "correct": False, "feedback": "Pérdida de tiempo crítico" },
            { "text": "Solo anticoagulación", "correct": False, "feedback": "Reperfusión mecánica necesaria" }
        ]
    },
    {
        "title": "Anticoagulación STEMI-ICP", "type": "stemi",
        "scenario": "STEMI programado para ICP primaria inmediata",
        "ecg": "⚡ Preparación para cateterismo ⚡",
        "question": "¿Anticoagulación para ICP según AHA 2025?",
        "options": [
            { "text": "Heparina no fraccionada IV", "correct": True, "feedback": "Correcto! HNF estándar para ICP primaria" },
            { "text": "Enoxaparina SC", "correct": False, "feedback": "HNF preferida para ICP" },
            { "text": "Rivaroxabán", "correct": False, "feedback": "DOAC no para fase aguda" },
            { "text": "Sin anticoagulación", "correct": False, "feedback": "Anticoagulación esencial" }
        ]
    },
    {
        "title": "Complicación Mecánica STEMI", "type": "stemi",
        "scenario": "Post-STEMI día 3, soplo holosistólico nuevo, deterioro hemodinámico",
        "ecg": "⚡ Q patológicas anteriores ⚡",
        "question": "¿Complicación más probable?",
        "options": [
            { "text": "Insuficiencia mitral aguda/ruptura de músculo papilar", "correct": True, "feedback": "Correcto! Soplo + deterioro = complicación mecánica" },
            { "text": "Reinfarto", "correct": False, "feedback": "No explica soplo nuevo" },
            { "text": "Pericarditis", "correct": False, "feedback": "No causa deterioro tan severo" },
            { "text": "TEP", "correct": False, "feedback": "No relacionado con soplo" }
        ]
    },
    {
        "title": "STEMI Posterior", "type": "stemi",
        "scenario": "Dolor torácico, ECG 12 derivaciones muestra R dominante V1-V2",
        "ecg": "⚡ R alto en V1-V2, ST depresión V1-V3 ⚡",
        "question": "¿Siguiente paso diagnóstico?",
        "options": [
            { "text": "ECG posterior (V7-V9)", "correct": True, "feedback": "Correcto! R dominante V1-V2 sugiere STEMI posterior" },
            { "text": "Ecocardiograma", "correct": False, "feedback": "ECG posterior primero" },
            { "text": "Troponinas", "correct": False, "feedback": "ECG posterior es prioritario" },
            { "text": "TC coronario", "correct": False, "feedback": "ECG posterior confirma diagnóstico" }
        ]
    },
    {
        "title": "Terapia Post-STEMI Alta", "type": "stemi",
        "scenario": "Post-ICP exitosa, FE 45%, sin contraindicaciones",
        "ecg": "⚡ Reperfusión exitosa, TIMI 3 ⚡",
        "question": "¿Terapia al alta AHA 2025?",
        "options": [
            { "text": "DAPT + Estatina alta intensidad + IECA + Betabloqueador", "correct": True, "feedback": "Perfecto! Prevención secundaria completa" },
            { "text": "Solo DAPT por 12 meses", "correct": False, "feedback": "Falta prevención secundaria completa" },
            { "text": "DAPT + Estatina", "correct": False, "feedback": "Faltan IECA y betabloqueador" },
            { "text": "Solo ASA de por vida", "correct": False, "feedback": "Terapia muy limitada" }
        ]
    },
    {
        "title": "STEMI con Fibrilación Auricular", "type": "stemi",
        "scenario": "Post-STEMI con FA de novo, CHA2DS2-VASc 4 puntos",
        "ecg": "⚡ FA + stent liberador de fármaco ⚡",
        "question": "¿Terapia antitrombótica óptima?",
        "options": [
            { "text": "Triple terapia: DOAC + ASA + P2Y12 (duración limitada)", "correct": True, "feedback": "Correcto! Triple terapia con DOAC preferido" },
            { "text": "Solo DAPT", "correct": False, "feedback": "Alto riesgo embólico (CHA2DS2-VASc 4)" },
            { "text": "Solo anticoagulación", "correct": False, "feedback": "Riesgo de trombosis de stent" },
            { "text": "Warfarina + DAPT completo", "correct": False, "feedback": "DOAC preferido sobre warfarina" }
        ]
    },
    {
        "title": "Diagnóstico NSTEMI", "type": "nstemi",
        "scenario": "Dolor torácico 4 horas, troponina elevada x3 LSN",
        "ecg": "📊 ECG: ST depresión V4-V6, sin elevación ST 📊",
        "question": "¿Clasificación según AHA 2025?",
        "options": [
            { "text": "NSTEMI (troponina+ sin elevación ST)", "correct": True, "feedback": "Correcto! Troponina elevada + síntomas = NSTEMI" },
            { "text": "Angina inestable", "correct": False, "feedback": "Troponina elevada define NSTEMI" },
            { "text": "STEMI atípico", "correct": False, "feedback": "No hay elevación de ST" },
            { "text": "Síndrome X", "correct": False, "feedback": "Troponina elevada excluye Sx X" }
        ]
    },
    {
        "title": "Estratificación Riesgo NSTEMI", "type": "nstemi",
        "scenario": "NSTEMI, 70 años, diabetes, troponina 15 ng/mL, GRACE score 140",
        "ecg": "📊 ST depresión >2mm múltiples derivaciones 📊",
        "question": "¿Clasificación de riesgo?",
        "options": [
            { "text": "Alto riesgo - estrategia invasiva precoz (<24h)", "correct": True, "feedback": "Correcto! GRACE >140 = alto riesgo" },
            { "text": "Riesgo moderado - invasiva en 72h", "correct": False, "feedback": "GRACE 140 es alto riesgo" },
            { "text": "Bajo riesgo - manejo conservador", "correct": False, "feedback": "Multiple factores de alto riesgo" },
            { "text": "Riesgo intermedio", "correct": False, "feedback": "GRACE >140 define alto riesgo" }
        ]
    },
    {
        "title": "Timing Invasivo NSTEMI", "type": "nstemi",
        "scenario": "NSTEMI alto riesgo, hemodinámicamente estable",
        "ecg": "📊 Cambios ST dinámicos 📊",
        "question": "¿Timing para estrategia invasiva según AHA 2025?",
        "options": [
            { "text": "Dentro de 24 horas", "correct": True, "feedback": "Correcto! Alto riesgo requiere invasiva <24h" },
            { "text": "Inmediata (<2 horas)", "correct": False, "feedback": "Solo si inestabilidad hemodinámica" },
            { "text": "Dentro de 72 horas", "correct": False, "feedback": "Muy tardío para alto riesgo" },
            { "text": "Manejo conservador inicial", "correct": False, "feedback": "Alto riesgo requiere estrategia invasiva" }
        ]
    },
    {
        "title": "NSTEMI con Inestabilidad", "type": "nstemi",
        "scenario": "NSTEMI con angina recurrente refractaria y cambios ST dinámicos",
        "ecg": "📊 ST depresión fluctuante durante dolor 📊",
        "question": "¿Estrategia de timing?",
        "options": [
            { "text": "Invasiva inmediata (<2 horas)", "correct": True, "feedback": "Correcto! Inestabilidad requiere invasiva urgente" },
            { "text": "Invasiva en 24 horas", "correct": False, "feedback": "Muy tardío para inestabilidad" },
            { "text": "Optimizar tratamiento médico primero", "correct": False, "feedback": "Refractario a tratamiento médico" },
            { "text": "Manejo conservador", "correct": False, "feedback": "Inestabilidad clínica requiere intervención" }
        ]
    },
    {
        "title": "Antiagregación NSTEMI", "type": "nstemi",
        "scenario": "NSTEMI programado para cateterismo en 12 horas",
        "ecg": "📊 ST depresión anterior 📊",
        "question": "¿DAPT óptima pre-cateterismo?",
        "options": [
            { "text": "ASA + Ticagrelor (estrategia pretratamiento)", "correct": True, "feedback": "Correcto! Pretratamiento recomendado NSTEMI" },
            { "text": "Solo ASA hasta definir anatomía", "correct": False, "feedback": "DAPT recomendado pre-cateterismo" },
            { "text": "ASA + esperar resultado cateterismo", "correct": False, "feedback": "Pretratamiento mejora resultados" },
            { "text": "ASA + Prasugrel siempre", "correct": False, "feedback": "Prasugrel post-cateterismo si no bypass" }
        ]
    },
    {
        "title": "NSTEMI Score GRACE", "type": "nstemi",
        "scenario": "NSTEMI: 55 años, FC 90, PA sistólica 110, creatinina normal, sin parada cardíaca",
        "ecg": "📊 ST depresión mínima 📊",
        "question": "¿Categoría de riesgo probable?",
        "options": [
            { "text": "Riesgo bajo-intermedio (GRACE <140)", "correct": True, "feedback": "Correcto! Perfil clínico sugiere riesgo menor" },
            { "text": "Alto riesgo (GRACE >140)", "correct": False, "feedback": "Perfil no sugiere alto riesgo" },
            { "text": "Riesgo muy alto", "correct": False, "feedback": "Sin criterios de muy alto riesgo" },
            { "text": "Imposible determinar sin score completo", "correct": False, "feedback": "Datos permiten estimación aproximada" }
        ]
    },
    {
        "title": "NSTEMI en Mujer", "type": "nstemi",
        "scenario": "Mujer 62 años, síntomas atípicos, troponina elevada, ECG normal",
        "ecg": "📊 ECG sin cambios significativos 📊",
        "question": "¿Consideración especial según AHA 2025?",
        "options": [
            { "text": "Alto índice sospecha - síntomas atípicos comunes en mujeres", "correct": True, "feedback": "Correcto! Presentación atípica más frecuente en mujeres" },
            { "text": "Baja probabilidad de SCA", "correct": False, "feedback": "Troponina elevada es diagnóstica" },
            { "text": "Mismo manejo que hombres sin diferencias", "correct": False, "feedback": "Hay consideraciones específicas de género" },
            { "text": "Esperar síntomas típicos", "correct": False, "feedback": "Síntomas atípicos no excluyen SCA en mujeres" }
        ]
    },
    {
        "title": "Anticoagulación NSTEMI", "type": "nstemi",
        "scenario": "NSTEMI, estrategia invasiva planeada, sin alto riesgo hemorrágico",
        "ecg": "📊 Cambios isquémicos difusos 📊",
        "question": "¿Anticoagulación de elección?",
        "options": [
            { "text": "Enoxaparina o HNF (ambas clase I)", "correct": True, "feedback": "Correcto! Ambas opciones clase I AHA 2025" },
            { "text": "Solo HNF", "correct": False, "feedback": "Enoxaparina también es opción clase I" },
            { "text": "Fondaparinux preferido", "correct": False, "feedback": "Requiere HNF adicional en ICP" },
            { "text": "Sin anticoagulación hasta cateterismo", "correct": False, "feedback": "Anticoagulación inmediata recomendada" }
        ]
    },
    {
        "title": "NSTEMI con Sangrado Alto Riesgo", "type": "nstemi",
        "scenario": "NSTEMI, historia de sangrado GI reciente, anemia",
        "ecg": "📊 ST depresión lateral 📊",
        "question": "¿Estrategia antitrombótica modificada?",
        "options": [
            { "text": "Estrategia invasiva precoz + duración DAPT reducida", "correct": True, "feedback": "Correcto! Invasiva precoz reduce exposición antitrombótica" },
            { "text": "Solo tratamiento médico", "correct": False, "feedback": "Invasiva reduce tiempo antitrombótico total" },
            { "text": "DAPT estándar 12 meses", "correct": False, "feedback": "Alto riesgo hemorrágico requiere ajuste" },
            { "text": "Solo ASA sin P2Y12", "correct": False, "feedback": "DAPT necesario pero duración ajustada" }
        ]
    },
    {
        "title": "NSTEMI Post-Bypass", "type": "nstemi",
        "scenario": "NSTEMI en paciente con bypass de 5 años, troponina muy elevada",
        "ecg": "📊 Cambios ST en territorio de injerto 📊",
        "question": "¿Manejo específico requerido?",
        "options": [
            { "text": "Cateterismo para evaluar injertos + arterias nativas", "correct": True, "feedback": "Correcto! Evaluar tanto injertos como progresión nativa" },
            { "text": "Solo tratamiento médico", "correct": False, "feedback": "Anatomía post-bypass requiere evaluación" },
            { "text": "Re-bypass inmediato", "correct": False, "feedback": "Cateterismo primero para definir anatomía" },
            { "text": "Mismo manejo que arteria nativa", "correct": False, "feedback": "Anatomía de injerto requiere consideraciones especiales" }
        ]
    },
    {
        "title": "NSTEMI con Diabetes", "type": "nstemi",
        "scenario": "NSTEMI en diabético tipo 2, HbA1c 9.2%, múltiples comorbilidades",
        "ecg": "📊 Cambios ST múltiples territorios 📊",
        "question": "¿Consideración especial manejo?",
        "options": [
            { "text": "Estrategia invasiva favorecida (beneficio mayor en diabéticos)", "correct": True, "feedback": "Correcto! Diabéticos se benefician más de estrategia invasiva" },
            { "text": "Manejo conservador por comorbilidades", "correct": False, "feedback": "Invasiva especialmente beneficiosa en diabéticos" },
            { "text": "Mismo manejo que no diabéticos", "correct": False, "feedback": "Diabetes modifica estrategia de manejo" },
            { "text": "Esperar control glucémico", "correct": False, "feedback": "SCA tiene prioridad sobre control glucémico" }
        ]
    },
    {
        "title": "NSTEMI Troponina Muy Elevada", "type": "nstemi",
        "scenario": "NSTEMI con troponina I >50 ng/mL (>10x LSN), estable hemodinámicamente",
        "ecg": "📊 ST depresión significativa V4-V6 📊",
        "question": "¿Implicación de troponina muy elevada?",
        "options": [
            { "text": "Alto riesgo - invasiva precoz independiente de otros factores", "correct": True, "feedback": "Correcto! Troponina muy elevada = alto riesgo per se" },
            { "text": "Esperar tendencia de troponina", "correct": False, "feedback": "Nivel ya define alto riesgo" },
            { "text": "Mismo manejo que troponina baja", "correct": False, "feedback": "Nivel de troponina modifica riesgo" },
            { "text": "Indica necrosis extensa - manejo conservador", "correct": False, "feedback": "Alto riesgo requiere estrategia invasiva" }
        ]
    },
    {
        "title": "NSTEMI Killip II", "type": "nstemi",
        "scenario": "NSTEMI con signos de insuficiencia cardíaca (estertores bibasales, S3)",
        "ecg": "📊 ST depresión anterior extensa 📊",
        "question": "¿Clasificación e implicaciones?",
        "options": [
            { "text": "Killip II - alto riesgo, invasiva precoz + optimización hemodinámica", "correct": True, "feedback": "Correcto! IC en NSTEMI = alto riesgo" },
            { "text": "Killip I - manejo estándar", "correct": False, "feedback": "Estertores + S3 = Killip II" },
            { "text": "Contraindicación para invasiva", "correct": False, "feedback": "IC es indicación para invasiva precoz" },
            { "text": "Esperar compensación antes de cateterismo", "correct": False, "feedback": "Revascularización puede mejorar función" }
        ]
    },
    {
        "title": "NSTEMI Octogenario", "type": "nstemi",
        "scenario": "NSTEMI en paciente 82 años, independiente, cognitivamente normal",
        "ecg": "📊 ST depresión inferolateral 📊",
        "question": "¿Estrategia apropiada según edad?",
        "options": [
            { "text": "Estrategia invasiva - edad sola no es contraindicación", "correct": True, "feedback": "Correcto!
             { "text": "Estrategia invasiva - edad sola no es contraindicación", "correct": True, "feedback": "Correcto! Funcionalidad más importante que edad cronológica" },
           { "text": "Solo tratamiento médico por edad", "correct": False, "feedback": "Discriminación etaria inapropiada" },
           { "text": "Invasiva solo si <80 años", "correct": False, "feedback": "Límite etario arbitrario no recomendado" },
           { "text": "Manejo paliativo", "correct": False, "feedback": "Paciente funcional se beneficia de tratamiento activo" }
       ]
   },
   {
       "title": "NSTEMI Prevención Secundaria", "type": "nstemi",
       "scenario": "Post-NSTEMI, cateterismo con stent DES, FE 50%, LDL 180 mg/dL",
       "ecg": "📊 Resolución cambios isquémicos post-ICP 📊",
       "question": "¿Terapia estatina al alta?",
       "options": [
           { "text": "Estatina alta intensidad (atorvastatina 80mg o rosuvastatina 40mg)", "correct": True, "feedback": "Correcto! Alta intensidad mandatoria post-SCA" },
           { "text": "Estatina moderada intensidad", "correct": False, "feedback": "Alta intensidad requerida post-SCA" },
           { "text": "Estatina solo si LDL >190", "correct": False, "feedback": "Post-SCA requiere estatina independiente de LDL" },
           { "text": "Esperar perfil lipídico en 6 semanas", "correct": False, "feedback": "Iniciar antes del alta hospitalaria" }
       ]
   }
]
