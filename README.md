# muster-Wugui.github.io

Coursework site, served by GitHub Pages at
<https://muster-Wugui.github.io>.

## Layout

```
index.html              Homepage — intro + course list
cs180/index.html        CS 180 landing page + project index
cs180/proj0/index.html  Project 0 write-up
cs180/proj0/img/        Web-sized photos for that write-up
cs180/proj0/originals/  Full-res camera files (gitignored, local only)
assets/css/style.css    Shared styles (light + dark)
assets/img/             Berkeley seal / shared images
.nojekyll               Serve files as-is, no Jekyll build
```

## Adding a project write-up

1. Copy `cs180/proj0/` to `cs180/proj1/` and rewrite the text.
2. Drop the full-res photos in `cs180/proj1/originals/`, then shrink them into
   `cs180/proj1/img/` (long side ~1800px, EXIF stripped):

   ```python
   from PIL import Image, ImageOps
   im = ImageOps.exif_transpose(Image.open("originals/foo.JPG")).convert("RGB")
   im.thumbnail((1800, 1800), Image.LANCZOS)
   im.save("img/foo.jpg", quality=82, optimize=True, progressive=True)
   ```

3. In `cs180/index.html`, swap that project's `<div class="row">` for a link and
   mark it as posted:

   ```html
   <a href="/cs180/proj1/">
     <span class="num">Proj 1</span>
     <span class="title">Colorizing the Prokudin-Gorskii Photo Collection</span>
     <span class="badge live">Posted</span>
   </a>
   ```

## Local preview

```
python3 -m http.server 8000
```

then open <http://localhost:8000>.
