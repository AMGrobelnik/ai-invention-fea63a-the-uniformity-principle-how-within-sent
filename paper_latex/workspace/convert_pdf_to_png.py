#!/usr/bin/env python3
import sys, os
try:
    import pymupdf
except ImportError:
    print('pymupdf not available')
    sys.exit(1)

def pdf_to_png(pdf_path, output_dir, dpi=150):
    os.makedirs(output_dir, exist_ok=True)
    doc = pymupdf.open(pdf_path)
    print(f'PDF has {len(doc)} pages')
    for i in range(len(doc)):
        page = doc[i]
        mat = pymupdf.Matrix(dpi/72, dpi/72)
        pix = page.get_pixmap(matrix=mat)
        out = os.path.join(output_dir, f'page_{i+1:02d}.png')
        pix.save(out)
        print(f'Saved page {i+1}: {out}')
    doc.close()
    print(f'Done! Converted {len(doc)} pages')

if __name__ == "__main__":
    pdf = sys.argv[1] if len(sys.argv) > 1 else "paper.pdf"
    outdir = sys.argv[2] if len(sys.argv) > 2 else "page_screenshots"
    if not os.path.exists(pdf):
        print(f'Error: {pdf} not found')
        sys.exit(1)
    pdf_to_png(pdf, outdir, dpi=150)
