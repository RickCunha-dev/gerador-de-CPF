import streamlit as st
import time
import random


st.markdown("<style> ... </style>", unsafe_allow_html=True)


st.title("Gerador e Validador de CPF")
st.caption("Verifique, corrija ou gere CPFs válidos.")

st.divider()


col1, col2 = st.columns(2, gap="large")

with col1:
    with st.container(border=True):
        st.subheader("Verificar / Corrigir")
        cpf = st.text_input("CPF", placeholder="000.000.000-00")
        if st.button("Verificar", type="primary"):
        # CPF sem ponto e traço
            semTraco_e_Ponto = cpf.replace('.', '').replace('-', '')

            # Pegando os 9 primeiros digitos para realizar a soma
            noveDigitos = semTraco_e_Ponto[0:9]

            # Criando uma lista dos noves digitos para o primeiro Digito:
            listaDigitos = [int(d) for d in noveDigitos]

            # st.write(listaDigitos2)

            # '''
            #     Multiplicar cada valor por uma contagem regressiva de 10 a 2 (para o primeiro)
            #     Multiplicar cada valor por uma contagem regresssiva de 11 a 2 (para o segundo)
            # '''

            # Usando uma expression para ocupar menos espaço na memória.
            contagemRegressiva = range(10, 1, -1)

            # Armazenando os digitos multiplicado em uma tupla
            digitosMultiplicados = []

            # Percorrendo duas listas ao mesmo tempo para realizar o calculo:
            # for digito, contagem in zip(listaDigitos, contagemRegressiva):
            #     multiplicacao = digito * contagem
            #     digitosMultiplicados.append(multiplicacao)

            # Realizando o calculo para o segundo digito

            digitosMultiplicados = [digito * contagem for digito, contagem in zip(listaDigitos, contagemRegressiva)]
            # print(digitosMultiplicados)

            # Somando os digitos após o cálculo
            somaDigMultiplicados = sum(digitosMultiplicados)

            # Multiplicar a soma por 10 para o primeiro digito, 
            multi_a_soma = somaDigMultiplicados * 10


            # Pegando o resto da divisão da soma dos digitos multiplicados por 11
            resto1 = multi_a_soma % 11

            # Verificando se o primeiro digito é maior que nove. Se for, ele será zero.
            primeiroDigito = 0 if resto1 > 9 else resto1

            listaDigitos2 = listaDigitos + [primeiroDigito]
            # Segunda contagem regressiva de 10 a 2 para o segundo digito
            contagemRegressiva2 = range(11, 1, -1)

            # lista dos digitos multiplicadas para a operação do segundo digito
            # for digito2, contagem2 in zip(listaDigitos2, contagemRegressiva2):
            #     multiplicacao2 = digito2 * contagem2
            #     digitosMultiplicados2.append(multiplicacao2)
            # Tentando com list comprehenshion
            digitosMultiplicados2 = [digito2 * contagem2 for digito2, contagem2 in zip(listaDigitos2, contagemRegressiva2)]

            # tentando comprimir toda a lógica de soma com a divisão pelo resto
            resto2 = (sum(digitosMultiplicados2) * 10) % 11
            segundoDigito = 0 if resto2 > 9 else resto2

            # print(f'Primeiro digito: {primeiroDigito}')
            # print(f'Segundo digito: {segundoDigito}')

            time.sleep(1)
            st.info('Verificando...\n')
            time.sleep(1)


            # Corrigindo o CPF com digito incorreto.
            lista_CPF_Completo = list(semTraco_e_Ponto)
            if len(cpf) == 14:
                if int(lista_CPF_Completo[9]) != primeiroDigito or int(lista_CPF_Completo[10]) != segundoDigito:
                    
                    time.sleep(1)
                    st.error('Erro! CPF inválido.\n')
                    time.sleep(1)
                    
                    # st.write('='*30)
                    st.info('Corrigindo...')
                    
                    lista_CPF_Completo[9], lista_CPF_Completo[10] = str(primeiroDigito), str(segundoDigito)
                    CPF_corrigido = ''.join(d for d in lista_CPF_Completo)
                    
                    # CPF_corrigido = '13324854644'
                    #                  012345678910
                    
                    time.sleep(3)
                    # st.write('='*30)

                    st.success(f'\nCPF registrado: {cpf}')
                    
                    st.success(f'CPF corrigido: {CPF_corrigido[:3]}.{CPF_corrigido[3:6]}.{CPF_corrigido[6:9]}-{CPF_corrigido[9:]}')
                    
                    time.sleep(1)
                    st.success('CPF corrigido com sucesso!')
                else:
                    time.sleep(1)
                    st.success('CPF válido!')
            else:
                # Para o CPF estar correto, a string deve conter 11 caracteres (incluindo pontos)
                if len(cpf) == 11 and '.' in cpf:
                    # Caso estiver ok, o programa irá gerar uma lista com os digitos.
                    lista_CPF_9digitos = list(semTraco_e_Ponto) + [str(primeiroDigito), str(segundoDigito)]
                    # Depois, essa lista será convertida em string novamente.
                    cpfGerado = ''.join(d for d in lista_CPF_9digitos)

                    st.warning('Gerando CPF...')
                    time.sleep(1)
                    # Depois a exibição será realizada com pontos e hífen.
                    st.success(f'CPF gerado: {cpfGerado[:3]}.{cpfGerado[3:6]}.{cpfGerado[6:9]}-{cpfGerado[9:]}')
                else:
                    st.markdown('''
                    Para gerar um CPF, por favor, digite 9 digitos `(com ponto (.)`)
                    Ou, digite os 11 digitos para realizar a correção `(com ponto (.) e hífen (-))`
                    ''')
                    st.warning('Execute o programa e tente novamente.')
                

with col2:
    with st.container(border=True):
        st.subheader("Gerar CPF")
        if st.button("Gerar aleatório"):
            # Nessa opção tentarei fazer uma forma mais comprimida da lógica acima.

            noveDigitosAleatorios = [random.randint(0, 9) for _ in range(9)]
            multi10Digitos = [digitoA * geradorA for digitoA, geradorA in zip(noveDigitosAleatorios, range(10, 1, -1))]
            
            restoDigito1 = (sum(multi10Digitos) * 10) % 11
            primeiroDigito = 0 if restoDigito1 > 9 else restoDigito1

            cpfComPrimeiroDig = noveDigitosAleatorios + [primeiroDigito]
            multi10Digitos2 = [digitoB * geradorB for digitoB, geradorB in zip(cpfComPrimeiroDig, range(11, 1, -1))]

            restoDigito2 = (sum(multi10Digitos2) * 10) % 11
            segundoDigito = 0 if restoDigito2 > 9 else restoDigito2

            cpfComDoisDigitos = cpfComPrimeiroDig + [segundoDigito]
            cpfGerado = ''.join(str(d) for d in cpfComDoisDigitos)
            time.sleep(1)
            st.success(f'CPF gerado: {cpfGerado[:3]}.{cpfGerado[3:6]}.{cpfGerado[6:9]}-{cpfGerado[9:]}')


                