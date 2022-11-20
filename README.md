# random-quiz

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
