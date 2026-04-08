Traxión Tech Challenge 2026 - Eje 2: Customer Health 

🚛💡Este proyecto presenta una solución de IA Conversacional diseñada para la detección temprana de clientes en riesgo dentro de la operación de Traxión. El objetivo es transformar la gestión reactiva actual en una cultura preventiva mediante el análisis de señales operativas simples.

📋 El Problema
Actualmente, las métricas de servicio se analizan de forma aislada y las alertas preventivas son inexistentes. Esto genera una reacción tardía ante la inconformidad del cliente y pérdida de oportunidades de retención.

🧠 La Solución: Agente de IA Proactivo
Hemos diseñado un agente que integra múltiples métricas (NPS, Puntualidad, Nivel de Servicio y Quejas) en una sola lectura de riesgo.

Lógica del Modelo (Business Logic)
El "cerebro" del agente se basa en reglas de clasificación estandarizadas para reducir la variabilidad en la toma de decisiones:
Riesgo Crítico: Activado por puntualidad < 80% o ≥ 3 quejas abiertas.
Riesgo Medio: Activado por NPS < 30 o Nivel de Servicio < 90%.
Diagnóstico Claro: El agente no solo clasifica, sino que explica el supuesto detrás de cada alerta.

🛠️ Estructura Técnica
Aunque el prototipo es estático (HTML/CSS), el proyecto está diseñado siguiendo una arquitectura de datos escalable basada en JSON.

Componentes:
Request DTO: Contrato de datos que simula la entrada desde formularios operativos o telemetría.
Logic Engine: Definición de prompts y reglas de negocio para el modelo de lenguaje (LLM).
Response DTO: Estructura de salida que alimenta la interfaz de usuario con acciones concretas de prevención.

🚀 Entregables Incluidos
Agente de IA: Reglas de clasificación y recomendaciones accionables.
Prototipo Web: Interfaz en HTML/CSS con semáforo de riesgo y carga de métricas simuladas.
Documento Ejecutivo: Resumen de impacto, lógica y limitaciones del modelo.

⚙️ Instalación y Uso
Clona el repositorio:
git clone https://github.com/alonso-git/DEV.F-Hackaton-Traxion.git

Abre index.html en tu navegador para ver el prototipo.
Consulta CustomerHealthAgent.json para revisar las reglas de decisión del agente.

⚠️ Limitaciones y Siguientes Pasos
El prototipo actual es una interfaz estática y no requiere conexión a bases de datos reales.
Siguiente fase: Implementación de una API RESTful para conectar el Logic Engine con modelos de lenguaje avanzados (Gemini/GPT).

Proyecto desarrollado para el Hackatón Bécalos Traxión Tech Challenge 2026.