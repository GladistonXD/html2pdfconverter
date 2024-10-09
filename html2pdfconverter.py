import pdfkit
from bs4 import BeautifulSoup
import re
import argparse

def process_html(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')

    style_tag = soup.new_tag('style')
    style_tag.string = '''
    * {
        box-sizing: border-box;
    }
    img {
        max-width: 100%;
        height: auto;
        object-fit: contain;
    }
    body, html {
        margin: 0;
        padding: 0;
        text-align: center; 
    }
    .content {
        max-width: 100%;
        max-height: 100%;
        width: 100%; 
        margin: 0 auto; 
    }
    table {
        width: 100%;
        table-layout: fixed;
        word-wrap: break-word;
    }
    td, th {
        word-wrap: break-word;
        overflow: hidden;
    }
    #cover--0 {
        position: relative; 
        page-break-inside: avoid; 
        height: 100vh; 
        width: 100vw; 
        overflow: hidden; 
    }
    .cover-text {
        position: absolute; 
        top: 10%;          
        left: 50%;         
        transform: translateX(-50%); 
        font-size: 24px;  
        color: rgba(64, 64, 72, 0); 
        font-family: Georgia; 
        font-weight: bold; 
        text-align: center; 
        z-index: 10; 
        pointer-events: none;
    }
    '''

    if soup.head:
        soup.head.append(style_tag)
    else:
        head_tag = soup.new_tag('head')
        head_tag.append(style_tag)
        soup.html.insert(0, head_tag)

    cover_section = soup.find(id='cover--0')

    if cover_section:
        specific_image = soup.find(attrs={"data-plgo-uid": "ch0__3__1"})
        if specific_image:
            if 'data-originalwidth' in specific_image.attrs:
                del specific_image['data-originalwidth']
            if 'style' in specific_image.attrs:
                del specific_image['style']

            specific_image['style'] = 'max-width: none; width: 100%; height: auto;'

        cover_marker = soup.new_tag('h1',
            align="center",
            **{
                'data-chapterid': '1',
                'data-plgo-uid': 'ch1__2',
                'id': 'navigation--2',
                'style': 'border: 0px; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: 24px; line-height: 1.6em; font-family: Georgia; margin: 0; padding: 0; color: rgba(64, 64, 72, 0); position: absolute; top: 10%; left: 50%; transform: translateX(-50%); z-index: 10;'
            }
        )
        cover_marker.string = "Cover"

        cover_section.append(cover_marker)

    script_tag = soup.new_tag('script')
    script_tag.string = '''
    document.addEventListener("DOMContentLoaded", function() {
        const tables = document.querySelectorAll('table');
        tables.forEach(table => {
            const boundingBox = table.getBoundingClientRect();
            if (boundingBox.width > window.innerWidth) {
                const scale = window.innerWidth / boundingBox.width; // Calcula a escala para caber na página
                table.style.transform = `scale(${scale})`;
                table.style.transformOrigin = 'top left';
                table.style.width = '100%'; // Mantém a largura 100% após a escala
            }
        });
    });
    '''

    if soup.body:
        soup.body.append(script_tag)
    else:
        body_tag = soup.new_tag('body')
        body_tag.append(script_tag)
        soup.html.append(body_tag)

    end_start = str(soup)
    end_medio = re.sub('<img id="trigger".data-chapterid="0".+?>','',end_start)
    end = re.sub('<img data-chapterid="0" data-originalfontsize="24px" id="trigger".+?>','',end_medio)
    return end


def html_to_pdf(processed_html, pdf_file, path_wkhtmltopdf, page_size):
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    options = {
        'enable-local-file-access': '',
        'viewport-size': '1000x1000',
        'disable-smart-shrinking': False,
        'page-size': page_size,
        'image-quality': '100',
        #'zoom': '1.1'
    }

    pdfkit.from_string(processed_html, pdf_file, configuration=config, options=options)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert HTML to PDF with custom options.')
    parser.add_argument('-i', '--input', required=True, help='Path to input HTML file')
    parser.add_argument('-o', '--output', required=True, help='Path to output PDF file')
    parser.add_argument('-s', '--page-size', default='A4', help='Page size for the PDF (default: A4)')
    parser.add_argument('-p', '--path', required=True, help='Path to wkhtmltopdf executable')

    args = parser.parse_args()

    processed_html = process_html(args.input)
    html_to_pdf(processed_html, args.output, args.path, args.page_size)
