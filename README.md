## Gerador de QR Code com Python

Este projeto tem como função, receber um endereço de URL e gerar uma imagem de QR Code que encaminha direto para a página da URL. Sendo útil em rotinas do dia a dia e para fins didáticos.

---

### Como utilizar

Primeiro para usar o cóidigo, primeiro fazer o caminho do github:

- git clone https://github.com/dboravitoria/gerador_QRCode.git
- Abrir o projeto e instalar as bibliotecas necessárias, são elas: 
  ```bash 
    python3 -m pip install "qrcode[pil]"
    python3 -c "import qrcode; print(qrcode.__file__)"
  ```

  (Lembrando que o python3 só é necessário se sua máquina for sistema Linux ou Mac)
- Rodar o comando: ```python3 app.py```

A partir disso você já consegue abrir uma aba que recebe a URL e gera o QR Code, além de gerar uma imagem PNG que vocẽ pode utilizar em sites e posts. Como no exemplo a seguir:

![Visualizar Gerador](img/exemplo.png)