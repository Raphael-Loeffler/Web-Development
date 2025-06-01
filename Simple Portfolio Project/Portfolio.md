# Portfolio Project

## Tasks 

### Week 1 (26.5.2025 - 1.6.2025)

##### 1. Project setup
- Create a folder portfolio
- Create the main folder structure:
        .
        ├── app.py
        ├── README.md
        ├── requirements.txt
        ├── static
        │   ├── css
        │   │   └── index.css
        └── templates
            └── index.html
- index.css: Create a basic css file.
- index.html: Create a basic html file and link the css file.
- app.py:
    - Create the root endpoint.
    - Render the index.html file.

##### 2. HTML
- body: Add a header-tag
    - header: Add a nav-tag with a ul-tag that contains 4 li-tags.
- body: Add a main-tag
    - main: Add 4 separate section-tags. 
        - section: id='hero'
            - h1-tag
            - p-tag
            - ul-tag with 3 li-tags.
                - li: contains an a-tag.
                    - a: contains an img-tag
        - section: id='about'
            - h2-tag
            - figure-tag
                - img-tag
            - p-tag
        - section: id='work'
            - h4-tag
            - ul-tag with 3 li-tags
                - li: img-tag
        - section: id='contact'
            - p-tag
            - h5-tag
            - form-tag with name, email and text input-tags
            - button-tag
- body: Add a footer-tag
    - section: id='footer'
        - p-tag

##### 3. CSS
- Leave it empty for now.