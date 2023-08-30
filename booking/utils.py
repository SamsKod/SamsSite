from django.urls import reverse
from datetime import datetime, timedelta, date
from calendar import HTMLCalendar
from .models import Post


class Calendar(HTMLCalendar):
    '''formats a day'''
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    def formatday(self, day, posts):
        if day == 0:
            return '<td></td>'

        today_date = date(self.year, self.month, day)
        posts_per_day = posts.filter(
            start_date__lte=today_date, end_date__gte=today_date)
        d = ''
        for post in posts_per_day:
            url = reverse('post-detail', kwargs={'pk': post.pk})
            d += f'<a href="{url}"> {post.author} </a>'

        return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"

    '''formats a week as a tr'''
    def formatweek(self, theweek, post):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, post)
        return f'<tr> {week} </tr>'

    '''formats a month as a table
    filter events by year and month'''
    def formatmonth(self, withyear=True):
        posts = Post.objects.filter(
            start_date__year=self.year, start_date__month=self.month)

        cal = f'<table border="0" cellpadding="0"'\
            ' cellspacing="0" class="calendar">\n'
        cal += (
            f'{self.formatmonthname(self.year,self.month, withyear=withyear)}\n'
        )
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, posts)}\n'
        return cal
