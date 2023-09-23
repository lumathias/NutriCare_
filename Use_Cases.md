### Cadastro de usuário  
**Ator:** Nutricionista  
**Fluxo Normal:**  
&nbsp;&nbsp;1 - O usuário informa email  
&nbsp;&nbsp;2 - Usuário informa nome  
&nbsp;&nbsp;3 - Usuário informa senha  
**Extensões:**  
&nbsp;&nbsp;1a - Se usuário informar email já cadastrado, solicitar novo email ou redefinir senha  
&nbsp;&nbsp;3a - Se usuário informar senha incorreta, solicitar novamente a senha ou redefini-la  

### Autenticação  
**Ator:** Nutricionista / Paciente  
**Fluxo Normal:**  
&nbsp;&nbsp;1 - Usuário informa email  
&nbsp;&nbsp;2 - Usuário informa senha  
**Extensões:**  
&nbsp;&nbsp;1a - Se usuário informar email incorreto, informa que email está incorreto e solicita novo login.   
&nbsp;&nbsp;2a - Se usuário informar senha incorreta, solicitar novamente a senha ou redefini-la  

### Cadastro de paciente  
**Ator:** Nutricionista  
**Pré-condição:** usuário estar autenticado.  
**Fluxo Normal:**  
&nbsp;&nbsp;1 - Usuário informa email do paciente  
&nbsp;&nbsp;2 - Gerar senha aleatória.  
&nbsp;&nbsp;3 - Envia informações de login para email do paciente.  
**Extensões:**  
&nbsp;&nbsp;1a - Se e-mail já estiver cadastrado, solicitar outro e-mail.  

### Gerenciamento de pacientes  
**Ator:** Nutricionista  
**Pré-condição:** usuário estar autenticado  
**Fluxo Normal:**  
&nbsp;&nbsp;1 - Selecionar paciente na lista.  
&nbsp;&nbsp;2 - Escolhe próxima ação: adicionar/editar plano, remover paciente, adicionar/editar medidas;  

### Gerenciar Plano alimentar  
**Ator:** Nutricionista  
**Pré-condição:** Usuário estar autenticado e paciente já está cadastrado.  
**Fluxo Normal:**  
&nbsp;&nbsp;1 - Usuário seleciona paciente
&nbsp;&nbsp;2 - Usuário cadastra refeições ao plano alimentar do paciente
&nbsp;&nbsp;3 - Usuário salva e compartilha o plano alimentar do paciente

### Gerenciar alimentos  
**Ator:** Nutricionista  
**Pré-condição:** usuário estar autenticado.  
**Fluxo Normal:**  
&nbsp;&nbsp;1 - Usuário seleciona adicionar ou remover alimento  
&nbsp;&nbsp;2.1 - Usuário adiciona alimento e suas informações nutricionais a lista do aplicativo  
&nbsp;&nbsp;2.2 - Usuário seleciona alimento a ser removido.  
**Extensões:**  
&nbsp;&nbsp;2.1a - Se alimento já estiver cadastrado, informar o usuário.  
&nbsp;&nbsp;2.1b - Se alguma informação nutricional estiver em formato incorreto, informar o erro.  

### Consultar plano  
**Ator:** Paciente  
**Pré-condição:** usuário estar autenticado  
**Fluxo Normal:** Paciente visualiza seu plano alimentar  

### Consultar Dados  
**Ator:** Paciente  
**Pré-condição:** usuário estar autenticado  
**Fluxo Normal:** Paciente visualiza seus dados

### Gerenciar diário alimentar  
**Ator:** Paciente  
**Pré-condição:** usuário estar autenticado  
**Fluxo Normal:**  
&nbsp;&nbsp;1 - Paciente adiciona refeição  
&nbsp;&nbsp;2 - Sistema calcula o consumo de calorias diário
