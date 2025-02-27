import schedule
import time
import pandas as pd
from datetime import datetime

def send_message(name, phone_number):
    message = f"Olá {name}, não se esqueça de entrar no site https://alistamento.eb.mil.br/ e verificar a data de apresentação na Organização Militar correspondente."
    print(f"Mensagem enviada para {name} ({phone_number}): {message}")

def schedule_message(date_time_str, name, phone_number):
    date_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
    delay = (date_time - datetime.now()).total_seconds()
    if delay > 0:
        schedule.enter(delay, 1, send_message, argument=(name, phone_number))
    else:
        print("A data e hora especificadas já passaram.")

def read_contact_from_excel(file_path):
    df = pd.read_excel(file_path)
    # Supondo que as colunas sejam 'Nome' e 'Telefone'
    name = df['Nome'][0]
    phone_number = df['Telefone'][0]
    return name, phone_number

if __name__ == "__main__":
    # Substitua esta string pela data e hora desejadas
    date_time_str = "2025-02-27 12:00:19"
    # Substitua pelo caminho para o seu arquivo Excel
    excel_file_path = "c:\Users\sgt\Documents\Teste 1.xlsx"
    
    name, phone_number = read_contact_from_excel(excel_file_path)
    schedule_message(date_time_str, name, phone_number)

    while True:
        schedule.run_pending()
        time.sleep(1)

    

        
    