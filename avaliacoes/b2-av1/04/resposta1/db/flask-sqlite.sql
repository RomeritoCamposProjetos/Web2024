
create table if not exists usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);

create table if not exists pecas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL
);

create table if not exists dancas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    danca TEXT NOT NULL,
    usuario INTEGER NOT NULL
);