#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class MyTag:
    '''Class returns HTML for accepted tag and params of tag '''
    
    def __init__(self, tag, is_single=False, toplevel=False):
        '''Inits the instance.
        tag - str with accepted HTML tag
        is_single - bool to discribe, tag is paired or not
        attributes - dict for build attributes of HTML tag
        chldren - list of children tags '''
        self.tag = tag
        self.content = ''
        self.is_single = is_single
        self.attributes = {}
        self.toplevel = toplevel
        self.children = list()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, value, traceback):
        if self.toplevel:
            print(self)
    
    def __str__(self):
        start_str = f'<{self.tag}'
        attrs_str = ''
        for i, v in self.attributes.items():
            attrs_str += f' {i}="{v}"'

        if self.is_single:
            content_str = ''
            end_str = '>'
        else:
            content_str = f'>{self.content}'
            end_str = f'</{self.tag}>'
        
        if self.children:
            for child in self.children:
                content_str += str(child)
        
        whole_str = start_str + attrs_str + content_str + end_str
        return whole_str
    
               
if __name__ == "__main__":
    with MyTag('H1', toplevel=True) as header:
        header.content = "Hello"
   

    with MyTag('hr', is_single=True, toplevel=True) as hr:
        pass


    with MyTag('a', toplevel=True) as href:
        href.content = 'bSPAM'
        href.attributes['class'] = 'link'
        href.attributes['href'] = './text.txt'

    with MyTag("body", toplevel=True) as body:
        body.attributes['class'] = 'body_top'
        with MyTag("div") as div:
            with MyTag("p") as paragraph:
                paragraph.content = "Какой-то текст"
            div.children.append(paragraph)
        body.children.append(div)


            
            