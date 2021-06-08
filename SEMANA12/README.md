# [Proteger servidores linux contra hackers](https://youtu.be/fKuqYQdqRIs)

### Desaativando login de senha SSH
Essa pratica não deixa seu sistema seguro, o uso de login por chaves não torna seu servidor mais seguro, é apenas mais conveniente.

### Desativando Login SSH de Raiz Direta
Desativar o acesso root  nao garante segurança, uma vez que, o comando sudo eleva o nivel de privilegio. Mesmo que é necessário inserir a senha, um simples alias pode ser usado para rodar um
programa sem q o usuario perceba.


### Alterando a porta SSH padrão

Não é um metodo eficaz, no minimo atrasará a invasão do hacker. Utilizar senhas unicas e chaves de login é mais eficiente.

### Desativando IPv6 para SSH
Apesar de diminui os canais de contato com o servidor, não é uma estrategia muito eficaz contra invasores.

### Configurando um Firewall Básico

O uso de bloqueio de portas ajuda na segurança do seu servidor, escutando naquela porta apenas o ip desejado, contudo não deixará seu sistema seguro.


### Atualização automática de servidor autônomo

Devido a possiveis erros vindos junto com as atualização, é recomendado que a atualização nao seja automatica e que seja feita manualmente apenas quando for uma atualização de segurança
evitando alguns problemas.


#[Entendendo Conceitos Básicos de CRIPTOGRAFIA](https://youtu.be/CcU5Kc_FN_4)

O melhor metodo para armazernar senhas é o uso da criptografia unidirecional, onde o embarcado salva apenas o codigo digerido e quando a senha é inserida é feito o hash novamente e comparada.
Nunca guardar as senhas em modo texto ou encriptadas, apenas no modo hash.

 Como a criptografia simetrica funciona?
 
INSERE CHAVE, INSERE MENSAGEM
PASSA POR FUNÇÃO
É GERADO A CIPHER (MENSAGEM CRIPTOGRAFADA)

INSERE CHAVE, INSERE CIPHER
PASSA POR FUNÇÃO 
É DEVOLVIDO A MENSAGEM ORIGINAL



a criptografia é possivel recuperar a mensagem original, o hash nao  pode ser recuperado.


