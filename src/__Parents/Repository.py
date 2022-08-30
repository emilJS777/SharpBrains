from datetime import date, datetime, time


class Repository:

    @staticmethod
    def get_dict_items(obj):
        dict_item = {}

        if not obj:
            return obj

        for key, value in obj.__dict__.items():
            if not key == '_sa_instance_state':
                if not type(value) == int \
                        and not type(value) == str \
                        and not type(value) == float \
                        and not type(value) == bool\
                        and not type(value) == list\
                        and not type(value) == date\
                        and not type(value) == datetime\
                        and not type(value) == time:
                    dict_item[key] = Repository.get_dict_items(value)
                else:
                    dict_item[key] = value

        return dict_item

    @staticmethod
    def get_page_items(page):
        page_items: dict = {'total': page.total,
                            'page': page.page,
                            'pages': page.pages,
                            'per_page': page.per_page,
                            'items': []}

        for item in page.items:
            page_items['items'].append(Repository.get_dict_items(item))

        return page_items

    @staticmethod
    def get_array_items(array):
        items: list = []

        for item in array:
            items.append(Repository.get_dict_items(item))

        return items
