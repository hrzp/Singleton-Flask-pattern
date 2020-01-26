from sqlalchemy.orm.collections import InstrumentedList
import re

class BaseMixin:

    def __init__(self,**kwargs):
        print(kwargs, '--------------------')
        for key in kwargs:
            setattr(self,self.__convert_to_snake_case(key),kwargs[key])
        print(kwargs, '++++'*5)
    def __convert_to_snake_case(self,key):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', key)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()



    caller_stack = list()

    def extract_relations(self):
        return self.__mapper__.relationships.keys()

    def extract_columns(self):
        return self.__mapper__.columns.keys()

    def get_columns(self):
        resualt = dict()
        resualt['relationships'] = self.extract_relations()
        resualt['columns'] = self.extract_columns()
        return resualt

    def convert_columns_to_dict(self, columns):
        resualt = dict()
        for item in columns:
            resualt[item] = getattr(self, item)
        return resualt

    def convert_instrumented_list(self, items):
        resualt = list()
        for item in items:
            resualt.append(item.json(self.caller_stack))
        return resualt

    def detect_class_name(self, item):
        if item.__class__.__name__ == 'InstrumentedList':
            return item[0].__class__.__name__.lower()
        return item.__class__.__name__.lower()

    def convert_relations_to_dict(self, relations):
        resualt = dict()
        me = self.__class__.__name__.lower()
        self.caller_stack.append(me)

        for relation in relations:
            obj = getattr(self, relation)
            if self.detect_class_name(obj) in self.caller_stack:
                continue
            if type(obj) == InstrumentedList:
                resualt[relation] = self.convert_instrumented_list(obj)
                continue
            resualt[relation] = obj.json(self.caller_stack)

        return resualt

    def json(self, caller_stack=None):
        if not caller_stack:
            self.caller_stack = []
        else:
            self.caller_stack = caller_stack
        final_obj = dict()
        columns = self.get_columns()
        final_obj.update(self.convert_columns_to_dict(columns['columns']))
        final_obj.update(self.convert_relations_to_dict(columns['relationships']))
        return final_obj
