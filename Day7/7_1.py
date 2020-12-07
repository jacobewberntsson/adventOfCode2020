with open("data/7_1.txt", "r") as f:
    content = [line for line in f.read().splitlines()]

def contentReader():
    container = {}
    for line in content:
        line = line.replace('bags', '').replace('bag', '').replace('.', '').strip()
        bag, bag_content = line.split('contain')
        bag = bag.strip()

        if 'no other' in line:
            bag_content = []
        else:
            bag_content = [contentOfBag(bag) for bag in bag_content.split(',')]
        
        container.update({bag: bag_content})

    return container
        
def contentOfBag(bag):
    bag = bag.strip()
    amount = bag[0]
    color = bag[1:].strip()
    return amount, color


def shinyBagHolder():
    data = contentReader()
    content = {}
    for key in data.keys():
        for amount, color in data[key]:
            if color not in content:
                content[color] = []
            content[color].append((amount, key))
    
    checked_bags = set('shiny gold')
    colors = ['shiny gold']

    i = 0
    while i < len(colors):
        if colors[i] in content:
            for _amount, color in content[colors[i]]:
                if color not in checked_bags:
                    colors.append(color)
                    checked_bags.add(color)
        i += 1

    return len(colors) - 1

def contentOfShinyBag():
    container = contentReader()
    count = 0
    color_queue = ['shiny gold']
    multiplier = [1]
    i = 0
    while i < len(color_queue):
        if color_queue[i] in container:
            for amount, color in container[color_queue[i]]:
                color_queue.append(color)
                multiplier.append(multiplier[i] * int(amount))
                count += multiplier[i] * int(amount)
        i += 1

    return count

print(shinyBagHolder())
print(contentOfShinyBag())