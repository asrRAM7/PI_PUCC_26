# ESCRITA
# Método de abrir um arquivo txt, váriavel arquivo
# Parâmetros para o open("nomedoarquivo.txt","w(para escrever, subrepõe oque já existe)/a(também faz escrita, porém mantém o txt anterior)") nessa ordem
# encoding="utf-8") para ter acentos no txt   Sempre colocar esse parâmetro
#with open("teste1.txt","w",encoding="utf-8") as arquivo:
#    arquivo.write("\nOlá Mundo!")

# LEITURA
# Deve-se colocar um arquivo já existente no open, pois o read não cria um arquivo!
nome_arquivo=str(input("Digite o nome do arquivo txt: "))

try:
    with open(nome_arquivo,"r",encoding="utf-8") as arquivo:
        conteudo=arquivo.read()
        print(conteudo)
except FileNotFoundError:
    with open(nome_arquivo,"a",encoding="utf-8") as arquivo:
        arquivo.write("Arquivo Criado!")