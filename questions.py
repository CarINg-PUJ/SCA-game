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
    }
]
