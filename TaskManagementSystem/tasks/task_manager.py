from db.db import create_connection

def add_task(user_id, title, description):
    conn, cursor = create_connection()
    with conn:
        cursor.execute("INSERT INTO tasks(user_id, task_title, task_description) VALUES (%s,%s,%s)",(user_id, title, description))
        conn.commit()
    
def remove_task(task_id):
    conn, cursor = create_connection()
    with conn:
        cursor.execute("DELETE FROM tasks WHERE id = %s",(task_id,))
        conn.commit()

def update_tasks(task_id, status):
    conn, cursor = create_connection()
    with conn:
        cursor.execute("UPDATE tasks SET status = %s WHERE id = %s",(status, task_id))
        conn.commit()
def get_task(user_id):
    conn, cursor = create_connection()
    if conn is None or cursor is None:
        return []
    with conn:
        cursor.execute("SELECT id, task_title, task_description, status FROM tasks WHERE user_id = %s",(user_id,))
        tasks = cursor.fetchall()
        return tasks

