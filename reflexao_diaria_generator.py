"""
Módulo para gerar reflexão diária de forma determinística
"""

import os
from datetime import datetime


def load_reflexoes(file_path="reflexoes_diarias.txt"):
    """
    Carrega reflexões diárias do arquivo local
    
    Args:
        file_path (str): Caminho para o arquivo de reflexões
        
    Returns:
        list: Lista de reflexões como dicionários
    """
    reflexoes = []
    
    if not os.path.exists(file_path):
        print(f"Arquivo de reflexões não encontrado: {file_path}")
        return reflexoes
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line and '|' in line:
                    parts = line.split('|', 1)  # Divide apenas na primeira ocorrência
                    if len(parts) == 2:
                        reflexao = {
                            'texto': parts[0].strip(),
                            'autor': parts[1].strip() if parts[1].strip() else None
                        }
                        reflexoes.append(reflexao)
    except Exception as e:
        print(f"Erro ao carregar reflexões: {e}")
    
    return reflexoes


def get_daily_reflexao():
    """
    Seleciona a reflexão do dia de forma determinística
    
    Returns:
        dict: Reflexão do dia ou None se não houver reflexões
    """
    reflexoes = load_reflexoes()
    
    if not reflexoes:
        return None
    
    # Calcula o dia do ano (1-366)
    current_date = datetime.now()
    day_of_year = current_date.timetuple().tm_yday
    
    # Seleciona reflexão de forma determinística
    reflexao_index = day_of_year % len(reflexoes)
    selected_reflexao = reflexoes[reflexao_index]
    
    return selected_reflexao


def generate_reflexao_diaria_section():
    """
    Gera a seção de reflexão diária em estilo terminal
    
    Returns:
        str: Seção da reflexão formatada em Markdown
    """
    reflexao = get_daily_reflexao()
    
    if not reflexao:
        return "```bash\n$ echo \"Daily Reflection\"\n*Reflection not available at the moment.*\n```"
    
    # Formata no estilo terminal CLI como o About Me
    if reflexao['autor']:
        reflexao_content = f"""```bash
$ echo "Daily Reflection"
{reflexao['texto']}

— {reflexao['autor']}
```"""
    else:
        reflexao_content = f"""```bash
$ echo "Daily Reflection"
{reflexao['texto']}
```"""
    
    return reflexao_content


if __name__ == "__main__":
    # Teste do módulo
    print("Reflexão Diária Section:")
    print(generate_reflexao_diaria_section())
