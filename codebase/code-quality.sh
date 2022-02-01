!#/bin/bash

sonar-scanner \
  -Dsonar.projectKey=Afr_tagging \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=f639c9ee69e9de397b1f2e9e3e233e72bf63d2cd
