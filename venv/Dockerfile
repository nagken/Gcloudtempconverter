name: Deploy to Google Cloud

on:
  push:
    branches:
      - test

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Google Cloud SDK
        uses: google-github-actions/setup-gcloud@master
        with:
          version: 'latest'
          project_id: tempconv1-389923
          service_account_key: ${{ secrets.GCLOUD_AUTH }}
          export_default_credentials: true

      - name: Configure Docker
        uses: docker/setup-docker@v1

      - name: Build and deploy
        run: |
          gcloud builds submit --tag gcr.io/tempconv1-389923/flask-app
          gcloud run deploy --image gcr.io/tempconv1-389923/tc --platform managed --region us-central1 --allow-unauthenticated --project your-project-id