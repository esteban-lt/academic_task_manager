"""Dibuja docs/arquitectura_capas.png y docs/navegacion.png.
Uso: python docs/fuentes/diagramas.py
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch, FancyBboxPatch, Rectangle

DOCS = Path(__file__).resolve().parents[1]
BLUE, BLUE_L = "#1565C0", "#E3EEFB"
GREEN, GREEN_L = "#2E7D32", "#E6F2E7"
TXT, MUTED = "#1F2933", "#5F6B7A"


def box(ax, x, y, w, h, title, sub="", fc="white", ec=BLUE, tc=TXT, size=12):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.15",
                                fc=fc, ec=ec, lw=1.8, zorder=2))
    if sub:
        ax.text(x + w / 2, y + h * 0.66, title, ha="center", va="center", fontsize=size,
                fontweight="bold", color=tc, zorder=3)
        ax.text(x + w / 2, y + h * 0.3, sub, ha="center", va="center", fontsize=9.2,
                color=MUTED, zorder=3, linespacing=1.4)
    else:
        ax.text(x + w / 2, y + h / 2, title, ha="center", va="center", fontsize=size,
                fontweight="bold", color=tc, zorder=3)


def arrow(ax, p1, p2, text="", both=False, rad=0.0, off=(0, 0.22), color=TXT):
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle="<|-|>" if both else "-|>", mutation_scale=16,
                                 lw=1.6, color=color, connectionstyle=f"arc3,rad={rad}", zorder=1,
                                 shrinkA=2, shrinkB=2))
    if text:
        ax.text((p1[0] + p2[0]) / 2 + off[0], (p1[1] + p2[1]) / 2 + off[1], text, ha="center",
                va="center", fontsize=9.2, color=TXT, zorder=4,
                bbox=dict(fc="white", ec="none", pad=1.2))


# --------------------------------------------------------------------------- capas
fig, ax = plt.subplots(figsize=(13, 7.2), dpi=150)
ax.set_xlim(0, 18)
ax.set_ylim(0, 10)
ax.axis("off")

# Contenedor de la app
ax.add_patch(FancyBboxPatch((0.3, 0.4), 8.4, 9.2, boxstyle="round,pad=0,rounding_size=0.3",
                            fc="#F5F7FA", ec=BLUE, lw=1.5, ls="--", zorder=0))
ax.text(4.5, 9.2, "App Flutter (Android · iOS · web)", ha="center", fontsize=13,
        fontweight="bold", color=BLUE)
layers = [
    ("Presentación", "pages: login, dashboard, task_form,\ntask_detail, subjects · widgets: task_card…"),
    ("Lógica y estado", "provider (ChangeNotifier): AuthProvider,\nTaskProvider, SubjectProvider · validaciones"),
    ("Repositorio", "AuthRepository, TaskRepository,\nSubjectRepository · modelos Task, Subject, User"),
    ("Cliente HTTP", "paquete http · JSON ↔ modelos\ntoken de sesión en cada petición"),
]
ys = [7.0, 5.0, 3.0, 1.0]
for (t, s), y in zip(layers, ys):
    box(ax, 0.9, y, 7.2, 1.55, t, s, fc="white")
for y1, y2 in zip(ys, ys[1:]):
    arrow(ax, (4.5, y1), (4.5, y2 + 1.55))

box(ax, 10.2, 3.6, 3.6, 2.8, "API REST",
    "/auth  /tareas  /materias\nvalida datos y permisos\ncredenciales en variables\nde entorno del servidor",
    fc=GREEN_L, ec=GREEN)
arrow(ax, (8.1, 1.78), (10.2, 4.3), "HTTPS + JSON", both=True, off=(0.75, -0.1))

# Cilindro de la base
cx, cy, cw, ch = 15.0, 3.7, 2.6, 2.4
ax.add_patch(Rectangle((cx, cy), cw, ch, fc=BLUE_L, ec="none", zorder=2))
ax.plot([cx, cx], [cy, cy + ch], color=BLUE, lw=1.8, zorder=3)
ax.plot([cx + cw, cx + cw], [cy, cy + ch], color=BLUE, lw=1.8, zorder=3)
ax.add_patch(Ellipse((cx + cw / 2, cy), cw, 0.6, fc=BLUE_L, ec=BLUE, lw=1.8, zorder=2.5))
ax.add_patch(Ellipse((cx + cw / 2, cy + ch), cw, 0.6, fc="white", ec=BLUE, lw=1.8, zorder=3))
ax.text(cx + cw / 2, cy + ch * 0.6, "Neon\nPostgres", ha="center", va="center",
        fontsize=12, fontweight="bold", color=TXT, zorder=4)
ax.text(cx + cw / 2, cy + ch * 0.3, "usuarios · materias\n· tareas", ha="center", va="center",
        fontsize=8.5, color=MUTED, zorder=4)
arrow(ax, (13.8, 5.0), (15.0, 5.0), "SQL", both=True, off=(0, 0.3))

ax.text(12.9, 1.4, "La app nunca se conecta directo a la base:\nno lleva usuario ni contraseña de Postgres.",
        ha="center", va="center", fontsize=9.5, color=MUTED, style="italic")
ax.text(12.9, 8.2, "Nube", ha="center", fontsize=13, fontweight="bold", color=GREEN)
fig.savefig(DOCS / "arquitectura_capas.png", bbox_inches="tight", facecolor="white")
plt.close(fig)

# --------------------------------------------------------------------------- navegación
fig, ax = plt.subplots(figsize=(13, 6.4), dpi=150)
ax.set_xlim(0, 18)
ax.set_ylim(0, 9)
ax.axis("off")
W, H = 3.2, 1.4
pos = {
    "login": (0.4, 3.8),
    "dash": (6.0, 3.8),
    "nueva": (11.6, 6.9),
    "detalle": (11.6, 3.8),
    "eliminar": (14.4, 0.6),
    "materias": (6.0, 0.6),
}
names = {
    "login": ("Login", "#login"),
    "dash": ("Dashboard", "#dashboard"),
    "nueva": ("Nueva tarea", "#nueva"),
    "detalle": ("Detalle de tarea", "#detalle"),
    "eliminar": ("¿Eliminar?", "#eliminar (diálogo)"),
    "materias": ("Materias", "#materias"),
}
for k, (x, y) in pos.items():
    fc = GREEN_L if k == "dash" else ("#FDECEA" if k == "eliminar" else "white")
    ec = GREEN if k == "dash" else ("#C62828" if k == "eliminar" else BLUE)
    box(ax, x, y, W, H, names[k][0], names[k][1], fc=fc, ec=ec, size=11.5)


def c(k, side):
    x, y = pos[k]
    return {"l": (x, y + H / 2), "r": (x + W, y + H / 2), "t": (x + W / 2, y + H),
            "b": (x + W / 2, y)}[side]


arrow(ax, c("login", "r"), c("dash", "l"), "Iniciar sesión")
arrow(ax, (pos["dash"][0] + 2.6, pos["dash"][1] + H), (pos["nueva"][0], pos["nueva"][1] + 0.9),
      "Botón + (FAB)", off=(-0.6, 0.35))
arrow(ax, (pos["nueva"][0], pos["nueva"][1] + 0.35), (pos["dash"][0] + W, pos["dash"][1] + 1.15),
      "Guardar → aviso\n«Tarea guardada»\no Cancelar", off=(1.25, 0.0))
arrow(ax, c("dash", "r"), c("detalle", "l"), "Toca una tarjeta", off=(0, 0.25))
arrow(ax, (pos["detalle"][0] + 2.4, pos["detalle"][1]), (pos["eliminar"][0] + 0.8, pos["eliminar"][1] + H),
      "Eliminar tarea", off=(0.5, 0.15))
arrow(ax, c("eliminar", "l"), (pos["dash"][0] + 2.4, pos["dash"][1]),
      "Eliminar → aviso «Tarea eliminada»", off=(0.2, -0.9))
arrow(ax, (pos["dash"][0] + 0.9, pos["dash"][1]), (pos["materias"][0] + 0.9, pos["materias"][1] + H),
      "Barra inferior", both=True, off=(-1.0, 0))
arrow(ax, (pos["dash"][0] + 0.3, pos["dash"][1] + H), (pos["login"][0] + 2.6, pos["login"][1] + H),
      "Salir", rad=0.35, off=(0, 1.0))
ax.text(9.0, 8.6, "Flechas de regreso (←) de Nueva, Detalle y Materias vuelven al Dashboard",
        ha="center", fontsize=9.5, color=MUTED, style="italic")
fig.savefig(DOCS / "navegacion.png", bbox_inches="tight", facecolor="white")
print("ok")
