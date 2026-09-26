# Registro de avaliações - *Record of evaluations*
## Faça o registro das avaliações recebidas - *Record the evaluations received.*
### Idealizaçao do projeto - *Project conception*
---
O projeto faz parte do conjunto de projetos academicos que estou realizando durante o curso técnico de Desenvolvimento de Sistemas.

*This project is part of the set of academic projects I am working on during the Systems Development technical course.*

A atividade propões criar um programa em Python capaz de realizar os registros vindos de uma pesquisa de opnião dos usuários para ter os parâmetros de satisfação referênte ao atendimento fornecido pela empresa, inicialmente a atividade propôe avaliar nossa capacidade de desenvolver um programa Python utilizando a estrutura de repetição para coletar e exibir informações, estrutura de decisão para afunilar os registros recebidos e a quantidade de dados suportados pelo programa.

*The activity involves creating a Python program capable of recording data from a user opinion survey to measure satisfaction with the company's customer service. It aims to assess our ability to develop a Python program that uses iteration structures to collect and display information, decision structures to filter the incoming records, and logic to handle the volume of data supported by the program.*

Como já foram feitas outras estruturas de repetições em meus outros projetos academicos, foi feita uma reutilização de conceitos já aplicados anteriormente, demonstrando uma competência no ato de reproduzir conceitos já trabalhos em códigos futuros, mantendo a particuliaridade de cada projeto e uma linha de pensamento central no ato de fazer uma estrutura de código que pode ser reaproveitada, personalizada e expandida.

*Having implemented repetition structures in previous academic projects, I reused concepts applied earlier; this demonstrates competence in reproducing previously utilized concepts in new code, while maintaining the unique nature of each project and a consistent approach to creating code structures that can be reused, customized, and expanded.*

### O que o codigo faz? - *What the code do?*
---
O código utiliza três *inputs* básicos para o funcionamento do código, sendo eles:

*The code relies on three basic **inputs** for its operation:*

- Nome do avaliador - *Evaluator's name*;
- Idade do avaliador - *Evaluator's age*;
- Nota da avaliação - *Evaluation score*.

Após isso, o código realiza a construção de um protocolo único para a sessão, e um protocolo individual para cada avaliação registrada; sendo possível registrar quantas avaliações forem necessárias em uma mesma sessão.  No final, o programa exibe um histórico que acomapanha cada registro feito, e um panorâma geral do que foi realizado na sessão, sendo exibido da seguinte forma:

*Following this, the code constructs a unique protocol for the session and an individual protocol for each recorded assessment; it is possible to record as many assessments as necessary within a single session. Finally, the program displays a history tracking each entry made, along with an overview of the session's activities, presented as follows:*

- Protocolo da sessão - *Session protocol*;
- Total de registros - *Total records*;
- Inicio da sessão - *Session start*;
- Fim da sessão - *End of session*;
- Quantidade de avaliações (Sendo exibida a soma de cada opção individualmente) - *Number of ratings (Showing the sum of each option individually)*;
- Confirmação do encerramento da sessão - *Session closure confirmation*

Além das orientações pedidas, foram adicionadas implementações visando o bom funcionamento do código e uma aplicação do programa em uma situação real onde seriam adicionados Banco de Dados, Front-End, e demais funcionalidades.

*In addition to the requested guidelines, implementations were added to ensure the code's proper functioning, along with an application of the program in a real-world scenario involving the integration of a database, a front-end, and other features.*

**Protocolo - Protocol >** Foi adicionado visando ser utilizado como *Primary key* em um banco de dados, facilitando a busca do registro, sendo ele individual (Registro) ou geral (Sessão) -- *It was added for use as a **primary key** in a database, facilitating record retrieval—whether at the individual level (Record) or the general level (Session).*.

**Data e hora - Date and time >** Foi adicionado visando ser utilizado como uma possibilidade de filtro para navegação dentro do banco de dados, sendo útil para busca ou separação de itens especificos a serem analisados -- *It was added to serve as a filtering option for database navigation, proving useful for searching or isolating specific items for analysis.*.

**Historico dos registros - Record history >** O histórico dos registros sendo demonstrados ainda dentro do programa foi uma implementação bônus visando melhor visualização do funcionamento do código enquanto ainda em periódo de testes, sendo uma ferramente útil enquanto ainda o código esta sendo estruturado e sofrendo implementações, permitindo melhor abertura para correção de códigos e treinamento de debugs -- *Displaying the record history directly within the program was a bonus feature designed to provide better visibility into the code's operation during the testing phase; it serves as a useful tool while the code is still being structured and developed, facilitating code corrections and debugging practice.*.

### Notas de atualizaçao - *Update notes*
---
Essa versão é a primeira versão do código, não representando o projeto final -
Novas implementação estão a caminho.

*This version represents the first version of the code, not the final project -*

*New implementations are on the way.*

**Aceito feedbacks! - I accept feedback!**