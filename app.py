import streamlit as st
import random
import time
from patient_avatar import MedicalAvatar
from questions import patients, question_bank

# Configuración de página
st.set_page_config(
    page_title="Simulador SCA - STEMI/NSTEMI",
    page_icon="🏥",
    layout="wide"
)

# Inicializar estado
if 'game_state' not in st.session_state:
    st.session_state.game_state = {
        'score': 0,
        'current_stage': 0,
        'time_remaining': 120,
        'answered_correctly': [],
        'patient': random.choice(patients),
        'selected_questions': random.sample(question_bank, 10),
        'game_started': False,
        'game_finished': False
    }

# Inicializar avatar
if 'avatar' not in st.session_state:
    st.session_state.avatar = MedicalAvatar()

def start_game():
    st.session_state.game_state['game_started'] = True
    st.session_state.start_time = time.time()

def check_answer(option_index):
    question = st.session_state.game_state['selected_questions'][st.session_state.game_state['current_stage']]
    option = question['options'][option_index]
    
    if option['correct']:
        st.session_state.game_state['score'] += 100
        st.session_state.game_state['answered_correctly'].append(st.session_state.game_state['current_stage'])
        st.success(f"✅ ¡Correcto! {option['feedback']}")
    else:
        st.error(f"❌ Incorrecto. {option['feedback']}")
        # Mostrar respuesta correcta
        for i, opt in enumerate(question['options']):
            if opt['correct']:
                st.info(f"Respuesta correcta: {chr(65+i)}. {opt['text']}")
    
    st.session_state.answer_given = True

def next_question():
    st.session_state.game_state['current_stage'] += 1
    st.session_state.answer_given = False
    
    if st.session_state.game_state['current_stage'] >= 10:
        st.session_state.game_state['game_finished'] = True

# Título principal
st.title("🏥 Simulador de Síndromes Coronarios Agudos")
st.subheader("STEMI/NSTEMI - Basado en Guías AHA 2025")

# Layout principal
if not st.session_state.game_state['game_started']:
    # Pantalla de inicio
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        ### 🎯 Características del Simulador
        - **30 preguntas** en banco aleatorio (15 STEMI + 15 NSTEMI)
        - **10 casos** por sesión seleccionados aleatoriamente
        - **Avatar interactivo** del paciente con librerías Python
        - **Monitor ECG** en tiempo real
        - **Signos vitales** animados
        - **Sistema de puntuación** profesional
        
        ### 🩺 Tipos de Casos
        - **STEMI**: Infarto con elevación del ST
        - **NSTEMI**: Infarto sin elevación del ST
        
        ### ⏱️ Tiempo Límite
        - **120 minutos** de ventana isquémica
        - Bonificación por velocidad de respuesta
        """)
        
        if st.button("🚀 Iniciar Simulación", type="primary", use_container_width=True):
            start_game()
            st.rerun()

elif st.session_state.game_state['game_finished']:
    # Pantalla final
    st.balloons()
    
    percentage = (len(st.session_state.game_state['answered_correctly']) / 10) * 100
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("# 🎉 ¡Simulación Completada!")
        
        # Puntuación
        st.metric("Puntuación Final", f"{st.session_state.game_state['score']} puntos")
        st.metric("Respuestas Correctas", f"{len(st.session_state.game_state['answered_correctly'])}/10 ({percentage:.0f}%)")
        
        # Logros
        st.markdown("### 🏆 Logros Desbloqueados")
        if percentage == 100:
            st.success("🏆 **Cardiólogo Intervencionista** - Perfección absoluta")
        elif percentage >= 80:
            st.success("⭐ **Especialista en SCA** - Excelente conocimiento")
        elif percentage >= 60:
            st.info("🩺 **Conocimiento Sólido** - Buen rendimiento")
        
        # Mensaje final
        if percentage >= 80:
            st.success("¡Excelente! Dominas el manejo de síndromes coronarios agudos.")
        elif percentage >= 60:
            st.info("Buen trabajo. Revisa las áreas de mejora para perfeccionar tu conocimiento.")
        else:
            st.warning("Necesitas repasar más las guías AHA 2025. ¡La práctica hace al maestro!")
        
        if st.button("🔄 Nueva Simulación", type="primary"):
            # Reiniciar juego
            st.session_state.game_state = {
                'score': 0,
                'current_stage': 0,
                'time_remaining': 120,
                'answered_correctly': [],
                'patient': random.choice(patients),
                'selected_questions': random.sample(question_bank, 10),
                'game_started': False,
                'game_finished': False
            }
            st.rerun()

else:
    # Juego activo
    current_question = st.session_state.game_state['selected_questions'][st.session_state.game_state['current_stage']]
    patient = st.session_state.game_state['patient']
    
    # Barra de progreso
    progress = (st.session_state.game_state['current_stage'] + 1) / 10
    st.progress(progress, text=f"Pregunta {st.session_state.game_state['current_stage'] + 1} de 10")
    
    # Información del paciente y avatares
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 👤 Información del Paciente")
        st.write(f"**{patient['name']}** | {patient['age']} años | {patient['gender']}")
        st.write(f"*{patient['symptoms']}*")
        
        # Avatar del paciente
        avatar_fig = st.session_state.avatar.create_patient_avatar(
            patient['vitals'], 
            current_question['type']
        )
        st.plotly_chart(avatar_fig, use_container_width=True)
    
    with col2:
        st.markdown("### 📊 Monitor Cardíaco")
        
        # ECG Monitor
        heart_rate = int(patient['vitals']['FC']['value'].split()[0])
        ecg_fig = st.session_state.avatar.create_ecg_monitor(heart_rate, current_question['type'])
        st.plotly_chart(ecg_fig, use_container_width=True)
    
    # Signos vitales
    st.markdown("### 🩺 Signos Vitales")
    
    # Radar de signos vitales
    vitals_fig = st.session_state.avatar.create_vitals_radar(patient['vitals'])
    st.plotly_chart(vitals_fig, use_container_width=True)
    
    # Mostrar signos vitales en métricas
    cols = st.columns(4)
    for i, (key, vital) in enumerate(patient['vitals'].items()):
        with cols[i]:
            delta_color = "inverse" if vital.get('critical', False) else "normal"
            st.metric(
                key, 
                vital['value'], 
                delta="CRÍTICO" if vital.get('critical', False) else "Normal",
                delta_color=delta_color
            )
    
    # Caso clínico
    case_type_color = "🚨" if current_question['type'] == 'stemi' else "📊"
    st.markdown(f"### {case_type_color} Caso {current_question['type'].upper()}")
    
    st.info(f"**{current_question['title']}**\n\n{current_question['scenario']}")
    
    # ECG
    st.markdown("### 📈 Electrocardiograma")
    st.code(current_question['ecg'], language=None)
    
    # Pregunta
    st.markdown(f"### ❓ {current_question['question']}")
    
    # Opciones
    if 'answer_given' not in st.session_state:
        st.session_state.answer_given = False
    
    if not st.session_state.answer_given:
        for i, option in enumerate(current_question['options']):
            if st.button(f"{chr(65+i)}. {option['text']}", key=f"option_{i}"):
                check_answer(i)
                st.rerun()
    else:
        # Mostrar botón siguiente
        if st.button("➡️ Siguiente Pregunta", type="primary"):
            next_question()
            st.rerun()
    
    # Puntuación actual
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Puntuación", st.session_state.game_state['score'])
    with col2:
        st.metric("Correctas", len(st.session_state.game_state['answered_correctly']))
    with col3:
        st.metric("Pregunta", f"{st.session_state.game_state['current_stage'] + 1}/10")
