import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

#
# Foram realizadas exclusões de avaliações dos trabalhos realizados a partir das 
#
#

# Load the Excel file
file_path = 'PI_2024_REV1.xlsx'
excel_data = pd.ExcelFile(file_path)

# Display sheet names to understand the structure of the file
sheet_names = excel_data.sheet_names
# sheet_names

# Load the data from the specific sheet
df = pd.read_excel(file_path, sheet_name='Respostas ao formulário 1')

# Display the first few rows of the dataframe to understand its structure
print(df.head())

# imprimindo os tipos de dados do dataframe
print(df.dtypes)


# Assuming df is your DataFrame and 'Hora e Minutos' is the column with time strings
# Convert 'Hora e Minutos' from string to datetime format
df['Hora e Minutos'] = pd.to_datetime(df['Carimbo de data/hora'], format='%H:%M')

# Convert times to minutes since midnight for easier calculations
df['Minutes'] = df['Hora e Minutos'].dt.hour * 60 + df['Hora e Minutos'].dt.minute

# Calculate bin edges for histogram
min_minutes = df['Minutes'].min()
max_minutes = df['Minutes'].max()
bins = np.linspace(min_minutes, max_minutes, 11)  # 10 bins means 11 edges

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    # Carregando logo da UNISO
    st.image('uniso_logo.png', width=400)
    # Carregando logo grup TI da Uniso
    st.image('logo_ti_uniso.png', width=100)


# Título da página utilizando o streamlit
st.title('Análise Trabalhos Projeto Integrador - Cursos de TI')

# Subtítulo
st.markdown("Projeto Integrador 2024 - Análise de Avaliações")

# Explicando o trabalho
st.write('Esta página apresenta uma análise das avaliações dos trabalhos de Projeto Integrador dos cursos de TI da Uniso.')

st.write('Os trabalhos da disciplina Projeto Integrador foram apresentados em 08JUN2024. Foram realizadas um total de 611 avaliações on-line destes trabalhos das 09h00 às 13h30.')

st.subheader('Análise dos Resultados')
st.write('Para todas as perguntas, a avaliação foi feita em uma escala de 1 a 5, onde 1 é a pior avaliação e 5 é a melhor avaliação.')
# Plot histogram
fig, ax = plt.subplots()

# Plot histogram

ax = plt.hist(df['Minutes'], bins=bins, edgecolor='black')

# Generate xticks
# xticks = np.linspace(min_minutes, max_minutes, 10)  # 10 xticks
xticks = bins[:-1]  # Exclude the last bin edge to align with the start of each bin
xtick_labels = [f"{int(x)//60:02d}:{int(x)%60:02d}" for x in xticks]

# Set xticks and labels
plt.xticks(ticks=xticks, labels=xtick_labels, rotation=45)
plt.xlabel('Hora')
plt.ylabel('QTD de Avaliações')
plt.title('Distribuição das Avaliações por Horário')
plt.tight_layout()

st.pyplot(fig)

# Separando os trabalhos por GRUPO
df_group = df.groupby('GRUPO')['GRUPO'].count()
print(df_group)

# Ordenando os grupos por número de avaliações
df_group = df_group.sort_values(ascending=False)
print(df_group)

# Plotando um gráfico de barras com os 10 grupos com mais avaliações
df_group.head(10).plot(kind='bar', color='blue')
plt.xlabel('Grupo')
plt.ylabel('QTD de Avaliacoes')
plt.title('Grupos com maior número de avaliações')
# estabelecendo o limite do eixo y
plt.ylim(0, 35)
plt.tight_layout()
st.pyplot(fig)

# Calculando a média de avaliações por grupo para a questão Q1
st.write('Q1 - Em um grau de 1 a 5: o quão impactante para a sociedade tal projeto seria? (1 - Nada impactante, 5 - Muito impactante)')
df_mean_q1 = df.groupby('GRUPO')['Q1'].mean()
print(df_mean_q1)

# Ordenando os grupos por média de avaliações
q1_top_10 = df_mean_q1.sort_values(ascending=False)
print(df_mean_q1)

