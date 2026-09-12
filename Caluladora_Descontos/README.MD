# Calculadora de descontos - Discount calculator
## Um projeto para aplicação de desconto em compras online - A project for applying discounts on online shopping. 
## Linguagem utilizada - Language used _ Python
### Idealização do projeto - Project conception
---
O projeto foi inicialmente pensado para aplicar descontos a partir do valor total da compra, tendo uma divisão de descontos a partir de preços pré definidos, sendo possível conceber 5, 10 e 15% de desconto.

*The project was initially designed to apply discounts based on the total purchase amount, with a breakdown of discounts based on predefined prices, making it possible to offer 5, 10, and 15% off.*

Com base nisso, podemos defenir uma série de preços como parâmetros e os descontos que serão aplicados quando a compra atingir determinado valor.

*Based on this, we can set a series of prices as parameters and the discounts that will be applied when the purchase reaches a certain amount.*

### O que o código faz? - What the code do?
---
O código pega o *input* referênte ao valor da compra e utilziando uma função, determina a porcentagem de desconto que será aplicada na compra.

*The code takes the **input** related to the purchase amount and, using a function, determines the percentage of discount that will be applied to the purchase*

Os preços foram pré definidos seguindo uma lógica simples no código, utilizando a função *if* combinadas com *Maior que, Menor que & Diferente de.* Onde para cada condição, um desconto será devidamente aplicado, retornano por fim, um texto sobre um panorâma geral da operação realizada.

*The prices were predefined following a simple logic in the code, using the **if** function combined with **Greater than, Less than & Not equal to.** Where for each condition, a discount will be properly applied, finally returning a text about an overall view of the operation carried out.*

A consulta sobre o desconto aplicada poderá ser feita repetidas vezes, onde ao final de cada consulta, tera um *input* para continuar, ou encerrar o código.

*The query about the applied discount can be done repeatedly, where at the end of each query, there will be an **input** to continue or exit the code.*

### O que foi feito de diferente? - What was done differently?
---
Além das variáveis de preços solicitadas na atividade, aloquei mais variaveis de preços, seguindo a mesma linha de pensamento das demais (Sendo aplicado desconto com base no valor da compra).

*Besides the price variables requested in the activity, I allocated more price variables, following the same line of thought as the others (applying a discount based on the purchase amount)*

Ao total, foram alocadas sete variáveis diferentes, sendo possível ganhar um desconto maior ou menor para cada parâmetro de preço determinado.

*In total, seven different variables were allocated, making it possible to get a bigger or smaller discount for each determined price parameter.*

Foram feitos diferentes testes para prevenção de quebra de código, onde com o auxilio do *GitHub Copilot*, foram realizados testes simultâneos de diferentes valores para descobrir os pontos de fragilidade do código, sendo resolvidas manualmente após um levamanto dos principais erros apontados.

*Different tests were done to prevent code breaking, where with the help of **GitHub Copilot**, simultaneous tests of different values were carried out to find the weak points in the code, and they were manually fixed after an assessment of the main errors found.*

Como implementações pessoal, adicionei um historico geral das consultas realizadas após o encerramento da sessão, onde é apresentada:

*As personal implementations, I added a general history of the queries made after the session ended, where it shows:*

- As consultas realizadas individualmente - *The consultations done individually*;
- O número de consultas feitas - *The number of appointments made*;
- A soma total do valor das compras - *The total sum of the purchase amounts*;
- A soma total de descontos aplicados - *The total sum of applied discounts*;
- O valor total das compras com os dencontos aplicados - *The total value of the purchases with the discounts applied*;

Onde, com base nesse histórico, é possível análisar a economia concedida através dos descontos aplicados nas compras realizadas, sendo uma panorâma geral do das aplicações feitas durante as consultas.

*Where, based on this history, it is possible to analyze the savings granted through the discounts applied to the purchases made, offering a general overview of the applications made during the consultations.*

Além do histórico, foram adicionados outras duas informações extras conforme as consultas são realizadas, sendo elas:

*In addition to the history, two other extra pieces of information were added as the queries are made, which are:*

- Data exata onde a consulta foi realizada - *Exact date when the appointment took place*;
- Número de protocolo da consulta - *Consultation protocol number*;

A data permite ter um registro de apoio para localizar a consulta feita, sendo possivel de utiliza-la futuramente como um filtro na hora de buscar registros especícos.

*The date allows you to have a support record to locate the consultation made, making it possible to use it later as a filter when searching for specific records.*

Já o protocolo, foi implementado pensando em ser uma *Primary Key*, no caso de alocar as consultas em um Banco de Dados; elas já serão geradas junto a um número único permitindo melhor localização de uma consulta específica ou até mesmo, exclusão dos dados quando necessário, onde são criados um protocolo para Consulta, e um para a sessão **(Sendo apresentada ao junto ao historico da sessão.)**

*As for the protocol, it was implemented with the idea of being a **Primary Key** in mind, in cases where queries are stored in a database; they are generated with a unique number, allowing better tracking of a specific query or even deletion of the data when necessary, where a protocol is created for the query and one for the session ***(Being presented along with the session history.)***

### Notas de atualização
---
Essa versão é a primeira versão do código, não representando o projeto final -
Novas implementação estão a caminho.

*This version represents the first version of the code, not the final project -*

*New implementations are on the way.*

**Aceito feedbacks! - I accept feedback!**
