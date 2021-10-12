

def main():
    wall = collect_wall()
    distance_matrix = get_distance_matrix(wall)
    distance = get_max_joints_distance(distance_matrix)
    print("\nSolution\n--------")
    print("the answer is:", distance)
    print_wall(wall, distance)


def get_distance_matrix(wall: list) -> dict:
    """Return a distance matrix for a given wall

    :param wall: a list of rows that contain a set of single bricks lengths
    :type wall: list[list[int]]

    :return: a distance matrix for a given wall
    :rtype: dict
    """

    distance_matrix = dict()
    for wall_row in wall:
        distance = 0
        for brick_length in wall_row[:-1]:
            distance += brick_length
            if distance in distance_matrix:
                distance_matrix[distance] += 1
            else:
                distance_matrix[distance] = 1

    return distance_matrix


def get_max_joints_distance(distance_matrix: dict) -> int:
    """Return a minimum distance to maxmimum count of joints

    :param distance_matrix: a distance matrix
    :type distance_matrix: dict

    :return: a distance from the left border to a maximum count of joints
        in a line. Returns 0 if there are no solutions.
    :rtype: int
    """

    if distance_matrix:
        max_joints_count = max(distance_matrix.values())

    for distance, joints_count in distance_matrix.items():
        if max_joints_count == joints_count:
            return distance

    return 0
# end of minimum functions


def print_wall(wall: list, distance: int) -> None:
    """Print a wall and place a minumin crosses line on it

    :param wall: a wall structure
    :type wall: list[list[int]]
    :param distance: a distance to place a line
    :type distance: int
    """

    # convert each idividual row to a string
    pwall = list()  # printed wall
    for wall_row in wall:
        prow = "|"  # printed row
        for brick_length in wall_row:
            prow += " " * (brick_length - 1) + "|"
        pwall.append(prow)

    # append top and bottom borders]
    border = "+" + "-" * (sum(wall[0]) - 1) + "+"
    pwall.insert(0, border)
    pwall.append(border)

    for prow in pwall:
        if prow[distance] in (" ", "-"):
            prow = prow[:distance] + "x" + prow[distance + 1:]
        print(prow)


def collect_wall():
    """Return a wall structure requested from a user

    :return: a wall structure requested from a user
    :rtype: list[list[int]]
    """

    print("""
    Enter a set of integers separated with a space to build a wall row.
    Or just pass an empty input to complete.
    """)

    wall = list()
    longest_row = 0
    while True:
        user_input = input("row: ")

        if not user_input:  # end of user input
            break

        user_input = list(map(int, user_input.split()))
        row_length = sum(user_input)

        if longest_row and row_length < longest_row:
            user_input.append(longest_row - row_length)

        if longest_row and row_length > longest_row:
            for wall_row in wall:
                wall_row.append(row_length - longest_row)

        wall.append(user_input)
        longest_row = max(longest_row, row_length)

    return wall