# Plotando um gráfico de barras com os 10 grupos com maior média de avaliações para a questão Q1
q1_top_10 = q1_top_10.head(10)

fig, ax = plt.subplots()

ax = plt.bar(q1_top_10.index, q1_top_10.values, color='green')
plt.xlabel('Grupo')
plt.ylabel('Média de Avaliações')
plt.title('10 Grupos com maior Média de Avaliações - Q1')
plt.xticks(rotation=90)
plt.tight_layout()
st.pyplot(fig)

# Calculando a média de avaliações por grupo para a questão Q2
st.write('Q2 - Em um grau de 1 a 5, o software apresenta acessibilidade? (1 - Não apresenta acessibilidade, 5 - Apresenta total acessibilidade)')
df_mean_q2 = df.groupby('GRUPO')['Q2'].mean()
print(df_mean_q2)

# Ordenando os grupos por média de avaliações
q2_top_10 = df_mean_q2.sort_values(ascending=False).head(10)
print(q2_top_10)

# Plotando um gráfico de barras com os 10 grupos com maior média de avaliações para a questão Q2
fig, ax = plt.subplots()

ax = plt.bar(q2_top_10.index, q2_top_10.values, color='red')
plt.xlabel('Grupo')
plt.ylabel('Média de Avaliações')
plt.title('10 Grupos com maior Média de Avaliações - Q2')
plt.xticks(rotation=90)
plt.tight_layout()
st.pyplot(fig)

# Calculando a média de avaliações por grupo para a questão Q3
st.write('Q3 - Em um grau de 1 a 5: nível de clareza do problema abordado pelo projeto (1 - Pouco claro, 5 - Muito claro)')
df_mean_q3 = df.groupby('GRUPO')['Q3'].mean()
print(df_mean_q3)

# Ordenando os grupos por média de avaliações
q3_top_10 = df_mean_q3.sort_values(ascending=False).head(10)
print(q3_top_10)

# Plotando um gráfico de barras com os 10 grupos com maior média de avaliações para a questão Q3
fig, ax = plt.subplots()

ax = plt.bar(q3_top_10.index, q3_top_10.values, color='purple')
plt.xlabel('Grupo')
plt.ylabel('Média de Avaliações')
plt.title('10 Grupos com maior Média de Avaliações - Q3')
plt.xticks(rotation=90)
plt.tight_layout()
st.pyplot(fig)

# Calculando a média de avaliações por grupo para a questão Q4
st.write('Q4 - Em um grau de 1 a 5. O projeto expõe o problema a ser resolvido pelo projeto? (1 - Não expõe o problema, 5 - Expõe claramente o problema)')
df_mean_q4 = df.groupby('GRUPO')['Q4'].mean()
print(df_mean_q4)

# Ordenando os grupos por média de avaliações
q4_top_10 = df_mean_q4.sort_values(ascending=False).head(10)
print(q4_top_10)

# Plotando um gráfico de barras com os 10 grupos com maior média de avaliações para a questão Q4
fig, ax = plt.subplots()

ax = plt.bar(q4_top_10.index, q4_top_10.values, color='orange')
plt.xlabel('Grupo')
plt.ylabel('Média de Avaliações')
plt.title('10 Grupos com maior Média de Avaliações - Q4')
plt.xticks(rotation=90)
plt.tight_layout()
st.pyplot(fig)

# Calculando a média de avaliações por grupo para a questão Q5
st.write('Q5 - Em um grau de 1 a 5. Qual a qualidade das telas apresentadas no projeto? (1 - Baixa qualidade, 5 - Alta qualidade)')
df_mean_q5 = df.groupby('GRUPO')['Q5'].mean()
print(df_mean_q5)

# Ordenando os grupos por média de avaliações
q5_top_10 = df_mean_q5.sort_values(ascending=False).head(10)
print(q5_top_10)

# Plotando um gráfico de barras com os 10 grupos com maior média de avaliações para a questão Q5
fig, ax = plt.subplots()

ax = plt.bar(q5_top_10.index, q5_top_10.values, color='brown')
plt.xlabel('Grupo')
plt.ylabel('Média de Avaliações')
plt.title('10 Grupos com maior Média de Avaliações - Q5')
plt.xticks(rotation=90)
plt.tight_layout()
st.pyplot(fig)

