# ExtractTag

Action GitHub (Docker) qui exporte le SHA du commit courant dans la variable d'environnement `TAG` pour les steps suivants du workflow.

## Prérequis

L'action doit être utilisée **après** `actions/checkout` pour que le dépôt soit présent dans le conteneur.

## Usage

### Dans le même dépôt

```yaml
- uses: actions/checkout@v4
- uses: ./
- run: echo "Commit SHA: $TAG"
```

### Depuis un autre dépôt (après publication)

```yaml
- uses: actions/checkout@v4
- uses: ValoriaTechnologia/ExtractTag@v1   # ou @main
- run: echo "Commit SHA: $TAG"
```

## Détails techniques

- **Type** : action Docker (non composite)
- **Image** : Python 3.12 Alpine + Git
- **Comportement** : exécute `git rev-parse HEAD` dans le workspace monté (`/github/workspace`) et écrit `TAG=<sha>` dans `GITHUB_ENV`
- **Inputs** : aucun
- **Sortie** : variable d'environnement `TAG` (disponible dans les steps suivants du même job)

## Exemple de workflow complet

```yaml
name: Test ExtractTag Action

on:
  push:
    branches: [main]

jobs:
  test-extract-tag:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: ExtractTag
        uses: ./

      - name: Verify TAG hash
        run: |
          expected=$(git rev-parse HEAD)
          echo "Expected: $expected"
          echo "TAG:      $TAG"
          if [ "$TAG" != "$expected" ]; then
            echo "::error::TAG mismatch: expected $expected, got $TAG"
            exit 1
          fi
          echo "::notice::TAG correctly set to $TAG"
```

## Référence

[ValoriaTechnologia/ExtractTag](https://github.com/ValoriaTechnologia/ExtractTag)
