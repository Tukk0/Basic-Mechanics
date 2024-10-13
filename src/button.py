import pygame

import config


class Button():
    def __init__(self, x_coord, y_coord, width, height, text, color_fore, color_back,
                 hover_color_fore, handle_func, **kwargs):
        """
        Button class
        :param x_coord: x coordinate
        :param y_coord: y coordinate
        :param width: width of the button
        :param height: height of the button
        :param text: text of the button
        :param color_fore: color for the
        :param color_back: color back the
        :param hover_color_fore: hover color
        :param handle_func: func to be done
        """
        self.text = text
        self.color_fore = color_fore
        self.color_back = color_back
        self.hover_color_fore = hover_color_fore
        self.image_fore = pygame.Rect(x_coord, y_coord, width, height)
        self.image_back = pygame.Rect(x_coord - config.BORDER_WIDTH, y_coord - config.BORDER_WIDTH,
                                      width +
                                      config.BORDER_WIDTH * 2, height + config.BORDER_WIDTH * 2)
        self.is_hovered = False
        self.is_active = True
        self.handle_func = handle_func
        self.kwargs = kwargs

    def draw(self, surface):
        current_color_fore = self.hover_color_fore if self.is_hovered else self.color_fore
        pygame.draw.rect(surface, self.color_back, self.image_back, 0, 10)
        pygame.draw.rect(surface, current_color_fore, self.image_fore, 0, 10)
        font = pygame.font.SysFont('couriernew', 30)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.image_fore.center)
        surface.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.image_fore.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered and self.is_active:
            self.handle_func(**self.kwargs)
