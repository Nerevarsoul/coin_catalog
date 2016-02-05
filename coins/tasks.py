# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

from celery.task import task
import xlwt

from .models import Coin


@task
def create_excel_document(filter_by, columns):
    queryset = Coin.objects.filter(**filter_by)
    
    response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=coin.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet(str(user))
        
        row_num = 0

        columns = [
            ("Наименование", 16000),
            ("Юридический адрес", 12000),
            ("ОКПО", 4000),
            ("Телефон", 3000),
            ("Факс", 2000),
            ("ОКФС", 8000),
            ("ОКОПФ", 7000),
            ("Архив", 2000),
            ("Дата удаления", 2000),
            ("код в САИС", 4000),
        ]

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        for col_num in xrange(len(columns)):
            ws.write(row_num, col_num, columns[col_num][0], font_style)
            # set column width
            ws.col(col_num).width = columns[col_num][1]

        font_style = xlwt.XFStyle()
        font_style.alignment.wrap = 1

        for coin in queryset:
            row_num += 1
            
            for i, col_attr in enumerate(columns):
                ws.write(row_num, i, getattr(coin, col_attr[2], font_style)

        ws.row(3).height_mismatch = True
        ws.row(3).height = 256*3

        wb.save(response)
        return response
