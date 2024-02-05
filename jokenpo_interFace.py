import random
import tkinter as tk
from PIL import Image, ImageTk

class JokenpoGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo Jokenpo")
        self.caminhos_imagens = {
            "pedra": 'img/pedra.png',
            "papel": 'img/papel.png',
            "tesoura": 'img/tesoura.png'
        }
        self.imagens = {opcao: ImageTk.PhotoImage(Image.open(caminho)) for opcao, caminho in self.caminhos_imagens.items()}

        self.botao_pedra = tk.Button(self.master, image=self.imagens["pedra"], command=lambda: self.iniciar_jogo("pedra"))
        self.botao_papel = tk.Button(self.master, image=self.imagens["papel"], command=lambda: self.iniciar_jogo("papel"))
        self.botao_tesoura = tk.Button(self.master, image=self.imagens["tesoura"], command=lambda: self.iniciar_jogo("tesoura"))

        self.botao_pedra.pack(side=tk.LEFT, padx=10)
        self.botao_papel.pack(side=tk.LEFT, padx=10)
        self.botao_tesoura.pack(side=tk.LEFT, padx=10)

    def escolher_jogada_computador(self):
        return random.choice(['pedra', 'papel', 'tesoura'])

    def vencedor(self, escolha_usuario, escolha_computador):
        if (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
           (escolha_usuario == "papel" and escolha_computador == "pedra") or \
           (escolha_usuario == "tesoura" and escolha_computador == "papel"):
            return "Você venceu!  (─‿‿─)"
        elif escolha_usuario == escolha_computador:
            return 'Empate!  (◑‿◐)'
        else:
            return 'Você perdeu! (｡•́︿•̀｡)'

    def exibir_resultado(self, escolha_usuario, escolha_computador, resultado):
        resultado_window = tk.Toplevel(self.master)
        resultado_window.title("Resultado")

        imagem_usuario = self.imagens.get(escolha_usuario)
        imagem_computador = self.imagens.get(escolha_computador)

        if imagem_usuario and imagem_computador:
            label_usuario = tk.Label(resultado_window, text="Escolha do Usuário", font=("Helvetica", 14))
            label_usuario.grid(row=0, column=0, padx=10)
            label_computador = tk.Label(resultado_window, text="Escolha do Computador", font=("Helvetica", 14))
            label_computador.grid(row=0, column=1, padx=10)

            label_usuario_imagem = tk.Label(resultado_window, image=imagem_usuario)
            label_usuario_imagem.grid(row=1, column=0, padx=10)
            label_computador_imagem = tk.Label(resultado_window, image=imagem_computador)
            label_computador_imagem.grid(row=1, column=1, padx=10)

            label_resultado = tk.Label(resultado_window, text=resultado, font=("Helvetica", 16, "bold"))
            label_resultado.grid(row=2, columnspan=2, pady=10)

            pergunta_label = tk.Label(resultado_window, text="Quer jogar novamente?", font=("Helvetica", 12))
            pergunta_label.grid(row=3, columnspan=2, pady=10)

            botao_sim = tk.Button(resultado_window, text="Sim", command=lambda: self.reiniciar_jogo(resultado_window),
                                  bg="white", font=("Helvetica", 12))
            botao_sim.grid(row=4, column=0, padx=10)
            botao_nao = tk.Button(resultado_window, text="Não", command=resultado_window.destroy,
                                  bg="white", font=("Helvetica", 12))
            botao_nao.grid(row=4, column=1, padx=10)

    def iniciar_jogo(self, escolha_usuario):
        escolha_computador = self.escolher_jogada_computador()
        resultado = self.vencedor(escolha_usuario, escolha_computador)

        self.exibir_resultado(escolha_usuario, escolha_computador, resultado)

    def reiniciar_jogo(self, resultado_window):
        resultado_window.destroy()
        self.botao_pedra.config(state=tk.NORMAL)
        self.botao_papel.config(state=tk.NORMAL)
        self.botao_tesoura.config(state=tk.NORMAL)

if __name__ == '__main__':
    root = tk.Tk()
    game = JokenpoGame(root)
    root.mainloop()
