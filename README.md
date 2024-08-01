## Análise de probabilidade utilizando Python
Projeto realizado durante o curso ["Intermediate Python"](https://app.datacamp.com/learn/courses/intermediate-python) da plataforma DataCamp, com o objetivo de demonstrar habilidades práticas e o domínio de bibliotecas Matplotlib e Numpy em Python.

## Sobre o projeto
Imagine o seguinte: Você está viajando com um amigo e avista o Burj Khalifa, maior edifício do mundo.
Vocês decidem jogar um jogo utilizando dados e apostar com seu amigo que é possível chegar a 60 degraus de altura jogando um dado cem vezes, sob as seguintes condições:
- Se o resultado do dado for 1 ou 2, você desce um degrau.
- Se o resultado do dado for 3, 4 ou 5, você sobe um degrau.
- Se você tirar um 6, você joga o dado novamente e sobe o número resultante de degraus.
- Claro, você não pode ir abaixo do degrau número 0. 
- Vocês admitem que é um pouco perigoso e tem uma chance de 0,1% de cair da escada quando faz um movimento. Cair significa que você tem que começar novamente do degrau 0.
### Como resolver? Qual é a chance de você ganhar esta aposta? 
Uma abordagem possível é simular esse processo milhares de vezes e ver em qual fração das simulações você atingirá 60 passos.
Será que é possível vencer essa aposta? 
