# Tileset Utils

Uma coleção de scripts para facilitar a criação de tilesets e mapas para jogos 2D.&#x20;

Esse repositório tem o intuito de armazenar pequenos fragmentos de código que vão me ajudar a agilizar o processo de criação de mapas e tilesets, além de me ajudar a  manter os estudos em Python em dia \:D

É bem provavel que eu esteja reinventando a roda com esses scripts e talvez não fazendo da melhor forma otimizada possível. Fique a vontade para contribuir com sugestões e críticas construtivas.

***

## 1 - Tilemap Extract

A partir de uma imagem, extrai os tiles únicos e monta um tileset para poder ser utilizado em editores de tilemap.

**Como usar:**

```txt
from tilemap_extract import *

filename = "meu_mapa.png"
tile_size = 64 # Sobre qual tamanho de tiles o mapa foi feito (16,32,64...)
tiles_per_row = 20 # Quantidade de tiles por linha que será salvo no tilemap gerado

tilemap_extract = TilemapExtract(filename, tile_size, tiles_per_row)
tilemap = tilemap_extract.create_tilemap()
tilemap_extract.to_file('tilemap.png')
```
Caso queria testar com uma imagem real, na pasta images existe um mapa do cenário World 1-1 do Super Mario Bros do NES (Não me processa, Nintendo ;~)