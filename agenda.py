import re
agenda = {}

def adicionar_nome():
    print('\nCONTATO')
    print('-' * 30)
    while True:
        nome = input('Digite o nome do contato: ')
        if nome.lower() in (chave.lower() for chave in agenda.keys()):
            print(f'>> Já existe um contato chamado "{nome}" na agenda. Tente novamente.\n')
        else:
            return nome


def adicionar_data_nascimento():
    while True:
        data_nascimento = input('Digite a data de nascimento (DD-MM-AAAA): ').strip()

        if not re.match(r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})$', data_nascimento):
            print('>> Data de nascimento inválida. Digite no formato correto.\n')
        
        else:
            return data_nascimento


def adicionar_endereco():
    print('\nENDEREÇO')
    print('-' * 30)
    rua = input('Digite o nome da rua: ')
    numero = input('Digite o número: ')
    complemento = input('Digite o complemento: ')
    bairro = input('Digite o bairro: ')
    municipio = input('Digite o município: ')
    estado = input('Digite o estado: ')
    
    while True:
        cep = input('Digite o CEP (XXXXX-XXX): ')
        if re.match(r'^\d{5}-\d{3}$', cep):
            break
        print('>> CEP inválido! Digite no formato XXXXX-XXX.\n')

    endereco = {
        'Rua': rua,
        'Número': numero,
        'Complemento': complemento,
        'Bairro': bairro,
        'Município': municipio,
        'Estado': estado,
        'CEP': cep
    }
    
    return endereco
    

def adicionar_telefones():
    print('\nTELEFONES')
    print('-' * 30)
    telefones = []
    while True:
        telefone = input('Digite o telefone (ou 0 para parar): ')
        
        if telefone == '0':
            break
        
        elif not re.match(r'^\d{10,11}$',telefone): 
            print('>> Telefone inválido. Digite no formato correto (10 ou 11 dígitos).\n')
        
        elif any(telefone in contato['Telefones'] for contato in agenda.values()):
            print(f'>> Já existe um com o número "{telefone}" na agenda. Tente novamente.\n')
            
        else: 
            telefones.append(telefone)
        
    return telefones


def adicionar_emails(): 
    print('\nE-MAILS')
    print('-' * 30)
    emails = []
    while True:
        email = input('Digite o e-mail (ou 0 para parar): ').strip()

        if email == '0':
            break
    
        elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            print('>> E-mail inválido. Digite no formato correto.\n')
            continue
    
        elif any(email in contato['Emails'] for contato in agenda.values()):
            print(f'>> Já existe um contato com o e-mail "{email}" na agenda. Tente novamente.\n')
            
        else:
            emails.append(email)
        
    return emails
        

def adicionar_contato():
    nome = adicionar_nome()
    data_nascimento = adicionar_data_nascimento()
    endereco = adicionar_endereco()
    telefones = adicionar_telefones()
    emails = adicionar_emails()

    contato = {
        'Nome': nome,
        'Data_nascimento': data_nascimento,
        'Endereço': endereco,
        'Telefones': telefones,
        'Emails': emails
    }

    agenda[nome] = contato
    print('\n>> CONTATO ADICIONADO COM SUCESSO!!')
