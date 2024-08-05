import pathlib
from django.shortcuts import render
from visits.models import PageVisits


this_dir = pathlib.Path(__file__).resolve().parent
def home_view(request, *args, **kwargs):
    qs = PageVisits.objects.all()
    page_qs = PageVisits.objects.filter(path=request.path)
    my_title = "Home Page"
    my_context = {
        "page_title": my_title,
        "page_visits_count": page_qs.count(),
        "total_page_visits": qs.count(),
    }
    html_template = "home.html"
    PageVisits.objects.create(path=request.path)
    return render(request, html_template, my_context)

def about_view(request, *args, **kwargs):
    qs = PageVisits.objects.all()
    page_qs = PageVisits.objects.filter(path=request.path)
    my_title = "Home Page"
    my_context = {
        "page_title": my_title,
        "page_visits_count": page_qs.count(),
        "total_page_visits": qs.count(),
    }
    html_template = "home.html"
    PageVisits.objects.create(path=request.path)
    return render(request, html_template, my_context)

# def my_old_home_page_view(request, *args, **kwargs):
#     my_title = "home Page"
#     my_context = {
#         "page_title": my_title,
#     }
#     html_ = """
# <!DOCTYPE html>
# <html lang="en" lang="en">
#     <body>
#         <h1>My new and improved {page_title}</h1>
#     </body>
# </html>
# """.format(**my_context)
#     # html_file_path = this_dir / 'home.html'
#     # html_ = html_file_path.read_text()
#     return HttpResponse(html_)