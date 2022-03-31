def last_viewed_books_middleware(get_response):
    def middleware(request):
        request.book = request.session.get('last_viewed_book',[])
        return get_response(request)

    return middleware

# def active_user_middleware(get_response):
#     def middleware(request):
#         if request.user.is_authenticated:
#             friends = request.user.friends
#
#     return middleware
