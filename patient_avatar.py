import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import random

class MedicalAvatar:
    def __init__(self):
        self.heart_rate = 75
        self.pain_level = 0
        self.critical_vitals = 0
        self.patient_data = None
        
    def create_patient_avatar(self, vitals, case_type):
        """Crear avatar 2D del paciente con animaciones"""
        fig = go.Figure()
        
        # Determinar estado crítico
        critical_count = sum(1 for v in vitals.values() if v.get('critical', False))
        
        # Colores según estado
        face_color = 'lightcoral' if critical_count >= 2 else 'peachpuff'
        body_color = 'lightblue' if case_type == 'nstemi' else 'lightcyan'
        
        # Cabeza del paciente
        fig.add_shape(
            type="circle",
            x0=0.35, y0=0.7, x1=0.65, y1=1.0,
            fillcolor=face_color,
            line=dict(color="black", width=2)
        )
        
        # Cuerpo
        fig.add_shape(
            type="rect",
            x0=0.3, y0=0.3, x1=0.7, y1=0.7,
            fillcolor=body_color,
            line=dict(color="black", width=2)
        )
        
        # Ojos
        fig.add_shape(
            type="circle",
            x0=0.42, y0=0.85, x1=0.46, y1=0.89,
            fillcolor="white",
            line=dict(color="black", width=1)
        )
        fig.add_shape(
            type="circle",
            x0=0.54, y0=0.85, x1=0.58, y1=0.89,
            fillcolor="white",
            line=dict(color="black", width=1)
        )
        
        # Pupilas (expresión según dolor)
        pupil_y = 0.87 - (critical_count * 0.01)
        fig.add_shape(
            type="circle",
            x0=0.435, y0=pupil_y-0.01, x1=0.445, y1=pupil_y+0.01,
            fillcolor="black"
        )
        fig.add_shape(
            type="circle",
            x0=0.555, y0=pupil_y-0.01, x1=0.565, y1=pupil_y+0.01,
            fillcolor="black"
        )
        
        # Boca (expresión según estado)
        if critical_count >= 2:
            # Boca de dolor
            fig.add_shape(
                type="path",
                path="M 0.46 0.78 Q 0.5 0.76 0.54 0.78",
                line=dict(color="black", width=2)
            )
        else:
            # Boca neutral
            fig.add_shape(
                type="line",
                x0=0.46, y0=0.78, x1=0.54, y1=0.78,
                line=dict(color="black", width=2)
            )
        
        # Corazón palpitante
        heart_size = 0.03 + (critical_count * 0.01)
        heart_color = 'red' if critical_count >= 2 else 'pink'
        
        fig.add_shape(
            type="circle",
            x0=0.48, y0=0.45, x1=0.52, y1=0.49,
            fillcolor=heart_color,
            line=dict(color="darkred", width=1)
        )
        
        # Efectos de dolor (ondas)
        if critical_count >= 1:
            for i in range(3):
                radius = 0.1 + (i * 0.05)
                fig.add_shape(
                    type="circle",
                    x0=0.5-radius, y0=0.5-radius, 
                    x1=0.5+radius, y1=0.5+radius,
                    line=dict(color="red", width=1, dash="dash"),
                    fillcolor="rgba(255,0,0,0.1)"
                )
        
        fig.update_layout(
            showlegend=False,
            xaxis=dict(visible=False, range=[0, 1]),
            yaxis=dict(visible=False, range=[0, 1]),
            margin=dict(l=0, r=0, t=0, b=0),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(240,248,255,0.5)',
            width=300,
            height=300,
            title=f"Paciente - Estado: {'Crítico' if critical_count >= 2 else 'Estable'}"
        )
        
        return fig
    
    def create_ecg_monitor(self, heart_rate, case_type):
        """Monitor ECG profesional"""
        # Generar señal ECG
        t = np.linspace(0, 4, 1000)
        
        # ECG base
        ecg_signal = np.zeros_like(t)
        
        # Frecuencia cardíaca
        beat_interval = 60 / heart_rate  # segundos entre latidos
        
        for beat_time in np.arange(0, 4, beat_interval):
            # Complejo QRS
            beat_mask = (t >= beat_time) & (t <= beat_time + 0.1)
            if np.any(beat_mask):
                beat_indices = np.where(beat_mask)[0]
                if len(beat_indices) > 0:
                    # Onda P
                    p_wave = 0.2 * np.exp(-((t[beat_mask] - beat_time) / 0.02)**2)
                    # Complejo QRS
                    qrs_wave = 1.0 * np.exp(-((t[beat_mask] - beat_time - 0.05) / 0.01)**2)
                    # Onda T
                    t_wave = 0.3 * np.exp(-((t[beat_mask] - beat_time - 0.08) / 0.03)**2)
                    
                    ecg_signal[beat_mask] += p_wave + qrs_wave + t_wave
        
        # Añadir ruido realista
        noise = 0.05 * np.random.randn(len(t))
        ecg_signal += noise
        
        # Modificaciones según tipo de caso
        if case_type == 'stemi':
            # Elevación del ST
            st_elevation = 0.2 * np.ones_like(t)
            ecg_signal += st_elevation
            line_color = 'red'
            title = "ECG: Elevación del ST (STEMI)"
        else:  # nstemi
            # Depresión del ST
            st_depression = -0.1 * np.ones_like(t)
            ecg_signal += st_depression
            line_color = 'orange'
            title = "ECG: Depresión del ST (NSTEMI)"
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=t,
            y=ecg_signal,
            mode='lines',
            line=dict(color=line_color, width=2),
            name='ECG',
            hovertemplate='Tiempo: %{x:.1f}s<br>Voltaje: %{y:.2f}mV<extra></extra>'
        ))
        
        fig.update_layout(
            title=title,
            xaxis_title="Tiempo (segundos)",
            yaxis_title="Voltaje (mV)",
            paper_bgcolor='black',
            plot_bgcolor='black',
            font=dict(color='lime'),
            xaxis=dict(gridcolor='darkgreen', color='lime'),
            yaxis=dict(gridcolor='darkgreen', color='lime'),
            width=600,
            height=300
        )
        
        return fig
    
    def create_vitals_radar(self, vitals):
        """Gráfico radar de signos vitales"""
        categories = []
        values = []
        colors = []
        
        # Normalizar valores para radar
        for key, vital in vitals.items():
            categories.append(key)
            
            # Convertir valores a números para radar
            if 'lpm' in vital['value']:
                val = int(vital['value'].split()[0])
                normalized = min(100, (val / 120) * 100)  # FC normal ~60-100
            elif 'mmHg' in vital['value']:
                val = int(vital['value'].split('/')[0])  # PA sistólica
                normalized = min(100, (val / 140) * 100)  # PA normal <140
            elif '%' in vital['value']:
                val = int(vital['value'].replace('%', ''))
                normalized = val  # SatO2 ya está en %
            elif '°C' in vital['value']:
                val = float(vital['value'].replace('°C', ''))
                normalized = min(100, ((val - 35) / 4) * 100)  # Temp normal 36-37°C
            else:
                normalized = 50  # valor por defecto
            
            values.append(normalized)
            colors.append('red' if vital.get('critical', False) else 'green')
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name='Signos Vitales',
            line=dict(color='blue', width=2),
            fillcolor='rgba(0,100,255,0.2)'
        ))
        
        # Añadir línea de referencia normal
        fig.add_trace(go.Scatterpolar(
            r=[80] * len(categories),  # Línea de referencia
            theta=categories,
            mode='lines',
            name='Valores Normales',
            line=dict(color='green', width=1, dash='dash')
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                    tickfont=dict(size=10)
                )
            ),
            title="Monitor de Signos Vitales",
            width=400,
            height=400
        )
        
        return fig
