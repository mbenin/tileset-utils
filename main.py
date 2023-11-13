from PIL import Image
import argparse

from tilemap_extract import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extrai tiles únicos de uma imagem e monta um tilemap.')
    parser.add_argument('--image', type=str, help='Caminho da imagem', required=True)
    parser.add_argument('--tilesize', type=int, help='Tamanho do tile. Exemplo: 16,32,64', required=True)
    parser.add_argument('--tilesperrow', type=int, help='Quantidade de tiles por linha', required=True)

    args = parser.parse_args()

    tile_size = args.tilesize
    tiles_per_row = args.tilesperrow
    filename = args.image

    tilemap_extract = TilemapExtract(filename, tile_size, tiles_per_row)
    tilemap = tilemap_extract.create_tilemap()
    tilemap_extract.to_file('tilemap.png')

