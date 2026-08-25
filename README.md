# Sistema de Gestão Residencial — Vitrine Técnica

Vitrine técnica de uma aplicação web para apoio à gestão de imóveis, locatários, contratos, cobranças e documentos.

> **Código-fonte principal privado.** Este repositório apresenta arquitetura, funcionalidades, decisões técnicas e processo de desenvolvimento sem expor implementação sensível, credenciais ou dados reais.

## Problema

Rotinas de locação costumam ficar distribuídas entre planilhas, mensagens, comprovantes, contratos e controles manuais. O projeto foi criado para centralizar essas operações em uma única aplicação.

## Funcionalidades trabalhadas

- cadastro e gestão de imóveis;
- cadastro de locatários;
- contratos e competências mensais;
- acompanhamento de cobranças;
- geração de Pix;
- recibos em PDF;
- autenticação e controle de acesso;
- painel administrativo;
- portal do locatário;
- registro de auditoria;
- cuidados relacionados à LGPD;
- testes de backend e autorização;
- experiência PWA.

## Stack

`Next.js` · `React` · `TypeScript` · `Node.js` · `Express` · `Prisma` · `PostgreSQL` · `Docker` · `JWT` · `bcrypt` · `Jest` · `Supertest` · `Playwright`

## Arquitetura resumida

```text
Usuário
  │
  ▼
Frontend Next.js
  │
  ▼
API Node.js / Express
  │
  ├─ autenticação e autorização
  ├─ regras de negócio
  ├─ serviços financeiros
  ├─ geração de documentos
  └─ integrações externas
  │
  ▼
Prisma ORM
  │
  ▼
PostgreSQL
```

## Segurança

O projeto passou por revisão de segurança durante o desenvolvimento. A partir dessa análise, pontos relacionados a autenticação, sessões, pagamentos, dados pessoais e operações financeiras passaram a ser tratados como bloqueadores antes de qualquer uso em produção.

Por isso, esta vitrine **não afirma que o sistema está pronto para produção**. O foco é demonstrar o processo de engenharia, incluindo identificação de riscos, correções e validação antes de deploy real.

## Infraestrutura

O projeto utiliza Docker no ambiente de desenvolvimento e foi estruturado com possibilidade de implantação em VPS. A publicação do ambiente real é mantida separada da documentação de portfólio para evitar exposição de credenciais, endereços e dados operacionais.

## IA no desenvolvimento

Ferramentas e agentes de IA foram utilizados como apoio em planejamento, implementação, revisão, testes, investigação de falhas e documentação. As alterações são revisadas e validadas antes de serem incorporadas.

## Status

Projeto em desenvolvimento e revisão técnica contínua.

## Autor

**Júlio Cézar**  
Estudante de Ciência da Computação · Técnico em Desenvolvimento de Sistemas

[LinkedIn](https://www.linkedin.com/in/j%C3%BAlio-c%C3%A9zar-0a26152b2/) · [GitHub](https://github.com/Jczarf)
