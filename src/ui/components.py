# src/ui/components.py
# ─────────────────────────────────────────────────────────────────────────────
# Componentes reutilizables de la interfaz Streamlit.
# ─────────────────────────────────────────────────────────────────────────────

import re
import streamlit as st


def render_header():
    """Renderiza el encabezado principal de la aplicación."""
    st.markdown(
        """
        <div class="app-hero">
            <span class="app-hero-icon">🗺️</span>
            <h1>Planes Familiares con IA</h1>
            <p class="subtitle">
                Descubre 10 planes gratuitos o de bajo coste para disfrutar en familia
            </p>
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
        # Modelo info
        st.caption("MODELO")
        st.markdown("**Llama 3.2 3B Instruct**")
        st.caption("Inferencia vía Hugging Face API")

        st.divider()

        # Acerca de
        st.caption("ACERCA DE")
        st.markdown(
            "Asistente de IA que recomienda **10 planes familiares** "
            "aptos para niños y de bajo coste para cualquier ciudad del mundo.",
        )

        st.divider()

        # Historial de búsquedas
        if "historial" in st.session_state and st.session_state.historial:
            st.caption("HISTORIAL")
            for entrada in reversed(st.session_state.historial):
                ciudad = entrada["ciudad"]
                if st.button(
                    f"📍 {ciudad}",
                    key=f"hist_{ciudad}",
                    use_container_width=True,
                ):
                    ciudad_historial = ciudad

        st.markdown(
            """
            <div class="sidebar-footer">
                Hecho con ❤️ usando Streamlit<br>
                <a href="https://huggingface.co" target="_blank">
                    Powered by Hugging Face
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    return ciudad_historial


# ── Parser de planes ─────────────────────────────────────────────────────────

def _parsear_planes(texto: str) -> list[dict]:
    """
    Parsea el texto del modelo y extrae cada plan como un dict con
    número, título y descripción.

    Soporta formatos:
      - '1. **Título**: Descripción'
      - '1. Título: Descripción'
      - '1. Título - Descripción'

    Returns:
        Lista de dicts con keys: num, titulo, descripcion.
    """
    planes = []

    # Patrón: número seguido de punto, espacio, contenido
    patron = re.compile(
        r"^(\d{1,2})\.\s+"  # Número + punto
        r"(?:\*\*)?(.+?)(?:\*\*)?"  # Título (con o sin **)
        r"(?::\s*|\s*[-–—]\s*)"  # Separador (: o -)
        r"(.+)$",  # Descripción
        re.MULTILINE,
    )

    for match in patron.finditer(texto):
        num = match.group(1)
        titulo = match.group(2).strip().rstrip("*").lstrip("*").strip()
        descripcion = match.group(3).strip()
        planes.append({
            "num": num,
            "titulo": titulo,
            "descripcion": descripcion,
        })

    return planes


def _detectar_coste(texto: str) -> str | None:
    """
    Intenta detectar indicaciones de coste en la descripción.

    Returns:
        Texto de coste formateado o None.
    """
    texto_lower = texto.lower()
    if "gratuit" in texto_lower or "gratis" in texto_lower or "libre" in texto_lower:
        return "Gratuito"
    if "bajo coste" in texto_lower or "económic" in texto_lower:
        return "Bajo coste"

    # Buscar precios explícitos tipo "1€", "2 euros", etc.
    precio_match = re.search(r"(\d+[\.,]?\d*)\s*€|(\d+[\.,]?\d*)\s*euros?", texto_lower)
    if precio_match:
        return f"~{precio_match.group(0).strip()}"

    return None


def render_resultado(ciudad: str, planes_texto: str):
    """
    Muestra los resultados: parsea los planes del modelo y los renderiza
    como tarjetas individuales. Si el parseo falla, muestra el texto plano.

    Args:
        ciudad: Nombre de la ciudad consultada.
        planes_texto: Texto con los planes generados por el modelo.
    """
    # Header de resultados
    st.markdown(
        f"""
        <div class="results-header">
            <span class="badge">📍 {ciudad.upper()}</span>
            <span class="count">10 planes familiares recomendados</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Intentar parsear los planes en tarjetas
    planes = _parsear_planes(planes_texto)

    if planes:
        for plan in planes:
            coste = _detectar_coste(plan["descripcion"])
            coste_html = (
                f'<span class="plan-cost">{coste}</span>' if coste else ""
            )

            st.markdown(
                f"""
                <div class="plan-card">
                    <div class="plan-number">{plan["num"]}</div>
                    <div class="plan-content">
                        <p class="plan-title">{plan["titulo"]}</p>
                        <p class="plan-desc">{plan["descripcion"]}</p>
                        {coste_html}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:
        # Fallback: si no se puede parsear, mostrar como markdown
        st.markdown(planes_texto)


def render_empty_state():
    """Muestra un estado vacío indicando al usuario cómo empezar."""
    st.markdown(
        """
        <div class="empty-state">
            <span class="icon">🏙️</span>
            <h3>¿Qué ciudad quieres explorar?</h3>
            <p>Escribe el nombre de una ciudad y descubre planes en familia</p>
            <div class="suggestions">
                <span class="suggestion-chip">Madrid</span>
                <span class="suggestion-chip">Barcelona</span>
                <span class="suggestion-chip">Granada</span>
                <span class="suggestion-chip">Sevilla</span>
                <span class="suggestion-chip">Valencia</span>
            </div>
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
