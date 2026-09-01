# muster-Wugui.github.io

Personal coursework site, served by GitHub Pages at
<https://muster-Wugui.github.io>.

## Layout

```
index.html            Homepage — intro + course list
cs180/index.html      CS 180 landing page + project index
assets/css/style.css  Shared styles (light + dark)
assets/img/           Berkeley seal / shared images
.nojekyll             Serve files as-is, no Jekyll build
```

## Adding a project write-up

1. Create `cs180/proj1/index.html` (copy the structure of `cs180/index.html`;
   the stylesheet path becomes `../../assets/css/style.css`).
2. Put its images in `cs180/proj1/img/`.
3. In `cs180/index.html`, swap that project's `<div class="row">` for a link and
   mark it live:

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
