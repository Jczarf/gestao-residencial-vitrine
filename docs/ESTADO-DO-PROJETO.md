# Estado real do projeto

Esta vitrine descreve um sistema **em desenvolvimento**. Ela não deve ser interpretada como evidência de que todos os módulos estão finalizados, integrados ou validados para produção.

## Legenda

- ✅ **Implementado e verificado no escopo indicado** — há código correspondente e uma validação recente reproduzível para aquela camada.
- 🧪 **Parcial / em validação** — há código, fluxo ou documentação, mas a conclusão end-to-end não foi confirmada.
- 📋 **Planejado / não validado para produção** — faz parte do desenho do produto ou depende de validação ainda pendente.

## Estado por área

| Área | Estado | Observação |
|---|---|---|
| Backend Express + TypeScript | ✅ | `npm ci` e `npm run build` concluíram com sucesso no CI em 26/08/2026. |
| Suíte Jest do backend | ✅ | A suíte atualmente descoberta pelo Jest concluiu com sucesso no mesmo CI. Isso não equivale a validar todos os fluxos do produto. |
| Frontend Next.js | ✅ | `npm ci`, lint e build de produção concluíram com sucesso no CI. |
| Prisma + PostgreSQL | ✅ | Schema relacional existe e representa o domínio principal; a baseline de CI atual não executa um teste completo de migrations contra banco limpo. |
| Docker para banco/backend/frontend | 🧪 | Há configuração containerizada, mas o Compose completo ainda não foi validado nesta baseline. |
| Autenticação/autorização | 🧪 | Há implementação e testes associados, mas ainda requer validação integrada de sessões, papéis e cenários adversariais. |
| Painel administrativo | 🧪 | Interface e rotas existem; o CI confirma que o frontend compila, não que todos os fluxos de usuário funcionem ponta a ponta. |
| Portal do locatário | 🧪 | Presente no desenvolvimento; não apresentado como fluxo integralmente concluído. |
| Contratos e cobranças | 🧪 | Modelagem e regras existem, mas o conjunto completo de cenários precisa de validação integrada. |
| PIX / integração financeira | 🧪 | Integração trabalhada; o CI não executa transações reais nem valida webhooks contra o provedor. |
| Recibos em PDF | 🧪 | Funcionalidade presente no protótipo, sem validação end-to-end nesta baseline. |
| Auditoria e solicitações de privacidade | 🧪 | Estruturas existem; não equivalem a conformidade jurídica integral. |
| PWA | 🧪 | Há implementação relacionada, mas não foi validada em matriz de dispositivos/navegadores. |
| Playwright / E2E | 🧪 | Playwright está configurado, porém não foi executado pela baseline de CI de 26/08/2026. |
| Deploy de produção | 📋 | Não é apresentado como concluído ou aprovado. |
| Segurança para operação financeira real | 📋 | Há controles e revisão, mas ainda existem itens que precisam ser resolvidos/verificados antes de produção. |
| Conformidade LGPD integral | 📋 | Não reivindicada. Exigiria análise jurídica e operacional além do código. |

## Evidência automatizada mais recente

Em **26/08/2026**, o workflow `CI` do repositório privado concluiu com sucesso no commit `0352694d9e8193f4e0ff777c1d38891d34d6851f`.

A execução verificou:

- instalação reprodutível das dependências do backend;
- compilação TypeScript do backend;
- suíte Jest atualmente configurada;
- instalação reprodutível das dependências do frontend;
- lint do frontend;
- build de produção do Next.js.

Essa evidência aumenta a confiança de que **as duas camadas compilam e a suíte atual passa**, mas não valida automaticamente banco/migrations, Playwright, pagamentos reais, webhooks, Docker Compose completo, segurança de produção ou conformidade legal.

## Inconsistência histórica de documentação

O projeto privado possui registros antigos que chegaram a usar expressões como “pronto para produção”. A auditoria atual adota uma regra mais rigorosa: **o status é determinado por evidência reproduzível, não por uma frase de um log antigo**.

## Como descrever em portfólio

Formulação recomendada:

> Protótipo full-stack avançado de gestão residencial, em desenvolvimento. A baseline atual confirma build do backend, suíte Jest, lint e build do frontend; fluxos financeiros, E2E e requisitos de produção continuam em validação.

Evite dizer:

- “sistema pronto para produção”;
- “plataforma financeira segura”;
- “LGPD compliant”;
- “todos os fluxos estão concluídos”; ou
- que CI verde significa validação end-to-end do sistema.

## Próximos passos

- validar migrations e setup do PostgreSQL a partir de ambiente limpo;
- executar Playwright para os fluxos prioritários;
- aprofundar testes de autenticação, autorização e sessões;
- fechar pendências de pagamentos/webhooks e operações financeiras;
- validar Docker Compose de ponta a ponta;
- somente depois avaliar qualquer deploy com dados ou pagamentos reais.
