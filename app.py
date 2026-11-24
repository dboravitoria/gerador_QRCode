import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import importlib


def gera_qr_code():
    url = website_entry.get()

    if len(url) == 0:
        messagebox.showinfo(
            title="Erro!",
            message="Favor insira uma URL válida"
        )
    else:
        opcao_escolhida = messagebox.askokcancel(
            title=url,
            message=f"O endereço URL é:\n"
                    f"Endereço: {url}\n"
                    f"Pronto para salvar?"
        )
        if opcao_escolhida:
            try:
                qrcode = importlib.import_module("qrcode")
            except ImportError:
                messagebox.showerror(
                    title="Dependência ausente",
                    message="Instale o pacote 'qrcode' executando:\n\npip install qrcode[pil]"
                )
                return

            qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=5
            )
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(
                fill_color='black',
                back_color='white'
            )
            img.save('qrExport.png')
            img = Image.open('qrExport.png')
            img = img.resize((180, 180))
            imagem = ImageTk.PhotoImage(img)
            imagem_label.config(image=imagem)
            imagem_label.image = imagem


janela = tk.Tk()
janela.title("Gerador de QRCODE")
janela.geometry("400x400")

label = tk.Label(janela, text="Digite a URL:", font=("arial", 12))
label.pack(pady=10)

website_entry = tk.Entry(janela, width=40, font=("arial", 11))
website_entry.pack(pady=5)

button = tk.Button(janela, text="Gerar QR CODE", command=gera_qr_code)
button.pack(pady=20)

imagem_label = tk.Label(janela)
imagem_label.pack(pady=10)

janela.mainloop()
