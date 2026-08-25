# Privacidade e dados

## Princípio

A aplicação foi desenhada para trabalhar com dados de locação sem transformar a vitrine pública em repositório de informações pessoais.

## Minimização

Quando possível, a modelagem reduz o volume de dados pessoais armazenados. Um exemplo técnico é o uso apenas dos últimos dígitos do CPF quando o documento completo não é necessário para a regra de negócio.

## Dados que não pertencem à vitrine

Este repositório não deve conter:

- nomes de locatários reais;
- CPF, telefone ou e-mail reais;
- endereços residenciais reais;
- contratos assinados;
- recibos reais;
- QR Codes de pagamento reais;
- identificadores de transação;
- comprovantes;
- logs com IP/user-agent de pessoas reais;
- exports de banco de dados;
- dumps, backups ou arquivos de produção.

## Dados de demonstração

Qualquer exemplo futuro deve usar dados **claramente fictícios**, evitando combinações que possam coincidir com uma pessoa real.

## LGPD

O projeto contempla elementos técnicos relacionados a privacidade, como aceite, solicitações de exportação/exclusão e trilha de tratamento. Esses recursos não significam automaticamente conformidade integral com a LGPD.

Conformidade depende também de finalidade, base legal, transparência, retenção, segurança, contratos, governança e atendimento efetivo aos titulares.

## Logs

Logs de aplicação devem privilegiar identificadores técnicos e evitar registrar conteúdo sensível desnecessário. Em especial, tokens, senhas, chaves, documentos e payloads financeiros completos não devem aparecer em logs.
