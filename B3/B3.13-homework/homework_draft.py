#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Мы хотим иметь возможность написать примерно такой код:

with HTML(output="test.html") as doc:
    with TopLevelTag("head") as head:
        with Tag("title") as title:
            title.text = "hello"
            head += title
        doc += head

    with TopLevelTag("body") as body:
        with Tag("h1", klass=("main-text",)) as h1:
            h1.text = "Test"
            body += h1

        with Tag("div", klass=("container", "container-fluid"), id="lead") as div:
            with Tag("p") as paragraph:
                paragraph.text = "another test"
                div += paragraph

            with Tag("img", is_single=True, src="/icon.png", data_image="responsive") as img:
                div += img

            body += div

        doc += body
А по результату в test.html увидеть следующее (отступы/пробелы могут быть другими, это не принципиально):

<html>
<head>
  <title>hello</title>
</head>
<body>
    <h1 class="main-text">Test</h1>
    <div class="container container-fluid" id="lead">
        <p>another test</p>
        <img src="/icon.png" data-image="responsive"/>
    </div>
</body>
</html>
Таким образом:

В коде должно быть минимум три основных класса HTML, TopLevelTag и Tag.
Класс HTML определяет, куда сохранять вывод: на экран через print или в файл.
Объекты класса TopLevelTag скорее всего не содержат внутреннего текста и всегда парные.
Объекта класса Tag могут быть непарные или быть парные и содержать текст внутри себя.
Должна быть возможность задать атрибуты в Tag, но в данном задании для TopLevelTag это необязательное условие.

'''

FILE="test.html"

class MyTag:
    '''Class returns HTML for accepted tag and params of tag '''
    
    def __init__(self, tag, is_single=False, toplevel=False):
        print('__init__ in MyTag and tag is ', tag)
        self.tag = tag
        self.content = ''
        self.is_single = is_single
        self.attributes = dict()
        self.toplevel = toplevel
        self.children = list()
        
    def __enter__(self):
        print('__enter__ in MyTag and tag is ', self.tag)
        return self
    
    def __exit__(self, exc_type, value, traceback):
        print('__exit__ in MyTag and tag is ', self.tag)
        
    def __str__(self):
        print('__str__ in MyTag and tag is ', self.tag)
        return 'STRING from __str__ of Tag ' + self.tag
    
    def __add__(self, other):
        print('__add__ in MyTag and tag is ', self.tag)
        return self
    
class HTML(MyTag):
    '''Class makes HTML-file from child tags strings '''
    
    def __init__(self, output=None):
        '''It called __init__ method of the MyTag and add new variable'''
        super().__init__('html', toplevel=True)
        self.output = output
        # print(dir(self), ' for ', self.tag)
    
    def __exit__(self, exc_type, value, traceback):
        # print('attributes', self.attributes, ' for ', self.tag)
        print(self, 'from __exit__ HTML')
        # print('exit')          
        # return str(self)
            
    def save(self, out, text):
        print('TEXT ', text, 'will writed to file')
        with open(out, mode='w') as f:
            f.write(text)
        print('text has written to file')
               
if __name__ == "__main__":
    head0 = MyTag("head")
    print(head0)
    title0 = MyTag("title")
    print(title0)
    head0 += title0
    print(head0)
    
    with MyTag("head") as head1:
        with MyTag("title") as title1:
            title1.content = "hello"
            head1 += title1
        print(head1)
        print(str(head1))
    
    
   
    
    # self.text заменен на self.content
    # with HTML(output=FILE) as doc:
        # with MyTag("head") as head:
            # with MyTag("title") as title:
                # title.content = "hello"
               # # print(head)
               # # print(title)
                # head += title
            # # print(doc)
            # # print(head)
            # doc += head
            # print(doc)
            # print(head)
			

#        with MyTag("body") as body:
#            with MyTag("h1", klass=("main-text",)) as h1:
#                h1.content = "Test"
#                body += h1
#
#            with MyTag("div", klass=("container", "container-fluid"), id="lead") as div:
#                with MyTag("p") as paragraph:
#                    paragraph.content = "another test"
#                    div += paragraph
#
#                with MyTag("img", is_single=True, src="/icon.png", data_image="responsive") as img:
#                    div += img
#
#                body += div
#
#            doc += body



#    with MyTag('H1', toplevel=True) as header:
#        header.content = "Hello"
#   
#
#    with MyTag('hr', is_single=True, toplevel=True) as hr:
#        pass
#
#
#    with MyTag('a', toplevel=True) as href:
#        href.content = 'bSPAM'
#        href.attributes['class'] = 'link'
#        href.attributes['href'] = './text.txt'
#
#    with MyTag("body", toplevel=True) as body:
#        body.attributes['class'] = 'body_top'
#        with MyTag("div") as div:
#            with MyTag("p") as paragraph:
#                paragraph.content = "Какой-то текст"
#            div.children.append(paragraph)
#        body.children.append(div)

