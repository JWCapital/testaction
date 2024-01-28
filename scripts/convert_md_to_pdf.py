import os
import markdown
import pdfkit

def convert_md_to_pdf(md_file, pdf_file):
    with open(md_file, 'r') as f:
        html_text = markdown.markdown(f.read())
        pdfkit.from_string(html_text, pdf_file)

def main():
    input_dir = os.getenv('INPUT_DIR', './docs')
    output_dir = os.getenv('OUTPUT_DIR', './docs/pdf')
    os.makedirs(output_dir, exist_ok=True)

    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".md"):
                md_file = os.path.join(root, file)
                pdf_file = os.path.join(output_dir, os.path.splitext(file)[0] + '.pdf')
                print(f"Converting | File: {md_file} | Output: {pdf_file}")
                convert_md_to_pdf(md_file, pdf_file)

if __name__ == "__main__":
    main()
