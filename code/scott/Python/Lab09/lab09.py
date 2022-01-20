# Lab09.py Compute Automated Readability Index - 22-01-12
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

fname = input("Please enter the filename.txt:")

with open(fname, 'r') as f:
    a = 0
    b = 0
    c = 0 
    num_lines = 0
    num_words = 0
    num_chars = 0
    x = 4.71
    y = 0.5
    z = 21.43
    for line in f:
        
        words = line.split()

        a += line.count(".")
        b += line.count("!")
        c += line.count("!")
        num_lines = a + b + c
        num_words += len(words)
        num_chars += len(line.replace(' ', ''))
 
    c_div_by_w = float(num_chars / num_words) 
    w_div_by_s = float(num_words / num_lines)
    test = float(x * c_div_by_w) + float(y * w_div_by_s) - z
    test = round(test)

print('\nNumber of characters in text file :', num_chars)    
print('\nNumber of words in text file :', num_words) 
print('\nNumber of sentences in text file:', num_lines)
print('\nThe ARI Score is:', test)

ARI = ari_scale.get(test) 
    

        






