import pyray as pr

class Load:
    '''
    Holds methods for creating images, loading textures, and drawing rectangles
    '''

    def text_to_image(character:str , font_size:int , color: pr.Vector4) -> pr.Image:
        '''
        Creates image from text
        
        Returns:
        - pr.Image
        '''
        return pr.image_text(character, font_size, color)

    def image_file_to_image(image: str):
        '''
        Takes a image file and makes it a pr.Texture

        Returns:
        - pr.Texture
        '''
        return pr.load_image(image)

    def image_file_to_texture(image: str):
        '''
        Takes a image file and makes it a pr.Texture

        Returns:
        - pr.Texture
        '''
        image = pr.load_image(image)
        return pr.load_texture_from_image(image)
    
    def image_to_texture(image: pr.Image):
        '''
        Takes a image and makes it a pr.Texture

        Returns:
        - pr.Texture
        '''
        return pr.load_texture_from_image(image)

    def text_to_texture(character: str, font_size: int, color: pr.Color) -> pr.Texture:
        '''
        Takes a string and makes it a pr.Texture

        Returns:
        - pr.Texture
        '''
        image = pr.image_text(character, font_size, color)
        return pr.load_texture_from_image(image)
    
    def draw_rectangle(actor) -> None:
        '''
        Creates a rectangle, renders it's texture, and places it on screen
        '''
        pr.draw_texture_rec(
            actor.texture,
            pr.Rectangle(0,0, float(actor.texture.width), float(actor.texture.height)),
            [actor.pos_x, actor.pos_y],
            pr.WHITE
        )