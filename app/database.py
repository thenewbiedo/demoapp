from sqlalchemy import create_engine
from sqlalchemy.engine.base import Connection
from sqlalchemy.engine.url import URL
from app import db  # Assuming db is an instance of SQLAlchemy engine

def fetch_todo() -> list[dict]:
    with db.connect() as conn:  # Use context manager for connection
        query_results = conn.execute("SELECT * FROM tasks;").fetchall()
    
    todo_list = []
    for result in query_results:
        item = {
            "id": result[0],
            "task": result[1],
            "status": result[2]
        }
        todo_list.append(item)
    
    return todo_list

def update_task_entry(task_id: int, text: str) -> None:
    with db.connect() as conn:  # Use context manager for connection
        query = f'UPDATE tasks SET task="{text}" WHERE id={task_id};'
        conn.execute(query)

def update_status_entry(task_id: int, status: str) -> None:
    with db.connect() as conn:  # Use context manager for connection
        query = f'UPDATE tasks SET status="{status}" WHERE id={task_id};'
        conn.execute(query)

def insert_new_task(text: str) -> int:
    with db.connect() as conn:  # Use context manager for connection
        query = f'INSERT INTO tasks (task, status) VALUES ("{text}", "Todo");'
        conn.execute(query)
        query_results = conn.execute("SELECT LAST_INSERT_ID();")
        task_id = query_results.fetchone()[0]  # Fetch the single result
    
    return task_id

def remove_task_by_id(task_id: int) -> None:
    """Remove entries based on task ID."""
    with db.connect() as conn:  # Use context manager for connection
        query = f'DELETE FROM tasks WHERE id={task_id};'
        conn.execute(query)
