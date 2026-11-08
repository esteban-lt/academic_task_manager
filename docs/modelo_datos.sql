-- Gestor de Tareas Académicas: modelo de datos (solo diseño, Neon Postgres).
-- No se ejecuta en esta fase; sirve de referencia para el diagrama ER y la API.

CREATE TABLE usuarios (
  id             UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
  nombre         VARCHAR(100) NOT NULL,
  correo         VARCHAR(150) NOT NULL UNIQUE,
  password_hash  VARCHAR(255) NOT NULL,          -- nunca la contraseña en texto plano
  creado_en      TIMESTAMPTZ  NOT NULL DEFAULT now()
);

-- Cada usuario tiene sus propias materias (Usuario 1:N Materia).
CREATE TABLE materias (
  id          UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
  usuario_id  UUID         NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
  nombre      VARCHAR(100) NOT NULL,
  profesor    VARCHAR(100),
  color       VARCHAR(7)   NOT NULL DEFAULT '#1565C0',  -- color del punto en la lista
  creado_en   TIMESTAMPTZ  NOT NULL DEFAULT now(),
  UNIQUE (usuario_id, nombre)
);

-- Usuario 1:N Tarea y Materia 1:N Tarea.
CREATE TABLE tareas (
  id             UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
  usuario_id     UUID         NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
  materia_id     UUID         NOT NULL REFERENCES materias(id) ON DELETE RESTRICT,
  titulo         VARCHAR(150) NOT NULL CHECK (char_length(trim(titulo)) >= 3),
  tipo           VARCHAR(10)  NOT NULL DEFAULT 'Tarea'
                 CHECK (tipo IN ('Tarea', 'Proyecto', 'Examen')),
  urgencia       VARCHAR(5)   NOT NULL DEFAULT 'Media'
                 CHECK (urgencia IN ('Baja', 'Media', 'Alta')),
  fecha_entrega  TIMESTAMPTZ,
  importante     BOOLEAN      NOT NULL DEFAULT false,
  recordatorio   BOOLEAN      NOT NULL DEFAULT false,
  esfuerzo       SMALLINT     NOT NULL DEFAULT 3 CHECK (esfuerzo BETWEEN 1 AND 5),
  creado_en      TIMESTAMPTZ  NOT NULL DEFAULT now()
);

-- La lista del dashboard filtra por usuario y ordena por fecha de entrega.
CREATE INDEX idx_tareas_usuario_fecha ON tareas (usuario_id, fecha_entrega);
