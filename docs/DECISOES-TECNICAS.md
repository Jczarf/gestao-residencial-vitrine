# Decisões técnicas

Este documento registra decisões de engenharia que ajudam a explicar o projeto em entrevistas e revisões técnicas.

## 1. Frontend e backend separados

**Decisão:** utilizar frontend Next.js e backend Express em serviços independentes.

**Motivo:** separar apresentação, API e regras de negócio facilita evolução, testes, isolamento de responsabilidades e implantação independente.

**Trade-off:** aumenta a complexidade operacional em comparação com uma aplicação monolítica simples.

## 2. TypeScript nas duas camadas

**Decisão:** TypeScript no frontend e backend.

**Motivo:** reduzir erros de contrato entre módulos, melhorar refatoração e tornar interfaces de dados mais explícitas.

## 3. Prisma + PostgreSQL

**Decisão:** PostgreSQL como banco relacional e Prisma como ORM.

**Motivo:** o domínio possui relações fortes entre locatários, imóveis, contratos, cobranças e pagamentos. Um banco relacional facilita integridade e consultas consistentes.

**Trade-off:** regras financeiras críticas ainda precisam ser validadas na camada de negócio; o ORM não substitui desenho transacional adequado.

## 4. Docker no ambiente

**Decisão:** containers para banco, backend e frontend.

**Motivo:** reduzir diferenças entre ambientes, facilitar setup e deixar dependências explícitas.

**Cuidados:** secrets não devem ser embutidos nas imagens. Configuração sensível deve entrar por variáveis de ambiente ou mecanismo de secrets do ambiente de implantação.

## 5. Auditoria como entidade própria

**Decisão:** registrar ações relevantes em trilha de auditoria.

**Motivo:** operações administrativas e financeiras exigem rastreabilidade: quem fez, quando, sobre qual entidade e em qual contexto.

## 6. Separação entre cobrança e transação

**Decisão:** modelar cobrança mensal e transação de pagamento como conceitos diferentes.

**Motivo:** uma transação pode ter ciclo de vida próprio e, dependendo da regra, liquidar uma ou mais cobranças. Essa separação reduz acoplamento entre obrigação financeira e evento de pagamento.

## 7. Integração de pagamento atrás do backend

**Decisão:** tokens e lógica sensível de pagamentos permanecem no servidor.

**Motivo:** o navegador não deve receber credenciais privadas nem ser a fonte de verdade para confirmação financeira.

## 8. Defaults conservadores de segurança

**Decisão:** CORS configurável, rate limiting, Helmet, CSRF, limites de corpo e tratamento central de erro.

**Motivo:** reduzir superfície de ataque antes das regras específicas de cada rota.

## 9. Portfólio sem código completo

**Decisão:** manter a implementação principal privada e publicar uma vitrine sanitizada.

**Motivo:** demonstrar capacidade técnica sem expor dados, segredos, detalhes operacionais ou entregar integralmente um projeto com potencial de uso real.

## 10. IA como ferramenta assistiva

Agentes de IA foram utilizados para apoiar planejamento, implementação, revisão, testes, documentação e investigação de falhas.

A decisão de engenharia é tratar saída de IA como **proposta sujeita a validação**, e não como fonte automática de verdade. Em especial, alterações relacionadas a autenticação, pagamentos, dados pessoais e infraestrutura exigem revisão adicional.
