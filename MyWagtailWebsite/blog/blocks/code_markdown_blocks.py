from django.utils.safestring import mark_safe
from markdown import markdown
from pygments import highlight
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name

from wagtail.wagtailcore import blocks


# from https://jordijoan.me/code-blocks-wagtail-using-pygments/
class CodeBlock(blocks.StructBlock):
    """
    Code Highlighting Block
    """
    LANGUAGE_CHOICES = (
        ('python', 'Python'),
        ('bash', 'Bash/Shell'),
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('scss', 'SCSS'),
        ('json', 'JSON'),
        ('c', 'C'),
        ('java', 'Java'),
        ('arduino', 'Arduino'),
    )

    STYLE_CHOICES = (
        ('syntax', 'default'),
        ('emacs', 'emacs'),
        ('monokai', 'monokai'),
        ('vim', 'vim'),
        ('xcode', 'xcode'),
    )

    language = blocks.ChoiceBlock(choices=LANGUAGE_CHOICES)
    style = blocks.ChoiceBlock(choices=STYLE_CHOICES, default='syntax')
    code = blocks.TextBlock()

    def render(self, value):
        src = value['code'].strip('\n')
        lang = value['language']
        lexer = get_lexer_by_name(lang)
        css_classes = ['code', value['style']]

        formatter = get_formatter_by_name(
            'html',
            linenos=None,
            cssclass=' '.join(css_classes),
            noclasses=False,
        )
        return mark_safe(highlight(lang + "--\n" + src, lexer, formatter))

    class Meta:
        icon = 'code'
