class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("author must be an instance of Author class")
        if not isinstance(magazine, Magazine):
            raise ValueError("magazine must be an instance of Magazine class")
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._author = author
            self._magazine = magazine
            self._title = title
        else:
            raise ValueError("Titles must be of type str and between 5 and 50 characters, inclusive")
    @property
    def title(self):
        return self._title
    
    @title.setter
    def set_title(self, value):
        if hasattr(self, '_title'):
            raise AttributeError("Cannot change title after it is set")
        
class Author:
    def __init__(self, name):
        if (type(name) == str) and (len(name) > 0):
            self._name = name
        else:
            raise ValueError("Names must be of type str and longer than 0 characters")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def set_name(self, value):
        if hasattr(self, '_name'):
            raise AttributeError("Cannot change name after it is set")

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def set_name(self, value):
        if (type(value) == str) and (2 <=len(value) <= 16):
            self._name = value
        else:
            raise ValueError("Name must be string between 2 and 16 characters.")


    @property
    def category(self):
        return self._category
    
    @category.setter
    def set_category(self, value):
        if (type(value) == str) and (len(value) > 0):
            self._category = value
        else:
            print("Categories must be of type str and longer than 0 characters")
            self._category = None

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass