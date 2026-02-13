Write-Host "Creating RAG project structure..."

New-Item -ItemType Directory -Force -Path app
New-Item -ItemType Directory -Force -Path data
New-Item -ItemType Directory -Force -Path scripts

New-Item app/__init__.py -ItemType File -Force
New-Item app/config.py -ItemType File -Force
New-Item app/ingestion.py -ItemType File -Force
New-Item app/retrieval.py -ItemType File -Force
New-Item app/llm.py -ItemType File -Force
New-Item app/rag.py -ItemType File -Force
New-Item app/main.py -ItemType File -Force

New-Item requirements.txt -ItemType File -Force
New-Item .env -ItemType File -Force
New-Item .gitignore -ItemType File -Force
New-Item README.md -ItemType File -Force

Write-Host "Structure created successfully!"
