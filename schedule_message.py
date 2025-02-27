import sched
import time
import pandas as pd
from datetime import datetime

schedule = sched.scheduler(time.time, time.sleep)

def send_message(*data):
    for contact in data:
        message = f"Olá {contact[0]}, não se esqueça de entrar no site https://alistamento.eb.mil.br/ e verificar a data de apresentação na Organização Militar correspondente."
        print(f"Mensagem enviada para {contact[0]} ({contact[1]}): {message}\n")

def schedule_message(date_time_str, data):
    date_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
    delay = (date_time - datetime.now()).total_seconds()
    if delay >= 0:
        schedule.enter(delay, 1, send_message, argument=(data))
    else:
        print("A data e hora especificadas já passaram.")

def read_contact_from_excel(file_path):
    df = pd.read_excel(file_path)
    data = df.values.tolist()
    return data

if __name__ == "__main__":
    # Substitua esta string pela data e hora desejadas
    date_time_str = "2025-02-27 15:23:00"
    # Substitua pelo caminho para o seu arquivo Excel
    excel_file_path = ".\Teste 1.xlsx"

    data = read_contact_from_excel(excel_file_path)
    schedule_message(date_time_str, data)

    while True:
        schedule.run(blocking=False)
        time.sleep(1)