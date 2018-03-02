# Linear Search Example

high_schools = ["Fern Creek", "Doss", "Newburg", "Jeffersontown", "Male", "Manual", "Eastern", "Seneca", "Ballard"]

# define a method that can take an array, and a search term, and perform linear search on that array until it finds the
# desired term


def search(arr, term):
    i = 0  # sets the counter
    while i < len(arr):  # len function allows us to identify how long the array is without providing a specific number.
        if arr[i] == term:  # if item at index i matches the given term, we return that term.
            print("Found " + arr[i] + " at index " + str(i))  # prints the found item, as well as its index.
            return arr[i]  # returns the value.  you should work on returning the correct value, but just print for now.
        else:
            i += 1  # increments our counter + 1 to continue our glorious search.

    print ("Item not found")  # if we didn't find anything, we let the user know.

# running with above test data and given term.


search(high_schools, "Ballard")

# Binary Search Example

# Binary search, in simple terms, splits a list in half until it finds the search term.  It does this by
# identifying midpoints, and dropping entire halves of the list where the search term is not present.

high_schools_bin = ["Fern Creek", "Doss", "Newburg", "Jeffersontown", "Male", "Manual", "Eastern", "Seneca", "Ballard",
                "Iroquois", "Lincoln", "Atherton", "Fairdale", "Butler" "Brown"]

# create a slightly larger list for our search, but this is a trivial data size for any computer.

# when you write your algorithm, try to keep it generic.  We could have our parameters with names like "school"
# or "school_list", but really if we write it well we can throw anything in our binary search (thanks Python!)



def bin_search(arr, search_term):

    sort_high = sorted(arr) # Binary search, to be effective, must run on a sorted list.  sorted() helps us here.
    start = 0  # our list begins at index 0
    end = len(sort_high) - 1  # there are multiple ways to set the end of the list.  we could use sort_high(-1), but
                                # this will be easier for you to reflect in Java.

    while start <= end:
        middle = (start + end)//2  # we set the index middle of the list with integer division.
        mid_index = sort_high[middle]  # defining the middle index itself.

        if mid_index > search_term:  #  so if mid_index turns out to be greater than our search term we set a new end.
            end = middle - 1  # remember, the sorting of the list is what makes this effective.
        elif mid_index < search_term:  #  same thing for less than
            start = middle + 1
        else:  #  once we've found the term, we're done.
            print("Found " + str(search_term) + " at " + str(middle))
            return mid_index

    print("Search term not found")


bin_search(high_schools_bin, "Fairdale")

# through the powers of ABSTRACTION!!11 one one we can implement our search in any way we like.
# High numbers can take quite a while here.

x = range(1, 1000000)
search_for = 99999

bin_search(x, search_for)

