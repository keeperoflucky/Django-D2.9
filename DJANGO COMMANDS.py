u1 = User.objects.create_user('John Boe')
u2 = User.objects.create_user('Mirko Crocop')
Author.objects.create(authorUser=u1)
Author.objects.create(authorUser=u2)
Category.objects.create(name='Medicine')
Category.objects.create(name='Sport')
Category.objects.create(name='News')
Category.objects.create(name='Film')

author = Author.objects.get(id=1)
author2 = Author.objects.get(id=2)

Post.objects.create(author=author, Category_type='NW', title='BreakingNews', text='Не пытайся покинуть Омск')
Post.objects.create(author=author2, Category_type='AR', title='Погода в Москве', text='Сегодня в Москве будет гололедица')
Post.objects.create(author=author2, Category_type='AR', title='Происхождение снежных бурь', text=Снежная буря образуется из за скопления частиц воды которые были подняты в небо')

Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=2))
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=3))

Comment.objects.create(commentPost = Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='В Омске Снег')
Comment.objects.create(commentPost = Post.objects.get(id=2), commentUser=Author.objects.get(id=2).authorUser, text='Отвратительная погода')
Comment.objects.create(commentPost = Post.objects.get(id=3), commentUser=Author.objects.get(id=2).authorUser, text='Ничего не понял из статьи')
Comment.objects.get(id=1).like()

>>> Comment.objects.get(id=2).like()
>>> Comment.objects.get(id=2).like()
>>> Comment.objects.get(id=2).like()
>>> Comment.objects.get(id=2).like()

>>> Comment.objects.get(id=3).dislike()
>>> Comment.objects.get(id=3).dislike()
>>> Comment.objects.get(id=3).dislike()

Comment.objects.get(id=1).rating
a = Author.objects.get(pk=1)
a.updaterating()
a.ratingAuthor

a2 = Author.objects.get(pk=2)
a2.updaterating()
a2.ratingAuthor

Comment.objects.all()

Post.objects.get(id=2).DateCreation

a = Author.objects.order_by("-ratingAuthor")
    for i in a:
        i.ratingAuthor
        i.authorUser.username

