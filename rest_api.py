from fastapi import FastAPI
import mysql.connector

app = FastAPI()

def conn():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "*****",
        database = "sample_db_ai"
    )
    
@app.get("/tasks")
def get_tasks():
    c = conn()
    cursor = c.cursor(dictionary=True) # returns each row as a dictionary
    cursor.execute("select * from tasks")
    rows = cursor.fetchall()
    cursor.close()
    c.close()
    return rows

@app.post("/tasks/{title}")
def insert_task(title: str):
    c = conn()
    cursor = c.cursor()
    cursor.execute("insert into tasks (title) values (%s)", (title,))
    c.commit()
    cursor.close()
    c.close()
    return {"status": "inserted"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    c = conn()
    cursor = c.cursor()
    cursor.execute("delete from tasks where id = %s", (task_id,))
    c.commit()
    cursor.close()
    c.close()
    return {"status": "deleted"}