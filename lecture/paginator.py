from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def my_paginator(lecture_list, page, num=20, page_num_range=5):

    paginator = Paginator(lecture_list, num) 
    
    max_idx = len(paginator.page_range)
    try:
        lectures = paginator.page(page)
        print('1', lectures)
    except PageNotAnInteger:
        lectures = paginator.page(1)
        print('2')
    except EmptyPage:
        lectures = paginator.page(paginator.num_pages)
        print('3')
    
    current_page = int(page) if page else 1
    print(current_page)
    start_idx = int((current_page -1) / page_num_range) * page_num_range

    end_idx = start_idx + page_num_range
    if end_idx >= max_idx:
        end_idx = max_idx
    
    page_range = paginator.page_range[start_idx:end_idx]
    return [lectures, page_range]