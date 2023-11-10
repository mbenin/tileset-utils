import argparse
import os
from PIL import Image


# Extrai tiles unicos a partir de uma imagem
# e monta um tilemap logo em seguida

def extract_unique_tiles(image_path, tile_width, tile_height):
    image = Image.open(image_path)
    image_width, image_height = image.size

    # Calcula quantos tiles no tamanho especificado a imagem tem
    num_tiles_x = image_width // tile_width
    num_tiles_y = image_height // tile_height

    #Array que irá armazenar os tiles unicos encontrados
    unique_tiles = set()
    unique_tile_images = []

    #percorre a imagem extraindo os tiles de acordo com o tamanho especificado
    for col in range(0,num_tiles_y):
        for row in range(0, num_tiles_x):
            #image.crop((left, top, right, bottom))
            #(left,top) ________
            #          |        |
            #          |        |
            #          |________| (right,bottom)
            bbox = (row * tile_width, col*tile_height, (row + 1)*tile_width, (col + 1)*tile_height)

            tile = image.crop(bbox)
            tile_data = tile.tobytes()

            if tile_data not in unique_tiles:
                unique_tiles.add(tile_data)
                unique_tile_images.append(tile)

    print(unique_tile_images[0].size)

    return unique_tile_images


def create_image_from_tiles(unique_tiles, tiles_per_row):
    if not unique_tiles:
        raise ValueError("A lista de tiles não pode estar vazia.")

    # Calcula a largura e altura da nova imagem
    tile_width, tile_height = unique_tiles[0].size

    #largura definida de acordo com a quantidade de tiles horizontais desejado
    image_width = tile_width * tiles_per_row

    #calcula a altura da imagem final baseado na quantidade de tiles por linha
    num_rows = len(unique_tiles) // tiles_per_row + (1 if len(unique_tiles) % tiles_per_row > 0 else 0)
    image_height = tile_height * num_rows

    # Cria uma nova imagem com a largura e altura calculadas
    combined_image = Image.new('RGB', (image_width, image_height))

    # Coloca cada tile na nova imagem
    for idx, tile in enumerate(unique_tiles):
        x = (idx % tiles_per_row) * tile_width
        y = (idx // tiles_per_row) * tile_height
        combined_image.paste(tile, (x, y))

    return combined_image


# metódo main
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extrai tiles únicos de uma imagem e monta um tilemap.')
    parser.add_argument('--image', type=str,help='Caminho da imagem', required=True)
    parser.add_argument('--tilesize', type=int, help='Tamanho do tile. Exemplo: 16,32,64', required=True)
    parser.add_argument('--tilesperrow', type=int, help='Quantidade de tiles por linha', required=True)

    args = parser.parse_args()

    tile_width = args.tilesize
    tile_height = args.tilesize
    tiles_per_row = args.tilesperrow
    filename = args.image

    unique_tiles = extract_unique_tiles(filename, tile_width, tile_height)
    combined_image = create_image_from_tiles(unique_tiles, tiles_per_row)

    # Para salvar a nova imagem com os tiles únicos lado a lado
    base_name, extension = os.path.splitext(filename)
    combined_image.save(base_name + '_unique.png')

