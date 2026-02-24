# 🗺️ Asistente de Planes Familiares con IA

Asistente de inteligencia artificial que recomienda **10 planes familiares, aptos para niños y de bajo coste o gratuitos** para cualquier ciudad que indiques.

Utiliza la API de inferencia de Hugging Face (modelo **Llama-3.2-3B-Instruct**), por lo que el modelo corre en los servidores de HF y **no consume recursos de tu PC**.

---

## 📁 Estructura del proyecto

```
asistente_de_planes/
├── main.py          → Punto de entrada del programa
├── asistente.py     → Lógica de llamada al modelo IA
├── config.py        → Lectura segura del token HF_TOKEN
├── requirements.txt → Dependencias necesarias
├── .env.example     → Plantilla para configurar tu token
└── .gitignore       → Excluye archivos sensibles de Git
```

---

## ⚙️ Preparar el entorno

### 1. Crear y activar el entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar el token de Hugging Face

Copia el archivo de ejemplo y añade tu token:

```bash
cp .env.example .env
```

Edita `.env` y reemplaza el valor:

```
HF_TOKEN=hf_tu_token_real_aqui
```

> 🔑 Consigue tu token gratuito en **https://huggingface.co/settings/tokens**
> (crea uno de tipo **Read**)

---

## ▶️ Ejecutar el programa

```bash
python main.py
```

El programa te pedirá el nombre de una ciudad y mostrará los 10 planes recomendados.

### Ejemplo de uso

```
📍 Ingresa el nombre de una ciudad: Granada

✅ 10 planes familiares recomendados para: GRANADA
------------------------------------------------------------
1. Visita a la Alhambra (entrada gratuita menores de 12 años): ...
2. Paseo por el Albaicín: ...
...
```

---

## 🔒 Seguridad

- **Nunca subas el archivo `.env` a GitHub.** Ya está incluido en el `.gitignore`.
- Si compartes el proyecto, usa `.env.example` como referencia.

