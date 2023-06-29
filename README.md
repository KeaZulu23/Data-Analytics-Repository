# Data-Analytics-Repository

It imports necessary libraries: nltk for natural language processing, stopwords from nltk.corpus to remove common words, WordCloud from the wordcloud library to generate a word cloud, and matplotlib.pyplot for visualization.

The text of the Universal Declaration of Human Rights is read from a file called "un_declaration_hr_text_data.txt" using the open() function and stored in the declaration_text variable.

The text is tokenized into individual words using the word_tokenize() function from nltk.

Stop words, which are common words like "the" and "is" that do not carry significant meaning, are loaded using stopwords.words("english") from nltk.corpus. These stop words are filtered out from the tokens.

A frequency distribution is created using FreqDist from nltk to count the occurrences of each word in the filtered tokens.

A word cloud is generated from the frequency distribution using WordCloud with customized settings for width, height, and background color.

The word cloud is displayed using imshow() from matplotlib.pyplot.

The top 25 frequent terms from the frequency distribution are extracted using most_common().

The labels (terms) and values (frequencies) are separated into two lists for plotting.

A bar plot is created using plt.bar() from matplotlib.pyplot, displaying the top 25 frequent terms on the x-axis and their corresponding frequencies on the y-axis.

The resulting word cloud and bar plot are shown using plt.show().

Overall, the code reads the text, preprocesses it by removing stop words, calculates the frequency distribution of the remaining words, generates a word cloud visualization, and plots a bar chart of the top 25 frequent terms.
