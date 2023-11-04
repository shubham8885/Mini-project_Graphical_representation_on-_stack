import pygame
import random

# Constants for window and stack dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
STACK_WIDTH = 100
STACK_HEIGHT = 400
STACK_X = 50
STACK_Y = 100

# Initialize Pygame
pygame.init()

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Stack Visualization")

# Initialize the stack
stack = []

# Create a font for text rendering
font = pygame.font.Font(None, 36)

# Define a maximum stack size
MAX_STACK_SIZE = 10

# Initialize messages for element insertion and deletion
insert_message = None
delete_message = None

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if len(stack) < MAX_STACK_SIZE:
                    value = random.randint(0, 99)
                    stack.insert(0, value)  # Insert a value at the top of the stack
                    insert_message = f"Inserted {value}"
                    delete_message = None  # Clear the delete message
                else:
                    insert_message = "Stack Overflow!"
                    delete_message = None

            elif event.key == pygame.K_BACKSPACE:
                if stack:
                    deleted_value = stack.pop(0)  # Remove the top element from the stack
                    delete_message = f"Deleted {deleted_value}"
                    insert_message = None  # Clear the insert message

    # Clear the screen
    window.fill((0, 0, 0))

    # Draw the stack visualization (blue bar)
    pygame.draw.rect(window, (0, 0, 255), (STACK_X, STACK_Y, STACK_WIDTH, STACK_HEIGHT))

    # Draw stack elements from top to bottom
    for i, value in enumerate(stack):
        text = font.render(str(value), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (STACK_X + STACK_WIDTH / 2, STACK_Y + i * 30 + 15)
        window.blit(text, text_rect)

    # Display element insertion message
    if insert_message:
        insert_text = font.render(insert_message, True, (0, 255, 0))
        insert_rect = insert_text.get_rect()
        insert_rect.center = (WINDOW_WIDTH // 2, STACK_Y - 50)
        window.blit(insert_text, insert_rect)

    # Display element deletion message
    if delete_message:
        delete_text = font.render(delete_message, True, (255, 0, 0))
        delete_rect = delete_text.get_rect()
        delete_rect.center = (WINDOW_WIDTH // 2, STACK_Y - 50)
        window.blit(delete_text, delete_rect)

    # Display stack size and limit
    size_text = font.render(f"Size: {len(stack)}", True, (255, 255, 255))
    size_rect = size_text.get_rect()
    size_rect.topleft = (10, 10)
    window.blit(size_text, size_rect)

    limit_text = font.render(f"Limit: {MAX_STACK_SIZE}", True, (255, 255, 255))
    limit_rect = limit_text.get_rect()
    limit_rect.topleft = (10, 50)
    window.blit(limit_text, limit_rect)

    pygame.display.update()
