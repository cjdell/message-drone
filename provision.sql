BEGIN;

CREATE TABLE message (
   id           INTEGER     PRIMARY KEY   AUTOINCREMENT,
   name         TEXT        NOT NULL,
   message      TEXT        NOT NULL
);

COMMIT;
