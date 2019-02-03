# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

#Utilizado um loop for para realizar um iteração na lista a partir da 2ª linha da lista até a 20ª. Logo depois foi solicitado a impressao dessa iteração.
for i in range(1,21):
    print(data_list[i])

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

#Utilizado um loop for na lista pegando os 20 primeiros gêneros
for sample in data_list[0:20]:
    print(sample[6])

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem

def column_to_list(data, index):
    """
    Função que cria uma lista a partir de colunas de uma lista dada (na mesma ordem).
      Argumentos:
          data: lista (data_list).
          index: índice da coluna da lista.
      Retorna:
          Uma nova lista somente com a coluna desejada.
    """
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
	#Utilizado um loop for para iterar sobre a lista data_list, onde pega as colunas dessa lista e transforma em uma nova lista, o usuário ao chamar a função deve informar a lista e a coluna da lista onde deve iterar.
    for sample in data:
        column_list.append(sample[index])
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.

#Através de um loop for realizado na coluna de gênero conta quantos são do sexo masculino e quantos do sexo feminino.
#Utiliza a coluna -2 (ou 6) do arquivo lista
#Imprimi na tela a quantidade de registros encontrados na coluna para ocorrencias do gênero masculina e feminino.
#Observação: foi criado uma variável empty, pois na lista há casos em que o gênero está nulo.
male = 0
female = 0
empty = 0
for gender in column_to_list(data_list, -2):
    if gender == "Male":
        male += 1
    elif gender == "Female":
        female += 1
    else:
        empty += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)

def count_gender(data_list):
    """
    Função que conta os gêneros.
      Argumentos:
          data_list: A partir da coluna de gênero (-2 ou 6) conta a ocorrência de cada um.
      Retorna:
          Um lista com os valores de cada gênero [masculino, feminino].
    """
    male = 0
    female = 0
    for gender in data_list:
        if gender[-2] == "Male":
            male += 1
        elif gender[-2] == "Female":
            female += 1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.

def most_popular_gender(data_list):
    """
    Função que mostra o gênero mais popular.
      Argumentos:
          data_list: utiliza do resultado da função count_gender() para realizar um comparação entre as duas ocorrências.
      Retorna:
          Retorno o gênero predominante ou se ambos forem iguais retorna Igual
    """
    answer = ""
    popular = count_gender(data_list)
    if popular[0] > popular[1]:
        answer = "Masculino"
    elif popular[0] < popular[1]:
        answer = "Feminino"
    else:
        answer = "Igual"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

#user_set utilizado somente para ver quais são os tipo de usuário [Customer, Subscriber, Dependent].
user_set = list(set(column_to_list(data_list, 5)))

def count_user(data_list):
    """
    Função que conta os tipos de usuário.
      Argumentos:
          data_list: A partir da coluna de tipos de usuários (-3 ou 5) conta a ocorrência de cada um.
      Retorna:
          Um lista com os valores de cada tipo de usuário [Customer, Subscriber, Dependent].
    """
    Customer = 0
    Subscriber = 0
    Dependent = 0
    for user in data_list:
        if user[-3] == "Customer":
            Customer += 1
        elif user[-3] == "Subscriber":
            Subscriber += 1
        elif user[-3] == "Dependent":
            Dependent += 1
    return [Customer, Subscriber, Dependent]

#Com o auxilio da função count_user monta um gráfico quantitativo.
#Imprimi na tela um gráfico quantitativo dos tipos de usuários.
user_list = column_to_list(data_list, -3)
types = ["Customer", "Subscriber", "Dependent"]
quantity = count_user(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Usuário')
plt.show(block=True)


input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão

#Com o auxilio da função count_gender() ajuda a responder a questão.
#Imprimi na tela o porque o tamanho dos dados da coluna de gêneros da data_list não é igual a soma da ocorrências do gênero masculino e feminino.
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Pois na coluna de gêneros existe {} campos em vazio.".format(empty)
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().

#Faz uma análise estatística básico da duração das viagens.
#Utilizando o coluna de duração da viagens (coluna 2)
#Imprimi na tela a viagem Mínima, Máxima, Média, e Mediana.
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

#Como não podemos utiliza 'float(trip_duration_list)', pois tal função só pode ser aplicada direto em uma string ou número, temos que converter cada elemento da lista para uma variável float.
#Utilizada a função for para iterar na coluna 0 da trip_duration_list, transformando os dados em float e logo em seguida ordenando os dados em ordem crescente e  "jogando" esses dados em uma lista
trip_duration = sorted([float(i) for i in trip_duration_list])

#Fazendo a soma dos elementos
soma = 0.
for trip in trip_duration:
    soma += trip
    
#Encontrando a duração mínima e máxima (para isso ordenaremos a lista do menor para o maior)
min_trip = trip_duration[0]
max_trip = trip_duration[-1]

#Encontrando a Média 
mean_trip = soma / len(trip_duration)

#Encontrando a médiana
median_trip = int(trip_duration[len(trip_duration) // 2])

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()


#Pega a coluna start_stations (coluna 3 da data_list) transforma em um conjunto (utilizando a função set(), pois não coloca repetições no conjunto) e mostra a quantidade de ocorrências e as ocorrências.
#Utilizando a coluna start_stations (coluna 3 da data_list)
#Imprimi na tela a quantidade de ocorrências e as estações.
#Observação: como já tinha sido dado a variável user_types para as estações, não quis alterar, porém um nome mais apropriado para essa variável seria start_stations, pois user_types sugere uma variável de tipo de usuários
user_types = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

"""

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "no"

def count_items(column_list):
    """Função que conta tipos de usuários, sem definir os tipos, podendo ser utilizado com outra categoria de dados.
    Argumentos:
        column_list: lista com as categorias de dados
    Retorna:
        Os tipos da categoria selecionada e a quantidade de ocorrências da categoria
    """
    item_types = []
    count_items = []
    for i in set(column_list):
        item_types.append(i)
        count_items.append(column_list.count(i))
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------