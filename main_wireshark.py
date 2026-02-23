import pandas as pd
import ollama

def report_wireshark(caminho_csv):
    try:
        df = pd.read_csv(caminho_csv)
    except Exception as e:
        return f"Erro ao ler arquivo: {e}"

    # 2. Conversão do DataFrame para String (Contexto para o modelo)
    # Transformamos o CSV em uma string formatada para o modelo entender
    contexto_dados = df.to_string(index=False)

    prompt = f"""
    Você é um especialista em segurança de redes. 
    Analise os seguintes logs de tráfego (Wireshark) e interprete os comportamentos dos fluxos de comunicação:
    
    {contexto_dados}
    
    Responda em português, focando em:
    •	Identificação do tipo de comunicação
    •	Explicação do objetivo do quadro
    •	Relação com conceitos da camada de enlace
    """

    try:
        response = ollama.chat(model='llama3', messages=[
            {
                'role': 'user',
                'content': prompt,
            },
        ])
        return response['message']['content']
    except Exception as e:
        return f"Erro na análise: {e}"

relatorio_wireshark = report_wireshark('wireshark.csv')

print("\n" + "="*60)
print(relatorio_wireshark)
print("="*60)