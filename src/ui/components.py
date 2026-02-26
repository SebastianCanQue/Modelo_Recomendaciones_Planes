# src/ui/components.py
# ─────────────────────────────────────────────────────────────────────────────
# Componentes reutilizables de la interfaz Streamlit.
# ─────────────────────────────────────────────────────────────────────────────

import streamlit as st


def render_header():
    """Renderiza el encabezado principal de la aplicación."""
    st.markdown(
        """
        <div class="main-header">
            <h1>🗺️ Planes Familiares con IA</h1>
            <p>Descubre 10 planes gratuitos o de bajo coste para disfrutar en familia</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar():
    """
    Renderiza el sidebar con información y el historial de búsquedas.

    Returns:
        str | None: Ciudad seleccionada del historial, o None.
    """
    ciudad_historial = None

    with st.sidebar:
        st.markdown("### ℹ️ Acerca de")
        st.markdown(
            "Asistente de IA que recomienda **10 planes familiares** "
            "aptos para niños y de bajo coste para cualquier ciudad.",
        )

        st.divider()

        st.markdown("### ⚙️ Modelo")
        st.caption("Meta Llama 3.2 3B Instruct")
        st.caption("Inferencia vía Hugging Face API")

        st.divider()

        # Historial de búsquedas
        if "historial" in st.session_state and st.session_state.historial:
            st.markdown("### 🕒 Historial")
            for entrada in reversed(st.session_state.historial):
                ciudad = entrada["ciudad"]
                if st.button(f"📍 {ciudad}", key=f"hist_{ciudad}", use_container_width=True):
                    ciudad_historial = ciudad

        st.divider()
        st.markdown(
            '<div class="app-footer">'
            "Hecho con ❤️ usando Streamlit<br>"
            '<a href="https://huggingface.co" target="_blank">Powered by Hugging Face</a>'
            "</div>",
            unsafe_allow_html=True,
        )

    return ciudad_historial


def render_resultado(ciudad: str, planes: str):
    """
    Muestra los resultados formateados en una tarjeta.

    Args:
        ciudad: Nombre de la ciudad consultada.
        planes: Texto con los planes generados por el modelo.
    """
    st.markdown(
        f'<span class="city-badge">📍 {ciudad.upper()}</span>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="result-card">
            <h3>10 planes familiares recomendados</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Usamos st.markdown para renderizar la respuesta (soporta **bold** del modelo)
    st.markdown(planes)


def render_empty_state():
    """Muestra un estado vacío indicando al usuario cómo empezar."""
    st.markdown("")  # Spacer
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(
            """
            <div style="text-align: center; padding: 3rem 1rem; color: #9ca3af;">
                <p style="font-size: 3rem; margin-bottom: 0.5rem;">🏙️</p>
                <p style="font-size: 1rem; font-weight: 500; color: #6b7280;">
                    Escribe el nombre de una ciudad para descubrir planes en familia
                </p>
                <p style="font-size: 0.85rem; margin-top: 0.5rem;">
                    Ejemplo: Madrid, Barcelona, Granada, Sevilla...
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_error(mensaje: str, tipo: str = "error"):
    """
    Muestra un mensaje de error formateado.

    Args:
        mensaje: Texto del error.
        tipo: 'error', 'warning' o 'info'.
    """
    if tipo == "warning":
        st.warning(mensaje, icon="⚠️")
    elif tipo == "info":
        st.info(mensaje, icon="ℹ️")
    else:
        st.error(mensaje, icon="🚨")
