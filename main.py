import chromadb


# Non-persistent client
chroma_client = chromadb.Client()

# We can create a persistent client by passing a path to the database
# chroma_client = chromadb.PersistentClient(path="chroma-db")


# Below code will use default sentence transformer embedding function.
# We can customize the embedding function by passing a function to the `embedding_function` parameter.
# Can also use external APIs like OpenAI, Cohere, HuggingFace etc.
collection = chroma_client.create_collection(name="admission_collection")

# Let's read the data from the file
with open("admission_rules.txt", "r") as f:
    rules = f.read().splitlines()

# Now let's add the data to the collection
collection.add(
    ids=[str(i) for i in range(len(rules))],
    documents=rules,
    metadatas=[{"rule_no": i + 1} for i in range(len(rules))],
)
# print(collection.peek())

questions = [
    "What is the deadline for filling the form?",
    "When the merit list will be published?",
    "When lectures will be started?",
]
# Let's query the collection
results = collection.query(
    query_texts=questions,
    n_results=2,
)

for i, question in enumerate(questions):
    print(10 * "*")
    print(f"\nQuestion: {question}")
    for j, result in enumerate(results["documents"][i]):
        print(f"\nAnswer({j+1}): {result}")
