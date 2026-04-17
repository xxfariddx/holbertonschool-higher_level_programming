#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of lists of integers representing 
    the Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        prev_row = triangle[i - 1]
        # Start the new row with the mandatory first '1'
        curr_row = [1]
        
        # Calculate the middle elements
        for j in range(1, i):
            # Sum the two numbers above the current position
            curr_row.append(prev_row[j - 1] + prev_row[j])
            
        # End the new row with the mandatory last '1'
        curr_row.append(1)
        
        # Add the completed row to our triangle
        triangle.append(curr_row)

    return triangle
