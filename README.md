# Objetivo
Com uma finalidade pedagógica, usando Python 3, neste projeto vai implementar o software clusteringRealities. É um software que permite obter o agrupamento de objetos de acordo com as suas características apresentadas num vetor.
No contexto das atividades da nossa disciplina, uma outra finalidade pedagógica encontra-se no desafio de se desenvolver software a partir de uma especificação muito mais difusa e aberta do que aquelas que foram recebidas como pontos de partida em projetos anteriores pelos alunos da disciplina.
Ainda outra finalidade pedagógica, consiste em os alunos ganharem prática em reutilizarem e adaptarem código pré-existente. Na resolução deste projeto, é obrigatório recorrer a e adaptar o código disponibilizado no manual desta unidade curricular para a tarefa de agrupamento. Resoluções que recorram a outros módulos e/ou respetivas funções para realizarem esta tarefa, como por exemplo, scikit-learn, SciPy, Pyclustering, entre possivelmente outros, recebem zero valores de classificação.# Funcionalidade
O seu programa recebe uma listagem de candidatos. Recebe ainda uma lista de títulos nobiliárquicos e tipos de celebridade e respetivos níveis hierárquicos quantitativos.
O seu programa entrega uma lista de grupos de candidatos e respetivos candidatos exemplares.

# Executar o software
O software é executado através da seguinte instrução na linha de comandos:

```python3 clusteringRealities.py k titles.txt inputFile.txt ```
em que k é o número de grupos a formar, titles.txt é o ficheiro de texto com a listagem das categorias nobiliárquicas/celebridade e sua hierarquia num formato como exemplificado acima, e inputFile.txt é um ficheiro com a listagem dos candidatos num formato exemplificado acima. O resultado é escrito num ficheiro com o nome candidates.txt.

Se no ficheiro de input inputFile.txt forem indicados os centróides iniciais na sua seção Exemplars, deve ser lançada uma exceção apropriada caso o número destes centróides seja diferente do número k indicado na linha de comandos.

# Especificação geral
 - Os grupos de candidatos devem ser formados atendendo ao grau de semelhança entre o nível nobiliárquico e de celebridade dos candidatos de forma a que cada grupo retenha os candidatos mais semelhantes entre si nessa perspetiva.
 - O nível nobiliárquico/celebridade de cada pretendente é caracterizado pelo vetor com os valores numéricos das categorias nobiliárquicas/celebridade dos seus ascendentes.
 - O agrupamento dos candidatos tem de usar a abordagem apresentada nas aulas baseada no manual da disciplina sobre agrupamento.
 - A métrica para a semelhança tem de usar a distância euclidiana apresentada no manual.
 - A seção Exemplars no ficheiro de input pode conter ou a palavra designada void, ou uma sublista dos candidatos, as quais têm de ser considerados como os únicos centróides iniciais.
 - No primeiro caso ,os centróides iniciais devem escolhidos aleatoriamente.

# Entradas do programa
O programa recebe dois ficheiros com uma estrutura interna para arrumação de informação similar à dos seguintes exemplos fragmentários:
candidates.txt
````
#Name and features:
#Name; father's title; mother's; paternal grandfather's; paternal grandmother's; maternal grandfather's; maternal grandmother's #Candidates:
Francisquinha Capuleto; duque; condessa; arquiduque; condessa; visconde; viscondessa
Esmeraldinha Montego; arquiduque; tiktokStar; duque; duquesa; arquiduque; baronesa
Armandinho de Alfama; youtubeInfluencer; tiktokStar; plebeu; plebeia; plebeu; plebeia
...
Stephanie Grimaldi; príncipe; plebeia; príncipe; princesa; plebeu; plebeia
#Exemplars:
...
```
titles.txt
```
#degree; title name masculine; feminine
14; imperador; imperatriz
13; rei; rainha
12; regente; regente
11; príncipe; princesa
10; tiktokStar; tiktokStar
9; arquiduque; arquiduquesa
8; duque; duquesa
7; youtubeInfluencer; youtubeInfluencer
6; conde; condessa
5; visconde; viscondessa
4; barão; baronesa
3; vencedorFestivalRTP; vencedoraFestivalRTP 2; apresentadorFamaShow; apresentadoraFamaShow 1; escudeiro; escudeira
0; plebeu; plebeia
```
# Saída do programa
O programa produz um ficheiro de output com uma estrutura interna similar ao exemplo abaixo, com uma listagem dos grupos de candidatos formados, em que o candidato exemplar i é o centróide do grupo i.

candidates.txt
````
#exemplar 1:
Jane Windsor; duque; princesa; arquiduque; arquiduquesa; conde; viscondessa
#cluster 1:
Francisquinha Capuleto; duque; condessa; arquiduque; condessa; visconde; viscondessa
Lili Lambrusca; apresentadorFamaShow; condessa; arquiduque; condessa; visconde; viscondessa
#exemplar 2:
Esmeraldinha Montego; arquiduque; tiktokStar; duque; duquesa; arquiduque; baronesa
#cluster 2:
...
#exemplar3:
Stephanie Grimaldi; príncipe; plebeia; príncipe; princesa; plebeu; plebeia
...
```

# Conjunto de testes
Para exercitar os princípios e métodos ensinados em Programação 1 sobre testar e depurar, os estudantes têm de construir o seu próprio conjunto de testes e usá-lo para testar e depurar a resolução que desenvolverem. Os ficheiros com esses testes utilizados tem de ser submetido para classificação juntamente com os demais ficheiros de código desenvolvido pelos estudantes.
De modo diferente do que aconteceu nos projetos anteriores, o conjunto de testes a ser usado pelos docentes na classificação das resoluções deste projeto pelos estudantes não serão por isso divulgados.

TODO: Listar e documentar os Testes a efectuar ...