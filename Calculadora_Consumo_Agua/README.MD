# Calculadora de Consumo de Agua - *Water Consumption Calculator*
## Faça o calculo de seu consumo e confira se esta dentro do consumo adequado - *Calculate your consumption and check if it’s within the proper range* 
### Idealizaçao do projeto - *Project conception*
### Linguagem Utilizada - *Programming language used*: 
![Python](https://img.shields.io/badge/python-%233670A0.svg?style=for-the-badge&logo=python&logoColor=ffdd54)
---
O projeto foi inicalmente idealizado como uma atividade academica, sendo dada instruções referênte as classificações que deveriam ser utilizadas, e os parâmetros que se enquadram para cada classificação.

*The project was initially designed as an academic activity, with instructions given regarding the classifications that should be used, and the parameters that fit each classification.*

A atividade consiste em avaliar nossa capacidade de construção de funcionalidades do código, estrutura GIt, a documentação redigida sobre o código, e a implementação do mesmo dentro do GitHub

*The activity consists of evaluating our ability to build code features, the Git structure, the documentation written about the code, and its implementation within GitHub*

### O que o codigo faz? - *What the code do?*
---
O codigo pega doir *inputs* principais, sendo eles o Tipo de Imovel, e o Consumo de Agua em M³, onde com esses resultados é gerado é gerada um protocolo contendo as informações referêntes a consulta.  É demonstrado a data da consulta; cosnumo mensal em m³; classificação do consumo; a tarifa utilizada e o custo estimado em R$ desse consumo mensal.

*The code takes two main **inputs**, namely the Property Type and the Water Consumption in m³, where, with these results, a protocol is generated containing the information related to the consultation. The date of the consultation is shown; monthly consumption in m³; consumption classification; the tariff used; and the estimated cost in R$ of this monthly consumption.*

As informações seguem consistentes, e atualizadas, tendo como base fontes atuais e seguras de informação como: A distribuidora de agua e esgoto do estado de São Paulo - Tabelas e tarifas disponibilzadas publicamente; métricas pré estabelecidas a respeito da classificação do consumo (Podendo ser alterada conforme necessidade visando melhores parâmetros) e testes praticos da estrutura do código.

*The information remains consistent and updated, based on current and reliable sources of information such as: the water and sewage distributor of the state of São Paulo - publicly available tables and rates; pre-established metrics regarding consumption classification (which may be altered as needed to achieve better parameters); and practical tests of the code structure.*

Além das consultas, o código também exibe no final da sessão um número de protocolo geral e um individual para cada consulta feita, sendo uma opção como ferramenta de busca em caso de implementação deum Banco de Dados para estes registros.

*In addition to the consultations, the code also displays at the end of the session a general protocol number and an individual one for each consultation made, serving as an option as a search tool in case of implementation of a Database for these records.*

### O que foi feito de diferente? - *What was done differently?*
---
Com base nas instruções passadas a respeito da atividade, e com a experiência derivada de outros códigos criados, foram implementadas funções básicas e bem estruturadas para dar continuidade ao código, sendo inicialmente pensadas como funções complementares mas que acabaram se tornando algo cricial no bom funcionamento do mesmo como um todo.

*Based on the instructions provided regarding the activity, and with the experience derived from other codes created, basic and well-structured functions were implemented to continue the code, initially conceived as complementary functions but which ended up becoming something crucial for its overall proper functioning.*

As implementações diferentes foram - *The different implementations were*:

- Adição de um protocolo para a sessão e para cada consulta - *Adding a protocol for the session and for each appointment*;
- Adição de data e hora para as consultas e sessões feitas - *Adding date and time for appointments and sessions made*;
- Uma ampla gama de dados para a definição da tarifa - *A wide range of data for setting the rate*;
- Soma dos valores e consumos (disponibilizados o final da consulta) - *Sum of the values and uses (provided at the end of the consultation)*;
- Historico das sessões realizadas - *History of sessions held*;

**Adição de um protocolo para as sessões e consultas:** A adição de um protocolo foi pensada para futuras implementações como a de um Banco de Dados, onde, com as sessões e consultas sendo protocoladas, podem ser utilizadas como *Primary keys* quando forem encorporadas;

***Addition of a protocol for sessions and queries:*** *The addition of a protocol was designed for future implementations like a Database, where, with sessions and queries being logged, they can be used as **Primary keys** when they are incorporated;*

**Adição de data e hora as consultas e sessões feitas:** A adição de data e hora foi algo conceitual, sendo utilizada como ferramenta de apoio para a filtragem de dados quando necessário, sendo permitido criar um funil de resultados quando implementada a um Banco de Dados;

***Addition of date and time to queries and sessions made:*** *The addition of date and time was something conceptual, being used as a support tool for data filtering when necessary, being allowed to create a funnel of results when implemented to a Database;*

**Definição das Tarifas:** As tarifas foram manualmente colocadas visando a melhor precisão na hora de gerar uma consulta do gasto estimado, sendo possível fazer a alteração conforme necessidade (Tarifas podem variar de acordo com região, estado e condicionais).

***Definition of Rates:*** *The rates were manually set to ensure the best accuracy when generating an estimated cost query, with the possibility of changing them as needed (Rates may vary depending on region, state, and conditions).*

**Soma dos valores e Histórico da sessão:** Após o final da sessão é realizada uma soma do Valor estimado e do Consumo mensal, permetindo um panorâma geral sobre ambos os gastos que podem ser futuramente utilizados para outras consultas. O histórico das sessões permite ter de forma rápida, tudo que foi realizado naquela sessão, sendo uma ferramenta excelente se combinada com o Protocolo (Primary key), e um filtro de Data e Hora aplicados.

***Sum of values and Session History:*** *After the session ends, a sum of the Estimated Value and the Monthly Consumption is made, allowing an overview of both expenses that can be used for future reference. The session history lets you quickly see everything that was done during that session, making it an excellent tool when combined with the Protocol (Primary key) and a Date and Time filter applied.*

### Notas de atualizaçao - *Update notes*
---
Essa versão é a primeira versão do código, não representando o projeto final -
Novas implementação estão a caminho.

*This version represents the first version of the code, not the final project -*

*New implementations are on the way.*

**Aceito feedbacks! - I accept feedback!**

