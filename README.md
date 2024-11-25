Bike Sharing Demand

Este código apresenta uma aplicação interativa desenvolvida com Streamlit para análise de dados relacionados à demanda de compartilhamento de bicicletas, utilizando o conjunto de dados Bike Sharing Demand. A aplicação combina técnicas de visualização com bibliotecas como Plotly Express e Plotly Graph Objects para explorar e entender padrões nos dados. A análise é organizada em várias seções interativas, permitindo ao usuário visualizar diferentes aspectos da demanda, como sazonalidade, condições climáticas, períodos do dia e comparações entre tipos de usuários.

A seguir, são descritas as principais análises realizadas pelo sistema:
1.	Estatísticas Descritivas:
•	A aplicação exibe estatísticas básicas do conjunto de dados, como médias, desvios padrão e outras métricas descritivas, para oferecer um panorama inicial dos registros.
2.	Análise Mensal:
•	Um gráfico de barras interativo apresenta os registros mensais de locação, juntamente com uma linha de tendência para ilustrar o crescimento ou a sazonalidade da demanda.
3.	Comparação de Dias Úteis vs Feriados:
•	Um gráfico de pizza destaca a proporção de locações realizadas em dias úteis comparadas a feriados, ajudando a compreender o impacto do calendário na demanda.
4.	Comparação de Usuários Casuais vs Registrados:
•	Outro gráfico de pizza analisa a distribuição entre usuários ocasionais (casuais) e os que possuem registro, permitindo identificar a importância de cada grupo para o sistema.
5.	Impacto das Condições Climáticas:
•	Um gráfico de barras mostra a relação entre condições climáticas (como chuva, sol ou neve) e a quantidade de locações, oferecendo insights sobre como o clima influencia o comportamento dos usuários.
6.	Análise Horária:
•	Uma série de gráficos interativos analisa o padrão de locações por hora do dia, categorizando os registros por diferentes fatores, como dia da semana, feriado, estação do ano e condições climáticas. Essa análise ajuda a identificar os horários de maior demanda.
7.	Correlação entre Variáveis:
•	Um mapa de calor das correlações entre variáveis numéricas do conjunto de dados é gerado para identificar relações estatísticas importantes, como a influência da temperatura ou da umidade na quantidade de locações.
Objetivo da Aplicação
O principal objetivo desta aplicação é fornecer uma plataforma interativa para analisar e visualizar os padrões da demanda de compartilhamento de bicicletas. Ao combinar visualizações claras e estatísticas detalhadas, a aplicação ajuda a responder perguntas importantes, como:
•	Quais períodos do dia têm maior ou menor demanda?
•	Como as condições climáticas ou a sazonalidade afetam o uso do sistema?
•	Qual é a proporção de usuários ocasionais versus registrados?
Tecnologias Utilizadas
•	Streamlit: Framework para criar aplicações web interativas e rápidas para análise de dados.
•	Pandas: Biblioteca para manipulação e análise de dados.
•	Plotly: Ferramenta para criação de visualizações interativas, incluindo gráficos de barras, linhas, pizzas e mapas de calor.
•	NumPy: Usada para manipulação de matrizes e cálculos numéricos.