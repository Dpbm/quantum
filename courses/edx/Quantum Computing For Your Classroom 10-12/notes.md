# Quantum Computing For Your Classroom 10-12
* Na computacao classica, para dizer um estado de dois bits, você só precisa dizer qual estado esta o primeiro e o segundo bit(duas informações). Já na computação quântica, você precisa de 4 informações, as quais descrevem a probabilidade de cada estado
* A computação quântica, não substitui a computação clássica, ela é boa para algumas coisas, principalmente quando podemos usar das caracteristicas quanticas para adicionar algum tipo de paralelismo
* Provavelmente, uma operação qualquer em um computador quântico, é muito mais lento que um computador clássico
* P problems --> problemas que podem ser resolvidos em um tempo polinomial, por exemplo O(n) = n^2
* NP problems --> problemas dificeis de resolver por terem um tempo não polinomial, por exemplo O(n) = 2^n
* para saber o O de algum algoritmo, basta somar os O de cada linha/bloco, tirando termos menores e pegando apenas o maior (lembrando que constantes não importam)
* particulas, tem uma certa chance de teleportar, atravessando barreiras, isso pode causar erros 
* a superposicao pode ajudar em calculos, uma vez que com ela, a gente pode testar diferentes resultados ao mesmo tempo, e aumentar a amplitude do resultado correto
* um qubit pode ser presentado como um esfera que possui uma flecha no meio que aponta para um direcao (bloch sphere), representando o estado qubit
* A vantagem do qubit, é que ele não possui apenas dois estados (0 e 1), mas tudo entre isso, podemos utilizar diversas operações para manipular esses estados para alcançar nosso objetivo
* Outra questão que o qubit possui é a superposição. Enquanto não medimos seu estado, ele está em uma superposição de probabilidades para cada estado possível
* Além disso, o entanglement, ajuda a computação quântica a conseguir uma vantagem a mais sobre a computação clássica. O entanglement, faz com que 2 qubits se relacionem, de forma que ao medir um você já recebe o resultado do outro,  dessa forma, temos uma velocidade maior nos calculos
* Por fim, outro fator chave é a Intereferencia. Os qubits e seus estados podem agir como ondas. A partir dai, podemos utilizar delas para criarmos interferencias construtivas (aumentar as amplitudes) para os estados que queremos, e interferencias destrutivas para aqueles que não queremos, aumentando a probabilidade de termos o resultado correto
* Poderiamos medir nosso qubit usando um polarizador, enquanto ele não passar, o qubit está em superposição
* Poderiamos tambem passar eletrons por um campo magnetico, iriamos ver que os eletrons nunca ficam no meio, apenas em cima ou em baixo devido ao seu spin
[Stern–Gerlach experiment](https://upload.wikimedia.org/wikipedia/commons/transcoded/9/9e/Quantum_spin_and_the_Stern-Gerlach_experiment.ogv/Quantum_spin_and_the_Stern-Gerlach_experiment.ogv.480p.vp9.webm)
* Em quantum computers feitos de supercondutores, poderiamos injetar atomos de fosforo, e atraves da ressonancia dos eletrons estimulados por um microondas, poderiamos fazer o spin dele virar para up ou down, ou se quisermos uma superposicao, podemos parar durante esse meio tempo em que ele esta sendo estimulado para criar uma superposição. Com isso, deixamos esse atomo proximo a um transistor, e para medir qual estado ele esta,  basta você ver se o transistor que esse atomo de fosforo esta deixou ou nao a corrente passar, se deixou foi o spin up (1) se não foi down
* Outra maneira de criar um qubit é usando o núcleo do fosforo, contudo é necessário uma onda muito maior e um pulso muito mais longo, por ser um estado muito mais fraco, mas por outro lado, esse estado dura por muito mais tempo. Para saber qual estado o nucleo esta, podemos usar os eletrons, dessa vez jogando aqueles mesmos pulsos q fariam ele virar spin up, se na medicao ele não apresentar resultados, é porque o núcleo está com o spin down, se não ele está com spin up. Isso acontece pois o nucleo também cria um campo que interfere nos eletrons.
* quando a luz não está polarizada, ela aparenta se movimentar em n axis diferentes
* regiões da interferencia onde se a diferente entre as ondas for um multiplo do comprimento de onda será construtivo($s= m \lambda$) caso o comprimento de onda for um multiplo mais metade do comprimento de onda, será destrutivo ($s= (m+\frac{\lambda}{2})$)
* um unico foton, tabém cria padrões no experimento da dupla fenda. 
* se durante o experimento de fenda dupla, observarmos as particulas depois delas passarem pelas fendas e chegarem ao anteparo, o padrão não se formará, pois estaremos interagindo com elas
