#!/usr/bin/env python3
"""Script para testar a integração com a API do GitHub"""

import os
from github_stats import fetch_github_stats

def test_github_integration():
    """Testa a busca de dados do GitHub"""
    
    # Substitua pelo seu token real
    github_token = "seu_token_aqui"  # OU use variável de ambiente
    
    # Se não tiver variável de ambiente, peça ao usuário
    if not github_token or github_token == "seu_token_aqui":
        github_token = input("Digite seu token do GitHub (gif-generation): ").strip()
    
    if not github_token:
        print("❌ Token não fornecido. Não é possível testar.")
        return
    
    print("🔍 Testando integração com a API do GitHub...")
    print(f"📱 Token: {github_token[:10]}...{github_token[-4:]}")
    
    try:
        # Buscar estatísticas
        stats = fetch_github_stats(github_token, "dudupys")
        
        print("\n✅ Dados obtidos com sucesso!")
        print("\n📊 Estatísticas do GitHub:")
        print(f"   • Nível: {stats.user_rank.level}")
        print(f"   • Seguidores: {stats.total_stargazers}")
        print(f"   • Commits (último ano): {stats.total_commits_last_year}")
        print(f"   • Pull Requests: {stats.total_pull_requests_made}")
        print(f"   • Taxa de Merge: {stats.pull_requests_merge_percentage}%")
        print(f"   • Repositórios: {stats.total_repo_contributions}")
        print(f"   • Linguagens Top 5: {', '.join([lang[0] for lang in stats.languages_sorted[:5]])}")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Erro ao buscar dados: {e}")
        print("\n🔧 Possíveis soluções:")
        print("   1. Verifique se o token está correto")
        print("   2. Verifique se o token tem permissões suficientes")
        print("   3. Verifique sua conexão com a internet")
        return False

def show_token_instructions():
    """Mostra instruções sobre como usar o token"""
    print("\n📋 Como configurar seu token:")
    print("   1. Vá para GitHub > Settings > Developer settings > Personal access tokens")
    print("   2. Gere um novo token com as permissões:")
    print("      - public_repo (acesso a repositórios públicos)")
    print("      - read:user (ler informações do perfil)")
    print("   3. Copie o token e use neste script ou configure como variável de ambiente:")
    print("      export GITHUB_TOKEN=seu_token_aqui")
    print("   4. No GitHub Actions, adicione nos secrets:")
    print("      GITHUB_TOKEN: seu_token_aqui")

if __name__ == "__main__":
    show_token_instructions()
    print("\n" + "="*50)
    test_github_integration()
