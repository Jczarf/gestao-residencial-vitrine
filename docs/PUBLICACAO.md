# Checklist para publicação da vitrine

A vitrine foi criada para poder ser tornada pública sem expor o código-fonte completo da aplicação.

## Antes de mudar para `Public`

- [x] README sem credenciais ou hosts reais
- [x] diagramas sem dados operacionais
- [x] mockup com dados fictícios
- [x] código-fonte principal não incluído
- [x] documentação de segurança com limites explícitos
- [x] documentação de privacidade
- [x] licença restritiva
- [x] nenhum `.env`, dump, backup ou documento real
- [x] scanner dedicado `detect-secrets` configurado para árvore e histórico alcançável
- [ ] confirmar execução verde do workflow `Security Audit`
- [ ] revisão manual final no GitHub
- [ ] configurar descrição e tópicos do repositório
- [ ] tornar o repositório público
- [ ] fixar no perfil somente depois da revisão final

## Auditoria automática

O workflow `.github/workflows/security-audit.yml` faz checkout com histórico completo, instala uma versão fixada do `detect-secrets` e verifica tanto os arquivos atuais quanto conteúdo e nomes de arquivos alcançáveis no histórico Git. Um resultado verde reduz o risco de publicação acidental de credenciais, mas não substitui revisão manual nem revogação de qualquer segredo que tenha sido exposto fora desta vitrine.

## Descrição sugerida

`Vitrine técnica de uma aplicação full-stack para gestão residencial: Next.js, TypeScript, Express, Prisma, PostgreSQL, Docker, pagamentos, auditoria e segurança.`

## Tópicos sugeridos

`typescript` `nextjs` `express` `prisma` `postgresql` `docker` `fullstack` `portfolio` `security` `software-engineering`

## O que não fazer

Não copiar o histórico Git do projeto privado para esta vitrine. Não adicionar screenshots de produção sem anonimização. Não publicar `.env.example` com valores reais. Não usar IP, usuário, senha ou token como exemplo "temporário".
