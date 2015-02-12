drop table if exists tasks;
create table tasks (
      id integer primary key autoincrement,
      category text not null,
      description text not null,
      priority text not null
);
