# Fluxos principais

## Fluxo administrativo

```text
Login administrativo
      ↓
Painel
      ↓
Imóveis / locatários / contratos
      ↓
Competências mensais
      ↓
Cobranças
      ↓
Pagamento / baixa manual
      ↓
Recibo + histórico + auditoria
```

## Fluxo do locatário

```text
Autenticação
      ↓
Portal do locatário
      ↓
Contrato e competências
      ↓
Cobranças pendentes/pagas
      ↓
PIX / comprovantes / recibos
      ↓
Solicitações e informações de privacidade
```

## Fluxo de cobrança

![Fluxo de cobrança](../assets/fluxo-cobranca.svg)

A regra importante é que **cobrança, transação e estado final de pagamento não são tratados como a mesma coisa**. O backend deve validar o evento financeiro antes de refletir a mudança no domínio.

## Webhook

Visão sanitizada:

```text
Provedor de pagamento
      ↓
Endpoint de webhook
      ↓
Validação de autenticidade
      ↓
Idempotência
      ↓
Localização da transação
      ↓
Atualização consistente
      ↓
Auditoria
```

Detalhes de assinatura, IDs reais e endpoints de produção não fazem parte desta vitrine.

## Recibos

Recibos são gerados a partir de estado financeiro validado. O objetivo é evitar que a interface, isoladamente, seja capaz de criar uma evidência de pagamento sem respaldo no backend.

## Solicitação LGPD

```text
Locatário solicita ação sobre dados
      ↓
Solicitação registrada
      ↓
Análise administrativa
      ↓
Aprovação/recusa conforme processo aplicável
      ↓
Registro do resultado
```

A implementação técnica é apenas uma parte do processo de privacidade; obrigações legais e organizacionais devem ser avaliadas separadamente.
