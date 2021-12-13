## Scripts para interação com as API's da Senior X Platform
### Remover usuários
Escripts para exclusão de usuários.
- `-burl` ou  `--baseurl`: Url base da API
- `-tk` ou `--token`: Token de autorização
- `-sz` ou `--size`: Quantidade de registros que deseja exluir, valor padrão `1000`
- `-blocked`: Incluir usuários bloqueados, valor padrão `True`
- `-ssl`: Habilitar ssl, valor padrão `False`

`python remove_users.py -burl api.senior.com.br -tk c84da3dbxxxxxxxxx -sz 100 -blocked True`
