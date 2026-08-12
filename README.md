# Retrospectiva Animada — página de vendas Flask

Landing page responsiva para apresentação e venda do curso Retrospectiva Animada.

## Como executar

1. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Inicie o site:

   ```bash
   python app.py
   ```

4. Abra `http://127.0.0.1:5000` no navegador.

O link de checkout da Hotmart e o ID do vídeo do YouTube ficam no início de `app.py` para facilitar futuras alterações.

No Windows, você também pode executar `iniciar.bat`; ele cria o ambiente, instala as dependências e inicia o site automaticamente.

## Produção

Em um servidor Linux, execute:

```bash
gunicorn app:app
```

O arquivo `Procfile` já contém esse comando para plataformas compatíveis.
