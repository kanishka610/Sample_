import spacy
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load documents
with open("one.txt", "r", encoding="utf-8") as f:
    doc1 = f.read()

with open("two.txt", "r", encoding="utf-8") as f:
    doc2 = f.read()

# ----------------------------
# 1. Tokenization + POS Tagging using spaCy
# ----------------------------
spacy_doc1 = nlp(doc1)
spacy_doc2 = nlp(doc2)

tokens_doc1 = [token.text for token in spacy_doc1]
tokens_doc2 = [token.text for token in spacy_doc2]

pos_doc1 = [(token.text, token.pos_) for token in spacy_doc1]
pos_doc2 = [(token.text, token.pos_) for token in spacy_doc2]

print("🔹 Tokens (Doc1):", tokens_doc1)
print("🔹 POS Tags (Doc1):", pos_doc1)

print("\n🔹 Tokens (Doc2):", tokens_doc2)
print("🔹 POS Tags (Doc2):", pos_doc2)

# ----------------------------
# 2. Sentiment Analysis with TextBlob
# ----------------------------
blob1 = TextBlob(doc1)
blob2 = TextBlob(doc2)

print("\n🔸 Sentiment Analysis:")
print(f"Doc1 → Polarity: {blob1.sentiment.polarity:.2f}, Subjectivity: {blob1.sentiment.subjectivity:.2f}")
print(f"Doc2 → Polarity: {blob2.sentiment.polarity:.2f}, Subjectivity: {blob2.sentiment.subjectivity:.2f}")

# ----------------------------
# 3. Document Similarity (TF-IDF + Cosine Similarity)
# ----------------------------
vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform([doc1, doc2])
similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
print(f"\n🔸 Similarity Score between documents: {similarity:.2f}")

# ----------------------------
# 4. Word Cloud
# ----------------------------
combined_text = doc1 + " " + doc2
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(combined_text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("☁️ Word Cloud")
plt.show()
'''from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

# # Sample Documents
# doc1 = "Data science is amazing. It uses algorithms to learn from data."
# doc2 = "Machine learning is a core part of AI and data science."

# Read from txt files
with open('one.txt', 'r', encoding='utf-8') as file1:
    doc1 = file1.read()

with open('two.txt', 'r', encoding='utf-8') as file2:
    doc2 = file2.read()

# Tokenization
tokens1 = word_tokenize(doc1.lower())
tokens2 = word_tokenize(doc2.lower())

print("Tokens from doc1:", tokens1)
print("Tokens from doc2:", tokens2)

# Word Cloud
def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

generate_wordcloud(doc1)
generate_wordcloud(doc2)'''
