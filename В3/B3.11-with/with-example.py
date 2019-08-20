#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Tag:
    '''Class returns HTML for accepted tag and params of tag'''
    
    def __init__(self, tag, toplevel=False, is_single=False):
        '''Inits the instance.
        tag - str with accepted HTML tag
        attributes - dict for build attributes of HTML tag
        chldren - list of children tags'''
        self.tag = tag
        self.text = ""
        self.attributes = {}

        self.toplevel = toplevel
        self.is_single = is_single
        self.children = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, value, traceback):
        if self.toplevel:
            print("<%s>" % self.tag)
            for child in self.children:
                print(child)

            print("</%s>" % self.tag)

    def __str__(self):
        attrs = []
        for attribute, value in self.attributes.items():
            attrs.append('%s="%s"' % (attribute, value))
        attrs = " ".join(attrs)

        if self.children:
            opening = "<{tag} {attrs}>".format(tag=self.tag, attrs=attrs)
            internal = "%s" % self.text
#            print(str(self.children))
            for child in self.children:
                internal += str(child)
            ending = "</%s>" % self.tag
            return opening + internal + ending
        else:
            if self.is_single:
                return "<{tag} {attrs}/>".format(tag=self.tag, attrs=attrs)

            else:
                return "<{tag} {attrs}>{text}</{tag}>".format(
                    tag=self.tag, attrs=attrs, text=self.text
                )
            
if __name__ == "__main__":
    with Tag("body", toplevel=True) as body:
        with Tag("div") as div:
            with Tag("p") as paragraph:
                paragraph.text = "Какой-то текст"
                div.children.append(paragraph)
        body.children.append(div)
        
    