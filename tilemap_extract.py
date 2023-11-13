from PIL import Image

# Extrai tiles unicos a partir de uma imagem
# e monta um tilemap logo em seguida

class TilemapExtract:

    def __init__(self, filename, tile_size, tiles_per_row):
        self.filename = filename
        self.tile_size = tile_size
        self.tiles_per_row = tiles_per_row
        self.image = Image.open(filename)
        self.tilemap_image = None

    def create_tilemap(self):
        # Extrai os tiles unicos da imagem
        unique_tiles = self.__extract_unique_tiles()

        # Cria uma nova imagem com os tiles unicos
        self.tilemap_image = self.__create_image_from_tiles(unique_tiles)

        return self.tilemap_image

    def to_file(self, filename):
        if self.tilemap_image is None:
            self.create_tilemap()

        self.tilemap_image.save(filename)

    def __extract_unique_tiles(self):
        image = Image.open(self.filename)
        image_width, image_height = image.size

        # Calcula quantos tiles no tamanho especificado a imagem tem
        num_tiles_x = image_width // self.tile_size
        num_tiles_y = image_height // self.tile_size

        # Array que irá armazenar os tiles unicos encontrados
        unique_tiles = set()
        unique_tile_images = []

        # percorre a imagem extraindo os tiles de acordo com o tamanho especificado
        for col in range(0, num_tiles_y):
            for row in range(0, num_tiles_x):
                # image.crop((left, top, right, bottom))
                # (left,top) ________
                #          |        |
                #          |        |
                #          |________| (right,bottom)
                bbox = (
                    row * self.tile_size, col * self.tile_size, (row + 1) * self.tile_size, (col + 1) * self.tile_size)

                tile = image.crop(bbox)

                if tile.tobytes() not in unique_tiles:
                    unique_tiles.add(tile.tobytes())
                    unique_tile_images.append(tile)

        return unique_tile_images

    def __create_image_from_tiles(self, unique_tiles):

        # largura definida de acordo com a quantidade de tiles horizontais desejado
        image_width = self.tile_size * self.tiles_per_row

        # calcula a altura da imagem final baseado na quantidade de tiles por linha
        num_rows = len(unique_tiles) // self.tiles_per_row

        # se a quantidade de tiles não for divisivel pela quantidade de tiles por linha
        # adiciona mais uma linha (significa que a ultima linha não está completa)
        if len(unique_tiles) % self.tiles_per_row > 0:
            num_rows += 1

        image_height = self.tile_size * num_rows

        # Cria uma nova imagem com a largura e altura calculadas
        tilemap_image = Image.new('RGB', (image_width, image_height))

        # Coloca cada tile na nova imagem
        for i, tile in enumerate(unique_tiles):
            # Calcula a posição X e Y do tile na imagem final
            # i % tiles_per_row retorna o resto da divisão
            # Exemplo: i = 22, tiles_per_row = 5, resto = 2
            # 2 * tile_width = 32
            x = (i % self.tiles_per_row) * self.tile_size

            # idx // tiles_per_row retorna a parte inteira da divisão
            # Exemplo: i = 22, tiles_per_row = 5, parte inteira = 4
            # 4 * tile_height = 64
            y = (i // self.tiles_per_row) * self.tile_size

            # Coloca o tile na posição calculada
            # Exemplo: (32, 64)
            tilemap_image.paste(tile, (x, y))

        return tilemap_image
