# seg_projeto_prog2: clusteringRealitiesProject

Repositorio para o codigo do segundo projecto de programacao 2 do 1 ano

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

# Conjunto de testes
Para exercitar os princípios e métodos ensinados em Programação 1 sobre testar e depurar, os estudantes têm de construir o seu próprio conjunto de testes e usá-lo para testar e depurar a resolução que desenvolverem. Os ficheiros com esses testes utilizados tem de ser submetido para classificação juntamente com os demais ficheiros de código desenvolvido pelos estudantes.
De modo diferente do que aconteceu nos projetos anteriores, o conjunto de testes a ser usado pelos docentes na classificação das resoluções deste projeto pelos estudantes não serão por isso divulgados.