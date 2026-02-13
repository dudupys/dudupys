#!/usr/bin/env python3
"""Script para criar GIF com os frames já existentes"""

import os
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

# Encontrar todos os arquivos de frame
frame_folder = "frames"
frame_files = []
if not os.path.exists(frame_folder):
    print(f"Pasta '{frame_folder}' não encontrada. Criando...")
    os.makedirs(frame_folder)

for file in os.listdir(frame_folder):
    if file.startswith("frame_") and file.endswith(".png"):
        frame_files.append(file)

# Ordenar por número
frame_files.sort(key=lambda x: int(x.replace("frame_", "").replace(".png", "")))

print(f"Encontrados {len(frame_files)} frames")

# Criar GIF com Pillow
if len(frame_files) > 0:
    print("Criando GIF com Pillow...")
    images = []
    durations = []
    
    for file in frame_files:
        img_path = os.path.join(frame_folder, file)
        img = Image.open(img_path).convert("RGBA")
        # Adiciona data/hora no frame para garantir mudança
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("arial.ttf", 14)
        except:
            font = ImageFont.load_default()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Centralizar o texto
        text_w, text_h = draw.textsize(now, font=font)
        img_w, img_h = img.size
        x = (img_w - text_w) // 2
        y = (img_h - text_h) // 2
        # Fundo branco para contraste
        draw.rectangle([x-2, y-2, x+text_w+2, y+text_h+2], fill=(255,255,255,200))
        draw.text((x, y), now, fill=(255,0,0,255), font=font)
        images.append(img)
        durations.append(100)  # 100ms por frame para evitar piscar
    
    # Adicionar delay extra nos últimos frames para melhor visualização
    if len(durations) > 0:
        durations[-1] = 1000  # 1s no último frame
    if len(durations) > 1:
        durations[-2] = 800  # 800ms no penúltimo frame
    if len(durations) > 2:
        durations[-3] = 600  # 600ms no antepenúltimo frame
    
    # Salvar GIF
    images[0].save(
        "output.gif",
        save_all=True,
        append_images=images[1:],
        duration=durations,  # Lista com duração individual por frame
        loop=0
    )
    print(f"GIF criado com sucesso! ({len(frame_files)} frames, duração total: {sum(durations)/1000:.1f}s)")
else:
    print("Nenhum frame encontrado para criar GIF")
