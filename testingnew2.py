try:
    from PIL import Image
except ImportError:
    import Image

background = Image.open("interP.png")
overlay = Image.open("dots.png")

background = background.convert("RGBA")
overlay = overlay.convert("RGBA")

new_img = Image.blend(background, overlay,0.3)
new_img.save("new.png","PNG")
