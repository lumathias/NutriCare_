#  Casos de Uso

### Cadastrar usuário  
**Ator:** Nutricionista  
**Fluxo Normal:**  
&nbsp;&nbsp;&nbsp;1 - Usuário informa um email  
&nbsp;&nbsp;&nbsp;2 - Usuário informa o nome  
&nbsp;&nbsp;&nbsp;3 - Usuário informa uma senha  
**Extensões:**  
&nbsp;&nbsp;&nbsp;1a - Se usuário informar email já cadastrado, solicitar novo email ou redefinir senha    

### Autenticar usuário 
**Ator:** Nutricionista / Paciente  
**Fluxo Normal:**  
&nbsp;&nbsp;&nbsp;1 - Usuário informa email  
&nbsp;&nbsp;&nbsp;2 - Usuário informa senha  
**Extensões:**  
&nbsp;&nbsp;&nbsp;1a - Se usuário informar email incorreto, informa que email está incorreto e solicita novo login.   
&nbsp;&nbsp;&nbsp;2a - Se usuário informar senha incorreta, solicitar novamente a senha ou redefini-la  

### Cadastrar paciente  
**Ator:** Nutricionista  
**Pré-condição:** usuário estar autenticado.  
**Fluxo Normal:**  
&nbsp;&nbsp;&nbsp;1 - Usuário informa email do paciente  
&nbsp;&nbsp;&nbsp;2 - Gerar senha aleatória.  
&nbsp;&nbsp;&nbsp;3 - Envia informações de login para email do paciente.  
**Extensões:**  
&nbsp;&nbsp;&nbsp;1a - Se e-mail já estiver cadastrado, solicitar outro e-mail.  

### Gerenciar pacientes  
**Ator:** Nutricionista  
**Pré-condição:** usuário estar autenticado  
**Fluxo Normal:**  
&nbsp;&nbsp;&nbsp;1 - Selecionar paciente na lista.  
&nbsp;&nbsp;&nbsp;2 - Escolhe próxima ação: adicionar/editar plano, remover paciente, adicionar/editar medidas;  

### Gerenciar Plano alimentar  
**Ator:** Nutricionista  
**Pré-condição:** Usuário estar autenticado e paciente já está cadastrado.  
**Fluxo Normal:**  
&nbsp;&nbsp;&nbsp;1 - Usuário seleciona paciente  <br>
&nbsp;&nbsp;&nbsp;2 - Usuário cadastra refeições ao plano alimentar do paciente de acordo com o seu perfil <br>
&nbsp;&nbsp;&nbsp;3 - Usuário salva e compartilha o plano alimentar do paciente  <br>

### Gerenciar alimentos  
**Ator:** Nutricionista  
**Pré-condição:** usuário estar autenticado.  
**Fluxo Normal:**  
&nbsp;&nbsp;&nbsp;1 - Usuário seleciona adicionar ou remover alimento    
&nbsp;&nbsp;&nbsp;2.1 - Usuário adiciona alimento e suas informações nutricionais a lista do aplicativo    
&nbsp;&nbsp;&nbsp;2.2 - Usuário seleciona alimento a ser removido.   
**Extensões:**   
&nbsp;&nbsp;&nbsp;2.1a - Se alimento já estiver cadastrado, informar o usuário.  
&nbsp;&nbsp;&nbsp;2.1b - Se alguma informação nutricional estiver em formato incorreto, informar o erro.   

### Consultar plano  
**Ator:** Paciente  
**Pré-condição:** usuário estar autenticado   
**Fluxo Normal:**   
&nbsp;&nbsp;&nbsp;1 - Paciente visualiza seu plano alimentar  <br>
&nbsp;&nbsp;&nbsp;2 - Paciente visualiza refeição  <br>
**Extensões:**  
&nbsp;&nbsp;&nbsp;1a - Se plano não estiver cadastrado, informar que o plano está vazio  <br>
&nbsp;&nbsp;&nbsp;2a - Se refeição não estiver cadastrada, informar que a refeição está vazia  <br>

### Consultar Dados   
**Ator:** Paciente   
**Pré-condição:** usuário estar autenticado   
**Fluxo Normal:**   
&nbsp;&nbsp;&nbsp;1 - Paciente seleciona dados a visualizar (medidas, calorias consumidas, IMC e percentual de gordura)   
**Extensões:**   
&nbsp;&nbsp;&nbsp;1a - Se dados não estiverem cadastrados, informar que dados estão vazios    

### Registar refeição  
**Ator:** Paciente  
**Pré-condição:** usuário estar autenticado  
**Fluxo Normal:**  
&nbsp;&nbsp;&nbsp;1 - Paciente adiciona refeição  
&nbsp;&nbsp;&nbsp;2 - Sistema calcula o consumo de calorias diário   
**Extensões:**  
&nbsp;&nbsp;&nbsp;1a - Se refeição já cadastrada, informar ao usuário
