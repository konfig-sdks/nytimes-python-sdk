operation_parameter_map = {
    '/lists/full-overview.json-GET': {
        'parameters': [
            {
                'name': 'published_date'
            },
        ]
    },
    '/lists.json-GET': {
        'parameters': [
            {
                'name': 'list'
            },
            {
                'name': 'bestsellers-date'
            },
            {
                'name': 'published-date'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/lists/overview.json-GET': {
        'parameters': [
            {
                'name': 'published_date'
            },
        ]
    },
    '/lists/{date}/{list}.json-GET': {
        'parameters': [
            {
                'name': 'date'
            },
            {
                'name': 'list'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/lists/best-sellers/history.json-GET': {
        'parameters': [
            {
                'name': 'age-group'
            },
            {
                'name': 'author'
            },
            {
                'name': 'contributor'
            },
            {
                'name': 'isbn'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'price'
            },
            {
                'name': 'publisher'
            },
            {
                'name': 'title'
            },
        ]
    },
    '/lists/names.json-GET': {
        'parameters': [
        ]
    },
    '/reviews.json-GET': {
        'parameters': [
            {
                'name': 'isbn'
            },
            {
                'name': 'title'
            },
            {
                'name': 'author'
            },
        ]
    },
};