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
    '''Class returns HTML for passed tag and params of tag '''
    
    def __init__(self,
                tag,
                is_single=False,
                toplevel=False,
                **kwargs):
        '''Inits the instance.
        tag - str with passed HTML tag
        is_single - bool type / to discribe, tag is paired or not
        attributes - dict type / for build attributes of HTML tag
        toplevel - bool type / perameter is not used currently
        chldren - list type / of children tags
        kwargs - parameters to fill attributes dict()'''
        # print('__init__ in MyTag class and tag is ', tag)
        self.tag = tag
        self.content = ''
        self.is_single = is_single
        self.attributes = dict()
        self.toplevel = toplevel
        self.children = list()
        if kwargs:
            for attrib, value in kwargs.items():
                if attrib == 'klass':
                    self.attributes['class'] = ' '.join(value)
                else:
                    if '_' in attrib: attrib = attrib.replace('_', "-")
                    self.attributes[attrib] = value
        
    def __enter__(self):
        # print('__enter__ in MyTag class and tag is ', self.tag)
        return self
    
    def __exit__(self, exc_type, value, traceback):
        # print('__exit__ in MyTag class and tag is ', self.tag)
        pass
        
    def __str__(self):
        # print('__str__ in MyTag class and tag is ', self.tag)
        start_str = f'<{self.tag}'
        attrs_str = ''
        closed_braket = '>'
        for i, v in self.attributes.items():
            attrs_str += f' {i}="{v}"'

        if self.is_single:
            content_str = ''
            end_str = '>'
        else:
            # по умолчанию - closed_braket - без переноса строки
            content_str = closed_braket + self.content
            end_str = f'</{self.tag}>'

        if self.children:
            # Но если есть child - closed_braket - C переносом строки
            closed_braket = '>\n' 
            content_str = closed_braket + self.content
            for child in self.children:
                content_str += str(child) + '\n'
        whole_str = start_str + attrs_str + content_str + end_str
        return whole_str
    
    def __add__(self, other):
        '''add (sum) other with the instance.
        It checks type of other'''
        # print('__add__ in MyTag class and tag is ', self.tag)
        if type(other) != str:
            self.children.append(str(other))
        elif type(other) == str:
            self.children.append(other)
        return self
    
class HTML(MyTag):
    '''Class makes HTML-file from child tags strings '''
    
    def __init__(self, output=None):
        '''It called __init__ method of the MyTag and add new variable'''
        super().__init__('html', toplevel=True) # импорт (инициализация) всех атрибутов родительского класса
        self.output = output
        
    def __enter__(self):
        # print('__enter__ in MyTag class and tag is ', self.tag)
        return self
    
    def __exit__(self, exc_type, value, traceback):
        # print(self, 'from __exit__ HTML')
        self.draw(self.output, str(self))
            
    def draw(self, out, text):
        '''It is taking out the final text to file or on screen.
        Depends on out parameters. 
        out - str type or None / If it set - it name of file, else - print on screen'''
        if out:
            print('Final text will be writed to file', out)
            with open(out, mode='w') as f:
                f.write(text)
            print('text has written to file')
        else:
            print('output parameter is not set. Text will be printed on screen')
            print(text)


class TopLevelTag:
    pass
               
               
class Tag:
    pass
    
    
if __name__ == "__main__":    
    # self.text заменен на self.content
    
    # with MyTag("head") as head:
        # with MyTag("title") as title:
            # title.content = "hello"
            # head += title
        # # print(head)

    # Можно расскомментировать блок 1 или 2 для вывода на экран или в файл
    # ############# БЛОК1 #############
    # output не задан - вывод будет сделан на экран
    # with HTML(output=FILE) as doc:
        # with MyTag("head") as head:
            # with MyTag("title") as title:
                # title.content = "hello"
                # head += title
            # doc += head
        # with MyTag("body") as body:
            # with MyTag("h1", klass=("main-text",)) as h1:
                # h1.content = "Test"
                # body += h1

            # with MyTag("div", klass=("container", "container-fluid"), id="lead") as div:
                # with MyTag("p") as paragraph:
                    # paragraph.content = "another test"
                    # div += paragraph

                # with MyTag("img", is_single=True, src="/icon.png", data_image="responsive") as img:
                    # div += img

                # body += div

            # doc += body
    # ############# БЛОК1 #############

    # ############# БЛОК2 #############
    # output задан - вывод будет сделан в файл
    with HTML(output=FILE) as doc:
        with MyTag("head") as head:
            with MyTag("title") as title:
                title.content = "hello"
                head += title
            doc += head
        with MyTag("body") as body:
            with MyTag("h1", klass=("main-text",)) as h1:
                h1.content = "Test"
                body += h1

            with MyTag("div", klass=("container", "container-fluid"), id="lead") as div:
                with MyTag("p") as paragraph:
                    paragraph.content = "another test"
                    div += paragraph

                with MyTag("img", is_single=True, src="/icon.png", data_image="responsive") as img:
                    div += img

                body += div

            doc += body
    # ############# БЛОК2 #############


