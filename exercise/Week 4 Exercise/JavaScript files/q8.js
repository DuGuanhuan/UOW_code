<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Q8 - Swap Images</title>
</head>
<body>
    <img id="lionImg" src="lion.jpg" alt="Lion" onmouseover="swapImages()">
    <img id="frogImg" src="frog.jpg" alt="Frog" onmouseover="swapImages()">

    <script>
        function swapImages() {
            const lion = document.getElementById('lionImg');
            const frog = document.getElementById('frogImg');
            const lionSrc = lion.src;
            lion.src = frog.src;
            frog.src = lionSrc;
        }
    </script>
</body>
</html>
