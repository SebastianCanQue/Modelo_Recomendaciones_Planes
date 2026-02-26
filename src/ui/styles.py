# src/ui/styles.py
# ─────────────────────────────────────────────────────────────────────────────
# CSS personalizado para la app de Streamlit.
# Diseño minimalista, limpio y profesional.
# ─────────────────────────────────────────────────────────────────────────────

CUSTOM_CSS = """
<style>
    /* ── Tipografía general ──────────────────────────────────────────────── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }

    /* ── Header principal ────────────────────────────────────────────────── */
    .main-header {
        text-align: center;
        padding: 1.5rem 0 1rem;
    }

    .main-header h1 {
        font-size: 2rem;
        font-weight: 700;
        color: #1a1a2e;
        margin-bottom: 0.25rem;
        letter-spacing: -0.5px;
    }

    .main-header p {
        font-size: 0.95rem;
        color: #6b7280;
        margin-top: 0;
    }

    /* ── Tarjeta de resultado ────────────────────────────────────────────── */
    .result-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 1.5rem 2rem;
        margin-top: 1rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
    }

    .result-card h3 {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1a1a2e;
        margin-bottom: 1rem;
        padding-bottom: 0.75rem;
        border-bottom: 2px solid #f3f4f6;
    }

    /* ── Indicador de ciudad ─────────────────────────────────────────────── */
    .city-badge {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.35rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
        letter-spacing: 0.3px;
        margin-bottom: 0.5rem;
    }

    /* ── Footer ──────────────────────────────────────────────────────────── */
    .app-footer {
        text-align: center;
        padding: 2rem 0 1rem;
        color: #9ca3af;
        font-size: 0.78rem;
    }

    .app-footer a {
        color: #667eea;
        text-decoration: none;
    }

    /* ── Sidebar limpio ──────────────────────────────────────────────────── */
    section[data-testid="stSidebar"] {
        background-color: #fafbfc;
        border-right: 1px solid #e5e7eb;
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 2rem;
    }

    /* ── Input estilizado ────────────────────────────────────────────────── */
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 1.5px solid #d1d5db;
        padding: 0.65rem 1rem;
        font-size: 0.95rem;
        transition: border-color 0.2s;
    }

    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.15);
    }

    /* ── Botón principal ─────────────────────────────────────────────────── */
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border: none;
        border-radius: 10px;
        padding: 0.6rem 2rem;
        font-weight: 600;
        font-size: 0.9rem;
        letter-spacing: 0.3px;
        transition: transform 0.15s, box-shadow 0.15s;
    }

    .stButton > button[kind="primary"]:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.35);
    }

    /* ── Historial ───────────────────────────────────────────────────────── */
    .history-item {
        background: #f9fafb;
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 0.6rem 1rem;
        margin-bottom: 0.5rem;
        font-size: 0.85rem;
        color: #374151;
        cursor: pointer;
        transition: background 0.15s;
    }

    .history-item:hover {
        background: #f3f4f6;
    }

    /* ── Ocultar elementos de Streamlit ────────────────────────────────── */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
"""
