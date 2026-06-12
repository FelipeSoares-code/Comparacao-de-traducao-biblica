# Comparação de Traduções Bíblicas

## Visão Geral do Projeto

Este projeto em Python oferece uma **plataforma interativa para análise estatística e comparativa de diversas traduções bíblicas**. Com foco em identificar padrões de linguagem, palavras exclusivas e o nível de similaridade semântica entre versículos, o projeto fornece insights aprofundados sobre as nuances de cada versão. Inicialmente focado na **Almeida Revista e Corrigida (ARC)** e na **Nova Versão Transformadora (NVT)**, o sistema agora suporta uma gama expandida de traduções, permitindo aos usuários comparar qualquer par disponível. Além de seu valor analítico, o projeto serve como um excelente portfólio para demonstrar habilidades em **manipulação de dados, processamento de linguagem natural (PLN), visualização de dados e desenvolvimento de interfaces gráficas (GUI) com Streamlit**.

## Funcionalidades

O projeto oferece as seguintes funcionalidades aprimoradas:

*   **Interface Gráfica Intuitiva (Streamlit):** Uma aplicação web amigável que permite aos usuários selecionar traduções e livros bíblicos para análise de forma interativa.
*   **Carregamento Dinâmico de Traduções:** Suporte para múltiplas traduções bíblicas carregadas a partir de arquivos JSON, as traduções disponíveis até o momento são: **ACF, ALM1911, ARA, KJA, KJF ARC, NAA, NTLH, NVI e NVT**. Os usuários podem escolher **qualquer combinação de duas traduções** para comparação.
*   **Pré-processamento de Texto:** Limpeza e normalização de versículos para garantir consistência na análise.
*   **Tokenização e Análise Lexical:** Utiliza a biblioteca `spaCy` para tokenização, remoção de *stopwords* e pontuação, gerando listas de tokens relevantes para cada versículo.
*   **Contagem de Palavras:** Quantifica a frequência de palavras em cada tradução para identificar termos dominantes.
*   **Identificação de Palavras Exclusivas:** Destaca palavras que aparecem predominantemente em uma tradução em comparação com outra, revelando características lexicais distintas.
*   **Análise de Similaridade Semântica:** Emprega modelos de *Sentence Transformers* (`paraphrase-multilingual-MiniLM-L12-v2`) e `cosine_similarity` para medir a semelhança entre versículos correspondentes de diferentes traduções.
*   **Geração de Gráficos:** Produz diversas visualizações para apresentar os resultados da análise de forma clara e intuitiva, utilizando `Matplotlib` e `Seaborn`. Os gráficos são gerados e exibidos diretamente na interface Streamlit, além de serem salvos localmente.

## Tecnologias Utilizadas

*   **Python:** Linguagem de programação principal.
*   **Streamlit:** Para o desenvolvimento da interface gráfica interativa.
*   **spaCy:** Para processamento de linguagem natural (tokenização, remoção de *stopwords*).
*   **Sentence Transformers:** Para geração de embeddings de sentenças e cálculo de similaridade semântica.
*   **scikit-learn:** Para cálculo de similaridade de cosseno.
*   **Pandas:** Para manipulação e análise de dados estruturados.
*   **Matplotlib:** Para criação de gráficos estáticos.
*   **Seaborn:** Para visualizações estatísticas aprimoradas.

## Estrutura do Projeto

```
. 
├── README.md
├── app.py
├── funcoes.py
├── funcoesGraficos.py
├── main.py
├── processamento.py
├── requirements.txt
├── runtime.txt
└── traducoes/
    ├── ACF.json
    ├── ALM1911.json
    ├── ARA.json
    ├── ARC.json
    ├── KJA.json
    ├── KJF.json
    ├── NAA.json
    ├── NTLH.json
    ├── NVI.json
    └── NVT.json
```

*   `app.py`: O arquivo principal da aplicação Streamlit, que orquestra a interface e a interação do usuário.
*   `main.py`: Contém a lógica central de execução da análise quando não utilizada via Streamlit.
*   `processamento.py`: Contém a lógica para carregar dados, organizar livros, realizar análises e chamar as funções de geração de gráficos.
*   `funcoes.py`: Implementa funções auxiliares para manipulação de texto, tokenização, contagem de palavras e cálculo de similaridade.
*   `funcoesGraficos.py`: Responsável pela criação e salvamento dos gráficos gerados.
*   `traducoes/`: Diretório contendo os arquivos JSON das diferentes traduções bíblicas, incluindo as novas adições.
*   `requirements.txt`: Lista as dependências do projeto para fácil instalação.

## Como Executar o Projeto

para exceutar o projeto pela web, sem baixar nada, acesse: https://comparacao-traducao-biblica.streamlit.app/

Para configurar e executar este projeto localmente, siga os passos abaixo:

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/FelipeSoares-code/Comparacao-de-traducao-biblica.git
    cd Comparacao-de-traducao-biblica
    ```

2.  **Crie um ambiente virtual (recomendado):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Baixe o modelo spaCy para português:**

    ```bash
    python -m spacy download pt_core_news_sm
    ```

5.  **Execute a aplicação Streamlit:**

    ```bash
    streamlit run app.py
    ```

    A aplicação será aberta em seu navegador padrão, permitindo que você selecione as traduções e livros para análise e visualize os resultados interativamente. Os gráficos gerados também serão salvos na pasta `graficos/`.

## Visualizações Geradas

O projeto gera os seguintes tipos de gráficos para cada par de traduções e livro analisado, exibidos na interface Streamlit e salvos localmente:

*   **Histograma de Similaridade:** Mostra a distribuição dos níveis de similaridade entre os versículos, com indicação da média e mediana.
*   **Gráfico de Linhas (Quantidade de Palavras):** Compara a quantidade de palavras por versículo (ou média por capítulo para livros longos) entre as duas traduções.
*   **Heatmap de Divergência:** Um mapa de calor que visualiza a similaridade entre versículos por capítulo, destacando áreas de maior ou menor concordância.
*   **Gráfico de Barras (Versículos Mais Divergentes):** Apresenta os versículos com menor similaridade por capítulo, indicando pontos de maior diferença entre as traduções.
*   **Gráfico de Barras (Palavras Exclusivas):** Exibe as palavras mais frequentes e exclusivas de cada tradução, revelando seu vocabulário característico.

## Próximos Passos e Roadmap

O projeto possui um roadmap ambicioso, incluindo:

*   **Expansão Contínua da Base de Dados:** Incluir na análise livros do antigo testamento para análises mais abrangentes.
*   **Refinamento da Análise Semântica:** Explorar modelos de PLN mais avançados para uma compreensão mais profunda das diferenças de significado.
*   **Desenvolvimento de IA para Classificação:** O objetivo de longo prazo é treinar um modelo de Inteligência Artificial capaz de identificar a tradução de um texto bíblico com base em suas características linguísticas.
*   **Otimização de Performance:** Melhorar a velocidade de processamento para análises de grandes volumes de dados.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir *issues* para sugestões de melhoria, relatar *bugs* ou enviar *pull requests* com novas funcionalidades.

## Autor

**Felipe Soares**

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
