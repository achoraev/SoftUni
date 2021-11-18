hour_exam = int(input())
minute_exam = int(input())
hour_arrived = int(input())
minute_arrived = int(input())

is_on_time = "On time"
text_to_print = ''

total_time_exam = hour_exam * 60 + minute_exam
total_time_arrived = hour_arrived * 60 + minute_arrived

if total_time_arrived < total_time_exam:
    diff = total_time_exam - total_time_arrived
    if diff > 30:
        is_on_time = 'Early'

    if diff < 60:
        text_to_print = f"{diff} minutes before the start"
    else:
        hours = diff // 60
        minutes = diff % 60

        text_to_print = f"{hours}:{minutes:02d} hours before the start"
elif total_time_arrived > total_time_exam:
    is_on_time = 'Late'
    diff = total_time_arrived - total_time_exam
    if diff < 60:
        text_to_print = f"{diff} minutes after the start"
    else:
        hours = diff // 60
        minutes = diff % 60

        text_to_print = f"{hours}:{minutes:02d} hours after the start"


print(is_on_time)
print(text_to_print)