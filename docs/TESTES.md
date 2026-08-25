# Estratégia de testes

O projeto privado possui testes no backend com **Jest + Supertest** e utiliza **Playwright** no frontend para fluxos end-to-end.

Esta vitrine não publica a suíte completa, mas documenta o que deve ser validado antes de qualquer uso real.

## Backend

Casos prioritários:

- autenticação válida e inválida;
- expiração e revogação de sessão;
- autorização por perfil e por recurso;
- criação e alteração de contratos;
- cálculo de cobrança, multa e juros;
- pagamentos manuais;
- transações de pagamento;
- idempotência de webhook;
- tentativa de repetir eventos financeiros;
- acesso indevido a dados de outro locatário;
- geração de recibo somente após estado válido;
- solicitações relacionadas a dados pessoais;
- rate limiting e validação de requisição.

## Frontend / E2E

Fluxos prioritários:

- login administrativo;
- login do locatário;
- criação de imóvel/locatário/contrato;
- consulta de competências;
- fluxo de cobrança;
- consulta e emissão de recibo;
- logout e expiração de sessão;
- bloqueio de páginas não autorizadas;
- navegação responsiva.

## Segurança

Os testes funcionais não substituem revisão de segurança. Antes de produção, é necessário validar também:

- autenticação e recuperação de acesso;
- exposição de PII;
- autorização horizontal/vertical;
- CSRF/CORS;
- webhooks;
- abuso de endpoints;
- logs sem dados sensíveis;
- segredos e configuração de infraestrutura;
- dependências vulneráveis.

## Critério de publicação

A vitrine pode ser pública mesmo enquanto o produto está em desenvolvimento, desde que deixe claro o estado do projeto e não exponha dados ou credenciais. Já o sistema completo só deve ser apresentado como pronto para produção após os bloqueadores técnicos e de segurança estarem resolvidos e verificados.
