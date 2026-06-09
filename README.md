# Comparação de Traduções Bíblicas

## Visão Geral do Projeto

Este projeto em Python realiza uma **análise estatística e comparativa de diferentes traduções bíblicas**, com um foco inicial na **Almeida Revista e Corrigida (ARC)** e na **Nova Versão Transformadora (NVT)**. O objetivo principal é identificar padrões de linguagem, palavras exclusivas e o nível de similaridade entre versículos, fornecendo insights valiosos sobre as nuances de cada tradução. Além de seu propósito analítico, o projeto serve como uma plataforma para o desenvolvimento de habilidades em **manipulação de dados, processamento de linguagem natural (PLN) e visualização de dados**.

## Funcionalidades

O projeto oferece as seguintes funcionalidades:

*   **Carregamento Dinâmico de Traduções:** Carrega dados de traduções bíblicas a partir de arquivos JSON, permitindo fácil expansão para novas versões.
*   **Pré-processamento de Texto:** Limpeza e normalização de versículos para análise consistente.
*   **Tokenização e Análise Lexical:** Utiliza a biblioteca `spaCy` para tokenização, remoção de *stopwords* e pontuação, gerando listas de tokens relevantes para cada versículo.
*   **Contagem de Palavras:** Quantifica a frequência de palavras em cada tradução para identificar termos dominantes.
*   **Identificação de Palavras Exclusivas:** Destaca palavras que aparecem predominantemente em uma tradução em comparação com outra, revelando características lexicais distintas.
*   **Análise de Similaridade Semântica:** Emprega modelos de *Sentence Transformers* (`paraphrase-multilingual-MiniLM-L12-v2`) e `cosine_similarity` para medir a semelhança entre versículos correspondentes de diferentes traduções.
*   **Geração de Gráficos:** Produz diversas visualizações para apresentar os resultados da análise de forma clara e intuitiva, utilizando `Matplotlib` e `Seaborn`.

## Tecnologias Utilizadas

*   **Python:** Linguagem de programação principal.
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
├── definições.txt
├── funcoes.py
├── funcoesGraficos.py
├── main.py
├── processamento.py
└── traducoes/
    ├── ARC.json
    ├── NAA.json
    ├── NTLH.json
    ├── NVI.json
    └── NVT.json
```

*   `main.py`: Ponto de entrada do programa, orquestra o fluxo de execução.
*   `processamento.py`: Contém a lógica para carregar dados, organizar livros, realizar análises e chamar as funções de geração de gráficos.
*   `funcoes.py`: Implementa funções auxiliares para manipulação de texto, tokenização, contagem de palavras e cálculo de similaridade.
*   `funcoesGraficos.py`: Responsável pela criação e salvamento dos gráficos gerados.
*   `traducoes/`: Diretório contendo os arquivos JSON das diferentes traduções bíblicas.

## Como Executar o Projeto

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
    pip install -r requirements.txt # Será necessário criar este arquivo com as dependências
    ```
    *Nota: As dependências incluem `spacy`, `sentence-transformers`, `scikit-learn`, `pandas`, `matplotlib`, `seaborn`.* Você pode gerar o `requirements.txt` com `pip freeze > requirements.txt` após instalar as bibliotecas.

4.  **Baixe o modelo spaCy para português:**

    ```bash
    python -m spacy download pt_core_news_sm
    ```

5.  **Crie a pasta para os gráficos:**

    ```bash
    mkdir graficos
    ```

6.  **Execute o script principal:**

    ```bash
    python main.py
    ```

    O programa solicitará que você insira as abreviações das duas traduções que deseja comparar (ex: `ARC`, `NVT`). Os gráficos gerados serão salvos na pasta `graficos/`.

## Visualizações Geradas

O projeto gera os seguintes tipos de gráficos para cada par de traduções e livro analisado:

*   **Histograma de Similaridade:** Mostra a distribuição dos níveis de similaridade entre os versículos, com indicação da média e mediana.
*   **Gráfico de Linhas (Quantidade de Palavras):** Compara a quantidade de palavras por versículo (ou média por capítulo para livros longos) entre as duas traduções.
*   **Heatmap de Divergência:** Um mapa de calor que visualiza a similaridade entre versículos por capítulo, destacando áreas de maior ou menor concordância.
*   **Gráfico de Barras (Versículos Mais Divergentes):** Apresenta os versículos com menor similaridade por capítulo, indicando pontos de maior diferença entre as traduções.
*   **Gráfico de Barras (Palavras Exclusivas):** Exibe as palavras mais frequentes e exclusivas de cada tradução, revelando seu vocabulário característico.

## Próximos Passos e Roadmap

O projeto possui um roadmap ambicioso, incluindo:

*   **Expansão da Base de Dados:** Incorporar mais traduções e versões da Bíblia para análises mais abrangentes.
*   **Refinamento da Análise Semântica:** Explorar modelos de PLN mais avançados para uma compreensão mais profunda das diferenças de significado.
*   **Desenvolvimento de IA para Classificação:** O objetivo de longo prazo é treinar um modelo de Inteligência Artificial capaz de identificar a tradução de um texto bíblico com base em suas características linguísticas.
*   **Interface Gráfica:** Desenvolver uma interface de usuário para facilitar a interação com o projeto e a visualização dos resultados.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir *issues* para sugestões de melhoria, relatar *bugs* ou enviar *pull requests* com novas funcionalidades.

## Autor

**Felipe Soares**

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes. (Assumindo licença MIT, caso contrário, ajustar.)
