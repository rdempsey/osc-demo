# How to Integrate Natural Language Processing and Elasticsearch for Better Analytics



## Amazon Comprehend

A fully managed and continously trained service that helps you analyze and organize unstructured text.



### APIs

* Sentiment: positive/negative/neutral/mixed
* Entity extraction: proper nouns
* Key phrases: common noun extractor
* Languages: over 100 unique languages (the rest of the APIs support English and Spanish docs)
* Topic Modeling: uses LDA to create topics across a corpus
* Syntax (newer): fine-grained analysis of sentence semantics, extract tokens and punctuation, and POS tagging



### Example Use: High-Fidelity Text Analysis (Comments)

1. Sentiment = negative.
2. Entity = brand/product/noun mentioned
3. Syntax =  get the descriptive words used



###  Comprehend Use Cases

* Analyze user-generated content and gain insight into what's being said.
* Analyze content, understand the sentiment, and identify common themes => later tag other content based on what's been learned.
* Tag entities with a high-confidence



### Comprehend Opportunities

* News media: brand trends, correlating events
* Increase customer engagement: call center, automatic issue triage, social media analytics
* Records and research: actionable document-centric processes, understand patterns



**Increase the signal of your unstructured data.**



### Pricing

* 50k units of text/month: Free
* 1 unit of text: $0.0001



### Popular AWS Text Analytics Use Cases

* Content personaliztion
* Semantic search (we'll look at this today)
* Intelligent data warehouse
* Social analytics



## A Few Stories...



### Transform a Call Center

Imagine if you will...

- Person calls into a call center with an issue.
- Agent types in what they're saying, it's transcribed on the fly.
- Perform sentiment analysis, entity extraction, etc to understand how the customer feels and what they're talking about.
- Do a search to find the best solution
- Present the solution to the call center agent



### Or Let's Say You Need to Be Able To Search a Ton of Academic Papers...

* Enrich each document with sentiment, entity extraction, key phrases, topic modeling, and syntax analysis.
* Store the documents in ES.
* Provide a much deeper experience to the user via Kibana as she can now filter by sentiment, entities, etc.



