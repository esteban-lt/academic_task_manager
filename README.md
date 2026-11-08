# Gestor de Tareas Académicas

Fase de **arquitectura, modelo de datos, UI/UX y prototipo navegable** (Actividad 3, Unidad 3 de
Desarrollo de Aplicaciones Móviles). App para registrar, listar y eliminar tareas escolares
(título, materia, tipo, urgencia, fecha, importante, recordatorio y esfuerzo).

- **Prototipo navegable:** https://esteban-lt.github.io/academic_task_manager/design/prototype/index.html
  (versión wireframe: agrega `?wireframe` antes del `#`)
- **Documento de arquitectura (PDF):** [docs/Actividad_3_Unidad_3.pdf](docs/Actividad_3_Unidad_3.pdf)

## Contenido

| Carpeta | Qué hay |
|---|---|
| `docs/` | PDF de arquitectura, [guía de estilo](docs/guia_estilo.md), diagrama ER, diagramas de capas y navegación, [modelo de datos en SQL](docs/modelo_datos.sql) |
| `docs/fuentes/` | Scripts de Python que dibujan los diagramas |
| `docs/material/` | Enunciado de la actividad y contexto del mini-proyecto |
| `design/prototype/` | Prototipo en HTML/CSS (una pantalla por sección, navegación con `#pantalla` y `:target`) |
| `design/wireframes/` · `design/prototipo/` | Capturas a 390 × 844 px |

## Decisiones principales

- App **multiplataforma con Flutter**: presentación → lógica y estado (`provider`) → repositorio → cliente `http`.
- Datos en **Neon Postgres** detrás de una **API REST**; la app nunca se conecta directo a la base.
- Entidades **Usuario**, **Materia** y **Tarea** (Usuario 1:N Tarea, Materia 1:N Tarea, Usuario 1:N Materia).

Regenerar diagramas y capturas: `python docs/fuentes/diagrama_er.py`, `python docs/fuentes/diagramas.py`
y `bash design/capturas.sh` (Git Bash, con Chrome instalado).
