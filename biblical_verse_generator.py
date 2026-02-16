"""
Módulo para gerar mensagem bíblica do dia de forma determinística
"""

import os
from datetime import datetime


def load_verses(file_path="versiculos_biblicos.txt"):
    """
    Carrega versículos bíblicos do arquivo local
    
    Args:
        file_path (str): Caminho para o arquivo de versículos
        
    Returns:
        list: Lista de versículos como dicionários
    """
    verses = []
    
    if not os.path.exists(file_path):
        print(f"Arquivo de versículos não encontrado: {file_path}")
        return verses
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line and '|' in line:
                    parts = line.split('|')
                    if len(parts) >= 4:
                        verse = {
                            'book': parts[0].strip(),
                            'chapter': parts[1].strip(),
                            'verse': parts[2].strip(),
                            'text': parts[3].strip()
                        }
                        verses.append(verse)
    except Exception as e:
        print(f"Erro ao carregar versículos: {e}")
    
    return verses


def get_daily_verse():
    """
    Seleciona o versículo do dia de forma determinística
    
    Returns:
        dict: Versículo do dia ou None se não houver versículos
    """
    verses = load_verses()
    
    if not verses:
        return None
    
    # Calcula o dia do ano (1-366)
    current_date = datetime.now()
    day_of_year = current_date.timetuple().tm_yday
    
    # Seleciona versículo de forma determinística
    verse_index = day_of_year % len(verses)
    selected_verse = verses[verse_index]
    
    return selected_verse


def generate_biblical_verse_section():
    """
    Gera a seção de versículo bíblico do dia
    
    Returns:
        str: Seção do versículo formatada em Markdown
    """
    verse = get_daily_verse()
    
    if not verse:
        return "📖 Versículo do dia\n\n*Versículo não disponível no momento.*"
    
    verse_content = f"""📖 Versículo do dia

"{verse['text']}"

— {verse['book']} {verse['chapter']}:{verse['verse']}"""
    
    return verse_content


if __name__ == "__main__":
    # Teste do módulo
    print("Biblical Verse Section:")
    print(generate_biblical_verse_section())
