from entity.book.category.BookCategoryId import BookCategoryId


class GetBooksByCategoryRequest:
    def __init__(self, request, category_id: int):
        self.__request = request
        self.__category_id = category_id

    def validate(self) -> bool:
        try:
            self.__book_category_id = BookCategoryId(value=self.__category_id)
        except ValueError as e:
            print(e)
            return False
        return True

    @property
    def category_id(self) -> BookCategoryId:
        return self.__book_category_id
