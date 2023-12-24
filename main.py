# importar o App, Builder (GUI)
# # criar o nosso aplicativo
# # criar a função build

from kivy.app import App
from kivy.lang import Builder #conect tela com python
import requests



GUI = Builder.load_file("main.kv")

class MeuAplicativo(App):
    def build(self):
        return GUI
        #return Builder.load_string(KV)

#Obs. (self) quer dizer que eu quero usar oque está DENTRO do meu app

# aqui dentro somente oque deve acontecer TODA vez que o app abrir!
    def on_start(self):
        self.root.ids["moeda1"].text = f"Dólar R${self.pegar_cotacao('USD')}"
        self.root.ids["moeda2"].text = f"Euro R${self.pegar_cotacao('EUR')}"
        self.root.ids["moeda3"].text = f"Bitcoin R${self.pegar_cotacao('BTC')}"
        self.root.ids["moeda4"].text = f"Ethereum R${self.pegar_cotacao('ETH')}"

#função que chama api e recebe o código pra poder buscar a moeda que eu quero;
    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao


MeuAplicativo().run()