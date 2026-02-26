# src/ui/styles.py
# ─────────────────────────────────────────────────────────────────────────────
# CSS personalizado para la app de Streamlit.
# Diseño profesional, limpio y moderno.
# ─────────────────────────────────────────────────────────────────────────────

CUSTOM_CSS = """
<style>
    /* ── Reset y tipografía ──────────────────────────────────────────────── */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .block-container {
        max-width: 820px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* ── Header ──────────────────────────────────────────────────────────── */
    .app-hero {
        text-align: center;
        padding: 2.5rem 1rem 1.5rem;
        margin-bottom: 0.5rem;
    }

    .app-hero-icon {
        font-size: 2.8rem;
        margin-bottom: 0.5rem;
        display: block;
    }

    .app-hero h1 {
        font-size: 1.75rem;
        font-weight: 800;
        color: #0f172a;
        margin: 0 0 0.4rem 0;
        letter-spacing: -0.8px;
        line-height: 1.2;
    }

    .app-hero .subtitle {
        font-size: 0.92rem;
        color: #64748b;
        font-weight: 400;
        margin: 0;
        line-height: 1.5;
    }

    /* ── Barra de búsqueda ───────────────────────────────────────────────── */
    .stTextInput > div > div > input {
        border-radius: 12px !important;
        border: 2px solid #e2e8f0 !important;
        padding: 0.75rem 1rem !important;
        font-size: 0.95rem !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        background: #ffffff !important;
        transition: all 0.2s ease !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.12) !important;
    }

    .stTextInput > div > div > input::placeholder {
        color: #94a3b8 !important;
    }

    /* ── Botón principal ─────────────────────────────────────────────────── */
    .stButton > button[kind="primary"] {
        background: #6366f1 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.7rem 1.5rem !important;
        font-weight: 600 !important;
        font-size: 0.88rem !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        letter-spacing: 0.2px !important;
        transition: all 0.2s ease !important;
        color: white !important;
    }

    .stButton > button[kind="primary"]:hover {
        background: #4f46e5 !important;
        box-shadow: 0 4px 16px rgba(99, 102, 241, 0.3) !important;
        transform: translateY(-1px) !important;
    }

    .stButton > button[kind="primary"]:active {
        transform: translateY(0) !important;
    }

    /* ── Encabezado de resultados ─────────────────────────────────────────── */
    .results-header {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 1.25rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid #f1f5f9;
    }

    .results-header .badge {
        display: inline-flex;
        align-items: center;
        gap: 0.35rem;
        background: #6366f1;
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 100px;
        font-size: 0.82rem;
        font-weight: 600;
        letter-spacing: 0.3px;
    }

    .results-header .count {
        color: #94a3b8;
        font-size: 0.82rem;
        font-weight: 400;
    }

    /* ── Tarjetas de plan individual ─────────────────────────────────────── */
    .plan-card {
        background: #ffffff;
        border: 1px solid #f1f5f9;
        border-radius: 14px;
        padding: 1.15rem 1.35rem;
        margin-bottom: 0.65rem;
        display: flex;
        align-items: flex-start;
        gap: 1rem;
        transition: all 0.2s ease;
    }

    .plan-card:hover {
        border-color: #e2e8f0;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
        transform: translateY(-1px);
    }

    .plan-number {
        flex-shrink: 0;
        width: 36px;
        height: 36px;
        background: #f1f5f9;
        color: #6366f1;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 0.85rem;
    }

    .plan-content {
        flex: 1;
        min-width: 0;
    }

    .plan-content .plan-title {
        font-weight: 700;
        font-size: 0.95rem;
        color: #0f172a;
        margin: 0 0 0.3rem 0;
        line-height: 1.4;
    }

    .plan-content .plan-desc {
        font-size: 0.87rem;
        color: #64748b;
        line-height: 1.55;
        margin: 0;
    }

    .plan-content .plan-cost {
        display: inline-block;
        margin-top: 0.4rem;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 0.2rem 0.6rem;
        border-radius: 6px;
        background: #f0fdf4;
        color: #16a34a;
    }

    /* ── Estado vacío ────────────────────────────────────────────────────── */
    .empty-state {
        text-align: center;
        padding: 4rem 2rem;
    }

    .empty-state .icon {
        font-size: 3.5rem;
        margin-bottom: 1rem;
        display: block;
        opacity: 0.7;
    }

    .empty-state h3 {
        font-size: 1.1rem;
        font-weight: 600;
        color: #334155;
        margin: 0 0 0.5rem 0;
    }

    .empty-state p {
        font-size: 0.88rem;
        color: #94a3b8;
        margin: 0;
    }

    .empty-state .suggestions {
        display: flex;
        justify-content: center;
        gap: 0.5rem;
        margin-top: 1.25rem;
        flex-wrap: wrap;
    }

    .empty-state .suggestion-chip {
        background: #f1f5f9;
        color: #475569;
        padding: 0.35rem 0.85rem;
        border-radius: 100px;
        font-size: 0.8rem;
        font-weight: 500;
    }

    /* ── Sidebar ─────────────────────────────────────────────────────────── */
    section[data-testid="stSidebar"] {
        background: #fafbfe;
        border-right: 1px solid #eef2f6;
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 1.5rem;
    }

    .sidebar-section .section-label {
        font-size: 0.68rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #94a3b8;
        margin-bottom: 0.6rem;
    }

    .sidebar-model-info {
        background: #f1f5f9;
        border-radius: 10px;
        padding: 0.85rem 1rem;
        font-size: 0.82rem;
    }

    .sidebar-model-info .model-name {
        font-weight: 700;
        color: #0f172a;
        font-size: 0.85rem;
        margin-bottom: 0.2rem;
    }

    .sidebar-model-info .model-provider {
        color: #64748b;
        font-size: 0.78rem;
    }

    .sidebar-footer {
        text-align: center;
        padding: 1.5rem 0 0.5rem;
        color: #cbd5e1;
        font-size: 0.72rem;
        line-height: 1.6;
    }

    .sidebar-footer a {
        color: #6366f1;
        text-decoration: none;
        font-weight: 500;
    }

    /* ── Historial botones ───────────────────────────────────────────────── */
    .stButton > button[kind="secondary"] {
        border-radius: 10px !important;
        border: 1px solid #e2e8f0 !important;
        font-size: 0.82rem !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        transition: all 0.15s ease !important;
        background: #ffffff !important;
    }

    .stButton > button[kind="secondary"]:hover {
        background: #f8fafc !important;
        border-color: #6366f1 !important;
        color: #6366f1 !important;
    }

    /* ── Ocultar cromo de Streamlit ───────────────────────────────────────── */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* ── Dividers más sutiles ─────────────────────────────────────────────── */
    hr {
        border: none;
        border-top: 1px solid #f1f5f9;
        margin: 1rem 0;
    }
</style>
"""
