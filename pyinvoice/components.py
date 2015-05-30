from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.shapes import Drawing
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import colors


class CodeSnippet(Paragraph):
    style = ParagraphStyle(
        name='CodeSnippet',
        parent=getSampleStyleSheet()['Code'],
        backColor=colors.lightgrey, leftIndent=0,
        borderPadding=(5, 5, 5, 5)
    )

    def __init__(self, code):
        Paragraph.__init__(self, code, self.style)


class SimpleTable(Table):
    style = TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), .25, colors.black),
        ('BOX', (0, 0), (-1, -1), .25, colors.black),
    ])

    def __init__(self, data, horizontal_align=None):
        Table.__init__(self, data, style=self.style, hAlign=horizontal_align)


class PaidStamp(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, canvas, doc):
        # "PAID"
        canvas.saveState()
        canvas.setFontSize(50)
        canvas.setFillColor(colors.red)
        canvas.setStrokeColor(colors.red)
        canvas.rotate(45)
        canvas.drawString(self.x, self.y, 'PAID')
        canvas.setLineWidth(4)
        canvas.setLineJoin(1)  # Round join
        canvas.rect(self.x - .25 * inch, self.y - .25 * inch, width=2*inch, height=inch)
        canvas.restoreState()