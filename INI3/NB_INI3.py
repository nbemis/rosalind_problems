'''
This script is meant to solve the following

    Given: A string s of length at most 200 letters and four integers a, b, c and d

    Return: The slice of this string from indices a
    through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.
'''

def splice_string(my_string, a, b, c, d):

    slice_a_b = my_string[a:b+1]
    slice_c_d = my_string[c:d+1]

    return "{0} {1}".format(slice_a_b, slice_c_d)

long_string = "UtKvRPIewkjU79IF8bCc0Aebg7qjxlMadagascarophisedhTRq00SweS7mXBASCPnSCREXzMQwysgProzjiChzazAh6dU76f5ax3aMtwo3KpLlHcHCqNxDkQqLsbK2C0JNUrhsMiIiLN9lC5AaiDlGkny7DCK19llRHheliacauAZOf3d8qurKaYT8gnFOywx."

print(splice_string(long_string, 30, 44, 164, 170))
