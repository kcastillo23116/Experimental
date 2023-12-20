import pyautogui


def get_region():
    get1 = input('\nPlace cursor at the top left of the region you want to capture, and then press enter \n')
    pos1 = pyautogui.position()

    get2 = input('Now place your cursor at the bottom right of the region you want to capture, and press enter \n')
    pos2 = pyautogui.position()

    width = pos2[0] - pos1[0]
    height = pos2[1] - pos1[1]

    print('Your region is... \n')

    print('region=('+str(pos1[0])+', '+str(pos1[1])+', '+str(width)+', '+str(height)+') \n')

    return [pos1[0], pos1[1], width, height]


# Bbox used to capture a specific area
# Bounding box is a (left_x, top_y, right_x, bottom_y) tuple, so with the values (500, 500, 600, 700),
# the image has a width of 100 pixels and a height of 200 pixels
# Can use region finder to get correct values for an area. Just add the third and fourth numbers for width and height
def get_bbox_region():
    region = get_region()

    x1 = region[0]
    y1 = region[1]
    width = region[2]
    height = region[3]

    x2 = x1 + width
    y2 = y1 + height

    return print('bbox=('+str(x1)+', '+str(y1)+', '+str(x2)+', '+str(y2)+') \n')


if __name__ == '__main__':
    get_bbox_region()
