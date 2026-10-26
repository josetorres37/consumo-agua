# Meus Sites Favoritos 🌐

Projeto desenvolvido como atividade prática da **Agenda 12 - Desenvolvimento de Sistemas I**. O objetivo principal é criar uma página web estruturada de forma semântica em HTML5 para catalogar e acessar de forma rápida as plataformas mais utilizadas no dia a dia para lazer, estudos e trabalho.

## 🚀 Funcionalidades e Requisitos Atendidos
- **Título Personalizado:** Configuração correta da tag `<title>` para a aba do navegador.
- **Cabeçalho Identificado:** Título principal (`<h1>`) no corpo da página identificando o aluno **JOSE FLAVIO TORRES**.
- **Catálogo de Favoritos:** Listagem de 5 sites contendo:
  - Nome do site acima da imagem em destaque.
  - Imagem do site armazenada e carregada localmente.
  - Link de redirecionamento logo abaixo da imagem.
- **Navegabilidade:** Todos os links abrem em uma nova aba do navegador utilizando o atributo `target="_blank"`.
- **Acessibilidade:** Uso do atributo `alt` em todas as imagens para descrição textual.

## 🛠️ Tecnologias e Boas Práticas Utilizadas
- **HTML5 Semântico:** Divisão estrutural organizada com as tags `<header>`, `<main>`, `<section>`, `<figure>`, `<figcaption>` e `<footer>`, garantindo melhor leitura por leitores de tela e robôs de busca (SEO).
- **Estruturação de Caminhos Locais:** Armazenamento das imagens em subpasta dedicada (`./imagens/`), utilizando caminhos relativos de forma segura para evitar quebras de carregamento.
- **Código Comentado:** Documentação interna detalhando o funcionamento das tags essenciais.

## 📂 Estrutura do Projeto
```text
jose_Ag12_DS_I/
│
├── imagens/                # Pasta contendo os logotipos locais
│   ├── webdev.png
│   ├── youtube.png
│   ├── wikipedia.png
│   ├── github.png
│   └── w3schools.png
│
├── index.html              # Código-fonte principal do site
└── README.md               # Documentação do repositório
```

## ⚙️ Como Executar o Projeto
1. Faça o download ou clone este repositório.
2. Certifique-se de manter a pasta `imagens` no mesmo diretório do arquivo `index.html`.
3. Dê um duplo clique no arquivo `index.html` para abri-lo diretamente em qualquer navegador web de sua preferência (Google Chrome, Microsoft Edge, Mozilla Firefox, etc.).
