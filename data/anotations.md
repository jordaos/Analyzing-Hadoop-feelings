# Algumas anotações

## Adicionei para chegar nos meus resultados
- Adicionei "fix*" com peso +3 no dicionário do SentiStrenght

## Baixar release para análise:
- `git clone -b <branch> --single-branch <remote_repo>`

## Releases:
- [Primeira](https://github.com/apache/hadoop/tree/release-0.1.0)
- [Segunda](https://github.com/apache/hadoop/tree/release-0.1.1)
- [Terceira](https://github.com/apache/hadoop/tree/release-0.2.0)

## JDeodorant
In JDeodorant analyzes, I ignore all errors in the eclipse of the hadoop project

## Classificação com NB
Para as classificações com Naive Bayes foi usado NLTK

## Classificação com SS
### Sem filtros
Tem que usar `sentistrenght_data/EmotionLookupTable-old`, que é o que contem todas as palavras de SentiStrength.

Além disso, quando for executar `src/from-sqlite-to-file-ss.py` não filtrar a mensagem (função `remove_URLs_informations`)
### Com filtros (*)
Usa o `EmotionLookupTable-new.txt` que foi gerado pela execução de `src/filter-wordlist.py`. E filtrar as mensagens com `remove_URLs_informations` em `src/from-sqlite-to-file-ss.py`