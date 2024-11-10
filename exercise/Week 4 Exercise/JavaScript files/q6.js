<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Q6 - Frog Faces</title>
</head>
<body>
    <img src="frog.jpg" alt="Frog" onclick="addFrogFace()">
    <div id="frogFaces"></div>

    <script>
        function addFrogFace() {
            const frogFace = document.createElement('span');
            frogFace.innerHTML = '&#x1F438;'; // Frog face emoji
            document.getElementById('frogFaces').appendChild(frogFace);
        }
    </script>
</body>
</html>
