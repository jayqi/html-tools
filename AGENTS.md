# AGENTS instructions

This is a collection of minimalist tools implemented as single HTML files with embedded CSS and Javascript.

## Coding standards

Unless otherwise instructed, follow these standards:

- Each tool is an independent single HTML file.
- Use plain modern HTML, vanilla modern JavaScript, and vanilla modern CSS.
- Use minimal dependencies.
- No React or any other frontend framework.
- Do not worry about supporting old browsers.

## Style

- CSS should be indented with two spaces and start like this:

  ```css
  <style>
  * {
    box-sizing: border-box;
  }
  ```
- Inputs and textareas should be font size 16px.
- For font family, use `system-ui, sans-serif`
- JavaScript should be two space indents and start like this:

  ```js
  <script type="module">
  // code in here should not be indented at the first level
  ```

## Structure

- The HTML file will be named `index.html`
- It will be in a subdirectory of the index root, whose name will be the URL slug for the tool
- I may have already created the directory and/or a blank `index.html` file. If not, please create both.
