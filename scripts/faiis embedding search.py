import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Load the CSV
df = pd.read_csv("./data/web_embedding.csv")

# Function to clean and parse embeddings from string to a list of floats
def clean_embedding(embedding_str):
    embedding_values = embedding_str.strip().split(',')
    cleaned_values = []
    for value in embedding_values:
        try:
            cleaned_values.append(float(value))
        except ValueError:
            cleaned_values.append(0.0)
    return cleaned_values

# Apply cleaning to the embedding column
df["embedding"] = df["embedding"].apply(clean_embedding)

# Convert to NumPy array
xb = np.array(df["embedding"].tolist(), dtype="float32")
print(xb.shape)

# Initialize FAISS index
d = 768  # Dimension of the embeddings
index = faiss.IndexFlatL2(d)  # Build the index using L2 distance

# Add the embeddings to the index
index.add(xb)
print(f"Number of vectors in the index: {index.ntotal}")

# Load the SentenceTransformer model for encoding user input
model = SentenceTransformer('sentence-transformers/multi-qa-mpnet-base-cos-v1')

# Function to search for the closest verses
def search_closest_verses(user_input, k=10): # k = number of verses to return
    # Encode the user's query
    user_input_encoded = model.encode(user_input, convert_to_tensor=True)
    user_input_encoded = np.array(user_input_encoded, dtype="float32").reshape(1, -1)

    # Search the index for the k closest vectors
    D, I = index.search(user_input_encoded, k)  # D = distances, I = indices of nearest vectors

    # Retrieve the associated verses using the indices
    closest_verses = df.iloc[I[0]]  # The first element since we passed a single query
    
    return closest_verses[['verse', 'embedding']]

# Example user input
user_input = "What does the Bible say about x?" #input

# Get the closest 10 verses
closest_verses = search_closest_verses(user_input)

# Display the results
print(closest_verses)
