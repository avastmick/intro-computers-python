# Builds docs - using Pandoc
# TODO: move this into something more elegant and configurable

pandoc --standalone --section-divs -t revealjs -V theme=moon -V transition=concave -V center=false index.md -o docs/index.html

pandoc --standalone --section-divs -t revealjs -V theme=moon -V transition=concave -V center=false about-me.md -o docs/About-me.html

pandoc --standalone --section-divs -t revealjs -V theme=moon -V transition=concave -V center=false Lesson-1.md -o docs/Lesson-1.html