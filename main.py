# main.py
# ─────────────────────────────────────────────────────────────────────────────
# Punto de entrada del asistente de planes familiares.
# Ejecuta este archivo directamente desde PyCharm o desde la terminal:
#   python main.py
# ─────────────────────────────────────────────────────────────────────────────

from asistente import obtener_planes


def mostrar_bienvenida():
    """Muestra el banner de bienvenida en la consola."""
    print("=" * 60)
    print("  🗺️   ASISTENTE DE PLANES FAMILIARES CON IA")
    print("  Planes aptos para niños · Familiares · Bajo coste")
    print("=" * 60)
    print()


def mostrar_resultado(ciudad: str, planes: str):
    """
    Muestra los planes generados de forma formateada.

    Args:
        ciudad (str): Nombre de la ciudad consultada.
        planes (str): Texto con los 10 planes devueltos por el modelo.
    """
    print()
    print(f"✅ 10 planes familiares recomendados para: {ciudad.upper()}")
    print("-" * 60)
    print(planes)
    print("-" * 60)
    print()


def main():
    """Función principal: gestiona el flujo completo de la aplicación."""
    mostrar_bienvenida()

    # ── Solicitar la ciudad al usuario ───────────────────────────────────────
    ciudad = input("📍 Ingresa el nombre de una ciudad: ").strip()

    if not ciudad:
        print("❌ No ingresaste ninguna ciudad. Por favor, vuelve a ejecutar el programa.")
        return

    print()
    print(f"🔍 Buscando planes para '{ciudad}'... (esto puede tardar unos segundos)")
    print()

    # ── Llamar al asistente y manejar errores ────────────────────────────────
    try:
        planes = obtener_planes(ciudad)
        mostrar_resultado(ciudad, planes)

    except EnvironmentError as e:
        # El token HF_TOKEN no está configurado
        print(f"\n{e}\n")

    except ConnectionError as e:
        # Fallo de red o API no disponible tras los reintentos
        print(f"\n{e}\n")

    except ValueError as e:
        # Respuesta vacía o inesperada del modelo
        print(f"\n⚠️  La respuesta del modelo no fue válida: {e}\n")

    except KeyboardInterrupt:
        print("\n\n👋 Programa interrumpido por el usuario.")

    except Exception as e:
        # Captura genérica para errores no previstos
        print(f"\n❌ Ocurrió un error inesperado: {type(e).__name__}: {e}\n")


# ── Punto de entrada ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()

