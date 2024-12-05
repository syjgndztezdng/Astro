while running:
    for event in pygame.event.get():
        # проверить закрытие окна
            if event.type == pygame.QUIT:
                running = False

    #математикa
    angle_F = math.atan((pos1[0] - pos2[0]) / (pos1[1] - pos2[1]))
    F1 = (scipy.constants.G / 1000 * M1 * M2 / distance(pos1, pos2) ** 2 * math.cos(math.atan(angle_F)), 
          scipy.constants.G * M1 * M2 / distance(pos1, pos2) ** 2 * math.sin(angle_F))

    F2 = (F1[0] * -1, F1[1] * -1)
    v1 = (v1[0] + F1[0] / M1 * 10 ** koef, v1[1] + F1[1] / M1 * 10 ** koef)
    print(angle_F, pos1, pos2)
    v2 = (v2[0] + F2[0] / M2 * 10 ** koef, v2[1] + F2[1] / M2 * 10 ** koef)
    pos1 = (pos1[0] + v1[0], pos1[1] + v1[1])
    pos2 = (pos2[0] + v2[0], pos2[1] + v2[1])
    
    #отрисовка
    screen.fill(BLACK)
    
    for I in range(0, int(grid / 2) + 1):   # сетка
        pygame.draw.line(screen, GRID_CLR, [0, nol[1] + nak * HEIGHT / grid * I], [WIDTH, nol[1] + nak * HEIGHT / grid * I])
        pygame.draw.line(screen, GRID_CLR, [0, nol[1] - nak * HEIGHT / grid * I], [WIDTH, nol[1] - nak * HEIGHT / grid * I])
        pygame.draw.line(screen, GRID_CLR, [WIDTH / grid * I, nol[1] + nol[1] * nak], [WIDTH / grid * I, nol[1] - nol[1] * nak])
        pygame.draw.line(screen, GRID_CLR, [WIDTH / grid * I + nol[0], nol[1] + nol[1] * nak], [WIDTH / grid * I + nol[0], nol[1] - nol[1] * nak])

    pygame.draw.circle(screen, CLR1, [k_len * pos1[0] + nol[0], k_len * nak * pos1[1] + nol[1]], 10)
    pygame.draw.circle(screen, CLR2, [k_len * pos2[0] + nol[0], k_len * nak * pos2[1] + nol[1]], 10)
    
    #остальное
    pygame.display.flip()
    clock.tick(FPS)
    break


exit()