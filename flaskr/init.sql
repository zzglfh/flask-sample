
create table  if not EXISTS user_blog (
  id integer primary key autoincrement,
  title text not null,
  text text not null,
  user_id int not null
);
create table if not EXISTS t_user (
  id integer primary key autoincrement,
  name text not null,
  account text not null,
  mobile text not null,
  mobile_valid INTEGER not null,
  email text not null,
  email_valid INTEGER not null,
  valid_flag INTEGER not null
);