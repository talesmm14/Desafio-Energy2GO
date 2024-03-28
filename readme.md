# Desafio Energy2GO

Para a posição de Desenvolvedor(a) Python Pleno

O teste permitia o uso livre de qualquer ferramenta para resolver o problema, então utilizei as seguintes: Python, C,
Django, Django Rest Framework, Celery, Docker, Docker Compose.

**Obs: A empresa parece utilizar o Bottle ou uma ferramenta similar. Pelo que eu vi na documentação, parece ser muito
simples.**

```
Criar uma API com um endpoint que inicia uma "transação"
Essa transação pode ser persistida em um banco de dados e ela deverá ter um status.
Após ser criada a transação com o status inicial, ela deverá passar para outra pequena aplicação que usará o MQTT para comunicação.
E essa aplicação com MQTT vai atualizar o status para "sucesso"
```

## Diagrama de Arquitetura da Solução

Utilizei a seguinte arquitetura para resolver o problema.

![diagrama.png](docs%2Fdiagrama.png)

Como podemos ver, após a criação da transação, a mesma imediatamente envia uma mensagem via MQTT
para o tópico `EQUIPMENT/VALIDATION`. Outra aplicação escrita em C recebe a mensagem, a processa e retorna de forma
aleatória se a mesma foi confirmada ou não. Uma tarefa assíncrona que roda ao lado do sistema escuta o tópico
`EQUIPMENT/VALIDATION/RESPONSE` durante todo o tempo de execução da aplicação, e então persiste no banco o novo status
da transação.

## Como rodar o projeto

* As variáveis de ambiente já estão preenchidas no arquivo .env para facilitar. (É claro que o .env não deve ser enviado
para produção, mas foi incluído para facilitar os testes.)
* Você precisa ter o Docker instalado na sua máquina. Com ele, você pode executar o projeto usando o comando
`docker-compose up`.

## Passo a Passo

### Entrando na [documentação swagger](http://localhost:8000/swagger/) podemos ver os seguintes endpoints.

![img.png](docs%2Fimg.png)

### Vamos criar uma estação, a mesma servira para o endpoint seguinte de transação.

![img_1.png](docs%2Fimg_1.png)

### Vamos ter o retorno com o id da estação.

![img_2.png](docs%2Fimg_2.png)

### Com esse id podemos criar uma transação para essa estação de baterias.

![img_3.png](docs%2Fimg_3.png)

### Vamos receber o id da transação.

![img_4.png](docs%2Fimg_4.png)

### Pesquisando essa transação.

![img_5.png](docs%2Fimg_5.png)

### Já podemos notar que seu status foi alterado de PENDING para COMPLETED.

![img_6.png](docs%2Fimg_6.png)

### A transação e sempre salva como PENDING no banco.

![img_7.png](docs%2Fimg_7.png)

### Após salva, um signal e chamado para realizar a ação de enviar via MQTT a transação.

![img_8.png](docs%2Fimg_8.png)

# Contato

<a href="https://www.linkedin.com/in/talesmelquiades/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></img></a>

```
talesmelquiades@hotmail.com
```