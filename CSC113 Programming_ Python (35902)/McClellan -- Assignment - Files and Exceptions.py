from importlib.resources import contents
from lib2to3.fixes.fix_input import context
from pathlib import Path

def main():
    name = input(str("What is your name? \n>>> "))
    info = input(str("Any info to share? \n>>> "))
    if '<' in (name or info):
        print("ERROR cannot contain '<' or '>'")
        exit()
    elif '>' in (name or info):
        print("ERROR cannot contain '<' or '>'")
        exit()

    path = Path('.other/OUT.HTML')

    #The WHOLE HTML document assigned to var html
    html = '<!DOCTYPE html>\n'
    html += '<html>\n'
    html += '   <head>\n'
    html += '      <meta charset="UTF-8">\n'
    html += '      <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    html += '      <title>3ds Test Page</title>\n'
    html += '   </head>\n'
    html += '   <body>\n'
    html += '      <!-- Headers -->\n'
    html += '      <h1>Header 1</h1>\n'
    html += '      <h2>Header 2</h2>\n'
    html += '      <h3>Header 3</h3>\n'
    html += '      <h4>Header 4</h4>\n'
    html += '      <h5>Header 5</h5>\n'
    html += '      <h6>Header 6</h6>\n'
    html += '      <!-- Paragraph -->\n'
    html += '      <p>This is a paragraph. It auto make new lines above and below it. It can wrap to a new line by default unless the CSS say otherwise<br>Recieved data!<br>Name: '
    html += name
    html += '<br>Info: '
    html += info
    html += '</p>\n'
    html += '      <!-- Lists -->\n'
    html += '         <!-- Ordered list (1. 2. 3.) -->\n'
    html += '         <ol>\n'
    html += '            <li>Pizza</li>\n'
    html += '            <li>Burger</li>\n'
    html += '            <li>French fries</li>\n'
    html += '         </ol>\n'
    html += '         <!-- Unordered list ( * * * ) -->\n'
    html += '         <ul>\n'
    html += '            <li>Gameboy</li>\n'
    html += '            <li>Nintendo 3ds</li>\n'
    html += '            <li>Nintendo Switch</li>\n'
    html += '         </ul>\n'
    html += '         <br> <!-- new line-->\n'
    html += '         <!-- DropDown list-->\n'
    html += '         <details>\n'
    html += '            <summary>DropDown list</summary>\n'
    html += '               <ul>\n'
    html += '                  <li>Item 1</li>\n'
    html += '                  <li>Item 2</li>\n'
    html += '                  <li>Item 3</li>\n'
    html += '               </ul>\n'
    html += '         </details>\n'
    html += '         <br>\n'
    html += '      <!-- Hyperlink -->\n'
    html += '      <a href="https://minecraft.net">Minecraft is awesome!</a>\n'
    html += '      <br>\n'
    html += '      <!--Text types-->\n'
    html += '      <span style="color:green">Colored text!</span>\n'
    html += '      <br>\n'
    html += '      <em>Emphasized text!</em>\n'
    html += '      <br>\n'
    html += '      <i>Italic text!</i>\n'
    html += '      <br>\n'
    html += '      <b>Bold text!</b>\n'
    html += '      <br>\n'
    html += '      <strong>Strong/imporant text!</strong>\n'
    html += '      <br>\n'
    html += '      <mark>Highlighted text!</mark>\n'
    html += '      <br>\n'
    html += '      <s>Crossed out text!</s>\n'
    html += '      <br>\n'
    html += '      <sub>Tiny text!  </sub> <sup>More tiny text!</sup>\n'
    html += '      <br>\n'
    html += '      <br>\n'
    html += '      <!--User Input-->\n'
    html += '      <label for="tbox">Text Box: </label>\n'
    html += '      <input type="text" id="tbox" name="tbox">\n'
    html += '      <br>\n'
    html += '      <input type="checkbox" id="cbox" name="cbox" value="cbox">\n'
    html += '      <lable for="cbox">Checkbox</label>\n'
    html += '      <br>\n'
    html += '      <label for="ddown">Dropdown: </label>\n'
    html += '      <select id="ddown" name="ddown">\n'
    html += '         <option value="food">Food</option>\n'
    html += '         <option value="vgames">Video Games</option>\n'
    html += '         <option value="videos">Videos/Movies</option>\n'
    html += '      </select>\n'
    html += '      <br>\n'
    html += '      <input type="button" onclick="alert("A wild textbox apeared! Press close this prompt to Flee!")" value="Button!">\n'
    html += '      <br>\n'
    html += '   </body>\n'
    html += '</html>'

    path.write_text(html)
    print("Generated! OUT.HTML")

try:
    main()
except:
    print('\nAn unknown error occurred')
    exit()