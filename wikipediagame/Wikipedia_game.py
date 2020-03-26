import sys
import wikipedia
import wikipediaclass
from collections import OrderedDict


class WikipediaGame():
    '''
    constuctor for the class WikipediaGame used for the initialization .
   '''

    def __init__(self):
        self.startPage = str(sys.argv[1])
        self.targetPage = str(sys.argv[2])

        self.visitedPath = []
        self.visited = []
        self.pathdict = OrderedDict()

    # This function is used for geting the wikipedia object from class and returns all the liks associated with it.
    def wiki_object(self, articleName):
        articleObject = wikipediaclass.wikipediaclass(articleName)
        articleObject.get_object()
        if articleObject.get_object() == []:
            return []

        return articleObject.get_links()

    '''
    This function is the heart of the problem and here i have impletmented Breadth first search
     for treversing through all the links.   
    '''

    def BFS_search(self):

        visited = []
        queue = []

        queue.append(self.startPage)
        visited.append(self.startPage)

        if wikipedia.page(self.startPage).links.__contains__(self.targetPage):
            self.visitedPath.append(wikipedia.page(self.startPage).title)
            return self.visitedPath[-1]

        while queue:

            currentArticle = visited.pop(0)
            self.visitedPath.append(currentArticle)
            if (currentArticle == self.targetPage):
                return self.visitedPath[-1]

            print("articleName: {}".format(currentArticle))

            for article in self.wiki_object(currentArticle):
                print(article)

                if article not in visited:
                    try:
                        currentArticlelist = wikipedia.page(article).links
                        self.pathdict[article] = currentArticlelist
                    except:
                        article = ""
                    if article != "":
                        if (currentArticlelist.__contains__(self.targetPage)):
                            self.visitedPath.append(article)
                            return self.visitedPath[-1]

                    queue.append(article)
                    visited.append(article)

        return self.visitedPath[-1]

    '''
    This function is used for getting the path from start page to target page.
    '''

    def backTrackpath(self, lastarticlename):
        temp = ""
        end = self.targetPage
        pathnew = []
        pathnew.append(end)
        pathnew.append(lastarticlename)

        if lastarticlename != self.startPage:
            while lastarticlename == self.startPage:
                for key, value in self.pathdict.items():
                    if (value.links.__contains__(lastarticlename)):
                        pathnew.append(key)
                        lastarticlename = key
                        break
            pathnew.append(self.startPage)
        return pathnew

    '''
    This function is used for the input string chages like strip capitalization, removing the white space.
    '''

    def input_formatchange(self):
        startp = self.startPage.rstrip().lstrip().split(" ")
        endp = self.targetPage.rstrip().lstrip().split(" ")
        startlist = []
        endlist = []
        for s in startp:
            startlist.append(s.capitalize())
        a = " "
        a = a.join(startlist)
        self.startPage = a
        b = " "
        for s in endp:
            endlist.append(s.capitalize())
        b = b.join(endlist)
        print(b)
        self.targetPage = b


'''
This is the starting point of our program.
'''


def run_main():
    wiki = WikipediaGame()
    wiki.input_formatchange()
    solution = wiki.BFS_search()
    path = wiki.backTrackpath(solution)
    path = path[::-1]
    formatpath = str(path)
    formatpathnew = formatpath.replace(',', ' ->').replace('[', "").replace("]", '')
    print(formatpathnew)


if __name__ == '__main__':
    run_main()
