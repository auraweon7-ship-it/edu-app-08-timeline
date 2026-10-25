# 08 인터랙티브 타임라인: src 조각을 합쳐 단일 HTML로 빌드
import pathlib
root = pathlib.Path(__file__).parent
parts = ['01_head.html', '02_kit.js', '03_app.js', '04_ui.js', '045_layers.js', '05_export.js']
html = '\n'.join((root / 'src' / p).read_text(encoding='utf-8') for p in parts)
tpl = (root / '.hwpx_tpl.js').read_text(encoding='utf-8').strip()
assert '/*__HWPX_TPL__*/' in html
html = html.replace('/*__HWPX_TPL__*/', tpl)
(root / 'index.html').write_text(html, encoding='utf-8')
print('built', len(html))
