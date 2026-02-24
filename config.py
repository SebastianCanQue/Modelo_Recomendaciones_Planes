# config.py
# ─────────────────────────────────────────────────────────────────────────────
# Módulo de configuración: lee variables de entorno de forma segura.
# El token de Hugging Face NUNCA debe escribirse directamente en el código.
# ─────────────────────────────────────────────────────────────────────────────

import os
from dotenv import load_dotenv

# Carga el archivo .env si existe (útil en desarrollo local)
# En producción o en PyCharm se puede definir la variable directamente
# en la configuración de ejecución sin necesitar el archivo .env
load_dotenv()


def obtener_token() -> str:
    """
    Lee el token de Hugging Face desde la variable de entorno HF_TOKEN.

    Returns:
        str: El token de API de Hugging Face.

    Raises:
        EnvironmentError: Si la variable HF_TOKEN no está definida.
    """
    token = os.getenv("HF_TOKEN")

    if not token:
        raise EnvironmentError(
            "❌ No se encontró la variable de entorno HF_TOKEN.\n"
            "   → Opción 1 (PyCharm): Ve a Run > Edit Configurations > "
            "Environment variables y añade: HF_TOKEN=hf_tu_token_aqui\n"
            "   → Opción 2 (archivo .env): Crea un archivo .env en la raíz "
            "del proyecto con la línea: HF_TOKEN=hf_tu_token_aqui\n"
            "   Consigue tu token en: https://huggingface.co/settings/tokens"
        )

    return token

