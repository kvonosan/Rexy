"""Proper personalized result for user search."""


class Personalize:
    def __init__(self, *args, **kwargs):
        self.user = kwargs['user']
