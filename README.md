<p align="center">
  <img src="assets/capa.svg" alt="Sistema de Gestão Residencial — Vitrine Técnica" width="100%">
</p>

# Sistema de Gestão Residencial — Vitrine Técnica

Aplicação full-stack desenvolvida para centralizar rotinas de **imóveis, locatários, contratos, cobranças, pagamentos, recibos e privacidade** em uma única plataforma.

> **Este repositório é uma vitrine de portfólio.** O código-fonte completo permanece privado. Aqui são publicados arquitetura, decisões técnicas, fluxos, segurança e representações visuais sanitizadas — sem credenciais, dados reais ou detalhes operacionais sensíveis.

## Visão do produto

Rotinas de locação frequentemente ficam espalhadas entre planilhas, mensagens, contratos, comprovantes e controles manuais. O projeto foi criado para reunir essas operações e manter rastreabilidade sobre o ciclo completo da locação.

### Principais áreas

- gestão de imóveis;
- cadastro e gestão de locatários;
- contratos e competências mensais;
- cobranças de aluguel e água;
- juros, multas e exceções;
- integração de pagamentos/PIX;
- pagamentos manuais com justificativa;
- geração de recibos em PDF;
- painel administrativo;
- portal do locatário;
- trilha de auditoria;
- solicitações relacionadas a dados pessoais;
- experiência responsiva/PWA.

## Stack

`Next.js` · `React` · `TypeScript` · `Node.js` · `Express` · `Prisma` · `PostgreSQL` · `Docker` · `JWT` · `bcrypt` · `Jest` · `Supertest` · `Playwright`

O backend também utiliza camadas como `Helmet`, CORS configurável, rate limiting, CSRF e validação de requisições.

## Arquitetura

<p align="center">
  <img src="assets/arquitetura.svg" alt="Arquitetura lógica sanitizada" width="100%">
</p>

```text
Usuário
  │
  ▼
Frontend Next.js
  │
  ▼
API Express / TypeScript
  │
  ├── autenticação e autorização
  ├── domínio residencial
  ├── regras financeiras
  ├── documentos
  ├── auditoria e privacidade
  └── integrações externas
  │
  ▼
Prisma ORM
  │
  ▼
PostgreSQL
```

Detalhamento em [`docs/ARQUITETURA.md`](docs/ARQUITETURA.md).

## Interface

<p align="center">
  <img src="assets/painel-conceitual.svg" alt="Mockup conceitual do painel administrativo" width="100%">
</p>

> O painel acima é um **mockup conceitual criado para o portfólio**. Os números, competências e valores são fictícios e não representam dados de usuários reais.

## Fluxo financeiro

<p align="center">
  <img src="assets/fluxo-cobranca.svg" alt="Fluxo conceitual de cobrança e conciliação" width="100%">
</p>

Uma decisão importante foi separar **cobrança** de **transação de pagamento**. A aplicação não trata uma notificação do navegador como fonte de verdade financeira: o backend precisa validar o estado da transação antes de refletir a alteração na cobrança.

Mais detalhes em [`docs/FLUXOS.md`](docs/FLUXOS.md).

## Modelagem

O domínio privado possui entidades específicas para representar, entre outros conceitos:

```text
Locatário ── Contrato ── Imóvel
                 │
                 └── Cobrança mensal
                         │
                         └── vínculo com Transação de pagamento

Auditoria
Solicitações de privacidade
Configurações do sistema
```

A modelagem utiliza PostgreSQL e Prisma para manter relações explícitas entre contratos, cobranças, transações e registros de auditoria.

## Segurança

O sistema manipula autenticação, dados pessoais e operações financeiras, portanto segurança é tratada como requisito de arquitetura.

Entre os controles presentes ou trabalhados no projeto estão:

- hash de senha;
- autenticação e autorização;
- cabeçalhos de segurança com Helmet;
- CORS restritivo por configuração;
- rate limiting;
- proteção CSRF;
- limite de payload;
- tratamento central de erros;
- segredos exclusivamente por configuração de ambiente;
- trilha de auditoria;
- validação adicional de eventos financeiros.

**Importante:** a existência desses controles não significa que o sistema está certificado ou pronto para produção. A revisão de segurança identificou pontos que precisam ser resolvidos e verificados antes de um ambiente real.

> **Status de segurança: em revisão. Não apresentado como production-ready.**

