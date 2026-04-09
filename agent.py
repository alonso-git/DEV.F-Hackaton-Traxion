import json
import openai # Ejemplo usando la interfaz estándar de OpenAI/Gemini

# 1. Simulación de carga de archivos locales (Tus Lineamientos)
with open('agente_config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# 2. Datos recibidos por HTTP (Request DTO)
request_payload = {
    "cliente_id": "TX-3245",
    "cliente_giro": "Educativo",
    "metricas_operativas": {
        "nivel_servicio": 85,
        "puntualidad": 85,
        "nps": 60,
        "quejas_abiertas": 2
    }
}

# 3. Construcción del Prompt dinámico
def generar_prompt(config_agente, datos_cliente):
    # Extraemos lineamientos y reglas del JSON local
    lineamientos = "\n- ".join(config_agente['agente_logic']['lineamientos_generales'])
    reglas = json.dumps(config_agente['agente_logic']['reglas_clasificacion'], indent=2)
    formato_respuesta = json.dumps(config_agente['response_dto'], indent=2)

    prompt = f"""
    ROL: {config_agente['agente_logic']['rol']}
    
    LINEAMIENTOS:
    - {lineamientos}
    
    REGLAS DE CLASIFICACIÓN:
    {reglas}
    
    DATOS DEL CLIENTE A ANALIZAR:
    {json.dumps(datos_cliente, indent=2)}
    
    INSTRUCCIÓN: 
    Analiza los datos, calcula el riesgo y el score de salud basándote en las reglas.
    Es obligatorio responder ÚNICAMENTE en formato JSON siguiendo esta estructura:
    {formato_respuesta}
    """
    return prompt

# 4. Llamada al modelo
client = openai.OpenAI(api_key="TU_API_KEY")

response = client.chat.completions.create(
    model="gpt-4-turbo-preview", # o gemini-1.5-pro
    messages=[
        {"role": "system", "content": "Eres un asistente técnico que solo responde en JSON."},
        {"role": "user", "content": generar_prompt(config, request_payload)}
    ],
    response_format={"type": "json_object"}
)

# El resultado final listo para el frontend
resultado_final = json.loads(response.choices[0].message.content)
print(resultado_final)