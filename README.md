# Site — Jhorrana Victória · Estética & Massoterapia

Landing page estática de conversão para WhatsApp. **Um arquivo só:** `index.html`
(HTML, CSS e JS inline, zero dependência, zero build).

## Estrutura

```
index.html          página completa — é aqui que se edita tudo
assets/img/         fotos (ver lista abaixo)
build-artifact.py   gera a versão para preview no claude.ai (opcional)
```

## O que falta preencher (busque por `Preencher` no arquivo)

| Onde | O que |
|---|---|
| Depoimentos | Trocar os 3 textos-modelo por depoimentos reais de clientes |
| Resultados | Trocar as 4 imagens e ajustar as legendas (nº real de sessões) |
| FAQ · preço | Decidir se mostra faixa de valor ("a partir de R$ …") ou mantém "no WhatsApp" |
| FAQ · região | Listar bairros/regiões atendidos sem taxa de deslocamento |
| FAQ · pagamento | Formas aceitas (Pix, cartão, pacotes) e se há sinal para reservar |
| Hero · selo | "Agenda aberta esta semana" — tirar se não for verdade sempre |
| `<link rel="canonical">` | Trocar pelo domínio real quando existir |

## Fotos necessárias

Coloque em `assets/img/` e troque cada `<div class="ph">` por um `<img>`:

| Arquivo | Formato | O que fotografar |
|---|---|---|
| `jhorrana-hero.jpg` | vertical 4:5, ≥1000px | Atendimento em andamento: mão na pele da cliente, luz quente, foco na mão |
| `jhorrana-retrato.jpg` | vertical 4:5, ≥1000px | Retrato olhando para a câmera, uniforme, fundo limpo |
| `resultado-1..4.jpg` | quadrado 1:1, ≥900px | Antes/depois lado a lado — **mesma luz, mesmo ângulo, sem filtro** |
| `og.jpg` | 1200×630 | Imagem que aparece ao compartilhar o link no WhatsApp/Instagram |

Como trocar:

```html
<!-- antes -->
<div class="ph ph--45"><span>Foto vertical 4:5 …</span></div>

<!-- depois -->
<div class="ph ph--45"><img src="assets/img/jhorrana-hero.jpg" alt="Jhorrana atendendo uma cliente"></div>
```

O `.ph` já cuida do enquadramento (`object-fit: cover`), então qualquer foto no
formato certo encaixa sem cortar torto.

## Rodar local

```bash
npx serve .        # ou: python -m http.server 8000
```

## Publicar

```bash
npm i -g vercel
vercel            # preview
vercel --prod     # produção
```

Depois é só apontar o domínio no painel da Vercel e trocar o link da bio do
Instagram para o site (o site manda para o WhatsApp — a bio deixa de ser um beco sem saída).

## Decisões de design (para manter a coerência ao editar)

- **Acento é um só:** o mel `--mel`. Verde eucalipto `--euca` aparece apenas em
  "Você sai com…" — é o fio terapêutico. Não espalhe.
- **Card é exceção**, não regra: só os 4 serviços e os depoimentos. O resto é
  separado por filete. Adicionar borda/sombra em tudo achata a hierarquia.
- **Numeração só onde há sequência real** (o passo a passo do atendimento).
- **Nada de promessa que a técnica não entrega.** A honestidade ("resultado se
  constrói em série, não em milagre") é o que gera confiança nesse nicho.
- Tema claro e escuro são tokenizados no `:root`. Nunca escreva cor literal em
  um componente — use a variável, senão um dos temas quebra.
