
# Natural-Language-Processing
Natural Language Processing

![image](https://user-images.githubusercontent.com/121180975/209106427-1ab2a325-b587-47cb-a039-12631f72b196.png)

**Tokenization**

  The tokenization stage involves converting a sentence into a stream of words, also called “tokens.” Tokens are the basic building blocks upon which analysis and other methods are built. 

Many NLP toolkits allow users to input multiple criteria based on which word boundaries are determined. For example, you can use a whitespace or punctuation to determine if one word has ended and the next one has started. Again, in some instances, these rules might fail. For example, don’t, it’s, etc. are words themselves that contain punctuation marks and have to be dealt with separately.


**Change Case**

  Changing the case involves converting all text to lowercase or uppercase so that all word strings follow a consistent format. Lowercasing is the more frequent choice in NLP software.

**Stop-Words Removal**

  "Stop words" are frequently occurring words used to construct sentences. In the English language, stop words include is, the, are, of, in, and and. For some NLP applications, such as document categorization, sentiment analysis, and spam filtering, these words are redundant, and so are removed at the preprocessing stage. 


**Stemming**

  The term word stem is borrowed from linguistics and used to refer to the base or root form of a word. For example, learn is a base word for its variants such as learn, learns, learning, and learned. 
  
  Stemming is the process of converting all words to their base form, or stem. Normally, a lookup table is used to find the word and its corresponding stem. Many search engines apply stemming for retrieving documents that match user queries. Stemming is also used at the preprocessing stage for applications such as emotion identification and text classification.  



**Lemmatization**

  Lemmatization is a more advanced form of stemming and involves converting all words to their corresponding root form, called “lemma.” While stemming reduces all words to their stem via a lookup table, it does not employ any knowledge of the parts of speech or the context of the word. This means stemming can’t distinguish which meaning of the word right is intended in the sentences “Please turn right at the next light” and “She is always right.”

The stemmer would stem right to right in both sentences; the lemmatizer would treat right differently based upon its usage in the two phrases. 

A lemmatizer also converts different word forms or inflections to a standard form. For example, it would convert less to little, wrote to write, slept to sleep, etc. 

A lemmatizer works with more rules of the language and contextual information than does a stemmer. It also relies on a dictionary to look up matching words. Because of that, it requires more processing power and time than a stemmer to generate output. For these reasons, some NLP applications only use a stemmer and not a lemmatizer. 
