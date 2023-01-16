# random-quiz

[![build](https://img.shields.io/github/actions/workflow/status/nalbam/random-quiz/push.yml?branch=main&style=for-the-badge&logo=github)](https://github.com/nalbam/random-quiz/actions/workflows/push.yml)
[![release](https://img.shields.io/github/v/release/nalbam/random-quiz?style=for-the-badge&logo=github)](https://github.com/nalbam/random-quiz/releases)

## requirements

```bash
pip3 install --upgrade -r requirements.txt
```

## fastapi

```bash
uvicorn src.main:app --reload
```

## put-item

```bash
CODE="nXJcDtPj1VM"
NAME="서태지와 아이들(Seo Taiji and Boys)"
TITLE="하여가 (Hayeoga)"

aws dynamodb put-item --table-name random-quiz \
 --item "{\"id\":{\"S\":\"$CODE\"},\"type\":{\"S\":\"music\"},\"code\":{\"S\":\"$CODE\"},\"name\":{\"S\":\"$NAME\"},\"title\":{\"S\":\"$TITLE\"}}"

```
