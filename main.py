import pygame
import time


pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


screen_info = pygame.display.Info()
WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Tcube")


font_large = pygame.font.Font(None, 100)
font_small = pygame.font.Font(None, 36)


start_time = None
best_time = float("inf")
last_times = []
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if start_time is None:
                    start_time = time.time()
                else:
                    end_time = time.time()
                    solve_time = end_time - start_time
                    start_time = None
              
                    last_times.append(solve_time)
                    best_time = min(best_time, solve_time)
                    last_times.sort()

            elif event.key == pygame.K_ESCAPE:
                running = False

    screen.fill(BLACK)


    if start_time is not None:
        elapsed_time = time.time() - start_time
    else:
        elapsed_time = 0


    text = font_large.render(f"{elapsed_time:.2f} s", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)


    best_text = font_small.render(f"Melhor Tempo: {best_time:.2f} s", True, WHITE)
    best_rect = best_text.get_rect(topright=(WIDTH - 20, 20))
    screen.blit(best_text, best_rect)


    last_text = font_small.render("Últimos Tempos:", True, WHITE)
    screen.blit(last_text, (20, 20))

    for i, solve_time in enumerate(last_times):
        last_time_text = font_small.render(f"{i+1}. {solve_time:.2f} s", True, GREEN)
        screen.blit(last_time_text, (20, 60 + i * 40))


    quit_text = font_small.render("Pressione ESC para sair", True, WHITE)
    quit_rect = quit_text.get_rect(bottomleft=(20, HEIGHT - 20))
    screen.blit(quit_text, quit_rect)

    pygame.display.flip()


pygame.quit()
