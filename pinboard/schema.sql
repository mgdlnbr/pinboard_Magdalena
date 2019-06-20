DROP TABLE IF EXISTS post;

CREATE TABLE post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    color TEXT NOT NULL,
    likes INTEGER DEFAULT 0,
    liked_by_user TEXT Default test
);
