"""
Módulo para gerar seção About Me em estilo terminal para README.md
"""

def generate_about_me_section():
    """
    Gera a seção About Me em estilo terminal
    
    Returns:
        str: Seção About Me formatada em Markdown
    """
    # Configurações personalizáveis
    USERNAME = "dudupys"
    DISPLAY_NAME = "Dudu"
    ABOUT_TEXT = "💻 Desenvolvedor de Sistemas em formação\n🤖 Interesse em Automação, Inteligência Artificial e Desenvolvimento de Software\n🎓 Estudante de Informática para Internet\n📚 Projetos em Tecnologia Educacional"
    
    about_me_content = f"""```bash
$ whoami
{DISPLAY_NAME} (@{USERNAME})

$ echo "About me"
{ABOUT_TEXT}
```"""
    
    return about_me_content


if __name__ == "__main__":
    # Teste do módulo
    print("About Me Section:")
    print(generate_about_me_section())
