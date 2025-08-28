import pygame
import socket
import time
import threading
import json

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 9999))

drawing_instructions = []
starting_point = (0,0)

def serve():
    while True:
        data, addr = server.recvfrom(1024)
        drawing_instructions.append(json.loads(data))
        


threading.Thread(target = serve).start()




screen = pygame.display.set_mode((1000,1000),flags=pygame.NOFRAME)
screen.fill((0,0,0))
clock = pygame.time.Clock()


def display():
    global drawing_instructions
    global starting_point
    color = 'green'
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        for instruct in drawing_instructions:
            if "color" in instruct.keys():
                color = instruct["color"]
                continue
            if instruct['start'] == 2:
                screen.fill((0,0,0))
                continue

            if instruct['start']:
                starting_point = (instruct['x'],instruct['y'])
                continue
            if not instruct['start']:
                starting_point = (instruct['start_x'],instruct['start_y'])
            pygame.draw.line(screen,color,starting_point,(instruct['x'],instruct['y']))
            starting_point = (instruct['x'],instruct['y'])
        drawing_instructions = []

        pygame.display.flip()
        clock.tick(60)



def main():
    display()
    pygame.display.quit()

if __name__ == '__main__':
    main()
            
