import svgwrite

WIDTH = 1400
LEVELS = 6

def draw_tree(dwg,start_y):

    # Definiera startpositionen för rotnoden
    start_x = WIDTH/2
    level_gap = 60  # Avstånd mellan nivåerna
    node_radius = 12 + 6

    # Definiera koefficient för horisontellt avstånd mellan noder
    def node_position(level, index):
        x_gap = WIDTH // (2 ** (level + 1))
        x = start_x + index * x_gap * 2 - x_gap * ((2 ** level) - 1)
        y = start_y + level * level_gap
        return x, y

    # Funktion för att rita en nod
    def draw_node(x, y, node_label):
        dwg.add(dwg.circle(center=(x, y), r=node_radius, fill="none", stroke="black", stroke_width=2))
        # dwg.add(dwg.text(node_label, insert=(x - 4, y + 4), font_size="10px", fill="black"))

    # Funktion för att rita en linje mellan noder (förbindelser) från cirklarnas medelpunkter
    def draw_line(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        dist = (dx ** 2 + dy ** 2) ** 0.5
        offset_x = node_radius * dx / dist
        offset_y = node_radius * dy / dist
        dwg.add(dwg.line(start=(x1 + offset_x, y1 + offset_y),
                         end=(x2 - offset_x, y2 - offset_y),
                         stroke="black", stroke_width=2))

    # Skapa binärträdets struktur
    nodes = list(range(1, 2**LEVELS))

    # Rita alla noder och deras förbindelser
    for level in range(LEVELS):
        for i in range(2 ** level):
            node_index = 2 ** level - 1 + i
            if node_index < len(nodes):
                x, y = node_position(level, i)
                draw_node(x, y, str(nodes[node_index]))

                # Rita linjer till vänster och höger barn om de finns
                left_child_index = 2 * node_index + 1
                right_child_index = 2 * node_index + 2

                if left_child_index < len(nodes):
                    left_x, left_y = node_position(level + 1, 2 * i)
                    draw_line(x, y, left_x, left_y)

                if right_child_index < len(nodes):
                    right_x, right_y = node_position(level + 1, 2 * i + 1)
                    draw_line(x, y, right_x, right_y)

    # Spara SVG-filen
    dwg.save()

# Skapa och spara den uppdaterade SVG-filen med det binära trädet
dwg = svgwrite.Drawing('tree.svg', size=(f"{WIDTH}px", "900px"))
dwg.add(dwg.rect(insert=(0, 0), size=("100%", "100%"), fill="white"))

draw_tree(dwg,120)
draw_tree(dwg,500)
