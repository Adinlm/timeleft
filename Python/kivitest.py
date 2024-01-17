import datetime
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


def contar_horas_hasta_fecha(hora_objetivo):
    tiempo_actual = datetime.datetime.now()
    diferencia_tiempo = hora_objetivo - tiempo_actual
    minutos_totales = diferencia_tiempo.total_seconds() / 60
    horas = minutos_totales // 60
    minutos = minutos_totales % 60
    return int(horas), int(minutos)


class MyApp(App):
    def build(self):
        self.hora_minuto = TextInput(hint_text='Ingrese la hora y el minuto (formato 24 horas HH:MM):')
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(self.hora_minuto)
        self.layout.add_widget(Label(text='Presione enter después de ingresar la hora'))
        self.hora_minuto.bind(on_text_validate=self.on_enter)
        return self.layout

    def on_enter(self, instance):
        hora, minuto = map(int, self.hora_minuto.text.split(':'))
        hora_objetivo = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, hora, minuto, 0)
        horas_hasta_la_fecha, minutos_hasta_la_fecha = contar_horas_hasta_fecha(hora_objetivo)
        self.imprimir_mensaje(horas_hasta_la_fecha, minutos_hasta_la_fecha)

    def imprimir_mensaje(self, horas, minutos):
        if horas < 0:
            popup = Popup(title='Time left', content=Label(text='El tiempo ya llegó a su objetivo'), size_hint=(None, None), size=(400, 400))
        else:
            popup = Popup(title='Time left', content=Label(text='Solamente ' + str(horas) + ' horas y ' + str(minutos) + ' minutos!'), size_hint=(None, None), size=(400, 400))
        popup.open()


if __name__ == '__main__':
    MyApp().run()