from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.utils import platform
from kivymd.uix.snackbar import Snackbar
from plyer import battery, gps
import socket



class App(MDApp):
    def build(self):
        self.screen = Builder.load_file("main.kv")
        
        return self.screen
    
   

    def abrir_config_localizacao():
        Intent = autoclass('android.content.Intent')
        Settings = autoclass('android.provider.Settings')
        PythonActivity = autoclass('org.kivy.android.PythonActivity')

        intent = Intent(Settings.ACTION_LOCATION_SOURCE_SETTINGS)
        currentActivity = PythonActivity.mActivity
        currentActivity.startActivity(intent)
        

    def enviar(self):
       

        ip_server = self.screen.ids.ip_server.text
        port_server = self.screen.ids.port_server.text
        if ip_server == '' or port_server == '':
            Snackbar(text="O campo IP do servidor ou porta está vazio!").open()
            return
        
        print(ip_server)

        try:
            status = battery.status
            print("Battery status:", status)

            porcentagem = status.get("percentage") if status else None
            self.porcentagem = porcentagem if porcentagem is not None else 0

        except Exception as e:
            print("Erro bateria:", e)
            self.porcentagem = 0

        # localização
        self.localizacao = None

        if platform == 'android':
            from jnius import autoclass
            from android.permissions import request_permissions, Permission

            request_permissions([
            Permission.ACCESS_FINE_LOCATION,
            Permission.ACCESS_COARSE_LOCATION
            ])

            try:
                gps.configure(on_location=self.on_location, on_status=self.on_status)
                gps.start()
            except:
                print("erro gps")
                self.abrir_config_localizacao()
        else:
            print("GPS: Apenas funciona no Android/iOS")

        try:
            self.con = Conect()
            self.con.conectar(ip_server,port_server)
            #self.con.enviar_requisicao(self.porcentagem,"sem gps") 
            Snackbar(text="Enviando Status").open()
            return
        except Exception as e:
            print("Erro conexão:", e)
            Snackbar(
                text="Falha ao conectar.\nVerifique o IP.\nServidor pode estar offline.",
                duration=3 

            ).open()
            return


    def on_location(self, **kwargs):
        lat = kwargs.get('lat', 0)
        lon = kwargs.get('lon', 0)
        if lat is not None and lon is not None:
            self.localizacao = f"{lat},{lon}"
            print("Localização:", self.localizacao)
            self.con.enviar_requisicao(self.porcentagem, self.localizacao)
          
            


    def on_status(self, stype, status):
        print('type={}\nstatus={}\n'.format(stype, status))
       
    


class Conect():

    def conectar(self,ip_server,port_server):
       
        self.HOST = ip_server  # The remote host
        self.PORT = int(port_server)             # The same port as used by the server

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.HOST, self.PORT))


    def enviar_requisicao(self,porcentagemBAT,localizacao):

        mensagem = f"Bateria: {porcentagemBAT} | Localizacao: {localizacao}"
        
        self.s.sendall(mensagem.encode())

        resposta = self.s.recv(1024)
        print("Resposta:", resposta.decode())

        #self.s.close()


if __name__ == "__main__":
    App().run()