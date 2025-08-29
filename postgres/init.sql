CREATE ROLE etl_writer LOGIN PASSWORD 'password';
CREATE ROLE etl_reader LOGIN PASSWORD 'password';

CREATE TABLE IF NOT EXISTS daily_avg (
  date DATE PRIMARY KEY,
  avg_close NUMERIC
);

GRANT INSERT, UPDATE, SELECT ON daily_avg TO etl_writer;
GRANT SELECT ON daily_avg TO etl_reader;