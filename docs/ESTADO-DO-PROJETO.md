# Estado real do projeto

Esta vitrine descreve um sistema **em desenvolvimento**. Ela não deve ser interpretada como evidência de que todos os módulos estão finalizados, integrados ou validados para produção.

## Legenda

- ✅ **Evidência no código** — existe implementação correspondente no repositório privado.
- 🧪 **Parcial / em validação** — há código, fluxo ou documentação, mas a conclusão end-to-end não foi confirmada.
- 📋 **Planejado / não validado** — faz parte do desenho do produto, da documentação ou de uma etapa ainda pendente.

## Estado por área

| Área | Estado | Observação |
|---|---|---|
| Backend Express + TypeScript | ✅ | Estrutura, rotas e middlewares existem no projeto privado. |
| Prisma + PostgreSQL | ✅ | Schema relacional existe e representa o domínio principal. |
| Docker para banco/backend/frontend | ✅ | Há configuração de ambiente containerizado. |
| Autenticação/autorização | 🧪 | Há implementação, mas deve ser tratada como em revisão até validação completa dos fluxos. |
| Painel administrativo | 🧪 | Há desenvolvimento de interface e rotas, sem afirmar cobertura funcional total. |
| Portal do locatário | 🧪 | Presente no escopo e em implementação; não apresentado como fluxo finalizado. |
| Contratos e cobranças | 🧪 | Modelagem e regras existem, mas o conjunto completo de cenários precisa de validação integrada. |
| PIX / integração financeira | 🧪 | Integração trabalhada; operações financeiras reais permanecem bloqueadas como critério de produção até revisão completa. |
| Recibos em PDF | 🧪 | Funcionalidade presente no projeto, ainda tratada como parte do protótipo. |
| Auditoria e solicitações de privacidade | 🧪 | Estruturas existem; não equivalem a conformidade jurídica integral. |
| PWA | 🧪 | Há trabalho nessa direção, mas não é apresentado como experiência concluída em todos os dispositivos. |
| Testes backend / autorização | 🧪 | Existem testes, porém esta vitrine não afirma que toda a suíte atual esteja verde sem execução recente verificada. |
| Playwright / E2E | 🧪 | Ferramenta presente; cobertura completa dos fluxos não é afirmada. |
| Deploy de produção | 📋 | Não é apresentado como concluído ou aprovado. |
| Segurança para operação financeira real | 📋 | Há revisão e controles, mas ainda existem itens que precisam ser resolvidos/verificados antes de produção. |
| Conformidade LGPD integral | 📋 | Não reivindicada. Exigiria análise jurídica e operacional além do código. |

## Inconsistência histórica de documentação

O projeto privado possui registros de desenvolvimento que chegaram a usar expressões como “pronto para produção”, enquanto outras partes da própria documentação ainda indicavam itens incompletos. Por isso, esta vitrine adota uma regra mais conservadora: **nenhuma funcionalidade é tratada como concluída apenas porque um log antigo a chamou de concluída**.

## Como descrever em portfólio

Formulação recomendada:

> Protótipo full-stack avançado de gestão residencial, em desenvolvimento, usado para praticar modelagem relacional, autenticação, regras financeiras, integrações, Docker, testes e revisão de segurança.

Evite dizer:

- “sistema pronto para produção”;
- “plataforma financeira segura”;
- “LGPD compliant”;
- “todos os fluxos estão concluídos”; ou
- “testes 100% aprovados” sem uma execução recente verificável.

## Próximos passos

- reconciliar documentação antiga com o estado atual do código;
- executar e registrar uma baseline reproduzível de testes;
- concluir validação de autenticação, autorização e sessões;
- fechar pendências de pagamentos/webhooks e operações financeiras;
- validar migrations e setup do banco a partir de ambiente limpo;
- revisar fluxos E2E prioritários;
- somente depois avaliar qualquer deploy com dados ou pagamentos reais.
