# app.py
# ─────────────────────────────────────────────────────────────────────────────
# Punto de entrada de la aplicación Streamlit.
# Ejecutar con:  streamlit run app.py
# ─────────────────────────────────────────────────────────────────────────────

import streamlit as st

from src.asistente import obtener_planes
from src.ui.styles import CUSTOM_CSS
from src.ui.components import (
    render_header,
    render_sidebar,
    render_resultado,
    render_empty_state,
    render_error,
)

# ── Configuración de la página ───────────────────────────────────────────────
st.set_page_config(
    page_title="Planes Familiares con IA",
    page_icon="🗺️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ── Inyectar CSS personalizado ───────────────────────────────────────────────
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ── Inicializar estado de sesión ─────────────────────────────────────────────
if "historial" not in st.session_state:
    st.session_state.historial = []

if "resultado_actual" not in st.session_state:
    st.session_state.resultado_actual = None

if "ciudad_actual" not in st.session_state:
    st.session_state.ciudad_actual = ""


# ── Función principal de búsqueda ────────────────────────────────────────────
def buscar_planes(ciudad: str):
    """Ejecuta la búsqueda de planes y actualiza el estado."""
    if not ciudad.strip():
        render_error("Por favor, escribe el nombre de una ciudad.", tipo="warning")
        return

    ciudad = ciudad.strip().title()

    # Comprobar si ya está en el historial (evitar duplicados)
    resultado_cacheado = next(
        (e for e in st.session_state.historial if e["ciudad"] == ciudad),
        None,
    )

    if resultado_cacheado:
        st.session_state.resultado_actual = resultado_cacheado["planes"]
        st.session_state.ciudad_actual = ciudad
        return

    # Buscar planes nuevos
    with st.status(f"🔍 Buscando planes para **{ciudad}**...", expanded=True) as status:
        try:
            def actualizar_estado(msg: str):
                status.update(label=f"🔍 {msg}")

            planes = obtener_planes(ciudad, callback_estado=actualizar_estado)

            # Guardar en historial
            st.session_state.historial.append({
                "ciudad": ciudad,
                "planes": planes,
            })
            st.session_state.resultado_actual = planes
            st.session_state.ciudad_actual = ciudad

            status.update(label="✅ ¡Planes encontrados!", state="complete")

        except EnvironmentError as e:
            status.update(label="❌ Error de configuración", state="error")
            render_error(
                "**Token no configurado.** Añade tu `HF_TOKEN` en el archivo "
                "`.env` o en los secrets de Streamlit.",
                tipo="error",
            )

        except ConnectionError as e:
            status.update(label="❌ Error de conexión", state="error")
            render_error(
                "No se pudo conectar con la API de Hugging Face. "
                "Comprueba tu conexión a internet y que tu token sea válido.",
                tipo="error",
            )

        except ValueError as e:
            status.update(label="⚠️ Respuesta vacía", state="error")
            render_error(
                "El modelo devolvió una respuesta vacía. Inténtalo de nuevo.",
                tipo="warning",
            )

        except Exception as e:
            status.update(label="❌ Error inesperado", state="error")
            render_error(f"Error inesperado: {type(e).__name__}: {e}")


# ── Layout principal ─────────────────────────────────────────────────────────
def main():
    # Header
    render_header()

    # Sidebar (puede devolver una ciudad del historial)
    ciudad_del_historial = render_sidebar()

    # Formulario de búsqueda
    col1, col2 = st.columns([4, 1])

    with col1:
        ciudad_input = st.text_input(
            "Ciudad",
            placeholder="Ej: Granada, Madrid, Barcelona...",
            label_visibility="collapsed",
        )

    with col2:
        boton_buscar = st.button("🔍 Buscar", type="primary", use_container_width=True)

    # Manejar acciones
    if boton_buscar and ciudad_input:
        buscar_planes(ciudad_input)
    elif ciudad_del_historial:
        buscar_planes(ciudad_del_historial)

    # Mostrar resultado o estado vacío
    if st.session_state.resultado_actual and st.session_state.ciudad_actual:
        render_resultado(
            st.session_state.ciudad_actual,
            st.session_state.resultado_actual,
        )
    else:
        render_empty_state()


if __name__ == "__main__":
    main()
