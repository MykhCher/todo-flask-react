import json

from sqlalchemy import table, column

from ..db.db import Todo

TODO_TABLE = table(Todo.__tablename__, column('id'), column('title'))

def get_todos(con):
    query = TODO_TABLE.select()
    result = con.execute(query)

    todo_list = []

    for todo in result:
        todo_list.append({"id": todo[0], "title": todo[1]})

    return todo_list

def create_todo(con, data):
    new_title = json.loads(data).get('title')
    query = TODO_TABLE.insert().values(title=new_title).returning(TODO_TABLE.c.id, TODO_TABLE.c.title)
    result = con.execute(query)
    con.commit()

    todo_obj = result.fetchone()
    response = { "id": todo_obj[0], "title": todo_obj[1] }

    return response

def delete_todo(con, id):
    query = TODO_TABLE.delete().where(TODO_TABLE.c.id == id)
    result = con.execute(query)

    return [result.rowcount]

