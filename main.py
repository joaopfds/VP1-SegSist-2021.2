import cryptocode

def Enviar(mensagem, segredo, chave):

    segredo = mensagem + str(segredo)

    #print(segredo)

    #print(str(hash(segredo)))

    mensagem = mensagem + '@' + str(hash(segredo))
    
    #print(mensagem)

    mensagem = cryptocode.encrypt(mensagem, str(chave))

    #print(mensagem)

    return mensagem


def Receber(mensagemCifrada, segredo, chave):

    mensagemCifrada = cryptocode.decrypt(mensagemCifrada, str(chave))

    #print(mensagemCifrada)

    mensagemCifrada = mensagemCifrada.split('@')

    #print(mensagemCifrada)

    mensagem, hashRecebido = mensagemCifrada

    mensagem = hash(mensagem + str(segredo))

    #print(mensagem, teste)

    if str(mensagem) == str(hashRecebido):
      print('Ok! Menssagem recebida com sucesso.')
    else:
      print('Deu ruim...')

    return mensagemCifrada


mensagem = 'T-e-s-t-e'
chave = 'key'
segredo = 'NaoContoANinguem'

print("Preparando envio...")
mensagemCifrada = Enviar(mensagem, segredo, chave)
print("Mensagem enviada")

mensagemDecifrada = Receber(mensagemCifrada, segredo, chave)

print('A enviou: '+ mensagem + ' || B recebeu: '+ mensagemDecifrada[0])