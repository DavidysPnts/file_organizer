# file_organizer
  Script em Python que organiza arquivos em subpastas com base em suas extensões.

- Descrição  
  Este projeto organiza arquivos de uma pasta, movendo-os para subpastas como "Imagens", "Documentos", "Músicas", "Vídeos" e "Outros", com base em suas extensões.

- Funcionalidades
  1. Cria pastas automaticamente por categoria;
  2. Move arquivos para a pasta correta com base na extensão;
  3. Garante que arquivos com nomes duplicados não sejam sobrescritos;
  4. Organiza apenas arquivos dentro de uma pasta alvo.

- Melhorias Futuras
  1. Detectar tipo de arquivo pelo conteúdo real usando `mimetypes` ou `python-magic`;
  2. Adicionar registro de logs e função para desfazer a organização;
  3. Criação de uma interface gráfica.

- Observação  
  A classificação é feita apenas por extensão. Contêineres como .mp4 podem conter apenas áudio ou vídeo; o script coloca .mp4 em Vídeos por convenção.
  
- Contribuição  
  Para recomendações de melhorias e reclamações: davidys.pontes@icloud.com
