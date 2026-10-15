import webbrowser
import os
import sys
import urllib.request
import json
import subprocess
import time
import random
from tkinter import PhotoImage

# chato pra caralho, espero que vale a pena essa merda 
codigo_terminado = "terminal, mp3 downloader"

def baixar_mp3_sem_pip(url_youtube):
    api_url = f"https://co.wuk.sh/api/json"
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"}
    
def carregar_usuario():
    try:
        with open("usuario.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return None
    
def limpar_tela():

    os.system('cls' if os.name == 'nt' else 'clear')

baixado = ""
usu = ""
sus = ""
uni = ""
nota = ""
cor = "normal"
aju = "disable"
sem_ajuda = "ativado"
print("""          _____                   _______                   _____                           _______                   _____          
         /\    \                 /::\    \                 /\    \                         /::\    \                 /\    \         
        /::\    \               /::::\    \               /::\____\                       /::::\    \               /::\    \        
       /::::\    \             /::::::\    \             /:::/    /                      /::::::\    \             /::::\    \       
      /::::::\    \           /::::::::\    \           /:::/   _/___                   /::::::::\    \           /::::::\    \      
     /:::/\:::\    \         /:::/~~\:::\    \         /:::/   /\    \                 /:::/~~\:::\    \         /:::/\:::\    \     
    /:::/  \:::\    \       /:::/    \:::\    \       /:::/   /::\____\               /:::/    \:::\    \       /:::/__\:::\    \    
   /:::/    \:::\    \     /:::/    / \:::\    \     /:::/   /:::/    /              /:::/    / \:::\    \      \:::\   \:::\    \   
  /:::/    / \:::\    \   /:::/____/   \:::\____\   /:::/   /:::/   _/___           /:::/____/   \:::\____\   ___\:::\   \:::\    \  
 /:::/    /   \:::\    \ |:::|    |     |:::|    | /:::/___/:::/   /\    \         |:::|    |     |:::|    | /\   \:::\   \:::\    \ 
/:::/____/     \:::\____\|:::|____|     |:::|    ||:::|   /:::/   /::\____\        |:::|____|     |:::|    |/::\   \:::\   \:::\____|
\:::\    \      \::/    / \:::\    \   /:::/    / |:::|__/:::/   /:::/    /         \:::\    \   /:::/    / \:::\   \:::\   \::/    /
 \:::\    \      \/____/   \:::\    \ /:::/    /   \:::\/:::/   /:::/    /           \:::\    \ /:::/    /   \:::\   \:::\   \/____/ 
  \:::\    \                \:::\    /:::/    /     \::::::/   /:::/    /             \:::\    /:::/    /     \:::\   \:::\    \     
   \:::\    \                \:::\__/:::/    /       \::::/___/:::/    /               \:::\__/:::/    /       \:::\   \:::\____\    
    \:::\    \                \::::::::/    /         \:::\__/:::/    /                 \::::::::/    /         \:::\  /:::/    /    
     \:::\    \                \::::::/    /           \::::::::/    /                   \::::::/    /           \:::\/:::/    /     
      \:::\    \                \::::/    /             \::::::/    /                     \::::/    /             \::::::/    /      
       \:::\____\                \::/____/               \::::/    /                       \::/____/               \::::/    /       
        \::/    /                 ~~                      \::/____/                         ~~                      \::/    /        
         \/____/                                           ~~                                                        \/____/         
                                                                                                                                     """)

print("""
 _________________________________
|  fala parceiro! qual seu nome?  |
|---------------------------------|
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||""")
dados_salvos = carregar_usuario()

if dados_salvos:
    novo_usuario, nova_senha = dados_salvos.split(";")
    print(f"Bem-vindo de volta, {novo_usuario}!")
else:
    while True:
        novo_usuario = input("Crie seu usuário: ")
        nova_senha = input("Crie sua senha: ")
        
        if novo_usuario and nova_senha:
            with open("usuario.txt", "w") as f:
                f.write(f"{novo_usuario};{nova_senha}")
            
            print("Conta criada e salva!")
            break
        else:
            print("Erro: Usuário/Senha não podem ser vazios!")

limpar_tela()
print("""         ____  ______ __  __     __      _______ _   _ _____   ____  
        |  _ \|  ____|  \/  |    \ \    / /_   _| \ | |  __ \ / __ \ 
        | |_) | |__  | \  / |_____\ \  / /  | | |  \| | |  | | |  | |
        |  _ <|  __| | |\/| |______\ \/ /   | | | . ` | |  | | |  | |
        | |_) | |____| |  | |       \  /   _| |_| |\  | |__| | |__| |
        |____/|______|_|  |_|        \/   |_____|_| \_|_____/ \____/ 
                                                              
                                                              """)
print("*OBS: codigo nao estao finalizados completamente, ou seja, nao espere muito!*")
print(f"bem vindo {novo_usuario}")
print(" ")
print("escreva 'ajuda' para poder ver os codigos")

while True:
    if sem_ajuda == "ativado":
        hel = input("oque queres?: ")

    if hel == "ajuda":
        os.system('mode con: cols=120 lines=30')
        limpar_tela()
        print(r""" 
 _______________
/  oque queres? \
\---------------/
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||""")
        print(" ")
        print("""    [que horas?] [vai chover?] [bloco de notas]
              
    [bloco de notas] [salvos] [internet]
              
    [calculadora] [pasta de jogos]
              
    [pasta de jogos] [configurações]
              
    [programar] [desligar]
              """)

    
    if hel == "sayori":
        imagem = PhotoImage(file="surprise.png")

    elif hel == "yuri":
        imagem = PhotoImage(file="OPTIONS.png")

    elif hel == "natsuki":
        imagem = PhotoImage(file="sem nda.png")

    elif hel == "monika":
        imagem = PhotoImage(file="i don't ned hlp.png")

    elif hel == "terminal":
        limpar_tela()
        print(""" /$$$$$$$$                                /$$                     /$$
|__  $$__/                               |__/                    | $$
   | $$  /$$$$$$   /$$$$$$  /$$$$$$/$$$$  /$$ /$$$$$$$   /$$$$$$ | $$
   | $$ /$$__  $$ /$$__  $$| $$_  $$_  $$| $$| $$__  $$ |____  $$| $$
   | $$| $$$$$$$$| $$  \__/| $$ \ $$ \ $$| $$| $$  \ $$  /$$$$$$$| $$
   | $$| $$_____/| $$      | $$ | $$ | $$| $$| $$  | $$ /$$__  $$| $$
   | $$|  $$$$$$$| $$      | $$ | $$ | $$| $$| $$  | $$|  $$$$$$$| $$
   |__/ \_______/|__/      |__/ |__/ |__/|__/|__/  |__/ \_______/|__/
                                                                     
                                                                     
                                                                     """)
        
        print("ola, o codigo do terminal ainda esta em processo, para verem os codigos")
        print("digite help, lembrando que é inspirado no derbiam/ubuntu")
        print("espero que gostem ")
        print(" ")
        while True:
            sus = input("user&mod $: ")

            if sus == "help":
                print("sudo apt install {pacote}")
                print("clear")
                print("echo")
                print("X-----X")
                print("(toys)")
                print("cowsay")


    if sus.startswith("cowsay"):

        palavra = sus[7:] 
        print(f" < {palavra} >")
        print(r"""        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
""")

        

    elif hel == "mp3 downloader":
        limpar_tela()
        url_youtube = input("Cole a URL do vídeo do YouTube: ")
        api_url = "https://co.wuk.sh/api/json"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        data = json.dumps({
        "url": url_youtube,
        "format": "mp3",
        "audioBitrate": "192"
        }).encode('utf-8')
    
        req = urllib.request.Request(api_url, data=data, headers=headers, method='POST')
    
        try:
            print("Buscando o áudio do vídeo...")
            with urllib.request.urlopen(req) as response:
                res_data = json.loads(response.read().decode('utf-8'))
            
                if res_data.get('status') == 'redirect' or res_data.get('status') == 'stream':
                    download_url = res_data.get('url')
                    titulo = res_data.get('text', 'audio_youtube')
                
                    nome_arquivo = "".join([c for c in titulo if c.isalpha() or c.isdigit() or c==' ']).rstrip()
                    nome_arquivo_mp3 = f"{nome_arquivo}.mp3"
                
                    print(f"Baixando: {nome_arquivo_mp3}...")
                    urllib.request.urlretrieve(download_url, nome_arquivo_mp3)
                    print("Download concluído com sucesso!")
                else:
                    print("Não foi possível obter o link de download desta vez.")
                
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    elif hel == "que horas?":
        limpar_tela()
        print(f"Agora são: {time.strftime('%H:%M:%S')}")

    elif hel == "programar":
        
        limpar_tela()
        print(r"""
$$$$$$$\ $$\     $$\ $$$$$$$$\ $$\   $$\  $$$$$$\  $$\   $$\       $$$$$$$\   $$$$$$\   $$$$$$\  $$\      $$\ 
$$  __$$\\$$\   $$  |\__$$  __|$$ |  $$ |$$  __$$\ $$$\  $$ |      $$  __$$\ $$  __$$\ $$  __$$\ $$$\    $$$ |
$$ |  $$ |\$$\ $$  /    $$ |   $$ |  $$ |$$ /  $$ |$$$$\ $$ |      $$ |  $$ |$$ /  $$ |$$ /  $$ |$$$$\  $$$$ |
$$$$$$$  | \$$$$  /     $$ |   $$$$$$$$ |$$ |  $$ |$$ $$\$$ |      $$$$$$$  |$$ |  $$ |$$ |  $$ |$$\$$\$$ $$ |
$$  ____/   \$$  /      $$ |   $$  __$$ |$$ |  $$ |$$ \$$$$ |      $$  __$$< $$ |  $$ |$$ |  $$ |$$ \$$$  $$ |
$$ |         $$ |       $$ |   $$ |  $$ |$$ |  $$ |$$ |\$$$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |\$  /$$ |
$$ |         $$ |       $$ |   $$ |  $$ | $$$$$$  |$$ | \$$ |      $$ |  $$ | $$$$$$  | $$$$$$  |$$ | \_/ $$ |
\__|         \__|       \__|   \__|  \__| \______/ \__|  \__|      \__|  \__| \______/  \______/ \__|     \__|
                                                                                                              
                                                                                                              
                                                                                                              
""")
        linhas = []
        while True:
            linha = input(">>> ")
            if linha == "":
                break
            linhas.append(linha)
        
        codigo = "\n".join(linhas)

        if not codigo:
            print("Nenhum código digitado.")
        else:
            salvar = input("deseja salvar? (s/n): ").lower()
            if salvar == "s":
                while True:
                    nome_arquivo = input("digite o nome do arquivo (sem extensao): ")
                    if nome_arquivo:
                        with open(f"{nome_arquivo}.py", "w") as f:
                            f.write(codigo)
                        break
                    else:
                        print("erro: nome do arquivo nao pode ser vazio!")
            elif salvar == "n":
                print("codigo nao salvo!")
                limpar_tela()
            else:
                print("opcao invalida! codigo nao salvo!")

            limpar_tela()
            try:
                print("--- Executando Código ---")
                exec(codigo)
            except Exception as e:
                print(" ")
                print(f"erro ao executar o codigo: {e}")

    elif hel == "bloco de notas":
        limpar_tela()
        nota = input("O que deseja anotar? ")
        sa = input("deseja salvar? (s/n): ").lower()
        if sa == "s":
            while True:
                nome_bloco = input("digite o nome do arquivo (sem extensao): ")
                if nome_bloco:
                    with open(f"{nome_bloco}.txt", "w") as f:
                        f.write(nota)
                    break
                else:
                    print("erro: nome do arquivo nao pode ser vazio!")

    elif hel == "salvos":
        limpar_tela()
        print(f"codigos salvos: {nome_arquivo}, {nome_arquivo}, {nome_arquivo}")
        print(f"notas salvas: {nome_bloco}, {nome_bloco}, {nome_bloco}")

        if nome_bloco == "":
            nome_bloco = "nenhum"
        
        if nome_arquivo == "":
            nome_arquivo = "nenhum"

        sem_ideia = input("deseja abrir algum? (s/n): ").lower()
        if sem_ideia == "s":
            abrir = input("qual deseja?: ").lower()
            if abrir == nome_arquivo:
                with open(f"{nome_arquivo}.py", "r") as f:
                    print(f.read)
            elif abrir == nome_bloco:
                with open(f"{nome_bloco}.txt", "r") as f:
                    print(f.read())
            else:
                print("arquivo nao encontrado!")

    elif hel == "internet":
        limpar_tela()
        print("Abrindo o navegador...")
        webbrowser.open('https://www.google.com')

    elif hel == "vai chover?":
     limpar_tela()
     os.system('curl wttr.in?0')

    elif hel == "creditos":
        limpar_tela()
        print("by: 01CR4M!")

    elif hel == "desligar":
        limpar_tela()
        os_system = input("Deseja desligar o computador? (s/n): ").lower()
        if os_system == "s":
            os.system("shutdown /s /t 0")

        elif os_system == "n":
            print("Desligamento cancelado.")
            time.sleep(2)
            limpar_tela()

        else:
            print("Opção invalida. Desligamento cancelado.")
            time.sleep()
            limpar_tela()

    elif hel == "pasta de jogos":
        limpar_tela()
        print("jo kem po")

        jogo = input("qual quer?: ")

        if jogo == "jo kem po":
                print(" ")
                print("escolha: pedra, papel ou tesoura")
                jokempo = input("escolha o seu: ")
                
                computador = random.choice(["pedra", "papel", "tesoura"])

                print(f"computador escolheu: {computador}")
                if jokempo == computador:
                    print(" ")
                    print("EMPATE!")
                elif (jokempo == "pedra" and computador == "tesoura") or (jokempo == "papel" and computador == "pedra") or (jokempo == "tesoura" and computador == "papel"):
                    print(" ")
                    print("você ganhou!")
                else:
                    print(" ")
                    print("computador ganhou!")

    elif hel == "configurações":
        limpar_tela()
        def salvar_config(status_aju):
            with open("config.txt", "w") as f:
                f.write(status_aju)

        def carregar_config():
            if os.path.exists("config.txt"):
                with open("config.txt", "r") as f:
                    return f.read()
            return "Ativado"
        print("(escreva o nome do que queira mudar!)")
        print(" ")
        print(f"sem ajuda: {aju}")
        print("apagar usuario")
        print(f"cor do terminal: {cor}")
        print(" ")
        
        mds = input("oque quer?: ")

        if mds == "monika" or mds == "just monika" or mds == "monika!":
            print("MONIKA!:D")

        if mds == "sayori" or mds == "natsuki" or mds == "yuri":
            print("just monika! >:(")

        if mds == "mlp":
            escolha = input("Para qual linguagem? (cpp / js / py): ").lower()
            
            if escolha == "cpp":
                linguagem = "c++"
                prefixo = "cpp_user@cowos> "
                with open("cpp.txt", "w") as f:
                    f.write(escolha)
                print("Ambiente alterado para C++. Use 'cout <<' para simular!")
            elif escolha == "js":
                linguagem = "javascript"
                prefixo = "node_user> "
                with open("js.txt", "w") as f:
                    f.write(escolha)
                print("Ambiente alterado para JavaScript. Use 'console.log'!")

        if mds == "sem ajuda":
            if aju == "Ativado":
                aju = "Desativado"
            else:
                aju = "Ativado"
            salvar_config(aju)
            print(f"Modo sem ajuda agora está: {aju}")
            time.sleep(1)

        elif mds == "apagar usuario":
            confirmar = input("Tem certeza...? (s/n): ").lower()
            if confirmar == "s":
                if os.path.exists("usuario.txt"):
                    os.remove("usuario.txt")
                    print("Conta excluída!")
                    time.sleep(2)
                    exit()
        elif mds == "cor do terminal":
            nova_cor = input("escolha a nova cor (normal, hacker, vermelho, azul): ").lower()
            if nova_cor in ["normal", "hacker", "vermelho", "azul"]:
                cor = nova_cor
                print(f"cor do terminal agora é: {cor}")

                if cor == "hacker":
                    os.system("color 0a")
                    with open("hacker.txt", "w") as f:
                        f.write("hacker")

                elif cor == "vermelho":
                    with open("red.txt", "w") as f:
                        f.write("red")
                    os.system("color 0c")
                elif cor == "azul":
                    with open("blue.txt", "w") as f:
                        f.write("blue")
                    os.system("color 0b")
                elif cor == "normal":
                    os.system("color reset")
                    with open("white.txt", "w") as f:
                        f.write("white")
            else:
                print("cor invalida! ecolha entre: normal, hacker, vermelha ou azul")


    elif hel == "calculadora":
        limpar_tela()
        num1 = int(input("escolha um numero: "))
        num2 = int(input("escolhe outro: "))
        cos = input("somar, diminuir, dividir e multiplicar: ")

        if cos == "somar":
            print(" ")
            print(num1+num2)

        elif cos == "diminuir":
            print(" ")
            print(num1-num2)

        elif cos == "dividir":
            print(" ")
            print(num1/num2)

        elif cos == "multiplicar":
            print(" ")
            print(num1*num2)

