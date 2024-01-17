import datetime
from tkinter import messagebox, Tk, simpledialog


def contar_horas_hasta_fecha(hora_objetivo):
    tiempo_actual = datetime.datetime.now()
    diferencia_tiempo = hora_objetivo - tiempo_actual
    minutos_totales = diferencia_tiempo.total_seconds() / 60
    horas = minutos_totales // 60
    minutos = minutos_totales % 60
    return int(horas), int(minutos)


def imprimir_mensaje(horas, minutos):
    root = Tk()
    root.withdraw()  # ocultar la ventana
    if horas < 0:
        messagebox.showinfo("Time left", "El tiempo ya llegó a su objetivo")
    else:
        messagebox.showinfo("Time left", "Solamente " + str(horas) + " horas y " + str(minutos) + " minutos!")
    root.destroy()  # Cierra la ventana


def solicitar_hora_objetivo():
    root = Tk()
    root.withdraw()  # ocultar la ventana
    hora_minuto = simpledialog.askstring("Input", "Ingrese la hora y el minuto (formato 24 horas HH:MM):")
    hora, minuto = map(int, hora_minuto.split(':'))
    root.destroy()  # Cierra la ventana
    return datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day,
                             hora, minuto, 0)


# Solicitar la hora objetivo
hora_objetivo = solicitar_hora_objetivo()
horas_hasta_la_fecha, minutos_hasta_la_fecha = contar_horas_hasta_fecha(hora_objetivo)
imprimir_mensaje(horas_hasta_la_fecha, minutos_hasta_la_fecha)