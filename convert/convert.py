from PIL import Image

def convert_to_ppm(input_image_path, output_image_path):
    try:
        # Abre a imagem com PIL
        img = Image.open(input_image_path)

        # Converte a imagem para o formato PPM
        img.save(output_image_path, "PPM")

        print(f"Imagem convertida para {output_image_path} com sucesso!")
    
    except Exception as e:
        print(f"Erro ao converter a imagem: {e}")

while True:
    diretorio = input('DIRETORIO: ')
    input_image = f'{diretorio}.png'  # Caminho da imagem original
    output_image = f'output\{diretorio}.ppm'  # Caminho da imagem convertida para PPM

    convert_to_ppm(input_image, output_image)
