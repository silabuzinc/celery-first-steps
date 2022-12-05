from celery import Celery
import time

# Por default una instancia de Redis admite 16 bases de datos lógicas,
# aisladas entre sí, numeradas del 0 al 15.
# De forma predeterminada se conecta a la base de dato cero.
app = Celery(
    "tasks", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0"
)


@app.task
def calculando_suma(x, y):
    time.sleep(3)
    return x + y