Leia [`docs/SEGURANCA.md`](docs/SEGURANCA.md).

## Privacidade

A modelagem busca aplicar minimização de dados quando possível. A vitrine, por sua vez, não contém documentos, dumps de banco, contratos, recibos, telefones, CPFs, endereços ou informações reais de locatários.

A aplicação também prevê fluxo técnico para solicitações relacionadas a exportação/exclusão de dados. Isso é parte da engenharia de privacidade, mas **não é uma declaração automática de conformidade jurídica integral com a LGPD**.

Leia [`docs/PRIVACIDADE.md`](docs/PRIVACIDADE.md).

## Testes

O projeto privado utiliza:

- **Jest + Supertest** no backend;
- **Playwright** para fluxos end-to-end do frontend.

Os cenários mais importantes envolvem autenticação, autorização, contratos, regras financeiras, webhooks, recibos e isolamento dos dados de cada locatário.

Leia [`docs/TESTES.md`](docs/TESTES.md).

## Infraestrutura

O ambiente de desenvolvimento utiliza Docker para separar banco, backend e frontend. Configurações privadas entram por variáveis de ambiente e não fazem parte desta vitrine.

Nenhum IP de servidor, usuário administrativo, senha, token de pagamento ou segredo de webhook é publicado aqui.

## Decisões de engenharia

Algumas decisões que orientaram o projeto:

- frontend e backend separados;
- TypeScript nas duas camadas;
- banco relacional para um domínio com forte integridade entre entidades;
- cobrança e transação modeladas separadamente;
- integração financeira controlada pelo servidor;
- auditoria como entidade própria;
- containers para reduzir divergência de ambiente;
- código completo privado e portfólio público sanitizado.

A justificativa e os trade-offs estão em [`docs/DECISOES-TECNICAS.md`](docs/DECISOES-TECNICAS.md).

## IA aplicada ao desenvolvimento

Agentes e modelos de linguagem foram utilizados como apoio em diferentes fases do projeto, incluindo planejamento, implementação, refatoração, testes, revisão, documentação e investigação de falhas.

O princípio adotado é simples: **saída de IA é proposta, não aprovação automática**. Mudanças relacionadas a autenticação, pagamentos, dados pessoais e infraestrutura exigem validação adicional antes de serem incorporadas.

## O que esta vitrine demonstra

Este repositório foi estruturado para demonstrar competências de engenharia sem precisar abrir todo o produto:

- desenho de arquitetura full-stack;
- modelagem relacional;
- APIs e regras de negócio;
- segurança aplicada ao desenvolvimento;
- integração com serviços externos;
- Docker e organização de ambiente;
- estratégia de testes;
- documentação técnica;
- capacidade de revisar criticamente um sistema antes de colocá-lo em produção.

## Documentação

| Documento | Conteúdo |
|---|---|
| [`ARQUITETURA.md`](docs/ARQUITETURA.md) | camadas e responsabilidades |
| [`FLUXOS.md`](docs/FLUXOS.md) | fluxos administrativo, locatário e financeiro |
| [`SEGURANCA.md`](docs/SEGURANCA.md) | controles, riscos e limites |
| [`PRIVACIDADE.md`](docs/PRIVACIDADE.md) | dados pessoais e publicação segura |
| [`TESTES.md`](docs/TESTES.md) | estratégia e cenários prioritários |
| [`DECISOES-TECNICAS.md`](docs/DECISOES-TECNICAS.md) | decisões e trade-offs |
| [`PUBLICACAO.md`](docs/PUBLICACAO.md) | checklist para tornar a vitrine pública |

## Código-fonte

O código integral do produto **não é distribuído neste repositório**. O objetivo é permitir avaliação técnica do projeto sem entregar a implementação completa nem expor dados e configurações privadas.

Consulte [`LICENSE`](LICENSE) para os termos desta vitrine.

## Status

**Em desenvolvimento e revisão técnica.**

O projeto é apresentado como trabalho de engenharia em evolução, não como sistema certificado ou pronto para operação financeira real.

## Autor

**Júlio Cézar**  
Estudante de Ciência da Computação · Técnico em Desenvolvimento de Sistemas

[LinkedIn](https://www.linkedin.com/in/j%C3%BAlio-c%C3%A9zar-0a26152b2/) · [GitHub](https://github.com/Jczarf)
