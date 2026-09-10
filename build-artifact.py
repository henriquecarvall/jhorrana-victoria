# Gera a versao "conteudo" da pagina (sem <html>/<head>/<body>) para publicar
# como Artifact no claude.ai. Fonte unica de verdade: index.html
import io, os, re, sys

src = io.open('index.html', encoding='utf-8').read()
title = re.search(r'<title>.*?</title>', src, re.S).group(0)
font  = re.search(r'<link rel="stylesheet" href="https://fonts\.googleapis[^>]*>', src).group(0)
style = re.search(r'<style>.*?</style>', src, re.S).group(0)
body  = re.search(r'<body>(.*)</body>', src, re.S).group(1)

out = sys.argv[1] if len(sys.argv) > 1 else 'artifact.html'
os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
io.open(out, 'w', encoding='utf-8').write(
    title + '\n' + font + '\n' + style + '\n' + body.strip() + '\n'
)
print('escrito:', out)
