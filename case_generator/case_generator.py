import math
import random
import numpy as np
import cv2
import pandas as pd
import os
import json


def generate_scenario(width, height,
                      min_num_cities, max_num_cities):

    # Generate the number of cities in field randomly
    num_cities = random.randint(min_num_cities, max_num_cities)

    if num_cities > height//10:
        num_cities = height//10

    # Generate random city
    cities = []
    i = 0
    while i < num_cities:
        # Generate the position of the city
        city_x = random.randint(0, width - 25)
        city_y = random.randint(0, height - 25)

        # Check if the city overlaps with any existing cities
        overlaps = False
        for city in cities:
            if (city[0] == city_x and
                    city[1] == city_y or
                    abs(city_x - city[0]) < 30 and
                    abs(city_y - city[1]) < 30):
                overlaps = True
                break

        # If the city doesn't overlap with any existing cities, add it to the list
        if not overlaps:
            cities.append((city_x, city_y))
            i += 1

    return cities


# To create an image of the cities to see
def convert_image_and_save(field_width, field_height, cities, img_path, show_image=False):
    # Create a blank image
    img = np.zeros((field_height, field_width, 3), np.uint8)
    img.fill(255)
    # Draw the cities as points on the image
    for city in cities:
        cv2.circle(img, (city[0], city[1]), 12, (0, 0, 255), 2)

    # Save the image to a file
    cv2.imwrite(img_path, img)

    if show_image:
        cv2.imshow("Cities", img)
        cv2.waitKey(0)


def store_case(cities, width, height, base_path=r'scenarios'):
    # Create a dataframe from the list of tuples
    df = pd.DataFrame(cities, columns=['x', 'y'])

    # Set the file name
    index = 1
    file_name = f"scenario_{index}.csv"

    # Check if the file exists
    while os.path.exists(os.path.join(base_path, file_name)):
        index += 1
        file_name = f"scenario_{index}.csv"

    # Save the dataframe to a CSV file
    df.to_csv(os.path.join(base_path, file_name), index=False)

    # also store the case virtualized as png
    convert_image_and_save(width, height, cities,
                           os.path.join(base_path, file_name[:-3] + "png"))


if __name__ == '__main__':
    width = 600
    height = 600
    cities = generate_scenario(width, height, 30, 50)

    # convert_image_and_save(width, height, cities, "case_1.png")

    store_case(cities, width, height)
