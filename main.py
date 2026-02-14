from datetime import datetime
import os

import gifos
from zoneinfo import ZoneInfo
from github_stats import fetch_github_stats

FONT_FILE_LOGO = "./fonts/vtks-blocketo.regular.ttf"
# FONT_FILE_BITMAP = "./fonts/ter-u14n.pil"
FONT_FILE_BITMAP = "./fonts/gohufont-uni-14.pil"
FONT_FILE_TRUETYPE = "./fonts/IosevkaTermNerdFont-Bold.ttf"
FONT_FILE_MONA = "./fonts/Inversionz.otf"


def main():
    import os
    t = gifos.Terminal(750, 500, 15, 15, FONT_FILE_BITMAP, 15)
    
    # FORÇAR cursor desligado permanentemente
    t.toggle_show_cursor(False)
    
    # Mudar o prompt para dudupys@gifos
    t._Terminal__prompt = "\x1b[0;91mdudupys\x1b[0m@\x1b[0;93mgifos ~> \x1b[0m"
    
    # Método personalizado para mostrar prompt sem ligar cursor
    def gen_prompt_no_cursor(row_num, col_num=1, count=1):
        t.clone_frame(1)
        # FORÇAR cursor desligado antes de cada prompt
        t.toggle_show_cursor(False)
        t.gen_text(t._Terminal__prompt, row_num, col_num, count, False, False)
        # FORÇAR cursor desligado depois do prompt também
        t.toggle_show_cursor(False)
    
    t.gen_text("", 1, count=20)
    # FORÇAR cursor desligado
    t.toggle_show_cursor(False)
    year_now = datetime.now(ZoneInfo("America/Sao_Paulo")).strftime("%Y")
    t.gen_text("GIF_OS Modular BIOS v1.0.11", 1)
    t.gen_text(f"Copyright (C) {year_now}, \x1b[31mEduardo Vinícios Softwares Inc.\x1b[0m", 2)
    t.gen_text("\x1b[94mGitHub Profile ReadMe Terminal, Rev 1011\x1b[0m", 4)
    t.gen_text("Krypton(tm) GIFCPU - 250Hz", 6)
    t.gen_text(
        "Press \x1b[94mDEL\x1b[0m to enter SETUP, \x1b[94mESC\x1b[0m to cancel Memory Test",
        t.num_rows,
    )
    for i in range(0, 65653, 7168):  # 64K Memory
        t.delete_row(7)
        if i < 30000:
            t.gen_text(
                f"Memory Test: {i}", 7, count=2, contin=True
            )  # slow down upto a point
        else:
            t.gen_text(f"Memory Test: {i}", 7, contin=True)
    t.delete_row(7)
    t.gen_text("Memory Test: 64KB OK", 7, count=10, contin=True)
    t.gen_text("", 11, count=10, contin=True)

    t.clear_frame()
    t.gen_text("Initiating Boot Sequence ", 1, contin=True)
    t.gen_typing_text(".....", 1, contin=True)
    t.gen_text("\x1b[96m", 1, count=0, contin=True)  # buffer to be removed
    t.set_font(FONT_FILE_LOGO, 66)
    # Garantir cursor desligado mesmo aqui
    t.toggle_show_cursor(False)
    os_logo_text = "GIF OS"
    mid_row = (t.num_rows + 1) // 2
    mid_col = (t.num_cols - len(os_logo_text) + 1) // 2
    effect_lines = gifos.effects.text_scramble_effect_lines(
        os_logo_text, 3, include_special=False
    )
    for i in range(len(effect_lines)):
        t.delete_row(mid_row + 1)
        t.gen_text(effect_lines[i], mid_row + 1, mid_col + 1)

    t.set_font(FONT_FILE_BITMAP, 15)
    t.clear_frame()
    t.clone_frame(5)
    # FORÇAR cursor desligado
    t.toggle_show_cursor(False)
    t.gen_text("\x1b[93mGIF OS v1.0.11 (tty1)\x1b[0m", 1, count=5)
    t.gen_text("login: ", 3, count=5)
    # FORÇAR cursor desligado
    t.toggle_show_cursor(False)
    t.gen_typing_text("dudupys", 3, contin=True)
    t.gen_text("", 4, count=5)
    # FORÇAR cursor desligado
    t.toggle_show_cursor(False)
    t.gen_text("password: ", 4, count=5)
    # FORÇAR cursor desligado
    t.toggle_show_cursor(False)
    t.gen_typing_text("*********", 4, contin=True)
    # FORÇAR cursor desligado
    t.toggle_show_cursor(False)
    time_now = datetime.now(ZoneInfo("America/Sao_Paulo")).strftime(
        "%a %b %d %I:%M:%S %p %Z %Y"
    )
    t.gen_text(f"Last login: {time_now} on tty1", 6)

    gen_prompt_no_cursor(7, count=5)
    prompt_col = t.curr_col
    # Cursor já está desligado permanentemente
    t.gen_typing_text("\x1b[91mclea", 7, contin=True)
    t.delete_row(7, prompt_col)  # simulate syntax highlighting
    t.gen_text("\x1b[92mclear\x1b[0m", 7, count=3, contin=True)

    # Tentar obter dados reais da API do GitHub
    git_user_details = None
    
    try:
        user_age = gifos.utils.calc_age(3, 12, 2007)
    except:
        user_age = type('obj', (object,), {'years': 18, 'months': 2, 'days': 9})()
    
    t.clear_frame()
    
    # Tentar obter dados reais do GitHub usando token
    github_token = os.getenv('GITHUB_TOKEN')
    if github_token:
        try:
            print("Buscando dados reais do GitHub...")
            git_user_details = fetch_github_stats(github_token, "dudupys")
            print("Dados do GitHub obtidos com sucesso!")
        except Exception as e:
            print(f"Erro ao buscar dados do GitHub: {e}")
            print("Usando dados mock como fallback...")
    
    # Se não conseguir obter dados do GitHub, usa dados mock com valores reais
    if git_user_details is None:
        print("Usando dados mock...")
        class MockGitHubDetails:
            def __init__(self):
                # Dados mock para fallback
                self.user_rank = type('obj', (object,), {'level': 'Active Developer'})()
                self.total_stargazers = 11  # followers
                self.total_commits_last_year = 156  # estimativa
                self.total_pull_requests_made = 23  # estimativa
                self.pull_requests_merge_percentage = 85  # estimativa
                self.total_repo_contributions = 10  # public_repos
                self.languages_sorted = [('Python', 35), ('JavaScript', 25), ('HTML', 20), ('CSS', 15), ('TypeScript', 5)]
        git_user_details = MockGitHubDetails()
    
    top_languages = [lang[0] for lang in git_user_details.languages_sorted]
    user_details_lines = f"""
    \x1b[30;101mdudupys@GitHub\x1b[0m
    --------------
    \x1b[96mOS:     \x1b[93mWindows 11, Android 14\x1b[0m
    \x1b[96mHost:   \x1b[93mInstituto Federal do Rio Grande do Norte \x1b[94m#IFRN\x1b[0m
    \x1b[96mKernel: \x1b[93mInformática para Internet \x1b[94m#IFRN\x1b[0m
    \x1b[96mUptime: \x1b[93m{user_age.years} years, {user_age.months} months, {user_age.days} days\x1b[0m
    \x1b[96mIDE:    \x1b[93mVSCode, Cursor, Windsurf\x1b[0m
    
    \x1b[30;101mContact:\x1b[0m
    --------------
    \x1b[96mEmail:      \x1b[93meduardo.vinicios.xt1@gmail.com\x1b[0m
    \x1b[96mLinkedIn:   \x1b[93meduardo-vin%C3%ADcius-344269361\x1b[0m
    
    \x1b[30;101mGitHub Stats:\x1b[0m
    --------------
    \x1b[96mUser Rating: \x1b[93m{git_user_details.user_rank.level}\x1b[0m
    \x1b[96mTotal Stars Earned: \x1b[93m{git_user_details.total_stargazers}\x1b[0m
    \x1b[96mTotal Commits ({int(year_now) - 1}): \x1b[93m{git_user_details.total_commits_last_year}\x1b[0m
    \x1b[96mTotal PRs: \x1b[93m{git_user_details.total_pull_requests_made}\x1b[0m
    \x1b[96mMerged PR %: \x1b[93m{git_user_details.pull_requests_merge_percentage}\x1b[0m
    \x1b[96mTotal Contributions: \x1b[93m{git_user_details.total_repo_contributions}\x1b[0m
    \x1b[96mTop Languages: \x1b[93m{', '.join(top_languages[:5])}\x1b[0m
    """
    gen_prompt_no_cursor(1)
    prompt_col = t.curr_col
    t.clone_frame(10)
    # Cursor já está desligado permanentemente
    t.gen_typing_text("\x1b[91mfetch.s", 1, contin=True)
    t.delete_row(1, prompt_col)
    t.gen_text("\x1b[92mfetch.sh\x1b[0m", 1, contin=True)
    t.gen_typing_text(" -u dudupys", 1, contin=True)

    t.set_font(FONT_FILE_MONA, 16, 0)
    # Cursor já está desligado permanentemente
    monaLines = r"""
    \x1b[49m     \x1b[90;100m}}\x1b[49m     \x1b[90;100m}}\x1b[0m
    \x1b[49m    \x1b[90;100m}}}}\x1b[49m   \x1b[90;100m}}}}\x1b[0m
    \x1b[49m    \x1b[90;100m}}}}}\x1b[49m \x1b[90;100m}}}}}\x1b[0m
    \x1b[49m   \x1b[90;100m}}}}}}}}}}}}}\x1b[0m
    \x1b[49m   \x1b[90;100m}}}}}}}}}}}}}}\x1b[0m
    \x1b[49m   \x1b[90;100m}}\x1b[37;47m}}}}}}}\x1b[90;100m}}}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}}\x1b[37;47m}}}}}}}}}}\x1b[90;100m}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}}\x1b[37;47m}\x1b[90;100m}\x1b[37;47m}}}}}\x1b[90;100m}\x1b[37;47m}}\x1b[90;100m}}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}\x1b[37;47m}}\x1b[90;100m}\x1b[37;47m}}}}}\x1b[90;100m}\x1b[37;47m}}}\x1b[90;100m}}}\x1b[0m
    \x1b[90;100m}}}\x1b[37;47m}}}}\x1b[90;100m}}}\x1b[37;47m}}}}}\x1b[90;100m}}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}\x1b[37;47m}}}}}\x1b[90;100m}}\x1b[37;47m}}}}}\x1b[90;100m}}}\x1b[0m
    \x1b[49m \x1b[90;100m}}\x1b[37;47m}}}}}}}}}}}}\x1b[90;100m}}}\x1b[0m
    \x1b[90;100m}\x1b[49m  \x1b[90;100m}}\x1b[37;47m}}}}}}}}\x1b[90;100m}}}\x1b[49m  \x1b[90;100m}\x1b[0m
    \x1b[49m        \x1b[90;100m}}}}}\x1b[0m
    \x1b[49m       \x1b[90;100m}}}}}}}\x1b[0m
    \x1b[49m       \x1b[90;100m}}}}}}}}\x1b[0m
    \x1b[49m      \x1b[90;100m}}}}}}}}}}\x1b[0m
    \x1b[49m     \x1b[90;100m}}}}}}}}}}}\x1b[0m
    \x1b[49m     \x1b[90;100m}}}}}}}}}}}}\x1b[0m
    \x1b[49m     \x1b[90;100m}}\x1b[49m \x1b[90;100m}}}}}}\x1b[49m \x1b[90;100m}}\x1b[0m
    \x1b[49m        \x1b[90;100m}}}}}}}\x1b[0m
    \x1b[49m         \x1b[90;100m}}}\x1b[49m \x1b[90;100m}}\x1b[0m
    """
    t.gen_text(monaLines, 10)

    t.set_font(FONT_FILE_BITMAP)
    # Cursor já está desligado permanentemente
    # t.pasteImage("./temp/x0rzavi.jpg", 3, 5, sizeMulti=0.5)
    t.gen_text(user_details_lines, 2, 35, count=5, contin=True)
    gen_prompt_no_cursor(t.curr_row)
    t.gen_typing_text(
        "\x1b[92m# Have a nice day kind stranger :D Thanks for stopping by!",
        t.curr_row,
        contin=True,
    )
    # t.save_frame("fetch_details.png")
    t.gen_text("", t.curr_row, count=120, contin=True)

    # Método alternativo para criar GIF sem ffmpeg
    print("Criando GIF com método alternativo...")
    import os
    from PIL import Image
    
    # Verificar pasta de frames
    frame_folder = "frames"
    if not os.path.exists(frame_folder):
        os.makedirs(frame_folder)
    
    # Encontrar todos os arquivos de frame
    frame_files = []
    for file in os.listdir(frame_folder):
        if file.startswith("frame_") and file.endswith(".png"):
            frame_files.append(file)
    
    frame_files.sort()  # Ordenar por número
    
    print(f"Encontrados {len(frame_files)} frames")
    
    # Criar GIF com Pillow
    if len(frame_files) > 0:
        print("Criando GIF com Pillow...")
        images = []
        durations = []
        
        for file in frame_files:
            img_path = os.path.join(frame_folder, file)
            img = Image.open(img_path)
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
        print("GIF criado com sucesso!")
    else:
        print("Nenhum frame encontrado para criar GIF")
    # image = gifos.utils.upload_imgbb("output.gif", 129600)  # 1.5 days expiration
    readme_file_content = rf"""<div align="justify">
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="./output.gif">
    <source media="(prefers-color-scheme: light)" srcset="./output.gif">
    <img alt="GIFOS" src="output.gif">
</picture>

<sub><i>Generated automatically using [dudupys/github-readme-terminal](https://github.com/dudupys/github-readme-terminal) on {time_now}</i></sub>

<!-- <details>
<summary>More details</summary>

</details> -->
</div>

<!-- Image deletion URL: NONE -->"""
    with open("README.md", "w") as f:
        f.write(readme_file_content)
        print("INFO: README.md file generated")


if __name__ == "__main__":
    main()