# Calculando a média de avaliações por grupo para a questão Q6
st.write('Q6 - Em um grau de 1 a 5, qual a qualidade do material exposto (apresentação) do projeto? (1 - Baixa qualidade, 5 - Alta qualidade)')
df_mean_q6 = df.groupby('GRUPO')['Q6'].mean()
print(df_mean_q6)

# Ordenando os grupos por média de avaliações
q6_top_10 = df_mean_q6.sort_values(ascending=False).head(10)
print(q6_top_10)

# Plotando um gráfico de barras com os 10 grupos com maior média de avaliações para a questão Q6
fig, ax = plt.subplots()

ax = plt.bar(q6_top_10.index, q6_top_10.values, color='pink')
plt.xlabel('Grupo')
plt.ylabel('Média de Avaliações')
plt.title('10 Grupos com maior Média de Avaliações - Q6')
plt.xticks(rotation=90)
plt.tight_layout()
st.pyplot(fig)

# Calculando a média de avaliações por grupo para a questão Q7
st.write('Q7- Em um grau de 1 a 5. Qual o conhecimento apresentado do grupo sobre o projeto? (1 - Baixo conhecimento, 5 - Alto conhecimento)')
df_mean_q7 = df.groupby('GRUPO')['Q7'].mean()
print(df_mean_q7)

# Ordenando os grupos por média de avaliações
q7_top_10 = df_mean_q7.sort_values(ascending=False).head(10)
print(q7_top_10)

# Plotando um gráfico de barras com os 10 grupos com maior média de avaliações para a questão Q7
fig, ax = plt.subplots()

ax = plt.bar(q7_top_10.index, q7_top_10.values, color='gray')
plt.xlabel('Grupo')
plt.ylabel('Média de Avaliações')
plt.title('10 Grupos com maior Média de Avaliações - Q7')
plt.xticks(rotation=90)
plt.tight_layout()
st.pyplot(fig)

st.subheader('Análise Personalizada por Grupo')
st.write('Escolha a seguir um grupo específico para visualizar as médias do trabalho para cada uma das questões (Q1 - Q7).')

# Selecionando um grupo específico
# Eliminando valores nulos
df = df.dropna(subset=['GRUPO'])

grupo_selecionado = st.selectbox('Selecione um grupo:', df['GRUPO'].unique())

# Filtrando o dataframe para o grupo selecionado
df_grupo = df[df['GRUPO'] == grupo_selecionado]

# Calculando a média de avaliações para cada questão
media_q1 = df_grupo['Q1'].mean()
media_q2 = df_grupo['Q2'].mean()
media_q3 = df_grupo['Q3'].mean()
media_q4 = df_grupo['Q4'].mean()
media_q5 = df_grupo['Q5'].mean()
media_q6 = df_grupo['Q6'].mean()
media_q7 = df_grupo['Q7'].mean()

# Indicando o número de avaliações para o grupo selecionado
num_avaliacoes = len(df_grupo)

# Exibindo as médias de avaliações para o grupo selecionado
st.write(f'Grupo: {grupo_selecionado}')
st.write(f'Média Q1: {media_q1:.2f} ------- Média Q2: {media_q2:.2f}')
st.write(f'Média Q3: {media_q3:.2f} ------- Média Q4: {media_q4:.2f}')
st.write(f'Média Q5: {media_q5:.2f} ------- Média Q6: {media_q6:.2f}')
st.write(f'Média Q7: {media_q7:.2f} ------- Total de avaliações: {num_avaliacoes}')

# Exibindo um gráfico de barras com as médias de avaliações para o grupo selecionado
fig, ax = plt.subplots()

# Plotando as médias de avaliações
ax = plt.bar(['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7'], [media_q1, media_q2, media_q3, media_q4, media_q5, media_q6, media_q7], color='purple')

plt.xlabel('Questão')
plt.ylabel('Média de Avaliações')
plt.title(f'Médias de Avaliações para o Grupo {grupo_selecionado}')
plt.tight_layout()
st.pyplot(fig)
