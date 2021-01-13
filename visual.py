import matplotlib.pyplot as plt
import sweetviz as sv
from tools import Clean
import texthero as hero
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from collections import Counter
from textblob import TextBlob
drop_list = ['id', 'conversation_id', 'created_at', 'name', 'timezone', 'user_id', 'cashtags', 'place', 'quote_url', 'near', 'geo',
             'source', 'user_rt_id', 'user_rt', 'retweet_id', 'retweet_date', 'translate', 'trans_src', 'trans_dest', 'video', 'retweet']


class Visual(Clean):
    def __init__(self, name_file=""):
        super().__init__(name_file)
        print("hello")
        # print(self.df.head())

    def cluster(self):
        self.df['pca'] = (
            self.df['clean_tweet']
            .pipe(hero.tfidf, max_features=300)
            .pipe(hero.pca)
        )
        # for s in self.df['pca']:
        #     print(s)
        # print("---------")
        self.df['kmeans'] = (
            self.df['clean_tweet']
            .pipe(hero.tfidf, max_features=300)
            .pipe(hero.kmeans, n_clusters=5)
        )
        print( self.df['pca'])
        # for i in range(0 ,5):#self.df['pca'][self.df['kmeans'] == i,0]
        #     plt.scatter( filter(,), self.df['pca'][self.df['kmeans'] == i,1])     #.apply(lambda x : if ), self.df['pca'].apply(lambda x : if ))
        # plt.show()
        # for s in self.df['kmeans']:
        #     print(s)
        # print("---------")
        # for s in self.df['clean_tweet']:
        #     print(s)
        # print("---------")
        # self.df.head()
        # hero.scatterplot(self.df, 'pca', color='kmeans',
        #                  hover_data=['clean_tweet'])

    def show_word(self):
        wordcloud = WordCloud(width=900, height=500, max_words=1628).generate(
            ''.join(self.df['clean_tweet']))
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()
        # plt.savefig('books_read.png')

    def language(self):
        dic = Counter(self.df['language'])
        plt.pie(dic.values(), labels=dic.keys(), autopct='%.1f%%')
        plt.show()
        # plt.savefig('books_read.png')
        # negative vs. positive neutral

    def analyse(self, text):
        try:
            analys = TextBlob(text)
        except:
            print('error textblob')

        if analys.polarity > 0.0:
            return 'positive'
        elif analys.polarity == 0.0:
            return 'neutral'
        else:
            return 'negative'

    def sentiment(self):
        self.df['sentiment'] = self.df['clean_tweet'].apply(self.analyse)
        dic = Counter(self.df['sentiment'])
        plt.pie(dic.values(), labels=dic.keys(), autopct='%.1f%%')
        # plt.show()

    def show(self):
        fig, x = plt.subplots(2, 2)
        dic = Counter(self.df['language'])
        # explode = (0, 0.1, 0, 0)

        x[0, 0].pie(dic.values(), labels=dic.keys(), autopct='%.1f%%')

        self.df['sentiment'] = self.df['clean_tweet'].apply(self.analyse)
        dic = Counter(self.df['sentiment'])
        x[0, 1].pie(dic.values(), labels=dic.keys(), autopct='%.1f%%')

        wordcloud = WordCloud(width=90, height=50, max_words=1628).generate(
            ''.join(self.df['clean_tweet']))
        x[1, 0].imshow(wordcloud, interpolation="bilinear")
        x[1, 0].axis("off")

        plt.show()


data = Visual('arr.csv')
data.cluster()
# data.language()

# data.show_word()
# data.sentiment()
# data.show()
