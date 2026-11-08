# Guía de estilo: Gestor de Tareas Académicas

Es la misma que usa el prototipo: todos los valores salen de las variables `:root` de
[`design/prototype/styles.css`](../design/prototype/styles.css). Sigue Material Design 3 con
una paleta sobria en azul y verde. Al pasar a Flutter, los colores van al `ColorScheme`
y las medidas a constantes de tema.

## 1. Paleta de colores

| Rol | Variable | Hex | Uso |
|---|---|---|---|
| Primario | `--primary` | `#1565C0` | App bar, botón principal, enlaces, íconos activos |
| Primario oscuro | `--primary-dark` | `#0D47A1` | Botón presionado, texto sobre contenedor primario |
| Contenedor primario | `--primary-container` | `#E3EEFB` | FAB, chip seleccionado, pestaña activa, logo |
| Secundario (verde) | `--secondary` | `#2E7D32` | Urgencia baja (barra lateral), estados positivos |
| Verde oscuro | `--secondary-dark` | `#1B5E20` | Texto del chip "Baja" |
| Contenedor secundario | `--secondary-container` | `#E6F2E7` | Fondo del chip "Baja" |
| Acento (ámbar) | `--accent` | `#F9A825` | Urgencia media (barra), estrella de importante |
| Texto ámbar | `--accent-text` | `#8A5300` | Texto del chip "Media" |
| Contenedor ámbar | `--accent-container` | `#FFF4E0` | Fondo del chip "Media" |
| Peligro (rojo) | `--danger` | `#C62828` | Urgencia alta, eliminar |
| Contenedor rojo | `--danger-container` | `#FDECEA` | Fondo del chip "Alta" y del ícono del diálogo |
| Fondo | `--bg` | `#F5F7FA` | Fondo de las pantallas |
| Superficie | `--surface` | `#FFFFFF` | Tarjetas, campos, barra inferior, diálogos |
| Texto | `--text` | `#1F2933` | Texto principal |
| Texto secundario | `--text-2` | `#5F6B7A` | Etiquetas, fechas, ayudas |
| Borde | `--border` | `#D9E0E8` | Bordes de campos, chips y divisores |

**Contraste (WCAG):** todas las combinaciones de texto pasan 4.5:1 (nivel AA).

| Combinación | Contraste |
|---|---|
| Blanco sobre `--primary` | 5.7 : 1 |
| `--text` sobre `--surface` | 14.8 : 1 |
| `--text-2` sobre `--surface` | 5.4 : 1 |
| `--primary-dark` sobre `--primary-container` | 7.4 : 1 |
| `--secondary-dark` sobre `--secondary-container` | 6.8 : 1 |
| `--accent-text` sobre `--accent-container` | 5.8 : 1 |
| `--danger` sobre `--danger-container` | 4.9 : 1 |
| Blanco sobre `--danger` | 5.6 : 1 |

**Colores de urgencia** (siempre con texto además del color, para no depender solo de él):
Baja = verde, Media = ámbar, Alta = rojo.

## 2. Tipografía

Fuente: **Roboto** (la de Material), pesos 400, 500 y 700. Respaldo: Arial, sans-serif.

| Estilo | Tamaño / interlineado | Peso | Uso |
|---|---|---|---|
| Encabezado (h1) | 24 / 32 px | 700 | Saludo del dashboard, título del login, título en detalle (22 px) |
| Título de barra | 20 / 28 px | 500 | Texto del app bar |
| Subtítulo | 16 / 24 px | 500 | Título de cada tarjeta de tarea o materia |
| Cuerpo | 14 / 20 px | 400 | Texto general, campos, botones (500) |
| Leyenda | 12 / 16 px | 400–500 | Etiquetas de campo, chips, fechas, ayudas, secciones en MAYÚSCULAS |

## 3. Iconografía

**Material Icons** (estilo relleno), 24 px por defecto, 20 px dentro de campos y botones,
16 px dentro de chips. Color: `--text-2` en campos, `--primary` en listas de detalle, blanco
en el app bar.

| Ícono | Dónde |
|---|---|
| `school` | Logo del login |
| `checklist` · `menu_book` · `logout` | Barra inferior: Tareas, Materias, Salir |
| `add` | FAB "Nueva" y "Materia" |
| `arrow_back` · `search` · `filter_list` · `edit` | App bar |
| `task_alt` · `category` · `event` | Campos de título, tipo y fecha |
| `star` / `star_outline` | Importante |
| `notifications_none` / `notifications_active` | Recordatorio |
| `timer` | Esfuerzo |
| `delete_outline` | Eliminar |
| `check_circle` | Aviso de éxito (snackbar) |

## 4. Botones y controles

| Componente | Estilo |
|---|---|
| Botón principal | Fondo `--primary`, texto blanco, alto 48 px, esquinas de píldora (999 px), sombra nivel 1 |
| Botón secundario | Contorno `--border`, texto `--primary`, fondo blanco |
| Botón de peligro | Contorno y texto `--danger`; dentro del diálogo, relleno `--danger` con texto blanco |
| Botón de texto | Sin fondo, texto `--primary` |
| FAB extendido | Alto 56 px, radio 16 px, fondo `--primary-container`, texto `--primary-dark`, sombra nivel 2; 16 px sobre la barra inferior |
| Campo de texto | Alto 48 px, borde 1 px `--border`, radio 8 px, ícono a la izquierda; al enfocar, borde 2 px `--primary` |
| Chip | Alto 28 px (32 px en filtros), radio de píldora, texto 12 px; seleccionado con `--primary-container` |
| Selector de urgencia | Botones segmentados de 40 px; la opción elegida con `--primary-container` y palomita |
| Casilla / interruptor / slider | Color `--primary` (`accent-color`); interruptor de 44 × 24 px |
| Aviso (snackbar) | Fondo `#2B3440`, texto blanco, radio 8 px, aparece arriba del FAB 2.5 s |

Áreas táctiles de al menos **48 × 48 px**.

## 5. Espaciado, bordes, sombras y layout

- **Espaciado:** escala de 4 px: 4, 8, 12, 16, 24, 32 (`--s1` a `--s6`). Margen de pantalla 16 px;
  separación entre tarjetas 12 px; entre secciones 24 px.
- **Bordes (radio):** 8 px campos y avisos · 12 px tarjetas · 16 px FAB y diálogos · 999 px botones y chips.
- **Sombras:** nivel 1 `0 1px 3px rgba(16,24,40,.12)` en tarjetas y app bar; nivel 2
  `0 4px 12px rgba(16,24,40,.18)` en FAB, diálogos y avisos.
- **Layout:** diseño para teléfono de 390 × 844 px. App bar de 56 px arriba, barra inferior de
  64 px (en Dashboard y Materias), contenido con scroll en medio. Formularios en una columna;
  campos cortos (tipo y fecha) pueden ir en dos columnas. Las tarjetas de tarea llevan una barra
  izquierda de 4 px con el color de urgencia.
- **Wireframes:** la misma estructura en escala de grises, Arial, sin sombras y con bordes
  punteados (clase `.wireframe`).
