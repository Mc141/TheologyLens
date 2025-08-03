# TheologyLens – AI-Powered Scripture Search

---

## Overview

**TheologyLens** is a semantic scripture search engine designed to understand the meaning behind your queries, not just match keywords. Leveraging natural language embeddings, clustering, and vector similarity, it surfaces relevant Bible verses based on concept and context.

This project was built as a learning experiment in AI/NLP techniques, with a focus on practical performance tuning and deep semantic matching.

---

## Features

* **Semantic Search** – Understands the *meaning* of questions
* **Embeddings via SentenceTransformers** – Converts verses and queries into numerical form
* **FAISS Similarity Search** – Fast vector similarity matching
* **Clustering Optimization** – Uses KMeans to search within relevant groups only
* **React Frontend** – Clean, responsive user interface
* **FastAPI Backend** – Python backend with pre-computed embeddings
* **Subsecond Inference** – Queries return in under 1 second using cluster-narrowed search

---

## Tech Stack

### Backend

* **FastAPI** – Python web framework
* **SentenceTransformers** – Embedding engine
* **FAISS** – Vector similarity search
* **scikit-learn** – KMeans clustering
* **Python 3.8+**

### Frontend

* **React** – UI framework
* **CSS** – Styling

---

## How It Works

1. User enters a natural-language query (e.g. “What does the Bible say about justice?”)
2. The query is embedded using a SentenceTransformer model
3. The embedding is matched to the closest KMeans cluster (pre-trained over verse embeddings)
4. Semantic search (FAISS) is performed only within the selected cluster
5. Top results are returned as relevant scripture passages

This reduces search from over 31,000 verses to \~300 per query, cutting runtime from 40s to <1s.

---

## Performance Optimization

* All 31,000+ verses were embedded once and clustered into semantic groups using **KMeans**
* Each query is first matched to a cluster
* Search happens only within that cluster using FAISS
* Tradeoff: negligible loss in recall, **massive** gain in speed

> Result: Subsecond responses, even on CPU-only servers

---

## Repository Structure

This repository only contains the scripts used to **generate and cluster the verse embeddings**.

Related repos:

* **Frontend:** [`TheologyLens-frontend`](https://github.com/Mc141/TheologyLens-frontend) – React-based search UI
* **Backend API:** [`TheologyLens-backend`](https://github.com/Mc141/TheologyLens-backend) – FastAPI serving semantic results
* **Embeddings + Indexing:** (this repo) – Scripts to build verse vectors and KMeans clusters

---

## Example Queries and Scriptural Insights

Due to the large dependency and embedding file size, the full app is not deployed live. Below are example queries and what TheologyLens returns:

---

### Prompt: **"What does the Bible say about justice?"**

| Reference      | Verse                                                                                             | Relevance                                                                |
| -------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Amos 5:24      | *"But let justice roll on like rivers, and righteousness like a mighty stream."*                  | A foundational verse on God's call for continuous, overflowing justice.  |
| Proverbs 21:15 | *"It is joy to the righteous to do justice; but it is a destruction to the workers of iniquity."* | Highlights the joy justice brings to the righteous and judgment to evil. |
| Luke 18:6      | *"The Lord said, 'Listen to what the unrighteous judge says.'"*                                   | Part of Jesus' parable emphasizing persistence and divine justice.       |
| Isaiah 32:16   | *"Then justice will dwell in the wilderness..."*                                                  | Prophetic vision of a society filled with justice and righteousness.     |
| Proverbs 28:5  | *"Evil men don't understand justice; but those who seek Yahweh understand it fully."*             | Draws a link between spiritual insight and moral clarity.                |

---

### Prompt: **"Where in the Bible does it talk about forgiveness?"**

| Reference    | Verse                                                                                      | Relevance                                                       |
| ------------ | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| Mark 11:26   | *"If you do not forgive, neither will your Father in heaven forgive your transgressions."* | Shows reciprocity in divine-human forgiveness.                  |
| Matthew 6:14 | *"If you forgive men... your heavenly Father will also forgive you."*                      | Part of the Lord’s Prayer teaching.                             |
| Romans 4:7   | *"Blessed are they whose iniquities are forgiven..."*                                      | Reinforces the joy and blessing of being forgiven.              |
| Mark 3:29    | *"Blaspheme against the Holy Spirit... guilty of an eternal sin."*                         | The gravity of unforgivable sin; defines limits of forgiveness. |
| John 20:23   | *"Whoever’s sins you forgive... they are forgiven them."*                                  | Jesus giving authority to forgive.                              |

---

### Prompt: **"Find verses that deal with anxiety and fear."**

| Reference        | Verse                                                     | Relevance                           |
| ---------------- | --------------------------------------------------------- | ----------------------------------- |
| Isaiah 41:10     | *"Don't be afraid, for I am with you..."*                 | A powerful comfort for the anxious. |
| Deuteronomy 31:6 | *"Be strong and courageous... He will not fail you."*     | Assurance of divine presence.       |
| Proverbs 3:25    | *"Don't be afraid of sudden fear..."*                     | Counsel during unexpected crisis.   |
| Psalms 23:4      | *"I will fear no evil... Your rod and staff comfort me."* | Trust even in death or danger.      |
| Psalms 43:5      | *"Why are you in despair... Hope in God!"*                | A self-directed rebuke to anxiety.  |

---

### Prompt: **"Who was Paul writing to in the book of Galatians?"**

| Reference     | Verse                                            | Relevance                                              |
| ------------- | ------------------------------------------------ | ------------------------------------------------------ |
| Galatians 1:1 | *"Paul, an apostle... through Jesus Christ..."*  | Opening of the letter, identifying Paul as the author. |
| Acts 21:39    | *"I am a Jew, from Tarsus..."*                   | Gives background on Paul’s origin.                     |
| Acts 17:22    | *"Paul stood in the middle of the Areopagus..."* | Example of his preaching to Gentiles.                  |
| Romans 1:1    | *"Paul, a servant of Jesus Christ..."*           | Reiterates his apostolic authority.                    |

> Paul was writing to the **churches in Galatia**, correcting doctrinal errors and emphasizing freedom in Christ over legalism.

---

### Prompt: **"What is the significance of the resurrection?"**

| Reference          | Verse                                                        | Relevance                                         |
| ------------------ | ------------------------------------------------------------ | ------------------------------------------------- |
| Romans 14:9        | *"Christ died, rose... Lord of the dead and the living."*    | Explains why resurrection gives Christ authority. |
| Romans 6:5         | *"United with him in death... part of his resurrection."*    | Believers share in resurrection life.             |
| 2 Timothy 1:10     | *"Christ... abolished death and brought life."*              | Highlights resurrection’s role in salvation.      |
| 1 Corinthians 15:4 | *"He was buried... raised on the third day."*                | Summary of gospel essentials.                     |
| Hebrews 11:35      | *"Others were tortured... to obtain a better resurrection."* | Expresses hope in resurrection even in suffering. |

---

## Future Improvements

* Implement a feature to view preceding and following verses to provide scriptural context
* Add support for multiple Bible versions
* Improve cluster granularity and interpretability
* Add a hosted demo using lightweight or streamed embeddings
* Offer advanced filtering (topics, themes, etc.)
* Add search logging or query analytics


