from django.contrib import admin
from models import Post, Person, Portfolio, Contacts


class PostAdmin(admin.ModelAdmin):
    pass

    class Media:
        js = [
            'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            'grappelli/tinymce_setup/tinymce_setup.js',
        ]
admin.site.register(Post, PostAdmin)
admin.site.register(Person)
admin.site.register(Portfolio, PostAdmin)
admin.site.register(Contacts)