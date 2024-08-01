import faiss
import requests
import numpy as np

local = '11434'
embedding_dimension = 4096

prompts = [
    'Unpleasant landscape',
    'Pleasant landscape'
]

comparison_prompt = 'landscape'

index = faiss.IndexFlatL2(embedding_dimension)

X = np.zeros((len(prompts), embedding_dimension), dtype='float32')

for i, prompt in enumerate(prompts):
    res = requests.post(f'http://localhost:{local}/api/embeddings',
                    json = {
                        'model': 'llama3',
                        'prompt': prompt
                    }
                    )

    X[i] = np.array(res.json()['embedding'])

index.add(X)

res = requests.post(f'http://localhost:{local}/api/embeddings',
                    json = {
                        'model': 'llama3',
                        'prompt': comparison_prompt
                    }
                    )

embedding = np.array([res.json()['embedding']], dtype='float32')

D, I = index.search(embedding, 1)
print(np.array(prompts)[I.flatten()])