import re
agenda = {
    'João Silva': {
        'Nome': 'João Silva',
        'Data_nascimento': '15-04-1985',
        'Endereço': {
            'Rua': 'Rua das Flores',
            'Número': '123',
            'Complemento': 'Apto 101',
            'Bairro': 'Centro',
            'Município': 'São Paulo',
            'Estado': 'SP',
            'CEP': '01010-000'
        },
        'Telefones': ['(11) 99999-8888', '(11) 98765-4321'],
        'Emails': ['joao.silva@gmail.com', 'joao.silva@yahoo.com']
    },
    'Maria Oliveira': {
        'Nome': 'Maria Oliveira',
        'Data_nascimento': '25-12-1990',
        'Endereço': {
            'Rua': 'Avenida Brasil',
            'Número': '456',
            'Complemento': 'Casa',
            'Bairro': 'Jardim Paulista',
            'Município': 'São Paulo',
            'Estado': 'SP',
            'CEP': '01311-000'
        },
        'Telefones': ['(11) 98888-7777'],
        'Emails': ['maria.oliveira@gmail.com']
    },
    'Carlos Pereira': {
        'Nome': 'Carlos Pereira',
        'Data_nascimento': '10-06-1978',
        'Endereço': {
            'Rua': 'Rua do Sol',
            'Número': '789',
            'Complemento': 'Bloco B',
            'Bairro': 'Vila Nova',
            'Município': 'Rio de Janeiro',
            'Estado': 'RJ',
            'CEP': '20000-000'
        },
        'Telefones': ['(21) 91234-5678'],
        'Emails': ['carlos.pereira@hotmail.com']
    }
}

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


def consultar_contatos():
    if not agenda:
        print('>> AGENDA VAZIA.')
        return
        
    print(f"{'Nome'.ljust(22)}{'Data de nascimento'.rjust(18)}{'Endereço'.rjust(25)}{'Telefones'.rjust(44)}{'E-mails'.rjust(26)}")
    print('-' * 150)

    for nome, contato in agenda.items():
        endereco_formatado = f"{contato['Endereço']['Rua']}, {contato['Endereço']['Número']} - {contato['Endereço']['Bairro']}, {contato['Endereço']['Estado']}"

        telefones = contato['Telefones']
        emails = contato['Emails']
        max_linhas = max(len(telefones), len(emails), 1)

        print(f"{nome.ljust(25)}{contato['Data_nascimento'].ljust(22)}{endereco_formatado.ljust(50)}", end="")

        for i in range(max_linhas):
            telefone = telefones[i] if i < len(telefones) else ""
            email = emails[i] if i < len(emails) else ""

            if i == 0:
                print(f"{telefone.ljust(25)}{email}")
            else:
                print(f"{' '.ljust(97)}{telefone.ljust(25)}{email}")

        print('-' * 150)


def menu():
    while True:
        print('_' * 150)
        print('\n======== MENU ========')
        print('[1] - Adicionar contato')
        print('[2] - Consultar contato')
        print('[0] - Encerrar programa\n')
        
        opcao = input('ESCOLHA UMA OPÇÃO: ')
        print('_' * 150)
        
        if opcao == '1':
            adicionar_contato()
        elif opcao == '2':
            consultar_contatos()
        elif opcao == '0':
            break
        else:
            print('>> OPÇÃO INVÁLIDA')
            
menu()