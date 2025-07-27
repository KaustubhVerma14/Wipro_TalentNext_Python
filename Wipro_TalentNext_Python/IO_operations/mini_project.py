# MINI-PROJECT 

def find_meeting_details(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    num_lines = len(lines)
    if num_lines > 24:
        print("Error: Number of lines exceeds 24.")
        return

    hour = num_lines
    if hour == 0:
        meeting_time = "12 AM"
    elif hour == 12:
        meeting_time = "12 PM"
    elif hour > 12:
        meeting_time = f"{hour - 12} PM"
    else:
        meeting_time = f"{hour} AM"

    from collections import Counter
    import string

    text = ' '.join(lines)

    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator).lower()
    words = clean_text.split()

    word_count = Counter(words)
    most_common_word, freq = word_count.most_common(1)[0]

    meeting_place = most_common_word.capitalize() + " Street"

    print("Meeting time:", meeting_time)
    print("Meeting place:", meeting_place)
    print(f"(Explanation: Number of lines = {num_lines}, "
          f"Most frequent word = '{most_common_word}' appeared {freq} times.)")

file_path = input("enter the path of file: ") 
find_meeting_details(file_path)
