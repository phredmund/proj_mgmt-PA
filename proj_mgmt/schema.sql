DROP TABLE IF EXISTS project;
DROP TABLE IF EXISTS team_member;
DROP TABLE IF EXISTS requirements;

CREATE TABLE project (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  proj_name TEXT UNIQUE NOT NULL,
  description TEXT NOT NULL,
  manager TEXT NOT NULL
);

CREATE TABLE team_member (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL
);

CREATE TABLE requirements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    proj_name TEXT NOT NULL,
    functional INTEGER NOT NULL,
    state INTEGER NOT NULL,
    FOREIGN KEY (proj_name) REFERENCES project (proj_name)
);

CREATE TABLE risks (
    id INTEGER primary key AUTOINCREMENT,
    risk_name TEXT NOT NULL,
    project_name TEXT NOT NULL,
    description TEXT NOT NULL,
    severity integer NOT NULL,
    mitigated integer NOT NULL,
    FOREIGN KEY (project_name) REFERENCES project (proj_name)
);