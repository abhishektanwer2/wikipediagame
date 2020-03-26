import wikipedia
from difflib import get_close_matches


class wikipediaclass():
    # constuctor for the class wikipediaclass used for the initialization .
    def __init__(self, articleName):
        self.article = articleName
        self.articleMainObject = object()

    # This function is used for checking the article name is present in wikipedia or not.
    def is_exists(self):
        try:
            wikipedia.search(self.article)
        except:
            print('Article not found')
            return []

    # This function is used for checking that particular object has any links or not.
    def is_connected(self):

        if len(self.articleMainObject.links) == 0:
            return False
        else:
            return True

    # This function is used for get the wikipedia object from the internet using Wikipedia library.
    def get_object(self):

        try:
            self.is_exists()

            self.articleMainObject = wikipedia.page(self.article)

            self.is_connected()


        except wikipedia.exceptions.DisambiguationError as e:

            articleList = e.options
            Modifiedarticle = get_close_matches(self.article, articleList, n=1)

            if Modifiedarticle == []:
                Modifiedarticle = e.options[0]

            self.articleMainObject = wikipedia.page(Modifiedarticle)

        except wikipedia.exceptions.PageError as p:

            self.articleMainObject = []
        except wikipedia.exceptions.WikipediaException as e:
            print("please type something in parameter")

    # This function is used for get the links from the  wikipedia object.
    def get_links(self):
        if self.articleMainObject == []:
            return []
        else:
            return self.articleMainObject.links
