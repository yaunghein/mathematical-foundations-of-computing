def is_inside(point, radius):
    return point[0]**2 + point[1]**2 <= radius**2


def find_area():
    radius = 1
    square_count = 10
    margin_of_error = 0.001
    previous_area = 0
    difference = 1

    while difference > margin_of_error:
        print(f"Squares: {square_count}, Area: {previous_area}")

        inside_count = 0
        edge_count = 0

        step = (radius * 2) / square_count
        square_area = step ** 2

        for i in range(square_count):
            for j in range(square_count):
                x_left = -radius + (i * step)
                x_right = x_left + step
                y_bottom = -radius + (j * step)
                y_top = y_bottom + step

                point1 = (x_left, y_bottom)
                point2 = (x_right, y_bottom)
                point3 = (x_left, y_top)
                point4 = (x_right, y_top)

                point1_inside = is_inside(point1, radius)
                point2_inside = is_inside(point2, radius)
                point3_inside = is_inside(point3, radius)
                point4_inside = is_inside(point4, radius)

                if point1_inside and point2_inside and point3_inside and point4_inside:
                    inside_count += 1
                elif point1_inside or point2_inside or point3_inside or point4_inside:
                    edge_count += 1

        inside_area = inside_count * square_area
        edge_area = edge_count * square_area * 0.5
        total_area = inside_area + edge_area

        difference = abs(total_area - previous_area)
        previous_area = total_area
        square_count *= 2

    print(f"Final Estimated Area: {previous_area}")


if __name__ == "__main__":
    find_area()
