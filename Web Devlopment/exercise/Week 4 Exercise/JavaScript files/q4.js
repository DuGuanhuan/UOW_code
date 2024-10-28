<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Q4 - Click Messages</title>
</head>
<body>
    <img src="lion.jpg" alt="Lion" onclick="showMessage('Roar', 'orange')">
    <img src="frog.jpg" alt="Frog" onclick="showMessage('Ribbit', 'green')">
    <p id="message"></p>

    <script>
        function showMessage(sound, color) {
            const messageElement = document.getElementById('message');
            messageElement.innerText = sound;
            messageElement.style.color = color;
        }
    </script>
</body>
</html>
