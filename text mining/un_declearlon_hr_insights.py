import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read the text from the file
with open("un_declaration_hr_text_data.txt", "r") as file:
    declaration_text = file.read()

# Tokenize the text into words
tokens = nltk.word_tokenize(declaration_text)

# Filter out stopwords
stop_words = set(stopwords.words("english"))
filtered_tokens = [token.lower() for token in tokens if token.lower() not in stop_words and token.isalpha()]

# Create a frequency distribution of the tokens
freq_dist = nltk.FreqDist(filtered_tokens)

# Generate a word cloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(freq_dist)

# Plot the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Universal Declaration of Human Rights")
plt.show()

# Get the top 25 frequent terms
top_25 = freq_dist.most_common(25)

# Prepare data for bar plot
labels, values = zip(*top_25)

# Plot the bar chart
plt.figure(figsize=(12, 6))
plt.bar(labels, values)
plt.xticks(rotation=90)
plt.xlabel("Terms")
plt.ylabel("Frequency")
plt.title("Top 25 Frequent Terms in Universal Declaration of Human Rights")
plt.tight_layout()
plt.show()
