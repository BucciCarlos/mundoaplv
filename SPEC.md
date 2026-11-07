# Especificaciones Técnicas y Arquitectura - Mundo APLV

## 1. Visión del Proyecto
Mundo APLV es una plataforma integral, gratuita y accesible de información, recursos educativos y acompañamiento, creada «de padres para padres». Se dirige principalmente a padres, madres y familias que conviven con Alergia a la Proteína de la Leche de Vaca (APLV), especialmente ante un diagnóstico reciente; otras alergias alimentarias son una temática secundaria. También contempla abuelos, familiares, amigos, cuidadores, docentes y centros educativos. Argentina es el contexto principal para normativa, etiquetado y productos, sin limitar necesariamente el conocimiento general al país.

No es una guía clínica para profesionales, un foro como producto principal, exclusivamente un recetario, una tienda ni un blog autobiográfico; no se centra en un caso familiar particular. La información esencial debe permanecer gratuita y accesible, sin convertir recursos sanitarios indispensables en productos pagos.

### Criterios editoriales y experiencia

**La experiencia familiar sirve para identificar las preguntas. La evidencia científica sirve para construir las respuestas.** El lenguaje cotidiano debe ser cercano y las explicaciones médicas rigurosas, claras y accesibles, con empatía y sin alarmismo ni falsas garantías. Los artículos deben responder preferentemente a preguntas reales, permitir profundizar y consultar fuentes, y distinguir evidencia sólida, cuestiones debatidas y experiencias anecdóticas. Priorizar guías clínicas, sociedades científicas, consensos, revisiones sistemáticas y estudios pertinentes; evitar afirmaciones médicas o alimentarias absolutas.

La plataforma explica y contextualiza, sin prescribir ni sustituir decisiones individualizadas del equipo tratante sobre fórmulas, medicamentos, tratamientos, pruebas de provocación o reintroducción. Los responsables y el procedimiento de revisión editorial siguen pendientes de definición.

La home debe representar la plataforma integral y facilitar el descubrimiento de sus áreas con comunicación clara, progresiva y accesible. No debe parecer una portada de foro o una enciclopedia médica especializada, ni centrarse exclusivamente en testimonios, recetas o compras. El menú y el diseño visual no están definidos.

### Áreas conceptuales

Comprender la APLV; leches y fórmulas infantiles; otras alergias y condiciones relacionadas, incluida dermatitis atópica; alimentación, etiquetas, ingredientes, productos y contaminación cruzada; recetas y sustituciones; vida cotidiana; recursos para familiares, cuidadores e instituciones; materiales infantiles; historias familiares; y comunidad futura. Son áreas de interés, no un menú definitivo ni compromisos de implementación inmediata.

Existe interés en cuentos, historias y actividades infantiles originales, para comprender alergias, favorecer inclusión y convivencia, comunicar necesidades, pedir ayuda y desarrollar autonomía apropiada a la edad. Se desean lectura digital y PDF imprimible, con posibles materiales para adultos y escuelas. Los niños pequeños no deben ser los únicos responsables de su seguridad alimentaria; no se reutilizarán personajes o materiales protegidos. Su inclusión en el primer MVP está pendiente.

Se prefiere un enfoque colectivo de «Historias familiares» a una sección centrada en la historia del fundador. Pueden contemplarse relatos anónimos o desidentificados; los testimonios de terceros requieren consentimiento y las experiencias inventadas no se presentarán como reales. Los planes individualizados de emergencia y tratamientos corresponden a profesionales y cuidadores responsables.

## 2. Pila Tecnológica (Stack)
* **Backend:** Django 5.2 LTS (Monolito para el MVP, preparado para API Headless).
* **Frontend:** Tailwind CSS, Django Templates (Server-Side Rendering para SEO óptimo).
* **Base de Datos:** SQLite (desarrollo) y configuración de producción mediante `DATABASE_URL`; PostgreSQL y `pgvector` se contemplan para capacidades futuras, sin acreditar su despliegue actual.
* **Entorno:** Linux Ubuntu nativo, Python 3.12.3.

