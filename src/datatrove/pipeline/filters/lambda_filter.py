from datatrove.data import Document
from datatrove.pipeline.filters.base_filter import BaseFilter
from typing import Callable

from datatrove.utils.typeshelper import NiceRepr


class LambdaFilter(BaseFilter):

    def __init__(
            self,
            filter_function: Callable[[Document], bool],
            **kwargs
    ):
        """
          filters documents triggering the given filter_function with respect to a specific metadata key.

          @param regex_exp: regex expression
          """
        super().__init__(**kwargs)
        self.filter_function = filter_function

    def __repr__(self):
        return " ".join([super().__repr__(), NiceRepr("👤", "metadata").get_name()])

    def filter(self, doc: Document) -> bool:
        """

        :param doc: document
        :return: is_filter
        """
        return self.filter_function(doc)