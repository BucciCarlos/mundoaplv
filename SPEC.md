# Especificaciones Técnicas y Arquitectura - Mundo APLV

## 1. Visión del Proyecto
Mundo APLV es una plataforma educativa y de soporte orientada a familias de niños con Alergia a la Proteína de la Leche de Vaca (APLV) y otras alergias alimentarias. Creada "de padres para padres", la plataforma traduce términos médicos a un lenguaje accesible, sin paywalls ni barreras económicas, con el fin de reducir la curva de aprendizaje tras el diagnóstico. Toda información médica provista advierte explícitamente que no reemplaza el consejo de un profesional de la salud.

## 2. Pila Tecnológica (Stack)
* **Backend:** Django 5.2 LTS (Monolito para el MVP, preparado para API Headless).
* **Frontend:** Tailwind CSS, Django Templates (Server-Side Rendering para SEO óptimo).
* **Base de Datos:** SQLite (Desarrollo) -> PostgreSQL (Producción) con extensión `pgvector`.
* **Entorno:** Linux Ubuntu nativo, Python 3.12.3.

## 3. Arquitectura de Datos (Módulos Base)
La lógica de negocio reside en `backend/apps/`:
* **`users`:** Gestión de roles de acceso (`PARENT`, `FAMILY`, `EDUCATOR`, `ADMIN`).
* **`taxonomy`:** Modelado estricto alineado con el Código Alimentario Argentino (CAA) y la Ley de Etiquetado. Incluye el registro de alérgenos y sus "nombres ocultos" (ej. caseína, suero).
* **`recipes`:** Recetario dinámico con filtrado relacional (Many-To-Many) en base a **`contains_allergens`** (Lógica *fail-safe* o *inseguro por defecto*, donde se declara qué alérgenos contiene la receta y se excluyen al buscar, previniendo falsos negativos médicos).
* **`articles`:** Base de conocimiento segmentada por perfil (Médico, Legal, Entorno Escolar, Familiar).

> [!NOTE]
> **Internacionalización (i18n) de Base de Datos:** Los campos de texto dinámico de negocio (descripciones de alérgenos, instrucciones de recetas, y contenido de artículos) se registrarán en `translation.py` mediante `django-modeltranslation`. Esto generará columnas dedicadas por idioma en la base de datos (ej. `instructions_es` e `instructions_en`) para garantizar una traducción nativa integral.

## 4. Hoja de Ruta (Roadmap y SDD)

### Fase 1: Producto Mínimo Viable (MVP) - En Desarrollo
* Estructuración del Monolito y Base de Datos (Modelos y Panel de Administración).
* Vistas estáticas informativas e Internacionalización (i18n).
* Sistema dinámico de filtrado de recetas por alérgeno excluido.
* Diseño UI responsivo orientado a accesibilidad.

### Fase 2: Comunidad y Contención - Futuro
* Integración de módulo de Foro para intercambio de información entre usuarios (médicos recomendados, soporte emocional).
* **Auditoría y Seguridad Anti-Estafas:** En consonancia con la Ley 27.305 (cobertura médica al 100% de leches medicamentosas en Argentina), se implementará un sistema automatizado de filtrado y logs para evitar transacciones comerciales no autorizadas. Las publicaciones del foro serán supervisadas para asegurar que se limite estrictamente a donaciones y redes de apoyo sin fines de lucro.

### Fase 3: Integración de Inteligencia Artificial - Futuro
* **Escáner de Etiquetas:** Procesamiento de imágenes (OCR) para identificar "nombres ocultos" de alérgenos en ingredientes según normativa local.
* **Chatbot RAG (Retrieval-Augmented Generation):** Implementación de una base de datos vectorial (`pgvector` en PostgreSQL) combinada con LLMs mediante `django-ninja` usando controladores asíncronos (`async def`) para evitar bloquear el hilo principal. La IA responderá consultas basándose estrictamente en el corpus de conocimiento validado de la plataforma para asegurar precisión médica y evitar alucinaciones.

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
