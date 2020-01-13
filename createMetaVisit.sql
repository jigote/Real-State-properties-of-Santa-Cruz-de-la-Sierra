CREATE TABLE visits_log (
  log_id SERIAL PRIMARY KEY,
  no_of_visits INTEGER NOT NULL,
  ip_address varchar(20) NULL,
  requested_url varchar(20) NULL,
  referer_page varchar(20) NULL,
  page_name varchar(20) NULL,
  query_string varchar(20) NULL,
  user_agent varchar(20) NULL,
  is_unique varchar(20) NOT NULL DEFAULT '0',
  access_date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

