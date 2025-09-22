import zipfile
import pathlib

# Define the zip path
zip_path = '/mnt/data/ProdWebsite_Netlify.zip'

# Define a simplified index.html for Netlify
index_html = """<!DOCTYPE html>
<html lang=\"en\">
<head>
<meta charset=\"UTF-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
<title>Prod - Tokyo2Tour</title>
<style>
body {margin:0; font-family:Orbitron,sans-serif; background:#fff; color:#000; overflow-x:hidden;}
header h1 {font-size:3em; color:#ff0000; text-align:center; padding:50px 20px;}
.products {display:flex; flex-wrap:wrap; justify-content:center; gap:25px; padding:20px;}
.product-card {background:#f5f5f5; border:2px solid #ff0000; border-radius:20px; width:250px; padding:20px; text-align:center;}
.product-card img {width:100%; border-radius:12px;}
.buy-btn {background:#ff0000; color:#fff; border:none; padding:10px 20px; border-radius:8px; cursor:pointer;}
.star-trail {position:absolute; color:#ff0000; font-size:12px; opacity:0.6;}
</style>
</head>
<body>
<header><h1>Prod</h1></header>
<main class=\"products\">
<div class=\"product-card\"><img src=\"images/hoodie.png\" alt=\"Hoodie\"><h3>Prod Hoodie</h3><p>$49.99</p><button class=\"buy-btn\" onclick=\"alert('Added Hoodie to cart!')\">Buy</button></div>
<div class=\"product-card\"><img src=\"images/jacket.png\" alt=\"Jacket\"><h3>Prod Jacket</h3><p>$79.99</p><button class=\"buy-btn\" onclick=\"alert('Added Jacket to cart!')\">Buy</button></div>
<div class=\"product-card\"><img src=\"images/sneakers.png\" alt=\"Sneakers\"><h3>Prod Sneakers</h3><p>$99.99</p><button class=\"buy-btn\" onclick=\"alert('Added Sneakers to cart!')\">Buy</button></div>
</main>
<script>
document.body.addEventListener('mousemove', function(e){
    let star=document.createElement('div');
    star.className='star-trail';
    star.style.left=e.pageX+'px';
    star.style.top=e.pageY+'px';
    star.textContent='★';
    document.body.appendChild(star);
    setTimeout(()=>{star.remove();},500);
});
</script>
</body>
</html>"""

# Create the ZIP file and add index.html and a placeholder images folder
with zipfile.ZipFile(zip_path, 'w') as zipf:
    zipf.writestr('index.html', index_html)
    # Add placeholder images folder (empty files)
    image_files = ['images/hoodie.png', 'images/jacket.png', 'images/sneakers.png']
    for img in image_files:
        zipf.writestr(img, '')

zip_path