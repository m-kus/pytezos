import re
import inspect
from functools import update_wrapper


def is_interactive():
    import __main__ as main
    return not hasattr(main, '__file__')


def get_attr_docstring(class_type, attr_name):
    if attr_name == 'get':
        attr_name = '__call__'

    attr = getattr(class_type, attr_name, None)
    if attr and attr.__doc__:
        return re.sub(r' {3,}', '', attr.__doc__)


def default_attr_filter(x):
    return True


def get_class_docstring(class_type, attr_filter=default_attr_filter, extended=False):
    def format_attribute(x):
        attr = getattr(class_type, x)
        if type(attr) == property:
            name = f'.{x}'
        else:
            if extended:
                sig = str(inspect.signature(attr)).replace('self, ', '')
            else:
                sig = '()'
            name = f'.{x}{sig}'

        if extended:
            doc = get_attr_docstring(class_type, x)
        else:
            doc = ''
        return f'{name}{doc}'

    def filter_attribute(x):
        return not x.startswith('_') and attr_filter(x) and type(getattr(class_type, x)) != property

    return '\n'.join(map(format_attribute, filter(filter_attribute, dir(class_type))))


def inline_doc(method):
    doc = [repr(method)]
    if method.__doc__:
        doc.append(re.sub(r' {3,}', '', method.__doc__))

    class CustomReprDescriptor:
        def __get__(self, instance, owner):
            class MethodWrapper:
                def __init__(self):
                    self.class_instance = instance
                    self.doc = '\n'.join(doc)

                def __call__(self, *args, **kwargs):
                    return method(self.class_instance, *args, **kwargs)

                def __repr__(self):
                    return self.doc

            return update_wrapper(MethodWrapper(), method)

    return CustomReprDescriptor()


class InlineDocstring(type):

    def __new__(mcs, name, bases, attrs, **kwargs):
        if is_interactive():
            new_attrs = {}
            for attr_name, attr in attrs.items():
                if callable(attr) and attr.__doc__ and not attr_name.startswith('_'):
                    attr = inline_doc(attr)
                new_attrs[attr_name] = attr
        else:
            new_attrs = attrs
        return type.__new__(mcs, name, bases, new_attrs, **kwargs)
