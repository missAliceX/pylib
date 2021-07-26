CREATE TABLE IF NOT EXISTS projects (
    project_id serial PRIMARY KEY,
    project_name VARCHAR ( 80 ) UNIQUE NOT NULL,
    tagline VARCHAR ( 255 ) NOT NULL
);

CREATE TABLE IF NOT EXISTS threads (
    thread_id bigserial PRIMARY KEY,
    project_id integer REFERENCES projects NOT NULL,
    parent_thread_id integer REFERENCES threads ON DELETE CASCADE,
    thread_type smallint NOT NULL,
    message text NOT NULL
);

CREATE TABLE IF NOT EXISTS tags (
    tag_id bigserial PRIMARY KEY,
    project_id integer REFERENCES projects,
    thread_id integer REFERENCES threads,
    tag VARCHAR( 50 ) NOT NULL
);