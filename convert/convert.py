from PIL import Image

def convert_to_ppm(input_image_path, output_image_path):
    try:
        img = Image.open(input_image_path)

        img.save(output_image_path, "PPM")

        print(f"Imagem convertida para {output_image_path} com sucesso!")
    
    except Exception as e:
        print(f"Erro ao converter a imagem: {e}")

while True:
    diretorio = input('DIRETORIO: ')
    input_image = f'{diretorio}.png'
    output_image = f'output\{diretorio}.ppm'

    convert_to_ppm(input_image, output_image)
