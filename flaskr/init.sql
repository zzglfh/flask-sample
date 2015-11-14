drop table if exists user_blog;
create table user_blog (
  id integer primary key autoincrement,
  title text not null,
  text text not null,
  user_id int not null
);