## 3. Arquitectura de Datos (Módulos Base)
La lógica de negocio reside en `backend/apps/`:
* **`users`:** Gestión de roles de acceso (`PARENT`, `FAMILY`, `EDUCATOR`, `ADMIN`).
* **`taxonomy`:** Modelado estricto alineado con el Código Alimentario Argentino (CAA) y la Ley de Etiquetado. Incluye el registro de alérgenos y sus "nombres ocultos" (ej. caseína, suero).
* **`recipes`:** El modelo registra alérgenos declarados mediante la relación **`contains_allergens`**. El filtrado dinámico es un objetivo a evaluar, no una funcionalidad verificada en las vistas actuales. La ausencia de alérgenos registrados no demuestra que una receta sea segura ni previene por sí sola falsos negativos; quedan pendientes la validación del alcance y, si fuera necesario, el rediseño de la solución.
* **`articles`:** Base de conocimiento segmentada por perfil (Médico, Legal, Entorno Escolar, Familiar).

> [!NOTE]
> **Internacionalización (i18n) de Base de Datos:** Los campos de texto dinámico de negocio (descripciones de alérgenos, instrucciones de recetas, y contenido de artículos) se registrarán en `translation.py` mediante `django-modeltranslation`. Esto generará columnas dedicadas por idioma en la base de datos (ej. `instructions_es` e `instructions_en`) para garantizar una traducción nativa integral.

## 4. Hoja de Ruta (Roadmap y SDD)

### Fase 1: Producto Mínimo Viable (MVP) - En Desarrollo
La prioridad es una primera versión pública informativa, útil, accesible y prudente. No requiere inicialmente usuarios públicos, foro, OCR, RAG ni marcas verificadas. Los contenidos concretos y criterios de aceptación siguen pendientes; los elementos siguientes describen trabajo existente u objetivos, no aprobación automática de todo su alcance.

* Estructuración del Monolito y Base de Datos (Modelos y Panel de Administración).
* Vistas estáticas informativas e Internacionalización (i18n).
* Filtrado dinámico de recetas por alérgeno excluido: alcance y seguridad pendientes de evaluación.
* Diseño UI responsivo orientado a accesibilidad.

### Fase 2: Comunidad y Contención - Futuro
* Un foro moderado para intercambio y apoyo es una posibilidad futura y complementaria; no es el núcleo del producto. Su alcance, arquitectura, fecha y mecanismos de moderación, incluida cualquier automatización, no están decididos.
* Si se considera, evaluar riesgos de estafas y transacciones, donaciones y normativa aplicable, incluida la Ley 27.305, antes de definir reglas o soluciones.

### Fase 3: Integración de Inteligencia Artificial - Futuro
Son ideas futuras, no requisitos del MVP ni decisiones definitivas de implementación:
* **Escáner de etiquetas:** explorar OCR para identificar posibles nombres de alérgenos en ingredientes según normativa local, sin asumir que garantice seguridad.
* **Chatbot RAG (Retrieval-Augmented Generation):** se ha propuesto combinar un corpus validado con una base vectorial y LLM, mediante `pgvector`, `django-ninja` y controladores asíncronos. Su necesidad, arquitectura y garantías requieren evaluación; basarse en fuentes validadas no elimina por sí solo los errores.

## 5. Ejecución local con settings de producción

Desde `backend/`, definir variables temporales seguras y una `DATABASE_URL` explícita. Para una comprobación local no persistente se puede usar `sqlite://:memory:`.

```bash
export DJANGO_SETTINGS_MODULE=core.settings.production
export DJANGO_SECRET_KEY='<clave-aleatoria-de-al-menos-50-caracteres>'
export DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
export DJANGO_CSRF_TRUSTED_ORIGINS=https://localhost
export DATABASE_URL=sqlite://:memory:

python manage.py collectstatic --noinput
./start-production.sh
```

El script de arranque ejecuta `gunicorn core.wsgi:application` y usa `PORT` si está definido, o el puerto `8000` localmente. Production requiere sus variables en el entorno del proceso; no carga `backend/.env`.
