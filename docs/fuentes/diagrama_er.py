"""Dibuja docs/diagrama_er.png (modelo de datos del Gestor de Tareas Académicas).

Notación pata de gallo: dos rayitas (||) = exactamente uno; tres patas = muchos.
Uso: python docs/fuentes/diagrama_er.py
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

OUT = Path(__file__).resolve().parents[1] / "diagrama_er.png"
ROW = 0.42
HEAD = 0.75
BLUE = "#1565C0"
GREEN = "#2E7D32"
TXT = "#1F2933"
MUTED = "#5F6B7A"

ENTITIES = {
    "usuarios": ("Usuario", 0.4, 10.6, 6.1, [
        ("PK", "id", "UUID"),
        ("", "nombre", "VARCHAR(100) NOT NULL"),
        ("UQ", "correo", "VARCHAR(150) NOT NULL"),
        ("", "password_hash", "VARCHAR(255) NOT NULL"),
        ("", "creado_en", "TIMESTAMPTZ DEFAULT now()"),
    ]),
    "materias": ("Materia", 11.3, 10.6, 6.1, [
        ("PK", "id", "UUID"),
        ("FK", "usuario_id", "UUID NOT NULL"),
        ("", "nombre", "VARCHAR(100) NOT NULL"),
        ("", "profesor", "VARCHAR(100)"),
        ("", "color", "VARCHAR(7)"),
        ("", "creado_en", "TIMESTAMPTZ DEFAULT now()"),
    ]),
    "tareas": ("Tarea", 5.4, 6.3, 7.0, [
        ("PK", "id", "UUID"),
        ("FK", "usuario_id", "UUID NOT NULL"),
        ("FK", "materia_id", "UUID NOT NULL"),
        ("", "titulo", "VARCHAR(150) NOT NULL"),
        ("", "tipo", "VARCHAR(10) CHECK"),
        ("", "urgencia", "VARCHAR(5) CHECK"),
        ("", "fecha_entrega", "TIMESTAMPTZ"),
        ("", "importante", "BOOLEAN DEFAULT false"),
        ("", "recordatorio", "BOOLEAN DEFAULT false"),
        ("", "esfuerzo", "SMALLINT CHECK 1–5"),
        ("", "creado_en", "TIMESTAMPTZ DEFAULT now()"),
    ]),
}


def entity(ax, key):
    title, x, top, w, fields = ENTITIES[key]
    h = HEAD + ROW * len(fields) + 0.15
    ax.add_patch(FancyBboxPatch((x, top - h), w, h, boxstyle="round,pad=0,rounding_size=0.18",
                                fc="white", ec=BLUE, lw=1.8, zorder=2))
    ax.add_patch(Rectangle((x, top - HEAD), w, HEAD, fc=BLUE, ec=BLUE, zorder=3))
    ax.text(x + 0.25, top - HEAD / 2, title, color="white", fontsize=13, fontweight="bold",
            va="center", zorder=4)
    ax.text(x + w - 0.25, top - HEAD / 2, key, color="#DCE8F8", fontsize=10, family="monospace",
            va="center", ha="right", zorder=4)
    for i, (tag, name, typ) in enumerate(fields):
        y = top - HEAD - ROW * (i + 0.5) - 0.07
        color = {"PK": "#B26A00", "FK": GREEN, "UQ": MUTED}.get(tag, TXT)
        ax.text(x + 0.2, y, tag, fontsize=8.5, fontweight="bold", color=color, va="center", zorder=4)
        ax.text(x + 0.8, y, name, fontsize=9.5, color=TXT, va="center", zorder=4,
                fontweight="bold" if tag == "PK" else "normal")
        ax.text(x + w - 0.2, y, typ, fontsize=8.5, family="monospace", color=MUTED,
                va="center", ha="right", zorder=4)
    return {"x": x, "top": top, "w": w, "bottom": top - h, "row": lambda i: top - HEAD - ROW * (i + 0.5) - 0.07}


def one(ax, x, y, direction):
    """Dos rayitas perpendiculares (exactamente uno) cerca de (x, y)."""
    dx, dy = direction
    for d in (0.25, 0.4):
        cx, cy = x + dx * d, y + dy * d
        ax.plot([cx - dy * 0.18, cx + dy * 0.18], [cy - dx * 0.18, cy + dx * 0.18], color=TXT, lw=1.6)


def many(ax, x, y, direction):
    """Pata de gallo (muchos) que toca la entidad en (x, y)."""
    dx, dy = direction
    bx, by = x + dx * 0.45, y + dy * 0.45
    for s in (-0.22, 0, 0.22):
        ax.plot([bx, x - dy * s], [by, y - dx * s], color=TXT, lw=1.6)
    cx, cy = x + dx * 0.6, y + dy * 0.6
    ax.plot([cx - dy * 0.18, cx + dy * 0.18], [cy - dx * 0.18, cy + dx * 0.18], color=TXT, lw=1.6)


def label(ax, x, y, text, **kw):
    ax.text(x, y, text, fontsize=10, color=TXT, ha="center", va="center",
            bbox=dict(fc="white", ec="none", pad=1.5), zorder=5, **kw)


fig, ax = plt.subplots(figsize=(13, 9.6), dpi=150)
ax.set_xlim(0, 17.8)
ax.set_ylim(-0.5, 11.2)
ax.axis("off")

u = entity(ax, "usuarios")
m = entity(ax, "materias")
t = entity(ax, "tareas")

# Usuario 1 ── N Materia (horizontal, a la altura de la fila "id")
y = u["row"](0)
ym = m["row"](1)
x1, x2 = u["x"] + u["w"], m["x"]
xm = (x1 + x2) / 2
ax.plot([x1, xm, xm, x2], [y, y, ym, ym], color=TXT, lw=1.6, zorder=1)
one(ax, x1, y, (1, 0))
many(ax, x2, ym, (-1, 0))
label(ax, xm, y + 0.35, "tiene")
label(ax, x1 + 0.55, y + 0.35, "1", fontweight="bold")
label(ax, x2 - 0.75, ym - 0.35, "N", fontweight="bold")

# Usuario 1 ── N Tarea (baja por la izquierda y entra en tareas.usuario_id)
ux = u["x"] + 1.6
ty = t["row"](1)
ax.plot([ux, ux, t["x"]], [u["bottom"], ty, ty], color=TXT, lw=1.6, zorder=1)
one(ax, ux, u["bottom"], (0, -1))
many(ax, t["x"], ty, (-1, 0))
label(ax, ux, (u["bottom"] + ty) / 2, "registra")
label(ax, ux + 0.35, u["bottom"] - 0.55, "1", fontweight="bold")
label(ax, t["x"] - 0.75, ty + 0.35, "N", fontweight="bold")

# Materia 1 ── N Tarea (baja por la derecha y entra en tareas.materia_id)
mx = m["x"] + m["w"] - 1.6
ty2 = t["row"](2)
tx2 = t["x"] + t["w"]
ax.plot([mx, mx, tx2], [m["bottom"], ty2, ty2], color=TXT, lw=1.6, zorder=1)
one(ax, mx, m["bottom"], (0, -1))
many(ax, tx2, ty2, (1, 0))
label(ax, mx, (m["bottom"] + ty2) / 2, "agrupa")
label(ax, mx + 0.35, m["bottom"] - 0.55, "1", fontweight="bold")
label(ax, tx2 + 0.75, ty2 + 0.35, "N", fontweight="bold")

ax.text(0.4, -0.05, "PK llave primaria · FK llave foránea · UQ único\n"
        "Pata de gallo = muchos · doble rayita = exactamente uno",
        fontsize=9.5, color=MUTED, va="center")
ax.text(17.4, -0.05, "tipo ∈ {Tarea, Proyecto, Examen}\nurgencia ∈ {Baja, Media, Alta}",
        fontsize=9.5, color=MUTED, va="center", ha="right", family="monospace")

fig.savefig(OUT, bbox_inches="tight", facecolor="white")
print(OUT)
