# Twitter Web Crawler

Análise de Sentimentos usando a nova API 2.0 do Twitter, Flask, Jinja2, Pandas e Plotly.

O projeto usa como algoritmo de análise de sentimentos o Sentipt, um fork do "LeIa", uma versão preliminar em português do consagrado "Vader", muito utilizado para língua inglesa.

https://github.com/FelipeNSantos/sentipt  (em desenvolvimento, instalação local apenas)

O projeto consiste em:

## app.py

A estrutura no Flask utiliza o conceito de 'factoring' no app principal, para evitar loops de dependência e facilitar a integração de novas features.

 Importação do Bearer Token para uso da API V2 do twitter (necessita conta de desenvolvedor) como variável de ambiente usando armazenamento seguro em um arquivo .env.

## apiv2.py

Requisição dos 100 tweets mais recentes em português utilizando o termo de busca escolhido (pode ser uma expressão com mais de uma palavra). Limpeza automática dos tweets e gravação do resultado em arquivo csv temporário.

## process.py

Análise de sentimentos dos tweets (o algoritmo do Sentipt internamente inclui tokenização, treino com um corpus etiquetado e classificação). Plotagem do grafico de resultado em estilo "donut", adequado a esse tipo de análise, inserido em uma sub-página html a ser inserida na página de resultado após processamento e renderização. Abertura da página de resultado.

## TODO

Aperfeiçoamento do frontend, ainda muito simplório, para algo melhor em termos de storytelling, citando amostras de tweets. Aperfeiçoamento do Sentipt, que se mostra pouco sensível, com alta porcentagem de classificação neutra mesmo sobre termos que envolvem polêmica.
