import json

print json.dumps(
    {
        'categories' : [
            'A',
            'B',
            'C',
            'D'
        ],
        'images' : [
            {
                'name' : 'img1',
                'category' : 3
            },
            {
                'name' : 'img2',
                'category' : 1
            },
            {
                'name' : 'img3',
                'category' : 4
            },
        ]
    }
)
