import blog

author = 'GnomeChompsky'

#### List comprehension to get posts by author ####
posts = [post for post in blog.posts if post['author'] == author]
print(posts)
###################################################

