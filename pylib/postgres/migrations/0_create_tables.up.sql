DO $$ BEGIN
    CREATE TYPE thread_type AS ENUM ('COMMENT', 'SOLUTION', 'PROBLEM');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

CREATE TABLE IF NOT EXISTS projects (
    project_id serial PRIMARY KEY,
    project_name VARCHAR ( 80 ) UNIQUE NOT NULL,
    tagline VARCHAR ( 255 ) NOT NULL
);

CREATE TABLE IF NOT EXISTS threads (
    thread_id bigserial PRIMARY KEY,
    project_id integer REFERENCES projects NOT NULL ON DELETE CASCADE,
    thread_type thread_type NOT NULL,
    message text NOT NULL
);

CREATE TABLE IF NOT EXISTS tags (
    tag_id bigserial PRIMARY KEY,
    project_id integer REFERENCES projects,
    tag VARCHAR( 50 ) NOT NULL
);