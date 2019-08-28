class Tag:
    def __init__(self, *args, is_single = False, **kwargs):
        self.tag = args[0]
        self.text = ''
        self.is_single = is_single
        self.attributes = kwargs
        self.is_parent = False
        self.children = []
        self.brothers = []
    
    #Немного модифицируем аттрибуты экземпляра, а именно:
    # - в случае если klass - кортеж, сольем его воедино через пробел
    # - аттрибуты class и klass сольем воедино через пробел
    # - поменяем все '_' на '-'
    def __get_attr(self):
        attributes = []
        if self.attributes.get('klass') is not None:
            if isinstance(self.attributes['klass'], tuple):
                self.attributes['klass'] = ' '.join(self.attributes['klass'])
            self.attributes['class'] = self.attributes.pop('klass') + (' ' + str(self.attributes.get('class','')))
        for attr, value in self.attributes.items():
            if '_' in attr:
                attr = attr.replace('_', "-")
            if '_' in value:
                value = value.replace('_', "-")
            attributes.append(f'{attr}="{value}"')
        return attributes

    #Формируем заготовку для выдачи строки
    def __get_str(self): 
        attributes = self.__get_attr()
        if self.is_single:
            self.text = ''
            opening = '<{tag} {attrs}'.format(tag = str(self.tag), attrs = " ".join(attributes))
            ending = '/>'
            return(opening, self.text, ending)                          #self.text оставил только для того, что бы не сбивалась нумерация. Хорошо бы переделать.
        else:
            opening = '<{tag} {attrs}>'.format(tag = str(self.tag), attrs = " ".join(attributes))
            ending = '</{tag}>'.format(tag = str(self.tag))
            return(opening, self.text, ending)

    def __str__(self):
        get_str = self.__get_str()
        if self.children:
            result = ''.join(get_str[0:2])
            for child in self.children:
                result += ('\n' + str(child))
            result += ('\n' + get_str[2])
        elif self.brothers:
            result = ''.join(get_str)
            for brother in self.brothers:
                result += ('\n' + str(brother))
        else:
            result = ''.join(get_str)
        return result

    #Если мы внутри with, считаем остальные экземпляры дочерними
    def __enter__(self, *args, **kwargs):
        self.is_parent = True
        return self

    #Если вышли из with, считаем остальные экземпляры равными
    def __exit__(self, *args, **kwargs):
        self.is_parent = False
        return self

    def __add__(self, other):
        if self.is_parent:
            self.children.append(other)
        else:
            self.brothers.append(other)
        return self

class TopLevelTag(Tag):
    pass

class HTML(Tag):
    def __init__(self, *args, is_single = False, **kwargs):
        self.output = kwargs.get('output')
        self.tag = 'HTML'
        self.text = ''
        self.is_single = False
        self.attributes = {}
        self.is_parent = False
        self.children = []
        self.brothers = []

    def __exit__(self, *args, **kwargs):
        if self.output:
            with open(self.output, 'w', encoding = 'utf-8') as fp:
                fp.write(str(self))
        else:
            print(str(self))